#!/usr/bin/env python3
"""
[INPUT]: 无外部依赖，仅承载受控词表常量
[OUTPUT]: 对外提供 skill 全部受控词表的单一事实源（验证器与模板对齐基准）
[POS]: scripts 的词表中枢，validate_skill 与 validate_test_run 共同 import，消除多处重复
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
from __future__ import annotations

# ── Coverage scoring ─────────────────────────────────────────────
WEIGHTS = {"P0": 3, "P1": 2, "P2": 1}
QUESTION_PRIORITY = set(WEIGHTS)
COVERAGE_CREDIT = {0.0, 0.5, 1.0}

# ── Evidence ledger ──────────────────────────────────────────────
EVIDENCE_STATUS = {"known", "inferred", "unknown", "contradiction"}
EVIDENCE_STRENGTH = {"strong", "limited", "none"}
MODULES = {
    "basic_info",
    "team",
    "product_technology",
    "ai_strategy",
    "traction_market",
    "financials",
    "legal_risk",
    "capital_path",
}

# ── Research log ─────────────────────────────────────────────────
# Must stay identical to the failure-type options shown in
# templates/appendices/external-research-log.md (CI enforces this).
FAILURE_TYPES = {
    "paywall",
    "login",
    "robots",
    "geo-block",
    "dynamic",
    "missing",
    "rate-limit",
    "unavailable-tool",
}

# ── Competitor landscape ─────────────────────────────────────────
APPLICABLE = {"yes", "applicable"}

# ── AI product lifecycle status ──────────────────────────────────
AI_STATUS = {"live", "beta/pilot", "announced", "retired", "unknown"}

# ── Verdicts ─────────────────────────────────────────────────────
VERDICTS = {"Proceed", "Watch", "Pass", "Need more evidence"}

# ── Four-dimensional stage map ───────────────────────────────────
STAGE = {
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
