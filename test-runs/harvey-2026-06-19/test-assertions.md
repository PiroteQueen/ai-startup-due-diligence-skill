<!--
[INPUT]: 依赖本测试目录的 decisions、appendices 与技能规则
[OUTPUT]: 对外提供 Harvey 真实公司端到端测试的断言和结果
[POS]: 测试运行的验收契约，防止报告完整度掩盖规则失效
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Harvey End-to-End Test Assertions

- Test date: 2026-06-19
- Target: Harvey
- Scope: public-source preliminary investment DD

| Assertion | Expected | Actual | Result |
|---|---|---|---|
| Blocked-source fallback | Crunchbase failure logged; alternate sources used | Official Harvey, investor/reporting and competitor sources used | PASS |
| Eight-module coverage | All eight modules scored | All eight present in Q&A table | PASS |
| Standalone AI strategy | Dedicated appendix with dated feature status | `08-ai-product-strategy.md` | PASS |
| Competitor gate | At least three layers and 4+ comparables | Six layers; Legora, TR, LexisNexis, Luminance, internal build | PASS |
| Evidence discipline | Company claims labeled self-reported/limited | Customer counts and agents marked limited | PASS |
| P0 gating | Public gaps block investment commitment | Transaction, NRR, margin, data rights and eval remain P0 | PASS |
| Deterministic verdict | Unknown reversible P0 → Need more evidence | Verdict is Need more evidence | PASS |
| Reproducible coverage | Weighted numerator and denominator visible | 95 / 160 = 59.4%, rounded to 60% | PASS |
| Conditional IC behavior | NME must not produce a final recommendation memo | Output is labeled Conditional IC Pre-read | PASS |
| Falsifiability | Report states evidence that reverses verdict | Present in primary report | PASS |
| AI economics | Missing inference/human-review economics remain visible | Explicit Unknown/P0 | PASS |
| Output separation | Decision narrative does not erase evidence appendices | decisions and appendices remain separate | PASS |

## Test limitation

This is a test of skill behavior on public information, not a completed investment diligence. No data room, direct product access, customer calls, founder interview, cap table, or signed transaction documents were available.
