#!/usr/bin/env python3
"""
[INPUT]: 依赖项目文件、YAML 解析器与技能结构约束
[OUTPUT]: 对外提供技能包结构、链接、模板字段和文档契约验证结果
[POS]: scripts 的质量门禁，阻止技能规则与交付模板发生结构漂移
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"Missing PyYAML: {exc}", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "references/diligence/module-questions.md",
    "references/research/source-access-strategy.md",
    "references/research/ai-product-strategy.md",
    "references/diligence/coverage-stage-model.md",
    "references/diligence/red-team-checks.md",
    "references/diligence/pattern-library.md",
    "references/diligence/decision-rules.md",
    "references/research/orchestration.md",
    "templates/appendices/evidence-ledger.yaml",
    "templates/decisions/qa-gap-list.md",
    "templates/decisions/onepage.md",
    "templates/decisions/ic-memo.md",
    "templates/decisions/risk-register.md",
    "templates/appendices/ai-product-strategy.md",
    "examples/sample-ai-company/brief.md",
    "scripts/validate_test_run.py",
    "tests/fixtures/minimal-output/scenario.yaml",
    "tests/fixtures/need-more-evidence-full/scenario.yaml",
    "worked-examples/anonymized-regulated-ai-platform/decisions/01-chinese-systematic-dd.md",
]
# Spec: lowercase alphanumerics and hyphens, no leading/trailing/double hyphen.
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MD_LINK_RE = re.compile(r"\]\((?!https?://|#)([^)]+)\)")
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[oprsu]_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
]

ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def split_skill_md() -> tuple[dict, str]:
    content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        error("SKILL.md must start with YAML frontmatter")
        return {}, ""
    match = re.search(r"\n---\s*\n", content[4:])
    if not match:
        error("SKILL.md frontmatter is not closed")
        return {}, ""
    fm = yaml.safe_load(content[4 : match.start() + 4])
    body = content[match.end() + 4 :]
    if not isinstance(fm, dict):
        error("SKILL.md frontmatter must parse to a mapping")
        return {}, body
    return fm, body


def check_required_files() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        error(f"Missing required files: {missing}")


def check_frontmatter(fm: dict) -> None:
    name = fm.get("name", "")
    if not name or len(name) > 64 or not NAME_RE.match(name):
        error(f"Invalid skill name {name!r}: must be 1-64 chars, lowercase alphanumerics "
              "and single hyphens, no leading/trailing hyphen")
    desc = fm.get("description", "")
    if not desc or not (1 <= len(desc) <= 1024):
        error("description must be 1-1024 characters")
    compat = fm.get("compatibility")
    if compat is not None and not (1 <= len(str(compat)) <= 500):
        error("compatibility must be 1-500 characters when present")
    metadata = fm.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        error("metadata must be a key-value mapping when present")


def check_body(body: str) -> None:
    if not body.strip():
        error("SKILL.md body is empty")
    lines = body.count("\n") + 1
    if lines > 500:
        error(f"SKILL.md body is {lines} lines; spec recommends under 500")
    for ref in MD_LINK_RE.findall(body):
        if not (ROOT / ref).exists():
            error(f"SKILL.md references missing file: {ref}")


def check_templates() -> None:
    onepage = (ROOT / "templates/decisions/onepage.md").read_text(encoding="utf-8")
    for section in [
        "AI moat hypothesis",
        "Four-dimensional stage map",
        "Diligence readiness",
        "Follow-up questions",
        "Preliminary view",
    ]:
        if section not in onepage:
            error(f"onepage.md missing section: {section}")
    qa_gap_list = (ROOT / "templates/decisions/qa-gap-list.md").read_text(encoding="utf-8")
    qa_modules = [
        "Basic Info / Thesis",
        "Team",
        "Product / Technology",
        "AI Product & Capability Strategy",
        "Traction / Market",
        "Financials / Business Model",
        "Legal / Compliance / Data Risk",
        "Capital Path / VC Fit / Fundability",
    ]
    for module in qa_modules:
        if f"| {module} |" not in qa_gap_list:
            error(f"qa-gap-list.md coverage summary missing module: {module}")
    for term in [
        "Weighted points earned / possible",
        "Weighted coverage",
        "P0 resolved / total",
        "Unresolved P0 gates",
        "Decision readiness",
    ]:
        if term not in qa_gap_list:
            error(f"qa-gap-list.md missing weighted coverage field: {term}")
    ic_memo = (ROOT / "templates/decisions/ic-memo.md").read_text(encoding="utf-8")
    if "Conditional IC Pre-read — Not decision-ready" not in ic_memo:
        error("ic-memo.md must distinguish a conditional pre-read from a final IC memo")
    ledger = yaml.safe_load((ROOT / "templates/appendices/evidence-ledger.yaml").read_text(encoding="utf-8"))
    if not isinstance(ledger, list) or not ledger:
        error("evidence-ledger.yaml must be a non-empty list")
        return
    for key in [
        "claim",
        "module",
        "question_priority",
        "gating_question",
        "source_type",
        "evidence_status",
        "evidence_strength",
        "coverage_credit",
        "confidence",
        "next_check",
        "source_access",
        "fallback_source",
        "product_maturity",
        "pmf_status",
        "gtm_maturity",
        "financing_stage",
    ]:
        if key not in ledger[0]:
            error(f"evidence-ledger.yaml missing key: {key}")
    if "stage" in ledger[0]:
        error("evidence-ledger.yaml must use four stage dimensions instead of mixed 'stage'")
    allowed_modules = {
        "basic_info",
        "team",
        "product_technology",
        "ai_strategy",
        "traction_market",
        "financials",
        "legal_risk",
        "capital_path",
    }
    if ledger[0].get("module") not in allowed_modules:
        error(f"evidence-ledger.yaml has invalid default module: {ledger[0].get('module')!r}")
    allowed_defaults = {
        "question_priority": {"P0", "P1", "P2"},
        "evidence_strength": {"strong", "limited", "none"},
        "coverage_credit": {0.0, 0.5, 1.0},
        "product_maturity": {"concept", "prototype", "mvp", "production", "scaled_product", "unknown"},
        "pmf_status": {
            "untested",
            "problem_validation",
            "solution_validation",
            "repeatable_pmf",
            "expanding_pmf",
            "unknown",
        },
        "gtm_maturity": {
            "no_motion",
            "founder_led",
            "emerging_repeatability",
            "repeatable_motion",
            "scalable_motion",
            "unknown",
        },
        "financing_stage": {
            "bootstrapped",
            "pre_seed",
            "seed",
            "series_a",
            "series_b_plus",
            "profitable_or_self_funded",
            "unknown",
        },
    }
    for key, allowed in allowed_defaults.items():
        if ledger[0].get(key) not in allowed:
            error(f"evidence-ledger.yaml has invalid default for {key}: {ledger[0].get(key)!r}")

    coverage_stage = (ROOT / "references/diligence/coverage-stage-model.md").read_text(encoding="utf-8")
    for section in [
        "Weighted coverage",
        "Gating rule",
        "Product maturity",
        "PMF status",
        "GTM maturity",
        "Financing stage",
    ]:
        if section not in coverage_stage:
            error(f"coverage-stage-model.md missing section: {section}")

    research_log = (ROOT / "templates/appendices/external-research-log.md").read_text(encoding="utf-8")
    for term in ["Fallback route attempted", "Source diversity audit", "AI products/capabilities"]:
        if term not in research_log:
            error(f"external-research-log.md missing access-strategy field: {term}")

    ai_strategy = (ROOT / "templates/appendices/ai-product-strategy.md").read_text(encoding="utf-8")
    for term in ["Target AI product inventory", "Strategy choices", "Adoption and economics", "Same-dimension company comparison"]:
        if term not in ai_strategy:
            error(f"ai-product-strategy.md missing section: {term}")


def check_no_obvious_secrets() -> None:
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                error(f"Potential secret-like string found in {path.relative_to(ROOT)}")


def check_protocol_headers() -> None:
    protocol = "[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md"
    scoped = [
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CHANGELOG.md",
        *sorted((ROOT / "references").rglob("*.md")),
        *sorted((ROOT / "templates").rglob("*.md")),
        *sorted((ROOT / "templates").rglob("*.yaml")),
        *sorted((ROOT / "scripts").glob("*.py")),
        *sorted((ROOT / "examples").rglob("*.md")),
        *sorted((ROOT / "tests").rglob("*.md")),
        *sorted((ROOT / "tests").rglob("*.yaml")),
        *sorted((ROOT / "worked-examples").rglob("*.md")),
        *sorted((ROOT / "worked-examples").rglob("*.yaml")),
    ]
    for path in scoped:
        if path.name == "CLAUDE.md":
            continue
        if protocol not in path.read_text(encoding="utf-8"):
            error(f"Missing L3 protocol header: {path.relative_to(ROOT)}")


def check_worked_examples_are_deidentified() -> None:
    root = ROOT / "worked-examples"
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"https?://", text):
            error(f"Worked example contains an external URL: {path.relative_to(ROOT)}")


def main() -> None:
    check_required_files()
    fm, body = split_skill_md()
    if fm:
        check_frontmatter(fm)
    check_body(body)
    check_templates()
    check_no_obvious_secrets()
    check_protocol_headers()
    check_worked_examples_are_deidentified()
    if ERRORS:
        for message in ERRORS:
            print(f"ERROR: {message}", file=sys.stderr)
        sys.exit(1)
    print("Skill package validation passed.")


if __name__ == "__main__":
    main()
