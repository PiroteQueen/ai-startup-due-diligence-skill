<!--
[INPUT]: 依赖覆盖率、P0 门禁、红队结果、阶段、VC-fit 与置信度降级
[OUTPUT]: 对外提供 Proceed、Watch、Pass、Need more evidence 的确定性映射
[POS]: references/diligence 的最终裁决规则，保证同一证据导出同一结论
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Decision Rules

Rules for mapping evidence state to a verdict: **Proceed / Watch / Pass / Need more evidence**. Apply after coverage scoring ([coverage-stage-model.md](coverage-stage-model.md)) and red-teaming ([red-team-checks.md](red-team-checks.md), [pattern-library.md](pattern-library.md)). A verdict is derived from these rules, not improvised — the same evidence must always produce the same verdict.

## The asymmetry principle

Saying **Proceed** requires broad, strong evidence. Saying **Pass** requires only one confirmed deal-breaker. Never hold a negative finding to the coverage standard required for a positive recommendation.

## Verdict eligibility

| Verdict | Eligibility conditions (all must hold) |
| --- | --- |
| **Proceed** | Thesis-critical modules decision-ready (≥80% weighted coverage); zero unresolved P0 questions; zero unresolved contradictions; no confirmed deal-breaker; VC-fit = venture_scale (when the mandate is venture investing); PMF dimension consistent with the claimed stage after pattern-library checks. |
| **Watch** | Overall coverage ≥60% (directional); at most 2 unresolved P0 questions, each with a defined re-engagement trigger; no confirmed deal-breaker. |
| **Pass** | At least one deal-breaker confirmed with strong evidence (1.0-credit quality), at any coverage level; **or** VC-fit assessed as good_non_vc_business / not_fundable_yet under a venture mandate with decision-ready evidence on that assessment. |
| **Need more evidence** | Default verdict whenever coverage <60%, or any P0 question that could reverse the verdict is Unknown or Contradicted. Output is the Q&A gap list and follow-up plan. A full-package IC file, if explicitly required, must be labeled `Conditional IC Pre-read — Not decision-ready` and must not recommend investing. |

Thesis-critical modules are the modules the investment thesis actually rests on (typically Product/Technology, AI Product & Capability Strategy, Traction/Market, and Capital Path; adjust per deal and say which ones you chose).

## Deal-breakers (confirmed = Pass, regardless of everything else)

A deal-breaker must be **confirmed** — supported by strong direct or independently corroborated evidence, not inferred. Suspected deal-breakers are P0 unknowns, not verdicts.

1. Founder misrepresentation of independently verifiable facts (credentials, revenue, customers, ownership).
2. No legal rights to core training data or core IP, with no feasible cure.
3. Unresolved contradiction in revenue, retention, or customer claims after direct confrontation with the source.
4. Cap table or preference stack that destroys exit economics for new investors at plausible outcomes.
5. Core technical claim demonstrated infeasible, or the product demonstrably does not perform its core claim.
6. Regulatory or compliance exposure that prohibits the core business in its primary market.

This list is a floor, not a ceiling — add deal-specific deal-breakers during Step 2 and label them P0.

## Red-flag arithmetic (pattern library → verdict caps)

Pattern matches act as caps on the verdict, not just notes:

- **≥2 unresolved founder/team red flags** → verdict capped at Watch.
- **PMF dimension downgraded by false-PMF patterns** → traction cannot be cited as a Proceed reason; verdict capped at Watch until a true-PMF signal is verified.
- **≥1 unmitigated AI-wrapper death pattern** on a thesis that depends on product moat → verdict capped at Watch; Proceed requires written mitigation evidence.
- **Fundraising red flags 1–2 (no theory / no buffer)** unresolved → cap at Watch; the capital plan is part of the thesis.
- A cap is released only when the underlying pattern match is resolved with evidence in the ledger — not by narrative reassurance.

## Watch requires triggers

A bare Watch is forbidden. Every Watch verdict must list 1–3 concrete re-engagement triggers, each naming the evidence and a time bound, for example:

- "First cohort passes its renewal date (Q3) with ≥80% logo retention."
- "Product survives the next frontier-model release without losing its core differentiation."
- "Two paying customers verified outside the founders' personal network."

If no meaningful trigger can be written, the honest verdict is Pass or Need more evidence.

## Falsifiability statement

Every verdict must end with one sentence: **"This verdict reverses if: ..."** naming the specific evidence that would flip it. A verdict that cannot be reversed by evidence is a position, not a judgment. This applies the doubt-avoidance discipline from the pattern library to the analyst as well as the founder.

## Decision gates format (IC memo section 13)

Each gate is a row, not a heading:

| Gate | Evidence threshold | Deadline | Owner | If missed |
| --- | --- | --- | --- | --- |
| e.g. Paid conversion | ≥2 pilots convert at list price | end of Q3 | Founder/CEO | revert to Pass |

A gate without an evidence threshold and an if-missed action is a wish, not a gate.
