<!--
[INPUT]: 依赖融资规模、估值、阶段、交易结构、用途与经营证据
[OUTPUT]: 对外提供超大融资和高估值项目的专项计算、门禁与反证
[POS]: references/diligence 的异常交易校验器，阻止融资规模冒充业务去风险
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Mega-Round Sanity Check

Use this reference when an AI startup is raising or has raised an unusually large round before clear revenue, PMF, product maturity, or public deployment evidence. This check prevents "large financing" from being mistaken for de-risking.

## Trigger

Run this check when any of these are true:

- pre-revenue, stealth, or pre-product company;
- financing size is far larger than normal stage norms;
- valuation implies category-winner status before product/market proof;
- memo emphasizes famous founders, strategic backers, GPU scale, holding-company strategy, or capital accumulation more than customer evidence;
- round is presented through SPV, allocation, secondary, or indirect access;
- public information supports company existence but not the specific round terms.

## Core question

> Does the mega-round buy the next stage of evidence, or does it merely raise the valuation and organizational risk before the core risk has been removed?

## Required calculations

| Calculation | Formula | Interpretation |
|---|---|---|
| Implied pre-money | post-money - primary round | How much success is already priced in |
| New investor ownership | primary round / post-money | Whether risk/reward is reasonable |
| Capital per employee/researcher | total capital / headcount | Capital intensity and org risk |
| Round per employee/researcher | round size / headcount | Whether funding exceeds execution capacity |
| Exit multiple needed | target return × post-money | Required exit value for fund-returning outcome |
| Next-round step-up required | next valuation / current valuation | Whether future financing is plausible |

## Evidence gates

| Gate | What must be proven | Evidence required | If missing |
|---|---|---|---|
| Transaction reality | The round, price, and allocation are real | signed term sheet, cap table, allocation confirmation | cannot Proceed |
| Use of funds | Money buys concrete milestones | budget, hiring plan, compute plan, deployment milestones | Watch / Need more evidence |
| Product maturity | Company can absorb capital into product progress | demo, benchmark, roadmap, technical diligence | technical confidence capped low |
| Market pull | Customers or internal deployments justify scale | contracts, paid pilots, usage, LOI quality | PMF cannot be claimed |
| Capital path | Next financing or exit path is plausible | milestone-to-next-round model, exit comparables | valuation may be overfit |
| Governance | Investor rights are not structurally impaired | legal docs, SPV terms, information rights | rights risk high |

## Red flags

- The memo uses financing size as the main proof of quality.
- Famous investor or founder name substitutes for operating evidence.
- The company has GPU/compute claims but no workload, benchmark, or customer deployment evidence.
- The round size is much larger than the next 12–24 months of executable milestones.
- The valuation already requires an exceptional exit before PMF is proven.
- The current round depends on a future holding company, acquisition strategy, or platform narrative that has not started.
- The investment entry is via a secondary/SPV layer with weak information or transfer rights.

## Decision effects

- If transaction documents are absent: verdict cannot exceed **Need more evidence**.
- If product and customer evidence are absent: verdict cannot exceed **Watch**, regardless of founder prestige.
- If valuation requires a top-decile exit and PMF is unproven: mark valuation as **likely pre-paid success**.
- If use-of-funds does not map to specific next-stage evidence: treat the financing as **narrative expansion**, not de-risking.
- If liquidation preference or indirect access structure is unclear: block Proceed until legal review.

## Output format

```markdown
### Mega-round sanity check

- 本轮融资：...
- 投后估值：...
- 推算投前估值：...
- 新投资人持股：...
- 资金强度：...
- 当前阶段：...
- 本轮资金购买的下一阶段证据：...
- 最大估值风险：...
- 结论影响：Proceed / Watch / Pass / Need more evidence
```
