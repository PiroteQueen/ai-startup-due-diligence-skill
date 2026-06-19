<!--
[INPUT]: 依赖 SKILL.md 的八模块工作流与 coverage-stage-model.md 的评分规则
[OUTPUT]: 对外提供各尽调模块的关键问题、AI 战略门禁与预期产物
[POS]: references/diligence 的问题库，驱动证据台账、覆盖率与 Q&A 缺口
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Module Question Bank

Full key-question bank for the eight diligence modules. Score coverage using the priorities, evidence credits, and gating rules in [coverage-stage-model.md](coverage-stage-model.md), not a raw answered-question count.

## 1. Basic Info / Thesis

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

## 2. Team

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

## 3. Product / Technology

Key questions:

- How does the product work in detail?
- What part is technically difficult or non-obvious?
- What architecture, integrations, and operational dependencies matter?
- What is the roadmap?
- What are the performance, security, privacy, reliability, and delivery risks?

Output:

- product workflow diagram
- architecture and integration assessment
- technical delivery risk
- reliability and product-evidence gaps

## 4. AI Product & Capability Strategy

Read [../research/ai-product-strategy.md](../research/ai-product-strategy.md).

Key questions:

- Which AI products, features, agents, copilots, models, or infrastructure capabilities exist?
- Which are live, beta/pilot, announced, retired, or unknown, and as of what date/version?
- What user workflow and measurable outcome does each capability improve?
- Is AI a feature, product line, platform, control point, or company-wide operating layer?
- What is built internally versus bought, licensed, open-source, or provided through partners?
- What model, data, retrieval, orchestration, eval, and infrastructure strategy is used?
- How are AI capabilities packaged, priced, adopted, retained, and expanded?
- What are inference cost, gross-margin, human-review, reliability, and liability implications?
- What data, workflow, integration, distribution, trust, or evaluation advantage can compound?
- Could a model provider, incumbent, or customer-built stack commoditize the capability?
- How does the target compare with each priority competitor on the same dated dimensions?

AI-specific moat tests:

- **Workflow lock-in**: Does the product become part of a daily operational workflow?
- **Data flywheel**: Does usage generate better labeled data or process memory?
- **Evaluation discipline**: Are there task-level metrics beyond generic model quality?
- **Distribution wedge**: Is there a low-friction entry point into a valuable account?
- **Model dependency risk**: Could OpenAI/Anthropic/Google or an incumbent commoditize it?

Output:

- dated AI product and feature inventory
- company-level AI strategy
- target-versus-competitor same-dimension matrix
- adoption and monetization evidence
- technical moat assessment
- dependency map
- AI evaluation gaps

AI strategy coverage is complete only after the dedicated gate in `SKILL.md` passes. A launch announcement or demo does not prove general availability, adoption, monetization, or strategic advantage.

## 5. Traction / Market

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
- source-dated competitor evidence matrix
- direct / adjacent / platform / incumbent / customer-build / manual-substitute layers
- same-dimension comparison of product, technology, data, workflow, traction, business model, distribution, and valuation
- target win/loss conditions and same-task diligence questions

Competition coverage is complete only after the mandatory competitor gate in `SKILL.md` passes. Naming competitors without primary-source product or deployment evidence is partial coverage.

## 6. Financials / Business Model

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

## 7. Legal / Compliance / Data Risk

Check for AI companies even when not raised by the materials:

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

## 8. Capital Path / VC Fit / Fundability

Add this module whenever the diligence is for an investment decision, fundraising review, IC memo, or VC-style startup assessment.

Key questions:

- Is this company actually VC-fit, or merely a good smaller / slower / cash-flow business?
- Is there credible potential for roughly 10x return on invested capital within a venture-relevant horizon, and what exit path could support that?
- What is the leverage mechanism: software, data, network effects, workflow lock-in, marketplace liquidity, platform/runtime, distribution, or capital efficiency?
- What are the independently supported product maturity, PMF status, GTM maturity, and financing stage? What evidence and next gate apply to each dimension?
- What is the current round supposed to buy: PMF experiments, growth scale, enterprise trust/compliance, GTM capacity, technical infrastructure, or merely more runway?
- Is the raise too little to survive internal/external bad surprises, or too much for the current stage and likely to create cultural corrosion or headcount bloat?
- What liquidation preference, dilution, valuation, and exit-optionality risks are created by the proposed financing?
- What kind of investor/partner does the company need, and has the specific partner's value-add been reference-checked with founders they funded?
- If multiple qualified investors said no, which risk layer are they really rejecting: founder, market, competition, timing, financing, marketing, distribution, technology, product, hiring, or location/ecosystem?

Output:

- VC-fit verdict: venture-scale / non-VC but good business / too early / not fundable yet / unclear
- four-dimensional stage map and next evidence gates
- funding plan sanity check
- investor fit and reference-check questions
- risk onion summary
- post-raise operating risk register
