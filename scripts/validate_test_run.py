#!/usr/bin/env python3
"""
[INPUT]: 依赖真实公司测试目录中的决策文档、附录和 evidence ledger
[OUTPUT]: 对外提供端到端技能行为断言的确定性验证结果
[POS]: scripts 的前向测试门禁，验证规则是否在真实产物中落地
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_test_run.py <test-run-directory>")

    root = Path(sys.argv[1]).resolve()
    errors: list[str] = []
    required = [
        "decisions/01-chinese-systematic-dd.md",
        "decisions/02-onepage.md",
        "decisions/03-qa-gap-list.md",
        "decisions/04-data-room-request.md",
        "decisions/05-ic-memo.md",
        "decisions/06-risk-register.md",
        "appendices/07-competitor-landscape.md",
        "appendices/08-ai-product-strategy.md",
        "appendices/09-external-research-log.md",
        "appendices/evidence-ledger.yaml",
        "test-assertions.md",
    ]
    for relative in required:
        require((root / relative).is_file(), f"missing {relative}", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)

    primary = (root / required[0]).read_text(encoding="utf-8")
    onepage = (root / required[1]).read_text(encoding="utf-8")
    qa = (root / required[2]).read_text(encoding="utf-8")
    ic = (root / required[4]).read_text(encoding="utf-8")
    competitor = (root / required[6]).read_text(encoding="utf-8")
    ai_strategy = (root / required[7]).read_text(encoding="utf-8")
    research = (root / required[8]).read_text(encoding="utf-8")
    ledger = yaml.safe_load((root / required[9]).read_text(encoding="utf-8"))

    require("Need more evidence" in primary, "primary verdict is not Need more evidence", errors)
    require("This verdict reverses if:" in primary, "missing falsifiability statement", errors)
    require("Conditional IC Pre-read — Not decision-ready" in ic, "IC file is not conditional", errors)
    require("95 / 160" in qa and "60%" in qa, "coverage is not reproducible", errors)
    require("Crunchbase" in research and "robots.txt" in research, "blocked source not logged", errors)
    require("recovered" in research, "fallback recovery status missing", errors)

    modules = [
        "Basic Info / Thesis",
        "Team",
        "Product / Technology",
        "AI Product & Capability Strategy",
        "Traction / Market",
        "Financials / Business Model",
        "Legal / Compliance / Data Risk",
        "Capital Path / VC Fit / Fundability",
    ]
    for module in modules:
        require(module in qa, f"missing module in coverage: {module}", errors)

    for status in ["live", "beta/early access"]:
        require(status in ai_strategy, f"AI product status missing: {status}", errors)
    for layer in ["Direct", "Platform/model", "Incumbent", "Customer-built", "Manual"]:
        require(layer in competitor, f"competitor layer missing: {layer}", errors)

    require(isinstance(ledger, list) and len(ledger) >= 8, "evidence ledger is too sparse", errors)
    if isinstance(ledger, list):
        unknown_p0 = [
            item
            for item in ledger
            if item.get("question_priority") == "P0"
            and item.get("evidence_status") in {"unknown", "contradiction"}
        ]
        require(bool(unknown_p0), "test lacks a reversible unknown P0 gate", errors)
        fallback_entries = [item for item in ledger if item.get("fallback_source")]
        require(bool(fallback_entries), "ledger does not retain fallback sources", errors)

    require(re.search(r"研究日期：2026-06-19", onepage) is not None, "research date missing", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("Real-company end-to-end test passed.")


if __name__ == "__main__":
    main()
