#!/usr/bin/env python3
"""
[INPUT]: 依赖 tests/fixtures 下的 scenario.yaml、输出文件和内部 evidence ledger
[OUTPUT]: 对外提供公司无关、数据驱动的技能场景验证结果
[POS]: scripts 的行为回归门禁，不包含公司名、日期、固定分数或固定文件包假设
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

WEIGHTS = {"P0": 3, "P1": 2, "P2": 1}


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def require_keys(mapping: dict, keys: list[str], where: str) -> None:
    missing = [k for k in keys if k not in mapping]
    if missing:
        raise SystemExit(f"scenario.yaml: {where} missing keys: {missing}")


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise SystemExit(f"scenario.yaml references missing file: {relative}")
    return path.read_text(encoding="utf-8")


def score(ledger: list[dict]) -> tuple[float, float, int]:
    earned = 0.0
    possible = 0.0
    for item in ledger:
        weight = WEIGHTS[item["question_priority"]]
        possible += weight
        earned += weight * float(item["coverage_credit"])
    percent = 0 if possible == 0 else earned / possible * 100
    rounded = int((percent + 2.5) // 5 * 5)
    return earned, possible, rounded


def format_points(value: float) -> str:
    return str(int(value)) if value.is_integer() else str(value)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_test_run.py <scenario-directory>")

    root = Path(sys.argv[1]).resolve()
    scenario_path = root / "scenario.yaml"
    if not scenario_path.is_file():
        raise SystemExit(f"missing scenario.yaml: {root}")

    scenario = load_yaml(scenario_path)
    require_keys(scenario, ["name", "verdict", "ledger"], "top level")
    require_keys(scenario["verdict"], ["label", "primary_file"], "verdict")
    require_keys(scenario["ledger"], ["file"], "ledger")
    errors: list[str] = []

    outputs = scenario.get("outputs", {})
    for relative in outputs.get("required", []):
        require((root / relative).is_file(), f"missing required output: {relative}", errors)
    for relative in outputs.get("forbidden", []):
        require(not (root / relative).exists(), f"forbidden output exists: {relative}", errors)

    ledger_path = scenario["ledger"]["file"]
    ledger_file = root / ledger_path
    if not ledger_file.is_file():
        raise SystemExit(f"scenario.yaml references missing ledger: {ledger_path}")
    ledger = load_yaml(ledger_file)
    require(isinstance(ledger, list), "ledger must be a list", errors)
    if not isinstance(ledger, list):
        ledger = []

    expected_verdict = scenario["verdict"]["label"]
    primary_file = scenario["verdict"]["primary_file"]
    primary = read(root, primary_file)
    require(expected_verdict in primary, f"primary output missing verdict: {expected_verdict}", errors)

    if scenario["verdict"].get("require_falsifiability"):
        require("This verdict reverses if:" in primary, "missing falsifiability statement", errors)

    conditional_file = scenario["verdict"].get("conditional_ic_file")
    if conditional_file:
        conditional = read(root, conditional_file)
        require(
            "Conditional IC Pre-read — Not decision-ready" in conditional,
            "Need more evidence scenario produced a non-conditional IC memo",
            errors,
        )

    omitted_file = outputs.get("omitted_notice_file")
    if omitted_file:
        omitted = read(root, omitted_file)
        require("Omitted appendices:" in omitted, "minimal output does not list omitted appendices", errors)

    minimum = int(scenario["ledger"].get("min_entries", 1))
    require(len(ledger) >= minimum, f"ledger has fewer than {minimum} entries", errors)

    if scenario["ledger"].get("require_unknown_p0"):
        unknown_p0 = any(
            item.get("question_priority") == "P0"
            and item.get("evidence_status") in {"unknown", "contradiction"}
            for item in ledger
        )
        require(unknown_p0, "scenario lacks an unresolved P0 gate", errors)
        require(
            expected_verdict == "Need more evidence",
            "an unresolved reversible P0 must derive Need more evidence",
            errors,
        )

    if scenario["ledger"].get("require_fallback"):
        require(any(item.get("fallback_source") for item in ledger), "ledger lacks fallback source", errors)

    coverage = scenario.get("coverage")
    if coverage:
        earned, possible, rounded = score(ledger)
        coverage_text = read(root, coverage["file"])
        points = f"{format_points(earned)} / {format_points(possible)}"
        require(points in coverage_text, f"coverage output missing computed points: {points}", errors)
        require(f"{rounded}%" in coverage_text, f"coverage output missing rounded score: {rounded}%", errors)

    modules = scenario.get("modules", [])
    if modules:
        if not (coverage and coverage.get("file")):
            raise SystemExit("scenario.yaml: 'modules' requires 'coverage.file'")
        module_text = read(root, coverage["file"])
        for module in modules:
            require(module in module_text, f"missing module: {module}", errors)

    research = scenario.get("research")
    if research and research.get("require_blocked_fallback"):
        log = read(root, research["file"])
        require("blocked" in log.lower(), "research log lacks blocked source", errors)
        require("recovered" in log.lower(), "research log lacks recovery status", errors)

    ai = scenario.get("ai_strategy")
    if ai:
        text = read(root, ai["file"])
        for status in ai.get("required_statuses", []):
            require(status in text, f"AI strategy missing status: {status}", errors)

    competition = scenario.get("competition")
    if competition:
        text = read(root, competition["file"])
        for layer in competition.get("required_layers", []):
            require(layer in text, f"competitor landscape missing layer: {layer}", errors)

    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Scenario passed: {scenario['name']}")


if __name__ == "__main__":
    main()
