#!/usr/bin/env python3
"""
[INPUT]: 依赖 tests/fixtures 下的 scenario.yaml、输出文件和内部 evidence ledger
[OUTPUT]: 对外提供公司无关、数据驱动的技能场景验证结果
[POS]: scripts 的行为回归门禁，不包含公司名、日期、固定分数或固定文件包假设
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Optional

import yaml

from vocab import (
    APPLICABLE as APPLICABLE_VALUES,
    COVERAGE_CREDIT as CREDITS,
    EVIDENCE_STATUS as EVIDENCE_STATUSES,
    FAILURE_TYPES,
    WEIGHTS,
)


class ValidationInputError(ValueError):
    """场景或台账结构不合法。"""


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValidationInputError(f"invalid YAML in {path.name}: {exc.problem}") from exc


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def require_mapping(value, where: str) -> dict:
    if not isinstance(value, dict):
        raise ValidationInputError(f"{where} must be a mapping")
    return value


def require_keys(mapping: dict, keys: list[str], where: str) -> None:
    missing = [k for k in keys if k not in mapping]
    if missing:
        raise ValidationInputError(f"{where} missing keys: {missing}")


def resolve_ref(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative.strip():
        raise ValidationInputError("file reference must be a non-empty string")
    path = (root / relative).resolve()
    if root not in path.parents:
        raise ValidationInputError(f"file reference escapes scenario directory: {relative}")
    return path


def read(root: Path, relative: str) -> str:
    path = resolve_ref(root, relative)
    if not path.is_file():
        raise ValidationInputError(f"scenario references missing file: {relative}")
    return path.read_text(encoding="utf-8")


def score(ledger: list[dict]) -> tuple[float, float, int]:
    earned = 0.0
    possible = 0.0
    for index, item in enumerate(ledger):
        item = require_mapping(item, f"ledger[{index}]")
        require_keys(item, ["question_priority", "coverage_credit", "evidence_status"], f"ledger[{index}]")
        priority = item["question_priority"]
        if priority not in WEIGHTS:
            raise ValidationInputError(f"ledger[{index}].question_priority must be P0, P1, or P2")
        try:
            credit = float(item["coverage_credit"])
        except (TypeError, ValueError) as exc:
            raise ValidationInputError(f"ledger[{index}].coverage_credit must be numeric") from exc
        if credit not in CREDITS:
            raise ValidationInputError(f"ledger[{index}].coverage_credit must be 0.0, 0.5, or 1.0")
        if item["evidence_status"] not in EVIDENCE_STATUSES:
            raise ValidationInputError(
                f"ledger[{index}].evidence_status must be known, inferred, unknown, or contradiction"
            )
        weight = WEIGHTS[priority]
        possible += weight
        earned += weight * credit
    percent = 0 if possible == 0 else earned / possible * 100
    rounded = int((percent + 2.5) // 5 * 5)
    return earned, possible, rounded


def format_points(value: float) -> str:
    return str(int(value)) if value.is_integer() else str(value)


def field(text: str, name: str) -> Optional[str]:
    match = re.search(rf"(?mi)^\s*-\s*{re.escape(name)}:\s*(.+?)\s*$", text)
    return match.group(1).strip() if match else None


def tables(text: str) -> list[list[dict[str, str]]]:
    lines = text.splitlines()
    parsed: list[list[dict[str, str]]] = []
    index = 0
    while index + 1 < len(lines):
        header = cells(lines[index])
        separator = cells(lines[index + 1])
        valid_separator = (
            header
            and len(header) == len(separator)
            and all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator)
        )
        if not valid_separator:
            index += 1
            continue
        rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines):
            row = cells(lines[index])
            if len(row) != len(header):
                break
            rows.append(dict(zip(header, row)))
            index += 1
        parsed.append(rows)
    return parsed


def cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def table_with(text: str, columns: set[str], where: str) -> list[dict[str, str]]:
    for rows in tables(text):
        if rows and columns.issubset(rows[0]):
            return rows
    raise ValidationInputError(f"{where} lacks a Markdown table with columns: {sorted(columns)}")


def optional_mapping(mapping: dict, key: str) -> Optional[dict]:
    value = mapping.get(key)
    return None if value is None else require_mapping(value, key)


def string_list(mapping: dict, key: str, where: str) -> list[str]:
    value = mapping.get(key, [])
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValidationInputError(f"{where}.{key} must be a list of strings")
    return value


def load_ledger(root: Path, config: dict) -> list[dict]:
    require_keys(config, ["file"], "ledger")
    path = resolve_ref(root, config["file"])
    if not path.is_file():
        raise ValidationInputError(f"scenario references missing ledger: {config['file']}")
    ledger = load_yaml(path)
    if not isinstance(ledger, list):
        raise ValidationInputError("ledger must be a list")
    score(ledger)
    return ledger


def validate_outputs(root: Path, outputs: dict, errors: list[str]) -> None:
    for relative in string_list(outputs, "required", "outputs"):
        require(resolve_ref(root, relative).is_file(), f"missing required output: {relative}", errors)
    for relative in string_list(outputs, "forbidden", "outputs"):
        require(not resolve_ref(root, relative).exists(), f"forbidden output exists: {relative}", errors)
    omitted_file = outputs.get("omitted_notice_file")
    if omitted_file:
        omitted = read(root, omitted_file)
        require("Omitted appendices:" in omitted, "minimal output does not list omitted appendices", errors)


def validate_verdict(root: Path, verdict: dict, errors: list[str]) -> str:
    require_keys(verdict, ["label", "primary_file"], "verdict")
    expected = verdict["label"]
    primary = read(root, verdict["primary_file"])
    require(field(primary, "Verdict") == expected, f"primary output has wrong verdict: {expected}", errors)
    if verdict.get("require_falsifiability"):
        reversal = re.search(r"(?mi)^\s*-?\s*This verdict reverses if:\s*(.+?)\s*$", primary)
        require(bool(reversal and reversal.group(1).strip()), "missing falsifiability statement", errors)
    validate_conditional_ic(root, verdict, expected, errors)
    return expected


def validate_conditional_ic(root: Path, verdict: dict, expected: str, errors: list[str]) -> None:
    conditional_file = verdict.get("conditional_ic_file")
    if conditional_file:
        conditional = read(root, conditional_file)
        require(
            "Conditional IC Pre-read — Not decision-ready" in conditional,
            "Need more evidence scenario produced a non-conditional IC memo",
            errors,
        )
        require(field(conditional, "Verdict") == expected, "conditional IC has wrong verdict", errors)
        require(
            "- No investment recommendation is made." in conditional,
            "conditional IC omits the no-recommendation guard",
            errors,
        )


def validate_ledger_rules(config: dict, ledger: list[dict], verdict: str, errors: list[str]) -> None:
    minimum = int(config.get("min_entries", 1))
    require(len(ledger) >= minimum, f"ledger has fewer than {minimum} entries", errors)
    if config.get("require_unknown_p0"):
        unknown_p0 = any(
            item.get("question_priority") == "P0"
            and item.get("evidence_status") in {"unknown", "contradiction"}
            for item in ledger
        )
        require(unknown_p0, "scenario lacks an unresolved P0 gate", errors)
        require(
            verdict == "Need more evidence",
            "an unresolved reversible P0 must derive Need more evidence",
            errors,
        )
    if config.get("require_fallback"):
        require(any(item.get("fallback_source") for item in ledger), "ledger lacks fallback source", errors)


def validate_coverage(
    root: Path,
    coverage: Optional[dict],
    modules: list[str],
    ledger: list[dict],
    errors: list[str],
) -> None:
    if not coverage and modules:
        raise ValidationInputError("'modules' requires 'coverage.file'")
    if not coverage:
        return
    require_keys(coverage, ["file"], "coverage")
    text = read(root, coverage["file"])
    earned, possible, rounded = score(ledger)
    points = f"{format_points(earned)} / {format_points(possible)}"
    require(field(text, "Weighted points earned / possible") == points, f"wrong coverage points: {points}", errors)
    require(field(text, "Weighted coverage") == f"{rounded}%", f"wrong rounded coverage: {rounded}%", errors)
    if modules:
        rows = table_with(text, {"Module", "Readiness"}, "coverage output")
        present = {row["Module"] for row in rows}
        for module in modules:
            require(module in present, f"missing module row: {module}", errors)


def validate_research(root: Path, research: Optional[dict], errors: list[str]) -> None:
    if research and research.get("require_blocked_fallback"):
        log = read(root, research["file"])
        rows = table_with(
            log,
            {"Failure type", "Fallback route attempted", "Recovery status"},
            "research log",
        )
        recovered = any(
            row["Failure type"].strip().lower() in FAILURE_TYPES
            and row["Fallback route attempted"].strip()
            and row["Recovery status"].strip().lower() == "recovered"
            for row in rows
        )
        require(recovered, "research log lacks a blocked source with fallback and recovered status", errors)


def validate_ai_strategy(root: Path, ai: Optional[dict], errors: list[str]) -> None:
    if ai:
        text = read(root, ai["file"])
        rows = table_with(text, {"Product / feature", "Status"}, "AI strategy")
        statuses = {row["Status"] for row in rows}
        for status in string_list(ai, "required_statuses", "ai_strategy"):
            require(status in statuses, f"AI strategy missing status row: {status}", errors)


def validate_competition(root: Path, competition: Optional[dict], errors: list[str]) -> None:
    if not competition:
        return
    text = read(root, competition["file"])
    rows = table_with(text, {"Layer", "Applicable?"}, "competitor landscape")
    addressed = [
        row["Layer"]
        for row in rows
        if row.get("Applicable?", "").strip().lower() in APPLICABLE_VALUES
    ]
    for layer in string_list(competition, "required_layers", "competition"):
        needle = layer.lower()
        hit = any(needle in cell.lower() for cell in addressed)
        require(hit, f"competitor landscape lacks an addressed layer matching: {layer}", errors)


def validate(root: Path) -> list[str]:
    scenario_path = root / "scenario.yaml"
    if not scenario_path.is_file():
        raise ValidationInputError(f"missing scenario.yaml: {root}")
    scenario = require_mapping(load_yaml(scenario_path), "scenario.yaml")
    require_keys(scenario, ["name", "verdict", "ledger"], "top level")
    errors: list[str] = []
    outputs = require_mapping(scenario.get("outputs", {}), "outputs")
    ledger_config = require_mapping(scenario["ledger"], "ledger")
    ledger = load_ledger(root, ledger_config)
    verdict = validate_verdict(root, require_mapping(scenario["verdict"], "verdict"), errors)
    validate_outputs(root, outputs, errors)
    validate_ledger_rules(ledger_config, ledger, verdict, errors)
    modules = string_list(scenario, "modules", "scenario")
    validate_coverage(root, optional_mapping(scenario, "coverage"), modules, ledger, errors)
    validate_research(root, optional_mapping(scenario, "research"), errors)
    validate_ai_strategy(root, optional_mapping(scenario, "ai_strategy"), errors)
    validate_competition(root, optional_mapping(scenario, "competition"), errors)
    return errors


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_test_run.py <scenario-directory>")
    root = Path(sys.argv[1]).resolve()
    try:
        errors = validate(root)
    except (ValidationInputError, TypeError, ValueError, KeyError, AttributeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        raise SystemExit(1)
    scenario = load_yaml(root / "scenario.yaml")
    print(f"Scenario passed: {scenario['name']}")


if __name__ == "__main__":
    main()
