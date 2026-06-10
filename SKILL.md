---
name: ai-startup-due-diligence
description: "Use for AI startup due diligence: turn scattered evidence into a structured investment memo, Q&A gap list, OnePage, risk register, and follow-up diligence plan. Based on the user’s DDyst project logic."
---

# AI Startup Due Diligence

Use this skill when the user is evaluating an AI startup, reviewing an investment target, preparing diligence questions, or asking for a DD memo / IC note / OnePage / red-flag analysis.

This skill is distilled from the DDyst project (`/Users/Hanxue/Desktop/Lucky5.org/DDyst` and `DDyst_admin`): modular diligence, key questions (`key_q`), evidence-backed answers (`key_q_answers`), completion status, AI-assisted gap detection, report export, OnePage, Q&A list, raw story, and co-analysis.

It is also reinforced by the user's Obsidian `The Future` VC / AI-startup synthesis, especially `outputs/ai-startup-dd-skill-vc-ask-20260610.md`, `wiki/concepts/创业融资与 VC 风险分层.md`, `wiki/concepts/产品市场契合 PMF.md`, `wiki/concepts/AI 原生创业生命周期.md`, and raw pmarca / Andreessen articles on VC fundability, PMF, risk onion, and funding amount.

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

DDyst’s reusable insight is that diligence is not “summarization”; it is **question coverage management**. A good DD result says which questions are answered, which are not, what evidence supports each answer, and what must be checked next.

## Default modules

Start with DDyst’s original five modules, then add AI-specific and investment-risk overlays.

### 1. Basic Info / Thesis

Key questions:
- What is the company thesis and product vision?
- Why did the founders choose this idea?
- What do they know about this space that outsiders do not?
- What exactly is new or different versus existing options?
- Why now?
- What milestones are expected in the next 12–18 months?
- How will raised funds be used?

Output:
- one-liner
- investment thesis
- why now
- milestone map
- initial uncertainty list

### 2. Team

Key questions:
- What is the founding team background?
- How did they meet and why did they choose to work together?
- Who owns product, engineering, sales, research, and operations?
- What have they built together before?
- What is the strongest evidence of resourcefulness?
- What is the biggest team risk?
- Who is the next critical hire?

Output:
- founder-market fit
- execution evidence
- missing capability map
- reference-check questions

### 3. Product / Technology / AI

Key questions:
- How does the product work in detail?
- Is the AI core workflow infrastructure or just a feature wrapper?
- What data, model, workflow, integration, or distribution advantage can compound?
- Is there proprietary data or a repeatable feedback loop?
- What part is technically difficult or non-obvious?
- What is the roadmap?
- What are the security, privacy, reliability, and eval risks?

AI-specific moat tests:
- **Workflow lock-in**: Does the product become part of a daily operational workflow?
- **Data flywheel**: Does usage generate better labeled data or process memory?
- **Evaluation discipline**: Are there task-level metrics beyond generic model quality?
- **Distribution wedge**: Is there a low-friction entry point into a valuable account?
- **Model dependency risk**: Could OpenAI/Anthropic/Google or an incumbent commoditize it?

Output:
- product workflow diagram
- technical moat assessment
- dependency map
- AI evaluation gaps

### 4. Traction / Market

Key questions:
- Who needs this product urgently?
- How do we know customers need it?
- Who are the first paying customers?
- What usage, retention, expansion, or revenue evidence exists?
- What is the customer acquisition motion and CAC risk?
- What competitors exist now and who may enter later?
- What resistance do reluctant users have?

Output:
- ICP and wedge
- traction evidence table
- market sizing with assumptions
- adoption friction list
- competitor / substitute map

### 5. Financials / Business Model

Key questions:
- How does the company make money?
- What are current ARR / MRR / pipeline / gross margin / burn / runway?
- What are LTV/CAC and payback assumptions?
- What are pricing and packaging assumptions?
- How much could this make per year if it works?
- What funding history and valuation expectations exist?

Output:
- unit economics sanity check
- runway and financing risk
- pricing logic
- sensitivity cases

### 6. Legal / Compliance / Data Risk

Add for AI companies even if not in the original five modules:
- customer data handling
- model training rights
- PII / PHI / financial / regulated data exposure
- IP ownership of generated outputs
- open-source license risk
- SOC2 / ISO / enterprise procurement readiness
- model safety / hallucination liability

Output:
- risk register
- must-check legal questions
- procurement blockers

### 7. Capital Path / VC Fit / Fundability

Add this module whenever the diligence is for an investment decision, fundraising review, IC memo, or VC-style startup assessment. Do **not** assume every good business is a good VC investment.

Key questions:
- Is this company actually VC-fit, or merely a good smaller / slower / cash-flow business?
- Is there credible potential for roughly 10x return on invested capital within a venture-relevant horizon, and what exit path could support that?
- What is the leverage mechanism: software, data, network effects, workflow lock-in, marketplace liquidity, platform/runtime, distribution, or capital efficiency?
- Is the company Before Product-Market Fit (BPMF), After Product-Market Fit (APMF), Launch, or Scale? What evidence proves that stage?
- What is the current round supposed to buy: PMF experiments, growth scale, enterprise trust/compliance, GTM capacity, technical infrastructure, or merely more runway?
- Is the raise too little to survive internal/external bad surprises, or too much for the current stage and likely to create cultural corrosion or headcount bloat?
- What liquidation preference, dilution, valuation, and exit-optionality risks are created by the proposed financing?
- What kind of investor/partner does the company need, and has the specific partner's value-add been reference-checked with founders they funded?
- If multiple qualified investors said no, which risk layer are they really rejecting: founder, market, competition, timing, financing, marketing, distribution, technology, product, hiring, or location/ecosystem?

Output:
- VC-fit verdict: venture-scale / non-VC but good business / too early / not fundable yet / unclear
- stage and next evidence gate
- funding plan sanity check
- investor fit and reference-check questions
- risk onion summary
- post-raise operating risk register

## Evidence ledger template

For each claim, record:

```yaml
claim: "..."
module: basic_info | team | technology | traction_market | financials | legal_risk | capital_path
source: "deck / website / interview / product demo / code / customer call / public data"
evidence_quote: "..."
confidence: high | medium | low
status: answered | partial | unanswered | contradicted
red_flag: true | false
next_check: "..."
# Optional for capital/path claims:
stage: idea | mvp | launch | scale | BPMF | APMF | unknown
risk_layer: founder | market | competition | timing | financing | marketing | distribution | technology | product | hiring | location | ai_dependency | legal_compliance | none
```

Never turn missing evidence into a confident conclusion. Use labels:
- **Known**: directly supported by source evidence.
- **Inferred**: reasonable but not directly proven.
- **Unknown**: must be asked or verified.
- **Contradiction**: sources conflict.

## Workflow

### Step 1 — Intake and external research

Collect available materials from the user:
- pitch deck / memo / website / demo notes
- founder interview transcript or notes
- product screenshots or trial access
- financials and pipeline
- customer references

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

### Step 2 — Build module coverage

Create a module table:

| Module | Coverage | Key answered questions | Key gaps | Confidence |
| --- | --- | --- | --- | --- |
| Basic Info | 0–100% | ... | ... | high/medium/low |
| Team | ... | ... | ... | ... |

Coverage is not amount of text; it is `answered key questions / total key questions`.

### Step 3 — Map stage, VC-fit, and the risk onion

Before writing a memo, force the evidence into a stage-and-risk map:

1. **Stage gate**: Idea / MVP / Launch / Scale, or BPMF / APMF. State the evidence for the stage; do not let a polished deck, prototype, or friendly pilot masquerade as PMF.
2. **VC-fit**: Decide whether this can plausibly become a venture-scale outcome. A company can be a good business and still fail VC-fit if it lacks leverage, speed, market size, or exit optionality.
3. **Capital path**: Explain what the current financing buys and what milestone must be achieved before the next financing or profitability path.
4. **Risk onion**: Peel risks by layer: founder/team, market, competition, timing, financing, marketing/CAC, distribution/partner dependency, technology, product execution, hiring/org, location/ecosystem, and AI-specific dependency/compliance.
5. **VC no diagnostics**: If qualified investors said no, treat that as evidence. One no may be noise; repeated no's should trigger a specific risk-layer diagnosis and plan revision.

### Step 4 — Produce the Q&A List

For each module, output:

```markdown
### Team

Answered:
- Q: ...
  A: ...
  Evidence: ...
  Confidence: ...

Unanswered / follow-up:
- Q: ...
  Why it matters: ...
  Best source to verify: founder / customer / data room / product demo / public source
```

### Step 5 — Red-team the investment thesis

Run nine contradiction checks:
1. **Pain vs willingness to pay**: Is there budget and urgency?
2. **Demo vs workflow**: Does the product enter real operations, or just impress in a demo?
3. **AI wrapper vs compounding system**: Is there a durable data/workflow/distribution advantage?
4. **Market size vs entry wedge**: Is there a narrow beachhead with credible expansion?
5. **Team story vs execution evidence**: Do past actions prove the claimed capability?
6. **VC-fit vs good business**: Is this venture-scale, or a good non-VC business being forced into a VC narrative?
7. **Plan vs market evolution**: Is the initial business plan treated as a fixed promise even though the real job is finding product-market fit?
8. **Funding amount vs stage**: Does the raise buy the next evidence gate, or does it create survival risk / cultural corrosion / liquidation-preference overhang?
9. **Platform/runtime dependency vs moat**: Does the AI/cloud/platform layer transfer costs and risk to the company, the customer, or the platform; and can the company defend value if the platform changes?

### Step 6 — Generate outputs

Pick the smallest useful output first:

1. **OnePage** — for quick investment conversation.
2. **Q&A List** — for founder follow-up and data room requests.
3. **IC Memo** — for decision-making.
4. **Risk Register** — for legal/technical/commercial red flags.
5. **BP / Slide critique** — if reviewing fundraising materials.

## Output formats

### OnePage

```markdown
# [Company] — AI Startup DD OnePage

## One-liner

## Why this could matter

## Product / Workflow

## AI moat hypothesis

## Traction evidence

## Team read

## Business model / financials

## VC-fit / capital path

## Stage and next evidence gate

## Main risks

## Follow-up questions

## Preliminary view
Proceed / Watch / Pass / Need more evidence
```

### IC memo skeleton

```markdown
# [Company] Due Diligence Memo

## 1. Executive view
- Recommendation:
- Confidence:
- Main reason to invest:
- Main reason not to invest:

## 2. Company thesis

## 3. Product and AI system

## 4. Market and customer pull

## 5. Team

## 6. Business model and financials

## 7. VC-fit, stage, and capital path

## 8. Competitive landscape

## 9. Risk onion

## 10. Post-raise operating risks

## 11. Risk register

| Risk | Severity | Evidence | Mitigation / next check |
| --- | --- | --- | --- |

## 12. Key unanswered questions

## 13. Decision gates
```

### Follow-up data request list

Group asks by owner:
- Founder / CEO
- CTO / product lead
- Finance
- Customers
- Legal / compliance
- Public research

## Quality bar

A good answer must:
- separate evidence from inference;
- show missing questions, not hide them;
- include AI-specific moat and dependency analysis;
- include VC-fit, stage, capital path, and risk-onion analysis when the context is investment or fundraising;
- separate good-business potential from venture-scale potential;
- include both why it can work and why it may fail;
- give next verification actions, not just a narrative.

Avoid:
- generic market-size optimism;
- unverified AI moat claims;
- treating a polished deck as proof;
- treating fundraising as an accomplishment by itself;
- assuming VC money is right for every startup;
- ignoring repeated investor no's instead of diagnosing the risk layer;
- converting unknowns into assumptions;
- writing an IC memo before making a Q&A gap list.
