<!--
[INPUT]: 依赖模块问题优先级、证据状态与四维阶段事实
[OUTPUT]: 对外提供加权覆盖率、门禁、就绪度和阶段分类规则
[POS]: references/diligence 的量化模型，连接证据台账与决策规则
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Coverage and Stage Model

Use this model whenever reporting diligence coverage or company stage. It prevents low-value answers from inflating coverage and prevents financing labels from masquerading as product or PMF evidence.

## Weighted coverage

### Question priority

Assign every key question a priority before scoring:

- **P0 / gating** — weight 3. The answer can change the investment decision, expose a deal-breaker, or block a reliable recommendation.
- **P1 / important** — weight 2. Material to the thesis, valuation, execution plan, or risk assessment.
- **P2 / contextual** — weight 1. Useful context but unlikely to change the decision by itself.

Typical P0 questions include data rights, founder/IP ownership, runway survival, retention or repeated usage, material customer concentration, security/compliance blockers, financing terms, and evidence required to support a PMF claim. Adapt the list to the company and deal.

### Answer credit

Score each question using evidence status and evidence strength:

| Answer state | Credit |
| --- | ---: |
| Known, supported by strong direct or independently corroborated evidence | 1.0 |
| Known but supported by limited, stale, or single-source evidence | 0.5 |
| Inferred | 0.5 |
| Unknown | 0.0 |
| Contradiction | 0.0 |

Do not award full credit merely because management answered the question. Record the answer, then judge the supporting evidence.

### Formula

```text
weighted coverage =
  sum(question weight × answer credit)
  / sum(question weight)
  × 100
```

Round to the nearest 5%. Always show the score inputs or at least the P0/P1/P2 status counts; do not present an unexplained precise percentage.

For every module and the overall score, show `weighted points earned / weighted points possible`. A percentage without this denominator is invalid. The overall score must be recomputed from all underlying questions, not averaged from already-rounded module percentages.

Use these interpretation bands:

- **80–100% / decision-ready** — major questions are strongly evidenced and no unresolved gating question blocks the decision.
- **60–79% / directional** — enough evidence for a preliminary view, but material verification remains.
- **40–59% / incomplete** — suitable for planning follow-up diligence, not a firm recommendation.
- **0–39% / sparse** — evidence is too limited for more than hypotheses and a request list.

### Gating rule

Coverage and decision readiness are separate:

- List every unresolved P0 question explicitly.
- If any unresolved P0 question could reverse the recommendation or reveal a deal-breaker, mark the module and overall diligence **Not decision-ready**, regardless of the numeric score.
- A contradiction on a P0 question requires resolution or an explicit conditional decision.
- Never average a critical unknown away with many answered P2 questions.

## Four-dimensional stage model

Do not use one mixed `stage` field. Report four independent dimensions, each with evidence and a next gate.

### 1. Product maturity

- **concept** — problem and proposed solution, no working product.
- **prototype** — demonstrable proof of concept, not yet reliable for real users.
- **mvp** — usable product in live or pilot workflows with limited scope.
- **production** — repeatable real-world use with operational reliability and support.
- **scaled_product** — proven at materially larger volume, complexity, or enterprise requirements.
- **unknown**

### 2. PMF status

- **untested** — no meaningful customer validation.
- **problem_validation** — pain and urgency are evidenced, but the solution is not validated.
- **solution_validation** — users adopt or pay, but retention and repeatability are not yet proven. This is BPMF.
- **repeatable_pmf** — retention, repeated usage, willingness to pay, and a repeatable ICP/use case are evidenced. This is APMF.
- **expanding_pmf** — repeatable PMF plus credible expansion across accounts, use cases, or segments.
- **unknown**

Do not infer PMF from a polished product, pilots, LOIs, fundraising, customer logos, pipeline, or one-off revenue.

### 3. GTM maturity

- **no_motion** — no repeatable acquisition or sales process.
- **founder_led** — founders acquire and close early customers manually.
- **emerging_repeatability** — a defined ICP, channel, and sales process show early repeatability.
- **repeatable_motion** — conversion, cycle, retention, and economics are sufficiently consistent to plan growth.
- **scalable_motion** — multiple reps/channels or self-serve acquisition scale without unacceptable efficiency decay.
- **unknown**

### 4. Financing stage

- **bootstrapped**
- **pre_seed**
- **seed**
- **series_a**
- **series_b_plus**
- **profitable_or_self_funded**
- **unknown**

Financing stage describes capital history, not company maturity. Never use a round label as evidence of product maturity, PMF, or GTM repeatability.

## Stage output

For each dimension record:

| Dimension | Current state | Evidence | Confidence | Next gate |
| --- | --- | --- | --- | --- |
| Product maturity |  |  |  |  |
| PMF status |  |  |  |  |
| GTM maturity |  |  |  |  |
| Financing stage |  |  |  |  |

If evidence conflicts, use `unknown` or the lower defensible state and record the contradiction.
