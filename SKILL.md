---
name: ai-startup-due-diligence
description: "Structured due diligence for AI startups: build an evidence ledger and weighted module coverage map, then produce a Q&A gap list, OnePage, IC memo, risk register, and follow-up diligence plan. Use when evaluating an AI startup or investment target, reviewing a pitch deck or data room, preparing investor or founder questions, writing a DD memo or IC note, or assessing VC-fit, product maturity, PMF, GTM maturity, fundability, and red flags."
license: MIT
metadata:
  author: PiroteQueen
  version: "1.3.1"
---

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
  → outputs: output package (Chinese Systematic DD, OnePage, Q&A gap list, IC memo, risk register, data-room request, research appendices)
```

Diligence is not "summarization"; it is **question coverage management**. A good DD result says which questions are answered, which are not, what evidence supports each answer, and what must be checked next.

## Modules

Cover these seven modules. The full key-question bank and per-module outputs are in [references/module-questions.md](references/module-questions.md). Use [references/coverage-stage-model.md](references/coverage-stage-model.md) for coverage scoring and stage classification.

1. **Basic Info / Thesis** — one-liner, why now, milestones, use of funds.
2. **Team** — founder-market fit, execution evidence, missing capabilities.
3. **Product / Technology / AI** — workflow depth, AI moat tests, model dependency risk.
4. **Traction / Market** — ICP, wedge, retention/revenue evidence, competition.
5. **Financials / Business Model** — unit economics, burn, runway, pricing.
6. **Legal / Compliance / Data Risk** — data rights, IP, licenses, procurement readiness.
7. **Capital Path / VC Fit / Fundability** — venture-scale vs good non-VC business, four-dimensional stage map, funding plan sanity, risk onion. Add this module whenever the context is an investment decision or fundraising review. Do **not** assume every good business is a good VC investment.

## Evidence ledger

Record every claim using the schema in [templates/evidence-ledger.yaml](templates/evidence-ledger.yaml).

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
- funding databases/news, press releases, Crunchbase/PitchBook/CB Insights if accessible
- customer logos, case studies, reviews, traffic/SEO signals, job postings, procurement/security docs
- competitors and substitutes, incumbent product launches, model-provider announcements
- patents, papers, open-source licenses, regulatory/compliance signals

Important: clearly separate **provided materials** from **externally verified evidence**. Cite source URLs/titles/dates where possible. If live web access is unavailable or a source cannot be accessed, say so and mark the claim as Unknown or Needs verification.

If only sparse material exists, still proceed, but mark confidence as low and produce a Q&A gap list plus an external research checklist.

#### Mandatory external-research gate

When the company, founders, product, market, or financing is identifiable, external research is **required**, not optional. Do not finalize a full IC memo from provided materials alone unless the user explicitly prohibits external research or live research tools are unavailable.

Before moving to module coverage:

1. Create a research log using [templates/external-research-log.md](templates/external-research-log.md).
2. Attempt research across the applicable source groups:
   - company-owned sources;
   - founder/team sources;
   - product/technical sources;
   - customer/traction sources;
   - financing/legal sources;
   - competitor and substitute sources.
3. Record queries attempted, sources opened, publication/source dates, access failures, and what each source proves or fails to prove.
4. Prefer primary sources for product, technical, customer, pricing, legal, and competitor claims. Use media reporting for financing or stealth-company facts when primary sources are unavailable, and label the limitation.
5. Search for disconfirming evidence, not only corroboration of the pitch.

The external-research gate passes only when:

- at least three applicable source groups have been searched;
- every high-materiality provided claim has either an external source, a documented failed search, or an explicit `Unknown` label;
- competitor research passes the dedicated gate below.

If the gate cannot pass, state `External research incomplete` prominently, lower confidence, and do not describe the output as a completed investment DD.

#### Mandatory competitor and substitute investigation

Read [references/competitor-research.md](references/competitor-research.md) and produce [templates/competitor-landscape.md](templates/competitor-landscape.md) whenever competition can materially affect product differentiation, market entry, pricing, moat, valuation, or exit outcomes.

Do not treat the competitor section as a list of similar startups. Cover the relevant layers:

- direct product competitors;
- adjacent technical approaches;
- platform/model/infrastructure providers;
- incumbent workflow or distribution owners;
- customer-built/internal alternatives;
- manual or non-consumption substitutes.

The competitor gate passes only when the analysis:

- identifies at least three competitor/substitute layers, or explains why fewer apply;
- selects 4–8 material comparables, including at least one incumbent/platform and one substitute where applicable;
- uses at least two evidence points per priority competitor, ideally one product/technical and one traction/deployment/commercial point;
- records product/version/date, benchmark or capability, customer/deployment evidence, data advantage, business model, and valuation/funding only where decision-relevant;
- compares the target and competitors on the same dimensions;
- includes at least one valuation counterexample or explains why no valid comparable exists;
- states what evidence would prove the target wins or loses.

If public evidence is sparse, preserve the empty cells as `Unknown`; do not replace the matrix with generic prose.

### Step 2 — Build module coverage

Follow the weighted scoring and gating rules in [references/coverage-stage-model.md](references/coverage-stage-model.md). Assign each question P0/P1/P2 priority, then award evidence credit of 1.0, 0.5, or 0.0. Round coverage to the nearest 5%.

Create a module table:

| Module | Weighted coverage | Unresolved P0 gates | Readiness | Confidence |
| --- | ---: | --- | --- | --- |
| Basic Info | 0–100% | ... | decision-ready / directional / incomplete / sparse | high/medium/low |
| Team | ... | ... | ... | ... |

Coverage is not amount of text or a raw answered-question count. Never let answered P2 context hide an unresolved P0 question. If a P0 unknown or contradiction could reverse the recommendation, mark the diligence **Not decision-ready** regardless of the numeric score.

Competitor evidence does not count as complete merely because competitors are named. Count the competition question as answered only after the competitor gate passes.

### Step 3 — Map stage, VC-fit, and the risk onion

Before writing a memo, force the evidence into a stage-and-risk map:

1. **Four-dimensional stage map**: Separately classify product maturity, PMF status, GTM maturity, and financing stage using [references/coverage-stage-model.md](references/coverage-stage-model.md). Give evidence and a next gate for each dimension. A financing round, polished prototype, friendly pilot, LOI, or customer logo is not proof of PMF — check traction evidence against the false-PMF and true-PMF patterns in [references/pattern-library.md](references/pattern-library.md) before classifying the PMF dimension.
2. **VC-fit**: Decide whether this can plausibly become a venture-scale outcome. A company can be a good business and still fail VC-fit if it lacks leverage, speed, market size, or exit optionality.
3. **Capital path**: Explain what the current financing buys and what milestone must be achieved before the next financing or profitability path.
4. **Risk onion**: Peel risks by layer: founder/team, market, competition, timing, financing, marketing/CAC, distribution/partner dependency, technology, product execution, hiring/org, location/ecosystem, and AI-specific dependency/compliance.
5. **VC no diagnostics**: If qualified investors said no, treat that as evidence. One no may be noise; repeated no's should trigger a specific risk-layer diagnosis and plan revision.

### Step 4 — Produce the Q&A List

Use [templates/qa-gap-list.md](templates/qa-gap-list.md). For each module, list answered questions (with evidence and confidence) and unanswered follow-ups (with why it matters and the best source to verify).

### Step 5 — Red-team the investment thesis

Run the nine contradiction checks in [references/red-team-checks.md](references/red-team-checks.md) before finalizing any recommendation. When testing AI moat claims (check 3) and traction claims (checks 1–2), match the evidence against the concrete patterns in [references/pattern-library.md](references/pattern-library.md) — a claim matching a false-PMF or wrapper-death pattern must be downgraded in the evidence ledger with a specific next check, not merely noted.

### Step 6 — Derive the verdict and generate outputs

Derive the verdict (Proceed / Watch / Pass / Need more evidence) from the rules in [references/decision-rules.md](references/decision-rules.md) — eligibility thresholds, deal-breakers, red-flag caps, Watch triggers, and the falsifiability statement. Apply [references/confidence-downgrade-rules.md](references/confidence-downgrade-rules.md) whenever material claims remain unverified, externally inaccessible, second-hand, or contradicted. Do not improvise a verdict: the same evidence must always produce the same verdict.

For pre-revenue, stealth, pre-product, unusually large financing, or unusually high valuation cases, run [references/mega-round-sanity-check.md](references/mega-round-sanity-check.md) before recommending any investment action.

### Output package behavior

When the user asks for a full diligence run, a project folder, or durable deliverables, generate a multi-file output package instead of one long chat response. Use safe, human-readable filenames and keep the decision narrative separate from evidence appendices:

| File | Purpose | Template |
| --- | --- | --- |
| `01-chinese-systematic-dd.md` | Chinese-facing investment judgment: one core question, verdict, five gates, evidence status, next actions | [templates/chinese-systematic-dd.md](templates/chinese-systematic-dd.md) |
| `02-onepage.md` | One-page decision summary for quick discussion | [templates/onepage.md](templates/onepage.md) |
| `03-qa-gap-list.md` | Answered/unanswered diligence questions with owner and source | [templates/qa-gap-list.md](templates/qa-gap-list.md) |
| `04-data-room-request.md` | Source-document request list generated from unresolved P0 gates and risk-onion layers | [templates/data-room-request.md](templates/data-room-request.md) |
| `05-ic-memo.md` | Full investment committee memo when decision-making depth is needed | [templates/ic-memo.md](templates/ic-memo.md) |
| `06-risk-register.md` | Legal, technical, commercial, AI, financing, and execution risk register | [templates/risk-register.md](templates/risk-register.md) |
| `07-competitor-landscape.md` | Same-dimension competitor/substitute landscape appendix | [templates/competitor-landscape.md](templates/competitor-landscape.md) |
| `08-external-research-log.md` | Auditable search/source log including access failures and unverified claims | [templates/external-research-log.md](templates/external-research-log.md) |

If the user only asks for a lightweight answer, produce the smallest useful subset, but always say which appendices were omitted. For Chinese users, make `01-chinese-systematic-dd.md` the primary deliverable and keep internal coverage details in appendices.

Then pick the smallest useful output first:

1. **Chinese Systematic DD** — for Chinese-facing investor/founder discussion where the user needs a coherent decision narrative instead of internal module sprawl. Template: [templates/chinese-systematic-dd.md](templates/chinese-systematic-dd.md)
2. **OnePage** — for quick investment conversation. Template: [templates/onepage.md](templates/onepage.md)
3. **Q&A List** — for founder follow-up and data room requests. Template: [templates/qa-gap-list.md](templates/qa-gap-list.md)
4. **Data Room Request** — when risk-onion layers or P0 gates require source documents before a verdict can improve. Template: [templates/data-room-request.md](templates/data-room-request.md)
5. **IC Memo** — for decision-making. Template: [templates/ic-memo.md](templates/ic-memo.md)
6. **Risk Register** — for legal/technical/commercial red flags. Template: [templates/risk-register.md](templates/risk-register.md)
7. **Competitor Landscape** — for investment decisions where differentiation, moat, valuation, or market entry matters. Template: [templates/competitor-landscape.md](templates/competitor-landscape.md)
8. **External Research Log** — evidence of what was actively searched and what remained inaccessible. Template: [templates/external-research-log.md](templates/external-research-log.md)
9. **BP / Slide critique** — if reviewing fundraising materials.

For follow-up data requests, group asks by owner: Founder/CEO, CTO/product lead, Finance, Customers, Legal/compliance, Public research. Risk-onion output should point to the next evidence request, interview, or external verification action, not just list abstract risks.

## Multi-agent execution (optional)

If the host environment supports subagents or parallel tasks, follow the topology in [references/orchestration.md](references/orchestration.md): fan out module research to parallel agents (each producing only evidence-ledger entries), run red-teaming in an independent context that sees the ledger but never the draft narrative, and keep the verdict single-threaded in the orchestrator. If subagents are unavailable, run the workflow above sequentially — the artifacts and rules are identical.

## Quality bar

A good answer must:

- separate evidence from inference;
- show missing questions, not hide them;
- use weighted coverage and surface unresolved P0 gates;
- include AI-specific moat and dependency analysis;
- include VC-fit, the four-dimensional stage map, capital path, and risk-onion analysis when the context is investment or fundraising;
- separate good-business potential from venture-scale potential;
- include both why it can work and why it may fail;
- derive the verdict from the decision rules and state what evidence would reverse it;
- give next verification actions, not just a narrative.
- show that external research was actively attempted when the target is identifiable;
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
