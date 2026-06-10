---
name: ai-startup-due-diligence
description: "Structured due diligence for AI startups: build an evidence ledger and module coverage map, then produce a Q&A gap list, OnePage, IC memo, risk register, and follow-up diligence plan. Use when evaluating an AI startup or investment target, reviewing a pitch deck or data room, preparing investor or founder questions, writing a DD memo or IC note, or assessing VC-fit, stage (BPMF/APMF), fundability, and red flags."
license: MIT
metadata:
  author: PiroteQueen
  version: "1.2.0"
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
  → stage gate / VC-fit / capital path
  → outputs: Q&A List, OnePage, IC memo, risk register, follow-up plan
```

Diligence is not "summarization"; it is **question coverage management**. A good DD result says which questions are answered, which are not, what evidence supports each answer, and what must be checked next.

## Modules

Cover these seven modules. The full key-question bank and per-module outputs are in [references/module-questions.md](references/module-questions.md) — read it when building coverage.

1. **Basic Info / Thesis** — one-liner, why now, milestones, use of funds.
2. **Team** — founder-market fit, execution evidence, missing capabilities.
3. **Product / Technology / AI** — workflow depth, AI moat tests, model dependency risk.
4. **Traction / Market** — ICP, wedge, retention/revenue evidence, competition.
5. **Financials / Business Model** — unit economics, burn, runway, pricing.
6. **Legal / Compliance / Data Risk** — data rights, IP, licenses, procurement readiness.
7. **Capital Path / VC Fit / Fundability** — venture-scale vs good non-VC business, stage gate, funding plan sanity, risk onion. Add this module whenever the context is an investment decision or fundraising review. Do **not** assume every good business is a good VC investment.

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

Create a module table:

| Module | Coverage | Key answered questions | Key gaps | Confidence |
| --- | --- | --- | --- | --- |
| Basic Info | 0–100% | ... | ... | high/medium/low |
| Team | ... | ... | ... | ... |

Coverage is not amount of text; it is `answered key questions / total key questions`.

Competitor evidence does not count as complete merely because competitors are named. Count the competition question as answered only after the competitor gate passes.

### Step 3 — Map stage, VC-fit, and the risk onion

Before writing a memo, force the evidence into a stage-and-risk map:

1. **Stage gate**: Idea / MVP / Launch / Scale, or BPMF / APMF. State the evidence for the stage; do not let a polished deck, prototype, or friendly pilot masquerade as PMF.
2. **VC-fit**: Decide whether this can plausibly become a venture-scale outcome. A company can be a good business and still fail VC-fit if it lacks leverage, speed, market size, or exit optionality.
3. **Capital path**: Explain what the current financing buys and what milestone must be achieved before the next financing or profitability path.
4. **Risk onion**: Peel risks by layer: founder/team, market, competition, timing, financing, marketing/CAC, distribution/partner dependency, technology, product execution, hiring/org, location/ecosystem, and AI-specific dependency/compliance.
5. **VC no diagnostics**: If qualified investors said no, treat that as evidence. One no may be noise; repeated no's should trigger a specific risk-layer diagnosis and plan revision.

### Step 4 — Produce the Q&A List

Use [templates/qa-gap-list.md](templates/qa-gap-list.md). For each module, list answered questions (with evidence and confidence) and unanswered follow-ups (with why it matters and the best source to verify).

### Step 5 — Red-team the investment thesis

Run the nine contradiction checks in [references/red-team-checks.md](references/red-team-checks.md) before finalizing any recommendation.

### Step 6 — Generate outputs

Pick the smallest useful output first:

1. **OnePage** — for quick investment conversation. Template: [templates/onepage.md](templates/onepage.md)
2. **Q&A List** — for founder follow-up and data room requests. Template: [templates/qa-gap-list.md](templates/qa-gap-list.md)
3. **IC Memo** — for decision-making. Template: [templates/ic-memo.md](templates/ic-memo.md)
4. **Risk Register** — for legal/technical/commercial red flags. Template: [templates/risk-register.md](templates/risk-register.md)
5. **Competitor Landscape** — for investment decisions where differentiation, moat, valuation, or market entry matters. Template: [templates/competitor-landscape.md](templates/competitor-landscape.md)
6. **External Research Log** — evidence of what was actively searched and what remained inaccessible. Template: [templates/external-research-log.md](templates/external-research-log.md)
7. **BP / Slide critique** — if reviewing fundraising materials.

For follow-up data requests, group asks by owner: Founder/CEO, CTO/product lead, Finance, Customers, Legal/compliance, Public research.

## Quality bar

A good answer must:

- separate evidence from inference;
- show missing questions, not hide them;
- include AI-specific moat and dependency analysis;
- include VC-fit, stage, capital path, and risk-onion analysis when the context is investment or fundraising;
- separate good-business potential from venture-scale potential;
- include both why it can work and why it may fail;
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
