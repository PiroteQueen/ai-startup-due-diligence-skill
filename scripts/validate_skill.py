#!/usr/bin/env python3
"""Validate the AI startup due diligence skill package."""
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
    "templates/evidence-ledger.yaml",
    "templates/qa-gap-list.md",
    "templates/onepage.md",
    "templates/ic-memo.md",
    "templates/risk-register.md",
    "examples/sample-ai-company/brief.md",
]
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[oprsu]_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def check_required_files() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail(f"Missing required files: {missing}")


def check_skill_frontmatter() -> None:
    content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    match = re.search(r"\n---\s*\n", content[4:])
    if not match:
        fail("SKILL.md frontmatter is not closed")
    fm_text = content[4 : match.start() + 4]
    fm = yaml.safe_load(fm_text)
    if not isinstance(fm, dict):
        fail("SKILL.md frontmatter must parse to a mapping")
    if fm.get("name") != "ai-startup-due-diligence":
        fail("SKILL.md name must be ai-startup-due-diligence")
    desc = fm.get("description")
    if not desc or len(desc) > 1024:
        fail("SKILL.md description is missing or too long")
    body = content[match.end() + 4 :].strip()
    if not body:
        fail("SKILL.md body is empty")


def check_templates() -> None:
    onepage = (ROOT / "templates/onepage.md").read_text(encoding="utf-8")
    for section in ["AI moat hypothesis", "Follow-up questions", "Preliminary view"]:
        if section not in onepage:
            fail(f"onepage.md missing section: {section}")
    ledger = yaml.safe_load((ROOT / "templates/evidence-ledger.yaml").read_text(encoding="utf-8"))
    if not isinstance(ledger, list) or not ledger:
        fail("evidence-ledger.yaml must be a non-empty list")
    for key in ["claim", "module", "source_type", "confidence", "next_check"]:
        if key not in ledger[0]:
            fail(f"evidence-ledger.yaml missing key: {key}")


def check_no_obvious_secrets() -> None:
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"Potential secret-like string found in {path.relative_to(ROOT)}")


def main() -> None:
    check_required_files()
    check_skill_frontmatter()
    check_templates()
    check_no_obvious_secrets()
    print("Skill package validation passed.")


if __name__ == "__main__":
    main()
