---
name: ai-startup-due-diligence
description: "Evidence-driven due diligence for AI startups: turns decks, interviews, demos, and public research into an auditable evidence ledger, then derives a verdict and decision documents. Use when evaluating an AI startup or investment target, reviewing a pitch deck or data room, comparing companies' AI products, preparing investor or founder questions, writing a DD memo or IC note, or assessing VC-fit, PMF, GTM maturity, fundability, and red flags."
license: MIT
metadata:
  author: PiroteQueen
  version: "1.4.0"
---

<!--
[INPUT]: 依赖 references/ 的尽调规则与 templates/ 的输出契约
[OUTPUT]: 对外提供 AI 创业公司尽调的完整工作流、门禁与交付物导航
[POS]: 项目核心技能入口，统领证据研究、模块覆盖、判断与输出
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# AI Startup Due Diligence

Use this skill when the user is evaluating an AI startup, reviewing an investment target, preparing diligence questions, or asking for a DD memo / IC note / OnePage / red-flag analysis.

## Core mental model

Do not start by writing a fluent memo. Start by building a **diligence evidence ledger**:

```text
Target company
  → modules
  → key questions
  → evidence-backed answers
  → unanswered gaps
  → confidence / contradiction / red flags
  → four-dimensional stage map / VC-fit / capital path
  → outputs: smallest useful subset by default, full output package on request
```

Diligence is not "summarization"; it is **question coverage management**. A good DD result says which questions are answered, which are not, what evidence supports each answer, and what must be checked next.

## Modules

Cover these eight modules. The full key-question bank and per-module outputs are in [references/diligence/module-questions.md](references/diligence/module-questions.md). Use [references/diligence/coverage-stage-model.md](references/diligence/coverage-stage-model.md) for coverage scoring and stage classification.

1. **Basic Info / Thesis** — one-liner, why now, milestones, use of funds.
2. **Team** — founder-market fit, execution evidence, missing capabilities.
3. **Product / Technology** — workflow depth, architecture, integrations, reliability, delivery risk.
4. **AI Product & Capability Strategy** — AI feature portfolio, user value, build/buy/model choices, adoption, monetization, moat, and model/platform dependency.
5. **Traction / Market** — ICP, wedge, retention/revenue evidence, competition.
6. **Financials / Business Model** — unit economics, burn, runway, pricing.
7. **Legal / Compliance / Data Risk** — data rights, IP, licenses, procurement readiness.
8. **Capital Path / VC Fit / Fundability** — venture-scale vs good non-VC business, four-dimensional stage map, funding plan sanity, risk onion. Add this module whenever the context is an investment decision or fundraising review. Do **not** assume every good business is a good VC investment.

## Evidence ledger

Record every claim using the schema in [templates/appendices/evidence-ledger.yaml](templates/appendices/evidence-ledger.yaml).

Never turn missing evidence into a confident conclusion. Use labels:

- **Known**: directly supported by source evidence.
- **Inferred**: reasonable but not directly proven.
- **Unknown**: must be asked or verified.
- **Contradiction**: sources conflict.

## Workflow

### Step 1 — Intake and external research

Collect available materials from the user: pitch deck, memo, website, demo notes, founder interview transcript, product screenshots, financials, customer references.

Then, when the target company, founders, product name, or market is identifiable, actively gather external evidence instead of relying only on provided materials. Use web/search tools as needed for:

- company website, docs, blog, changelog, pricing, terms, privacy policy, security page
- founder/team LinkedIn, GitHub, Google Scholar, personal sites, prior companies, interviews
- Product Hunt, G2, app stores, Chrome extension store, Hugging Face, GitHub repos, package registries
- financing announcements, regulatory filings, investor portfolio pages, reputable reporting, and funding databases if accessible
- customer logos, case studies, reviews, traffic/SEO signals, job postings, procurement/security docs
- competitors and substitutes, incumbent product launches, model-provider announcements
- patents, papers, open-source licenses, regulatory/compliance signals

Important: clearly separate **provided materials** from **externally verified evidence**. Cite source URLs/titles/dates where possible. If live web access is unavailable or a source cannot be accessed, say so and mark the claim as Unknown or Needs verification.

Read [references/research/source-access-strategy.md](references/research/source-access-strategy.md) before external research. Select sources by the claim being tested, not by database habit. Crunchbase, PitchBook, CB Insights, LinkedIn, and other blocked/paywalled sources are optional leads, never mandatory evidence gates. After one failed access attempt, record the failure and switch to the prescribed fallback ladder; do not spend the research budget repeatedly retrying one domain.

If only sparse material exists, still proceed, but mark confidence as low and produce a Q&A gap list plus an external research checklist.

#### Mandatory external-research gate

When the company, founders, product, market, or financing is identifiable, external research is **required**, not optional. Do not finalize a full IC memo from provided materials alone unless the user explicitly prohibits external research or live tools are unavailable.

Before module coverage: create a research log ([templates/appendices/external-research-log.md](templates/appendices/external-research-log.md)), then route every material claim through the claim-specific ladders and the completion test in [references/research/source-access-strategy.md](references/research/source-access-strategy.md). Prefer primary sources for product, technical, customer, pricing, legal, and competitor claims; search for disconfirming evidence, not only corroboration.

The gate passes only when the source-strategy completion test and the competitor gate below both pass. If it cannot, state `External research incomplete` prominently, lower confidence, and do not describe the output as a completed investment DD.

#### Mandatory competitor and substitute investigation

Whenever competition can materially affect differentiation, market entry, pricing, moat, valuation, or exit, follow [references/research/competitor-research.md](references/research/competitor-research.md) and produce [templates/appendices/competitor-landscape.md](templates/appendices/competitor-landscape.md). Cover the six competitor/substitute layers — do not reduce competition to a list of similar startups — and pass the gate defined in that reference (§10: layers covered, 4–8 comparables including an incumbent/platform and a substitute, two evidence points each, same-dimension matrix, a valuation counterexample, and stated win/lose evidence). If public evidence is sparse, keep cells `Unknown`; do not replace the matrix with prose.

#### Mandatory AI product and capability strategy

Whenever the target or a material competitor offers AI functionality, products, models, agents, copilots, automation, or infrastructure, treat AI product/capability strategy as a **standalone analysis**, not a paragraph hidden inside Product / Technology. Follow [references/research/ai-product-strategy.md](references/research/ai-product-strategy.md) and produce [templates/appendices/ai-product-strategy.md](templates/appendices/ai-product-strategy.md): separate announced from generally available, workflow value from capability claims, in-house from third-party, adoption from demos, and feature parity from strategic advantage. Pass the gate in that reference (§8: same dated dimensions for target and each priority competitor, every material feature labeled `live`/`beta/pilot`/`announced`/`retired`/`unknown`, access failures visible).

### Step 2 — Build module coverage

Follow the weighted scoring and gating rules in [references/diligence/coverage-stage-model.md](references/diligence/coverage-stage-model.md). Assign each question P0/P1/P2 priority, then award evidence credit of 1.0, 0.5, or 0.0. Round coverage to the nearest 5%.

Create a module table:

| Module | Weighted coverage | Unresolved P0 gates | Readiness | Confidence |
| --- | ---: | --- | --- | --- |
| Basic Info | 0–100% | ... | decision-ready / directional / incomplete / sparse | high/medium/low |
| Team | ... | ... | ... | ... |
| AI Product & Capability Strategy | ... | ... | ... | ... |

Coverage is not amount of text or a raw answered-question count. Never let answered P2 context hide an unresolved P0 question. If a P0 unknown or contradiction could reverse the recommendation, mark the diligence **Not decision-ready** regardless of the numeric score.

Competitor evidence does not count as complete merely because competitors are named. Count the competition question as answered only after the competitor gate passes.

### Step 3 — Map stage, VC-fit, and the risk onion

Before writing a memo, force the evidence into a stage-and-risk map:

1. **Four-dimensional stage map**: Separately classify product maturity, PMF status, GTM maturity, and financing stage using [references/diligence/coverage-stage-model.md](references/diligence/coverage-stage-model.md). Give evidence and a next gate for each dimension. A financing round, polished prototype, friendly pilot, LOI, or customer logo is not proof of PMF — check traction evidence against the false-PMF and true-PMF patterns in [references/diligence/pattern-library.md](references/diligence/pattern-library.md) before classifying the PMF dimension.
2. **VC-fit**: Decide whether this can plausibly become a venture-scale outcome. A company can be a good business and still fail VC-fit if it lacks leverage, speed, market size, or exit optionality.
3. **Capital path**: Explain what the current financing buys and what milestone must be achieved before the next financing or profitability path.
4. **Risk onion**: Peel risks by layer: founder/team, market, competition, timing, financing, marketing/CAC, distribution/partner dependency, technology, product execution, hiring/org, location/ecosystem, and AI-specific dependency/compliance.
5. **VC no diagnostics**: If qualified investors said no, treat that as evidence. One no may be noise; repeated no's should trigger a specific risk-layer diagnosis and plan revision.

### Step 4 — Produce the Q&A List

Use [templates/decisions/qa-gap-list.md](templates/decisions/qa-gap-list.md). For each module, list answered questions (with evidence and confidence) and unanswered follow-ups (with why it matters and the best source to verify).

### Step 5 — Red-team the investment thesis

Run the nine contradiction checks in [references/diligence/red-team-checks.md](references/diligence/red-team-checks.md) before finalizing any recommendation. When testing AI moat claims (check 3) and traction claims (checks 1–2), match the evidence against the concrete patterns in [references/diligence/pattern-library.md](references/diligence/pattern-library.md) — a claim matching a false-PMF or wrapper-death pattern must be downgraded in the evidence ledger with a specific next check, not merely noted.

### Step 6 — Derive the verdict and generate outputs

Derive the verdict (Proceed / Watch / Pass / Need more evidence) from the rules in [references/diligence/decision-rules.md](references/diligence/decision-rules.md) — eligibility thresholds, deal-breakers, red-flag caps, Watch triggers, and the falsifiability statement. Apply [references/diligence/confidence-downgrade-rules.md](references/diligence/confidence-downgrade-rules.md) whenever material claims remain unverified, externally inaccessible, second-hand, or contradicted. Do not improvise a verdict: the same evidence must always produce the same verdict.

For pre-revenue, stealth, pre-product, unusually large financing, or unusually high valuation cases, run [references/diligence/mega-round-sanity-check.md](references/diligence/mega-round-sanity-check.md) before recommending any investment action.

### Output package behavior

Default to the smallest useful output for the question asked. Generate the full multi-file package only when the user asks for a full diligence run, a project folder, or durable deliverables — then use safe, human-readable filenames and keep the decision narrative separate from evidence appendices:

| File | Purpose | Template |
| --- | --- | --- |
| `01-chinese-systematic-dd.md` | Chinese-facing investment judgment: one core question, verdict, five gates, evidence status, next actions | [templates/decisions/chinese-systematic-dd.md](templates/decisions/chinese-systematic-dd.md) |
| `02-onepage.md` | One-page decision summary for quick discussion | [templates/decisions/onepage.md](templates/decisions/onepage.md) |
| `03-qa-gap-list.md` | Answered/unanswered diligence questions with owner and source | [templates/decisions/qa-gap-list.md](templates/decisions/qa-gap-list.md) |
| `04-data-room-request.md` | Source-document request list generated from unresolved P0 gates and risk-onion layers | [templates/decisions/data-room-request.md](templates/decisions/data-room-request.md) |
| `05-ic-memo.md` | Full IC memo only for Proceed/Watch/Pass; conditional IC pre-read for Need more evidence | [templates/decisions/ic-memo.md](templates/decisions/ic-memo.md) |
| `06-risk-register.md` | Legal, technical, commercial, AI, financing, and execution risk register | [templates/decisions/risk-register.md](templates/decisions/risk-register.md) |
| `07-competitor-landscape.md` | Same-dimension competitor/substitute landscape appendix | [templates/appendices/competitor-landscape.md](templates/appendices/competitor-landscape.md) |
| `08-ai-product-strategy.md` | Standalone target-and-competitor AI feature, product, adoption, monetization, moat, and dependency analysis | [templates/appendices/ai-product-strategy.md](templates/appendices/ai-product-strategy.md) |
| `09-external-research-log.md` | Auditable search/source log including fallback paths, access failures, and unverified claims | [templates/appendices/external-research-log.md](templates/appendices/external-research-log.md) |

Whenever you produce less than the full package, say which appendices were omitted. For Chinese users, make `01-chinese-systematic-dd.md` the primary deliverable and keep internal coverage details in appendices.

When the derived verdict is `Need more evidence`, do not write a final recommendation memo. If a full durable package was explicitly requested, `05-ic-memo.md` may exist only as a prominently labeled **Conditional IC Pre-read — Not decision-ready**. It must preserve the `Need more evidence` verdict, list blocking P0 gates, and contain no investment recommendation beyond the next diligence action.

Then pick the smallest useful output first:

1. **Chinese Systematic DD** — for Chinese-facing investor/founder discussion where the user needs a coherent decision narrative instead of internal module sprawl. Template: [templates/decisions/chinese-systematic-dd.md](templates/decisions/chinese-systematic-dd.md)
2. **OnePage** — for quick investment conversation. Template: [templates/decisions/onepage.md](templates/decisions/onepage.md)
3. **Q&A List** — for founder follow-up and data room requests. Template: [templates/decisions/qa-gap-list.md](templates/decisions/qa-gap-list.md)
4. **Data Room Request** — when risk-onion layers or P0 gates require source documents before a verdict can improve. Template: [templates/decisions/data-room-request.md](templates/decisions/data-room-request.md)
5. **IC Memo** — for decision-making. Template: [templates/decisions/ic-memo.md](templates/decisions/ic-memo.md)
6. **Risk Register** — for legal/technical/commercial red flags. Template: [templates/decisions/risk-register.md](templates/decisions/risk-register.md)
7. **Competitor Landscape** — for investment decisions where differentiation, moat, valuation, or market entry matters. Template: [templates/appendices/competitor-landscape.md](templates/appendices/competitor-landscape.md)
8. **AI Product Strategy** — for a dated, same-dimension analysis of the target's and competitors' AI functionality and strategic position. Template: [templates/appendices/ai-product-strategy.md](templates/appendices/ai-product-strategy.md)
9. **External Research Log** — evidence of what was actively searched, which fallback routes were used, and what remained inaccessible. Template: [templates/appendices/external-research-log.md](templates/appendices/external-research-log.md)
10. **BP / Slide critique** — if reviewing fundraising materials.

For follow-up data requests, group asks by owner: Founder/CEO, CTO/product lead, Finance, Customers, Legal/compliance, Public research. Risk-onion output should point to the next evidence request, interview, or external verification action, not just list abstract risks.

## Multi-agent execution (optional)

If the host environment supports subagents or parallel tasks, follow the topology in [references/research/orchestration.md](references/research/orchestration.md): fan out module research to parallel agents (each producing only evidence-ledger entries), run red-teaming in an independent context that sees the ledger but never the draft narrative, and keep the verdict single-threaded in the orchestrator. If subagents are unavailable, run the workflow above sequentially — the artifacts and rules are identical.

## Quality bar

A good answer must:

- separate evidence from inference;
- show missing questions, not hide them;
- use weighted coverage and surface unresolved P0 gates;
- include AI-specific moat and dependency analysis;
- keep AI product/capability strategy as a dedicated module and appendix rather than burying it in general product prose;
- include VC-fit, the four-dimensional stage map, capital path, and risk-onion analysis when the context is investment or fundraising;
- separate good-business potential from venture-scale potential;
- include both why it can work and why it may fail;
- derive the verdict from the decision rules and state what evidence would reverse it;
- give next verification actions, not just a narrative.
- show that external research was actively attempted when the target is identifiable;
- route around blocked/paywalled sources and avoid treating Crunchbase or any single database as required;
- keep a source-dated competitor matrix with comparable evidence dimensions;
- retain competitor evidence in a dedicated appendix even when the IC memo summarizes it;

Avoid:

- generic market-size optimism;
- unverified AI moat claims;
- treating a polished deck as proof;
- treating fundraising as an accomplishment by itself;
- assuming VC money is right for every startup;
- ignoring repeated investor no's instead of diagnosing the risk layer;
- converting unknowns into assumptions;
- writing an IC memo before making a Q&A gap list.
- claiming a completed DD after only reading user-provided materials when external research was possible;
- compressing competitor research into names and generic positioning without products, dates, deployments, substitutes, and source links.
