---
name: ai-startup-due-diligence
description: "Use for AI startup due diligence: turn scattered evidence into a structured investment memo, Q&A gap list, OnePage, risk register, and follow-up diligence plan. Based on the user’s DDyst project logic."
---

# AI Startup Due Diligence

Use this skill when the user is evaluating an AI startup, reviewing an investment target, preparing diligence questions, or asking for a DD memo / IC note / OnePage / red-flag analysis.

This skill is distilled from the DDyst project (`/Users/Hanxue/Desktop/Lucky5.org/DDyst` and `DDyst_admin`): modular diligence, key questions (`key_q`), evidence-backed answers (`key_q_answers`), completion status, AI-assisted gap detection, report export, OnePage, Q&A list, raw story, and co-analysis.

## Core mental model

Do not start by writing a fluent memo. Start by building a **diligence evidence ledger**:

```text
Target company
  → modules
  → key questions
  → evidence-backed answers
  → unanswered gaps
  → confidence / contradiction / red flags
  → outputs: Q&A List, OnePage, IC memo, follow-up plan
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

## Evidence ledger template

For each claim, record:

```yaml
claim: "..."
module: basic_info | team | technology | traction_market | financials | legal_risk
source: "deck / website / interview / product demo / code / customer call / public data"
evidence_quote: "..."
confidence: high | medium | low
status: answered | partial | unanswered | contradicted
red_flag: true | false
next_check: "..."
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

### Step 3 — Produce the Q&A List

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

### Step 4 — Red-team the investment thesis

Run five contradiction checks:
1. **Pain vs willingness to pay**: Is there budget and urgency?
2. **Demo vs workflow**: Does the product enter real operations, or just impress in a demo?
3. **AI wrapper vs compounding system**: Is there a durable data/workflow/distribution advantage?
4. **Market size vs entry wedge**: Is there a narrow beachhead with credible expansion?
5. **Team story vs execution evidence**: Do past actions prove the claimed capability?

### Step 5 — Generate outputs

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

## 7. Competitive landscape

## 8. Risk register

| Risk | Severity | Evidence | Mitigation / next check |
| --- | --- | --- | --- |

## 9. Key unanswered questions

## 10. Decision gates
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
- include both why it can work and why it may fail;
- give next verification actions, not just a narrative.

Avoid:
- generic market-size optimism;
- unverified AI moat claims;
- treating a polished deck as proof;
- converting unknowns into assumptions;
- writing an IC memo before making a Q&A gap list.
