<!--
[INPUT]: 依赖虚构公司的最小材料与技能预期行为
[OUTPUT]: 对外提供无真实公司数据的回归测试输入
[POS]: examples/sample-ai-company 的示例材料，用于验证证据降级与阶段分离
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Sample AI Company Brief

This is a fictional example for testing the skill package.

## Provided material

- Company claims it automates enterprise customer support using AI agents.
- Founders previously worked in support operations and ML infrastructure.
- The deck claims three pilots but does not provide retention, revenue, or customer references.

## Expected analysis behavior

The skill should mark traction as low-credit evidence, treat retention and customer validation as unresolved P0 gates, and ask for pilot usage data, customer references, pricing, model evaluation metrics, and data/privacy posture before writing a confident IC memo.

It should also produce a standalone AI product strategy section, label the agent capability status as unverified, separate the product claim from adoption evidence, and request model-route, inference-cost, packaging, and feature-level usage data.

It should classify stage dimensions separately rather than calling the company simply "MVP" or "BPMF":

- product maturity: likely MVP, subject to demo and production-use verification
- PMF status: solution validation at most; repeatable PMF is not evidenced
- GTM maturity: founder-led or unknown
- financing stage: unknown
