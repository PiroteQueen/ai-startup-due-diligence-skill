#!/usr/bin/env python3
"""
[INPUT]: 依赖 need-more-evidence-full 场景与 validate_test_run.py
[OUTPUT]: 对外提供失败类型、竞争适用性与 AI 状态词的反向回归测试
[POS]: tests 的验证器防回归入口，确保错误产物不能获得假绿灯
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/need-more-evidence-full"
VALIDATOR = ROOT / "scripts/validate_test_run.py"

sys.path.insert(0, str(ROOT / "scripts"))
import validate_skill  # noqa: E402
import vocab  # noqa: E402


class ValidatorNegativeCases(unittest.TestCase):
    def assert_rejected(self, relative: str, old: str, new: str, message: str) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            scenario = Path(temporary) / "scenario"
            shutil.copytree(FIXTURE, scenario)
            target = scenario / relative
            text = target.read_text(encoding="utf-8")
            self.assertIn(old, text)
            target.write_text(text.replace(old, new, 1), encoding="utf-8")
            result = subprocess.run(
                ["python3", str(VALIDATOR), str(scenario)],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(result.returncode, 1)
        self.assertIn(message, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_invalid_failure_type_is_rejected(self) -> None:
        self.assert_rejected(
            "appendices/09-external-research-log.md",
            "| robots |",
            "| none |",
            "research log lacks a blocked source",
        )

    def test_not_applicable_layer_is_not_covered(self) -> None:
        self.assert_rejected(
            "appendices/07-competitor-landscape.md",
            "| Direct product | yes | Rival A |",
            "| Direct product | no |  |",
            "competitor landscape lacks an addressed layer matching: Direct",
        )

    def test_noncanonical_ai_status_is_rejected(self) -> None:
        self.assert_rejected(
            "appendices/08-ai-product-strategy.md",
            "beta/pilot",
            "beta-pilot",
            "AI strategy missing status row: beta/pilot",
        )

    def test_noncanonical_verdict_label_is_rejected(self) -> None:
        self.assert_rejected(
            "scenario.yaml",
            "label: Need more evidence",
            "label: Bogus verdict",
            "verdict.label not in controlled vocab",
        )

    def test_template_vocab_alignment_catches_drift(self) -> None:
        # Extraction keeps an internal slash ("beta/pilot") as one token,
        # and any option outside the controlled vocab is detectable (extra direction).
        tokens = validate_skill.option_tokens(
            "| Agent workflow | live / beta/pilot / bogus-status |", "beta/pilot"
        )
        self.assertIn("beta/pilot", tokens)
        self.assertEqual(sorted(tokens - vocab.AI_STATUS), ["bogus-status"])
        # Omission is caught too: a vocab value missing from the option list.
        partial = validate_skill.option_tokens(
            "| x | live / beta/pilot / announced / unknown |", "beta/pilot"
        )
        self.assertEqual(sorted(vocab.AI_STATUS - partial), ["retired"])
        # The live template equals the controlled vocab today (no drift either way).
        real = validate_skill.option_tokens(
            (ROOT / "templates/appendices/ai-product-strategy.md").read_text(encoding="utf-8"),
            "beta/pilot / announced",
        )
        self.assertEqual(real, set(vocab.AI_STATUS))

    def test_reference_docs_define_vocab_in_sync(self) -> None:
        # Bold-token extraction surfaces a stage value that drifts from vocab.
        drifted = validate_skill.bold_tokens("- **concept** —\n- **bogus_x** —")
        self.assertEqual(sorted(drifted - vocab.STAGE["product_maturity"]), ["bogus_x"])
        # The reference stage doc still defines exactly the vocab tokens.
        stage = (ROOT / "references/diligence/coverage-stage-model.md").read_text(encoding="utf-8")
        for dim, allowed in vocab.STAGE.items():
            self.assertTrue(allowed <= validate_skill.bold_tokens(stage), f"{dim} missing from reference")
        # The AI-status reference line equals the controlled vocab exactly.
        ai_tokens = validate_skill.backtick_tokens(
            (ROOT / "references/research/ai-product-strategy.md").read_text(encoding="utf-8"),
            "`beta/pilot`",
        )
        self.assertEqual(ai_tokens, set(vocab.AI_STATUS))


if __name__ == "__main__":
    unittest.main()
