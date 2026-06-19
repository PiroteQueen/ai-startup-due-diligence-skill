<!--
[INPUT]: 依赖公司行为、PMF、AI 产品、团队、融资与市场证据
[OUTPUT]: 对外提供可复用的失败/成功模式及对应验证测试
[POS]: references/diligence 的校准模式库，为阶段判断和红队降级提供实例
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Pattern Library: Calibration Examples

Concrete patterns for calibrating judgment. Use during Step 3 (stage gate) and Step 5 (red-team). When evidence matches a pattern below, do not just note it — downgrade the claim's `evidence_status`, set `red_flag` where indicated, and write a specific `next_check` in the evidence ledger.

Sections: false-PMF patterns · AI-wrapper death patterns · true-PMF signals · founder/team red flags · fundraising red flags · market reality checks.

## False-PMF patterns (looks like traction, is not)

### 1. Friendly pilots

- **Looks like**: 3–5 pilots with respectable logos, often started within weeks of fundraising.
- **Why misleading**: Sourced through investor intros or founder friendships; the "customer" is doing a favor, not solving a burning problem.
- **How to test**: Ask how each pilot was sourced. Ask who owns the budget and what the signed paid-conversion criteria are. A pilot without a named budget owner and conversion terms is marketing, not traction.

### 2. Free pilots with no conversion path

- **Looks like**: Active usage, positive feedback, "expanding the pilot next quarter."
- **Why misleading**: Free usage measures curiosity, not willingness to pay. Procurement is where AI products die.
- **How to test**: Has any pilot converted to a paid contract at list price? Has procurement/security review started anywhere?

### 3. Founder-delivered revenue

- **Looks like**: Real revenue, even six figures.
- **Why misleading**: The founder personally onboards, configures, and rescues every account — it is consulting wearing a SaaS costume.
- **How to test**: Ask what happens to retention if the founder stops touching accounts. Check gross margin and onboarding hours per account.

### 4. Logo collecting

- **Looks like**: A slide of Fortune 500 logos.
- **Why misleading**: One team's unpaid experiment inside a big company produces the same logo as an enterprise-wide contract.
- **How to test**: For each logo ask seat count, contract value, renewal status, expansion history.

### 5. Demo-driven enthusiasm

- **Looks like**: High meeting-to-interest conversion, "everyone we show this to loves it."
- **Why misleading**: AI demos are intrinsically impressive; admiration is not adoption.
- **How to test**: Weekly active usage of the core workflow, time-in-product, what task the user completed last week. Demo conversion is not a traction metric.

### 6. Launch-spike traction

- **Looks like**: Product Hunt #1, viral thread, hockey-stick signup chart.
- **Why misleading**: Cumulative signup charts hide decay. AI tools have notoriously high tourist traffic.
- **How to test**: Demand cohort retention curves (D7/D30/W4), never cumulative counts. Compare signup spike dates to press dates.

### 7. LOI inflation

- **Looks like**: "$2M in signed LOIs / pipeline."
- **Why misleading**: Non-binding letters cost the signer nothing and are often collected specifically for fundraising.
- **How to test**: For each LOI: budget line, decision timeline, signatory's authority to spend. Treat unverified LOIs as marketing, not pipeline.

### 8. Paid-but-not-used (innovation-budget buying)

- **Looks like**: Real contracts, real revenue, enterprise customers.
- **Why misleading**: 2023–2026 enterprise AI FOMO created innovation budgets that buy tools nobody operationalizes. First renewal cycle is the truth.
- **How to test**: Usage telemetry per paying account; who owns the renewal decision; any account past its first renewal.

### 9. AI-generated supportive evidence

- **Looks like**: A well-researched market validation deck: surveys, TAM analyses, quotes, competitor teardowns.
- **Why misleading**: When founders use AI for research, it cheerfully produces supporting evidence for any thesis. Building friction has dropped; validation discipline rarely rose to match. A prototype plus AI-assembled "research" is not problem-solution fit.
- **How to test**: Ask what disconfirming research was done — failed competitors in this exact space, structural blockers, alternative explanations for the demand signal. Ask for raw interview notes, not synthesized summaries. A founder who only has supportive evidence has not validated anything.

## AI-wrapper death patterns

### 1. Model-update kill

- **Pattern**: The next frontier model release covers the product's core capability natively (longer context, better reasoning, built-in agents).
- **How to test**: Ask the founder which specific model capability improvement would hurt them most, and what survives it. No answer = red flag.

### 2. Platform feature absorption

- **Pattern**: The incumbent platform (Office, Salesforce, GitHub, Figma...) ships the feature as a checkbox in their AI bundle, priced at zero.
- **How to test**: Map the product against incumbent AI roadmaps. Ask why the customer would not wait for the bundled version.

### 3. Prompt replication

- **Pattern**: A customer's internal team replicates the workflow with ChatGPT/Claude plus a prompt doc in a week.
- **How to test**: Ask what in the product cannot be reproduced by prompting a frontier model: proprietary data, integrations, accumulated state, eval-tuned reliability. "Our prompts are better" is not an answer.

### 4. Thin orchestration with no accumulation

- **Pattern**: The product is glue code over model APIs; nothing compounds with usage — no labeled data, no workflow memory, no network.
- **How to test**: Ask what is measurably better for customer #100 than it was for customer #1, and what asset grows automatically with usage.

### 5. Cost-structure squeeze

- **Pattern**: Margins depend on reselling tokens at a markup; model price drops help every competitor equally, and customers eventually call the API themselves.
- **How to test**: Token cost as % of COGS; pricing power evidence; what happens to the margin story if inference cost falls 10x (it has, repeatedly).

### 6. Eval-free quality claims

- **Pattern**: "Our AI is more accurate" with no task-level eval set, no golden dataset, no regression testing.
- **How to test**: Ask to see the eval harness. A team that cannot show task-level metrics cannot maintain quality through model swaps — treat the quality claim as Unknown.

## True-PMF signals (what the real thing looks like)

1. **Pull over push**: Inbound from word of mouth; sales hiring lags demand instead of leading it.
2. **Usage despite friction**: Users tolerate bugs and downtime and complain loudly — they complain because they depend on it. Silence after churn is the opposite signal.
3. **Organic expansion**: Seats and usage grow inside accounts without sales effort; new teams self-onboard.
4. **Workflow embedding**: The product appears in the customer's own SOPs, onboarding docs, or job descriptions.
5. **Budget reallocation**: Customers cut another line item, tool, or planned hire to pay for it — named, verifiable substitution.
6. **Early renewal or prepay**: Customers renew before the deadline or prepay for annual terms without discounting pressure.

A company showing two or more true-PMF signals with verifiable evidence may be APMF. A company showing only false-PMF patterns is BPMF regardless of revenue, logos, or narrative — write the stage accordingly and list the next evidence gate.

When PMF is absent, the texture is equally recognizable (per Andreessen): users do not quite get value, word of mouth does not spread, usage grows slowly, press reviews are "blah", sales cycles drag. A quantitative cross-check is the Sean Ellis test: what share of active users would be "very disappointed" if the product disappeared (40%+ is the classic strong-signal threshold).

## Founder and team red-flag patterns

### 1. Doubt-avoidance lock-in

- **Pattern**: Founder cannot articulate what evidence would make them change course; every flat metric is reframed as "almost working." Munger's doubt-avoidance and inconsistency-avoidance tendencies, which help founders survive early skepticism, become an inability to admit PMF has not arrived.
- **How to test**: Ask "what result over the next two quarters would tell you this approach is wrong?" A founder with no answer is iterating on commitment, not evidence.

### 2. Hindsight-narrative reasoning

- **Pattern**: The pitch leans on pattern-matching to past successes ("we're doing what X did early on"). Successful founders' own explanations of why they won are routinely wrong; the real cause is almost always PMF, not the rituals being imitated.
- **How to test**: Strip the analogy and ask for this company's own market-pull evidence.

### 3. Competitor obsession in a small market

- **Pattern**: Strategy is defined by reacting to a rival startup's announcements; both are fighting over a market too small to matter yet. Teams see competitors' polished external moves and not their internal chaos, so they overrate them.
- **How to test**: Ask whether the contested segment, fully won, changes the company's outcome. If not, the obsession is a focus risk.

### 4. "We have no competitors"

- **Pattern**: Claimed as a strength. It signals naivete: great markets draw competitors, so no competition usually means no market.
- **How to test**: Build the substitute map yourself — adjacent players, incumbents, in-house builds, "do nothing." If the founder has not done this, mark team risk, not just market risk.

### 5. The 2%-of-a-huge-market plan

- **Pattern**: "We only need 2% of this $50B market." It implies the players taking the other 98% will crush you, and substitutes top-down arithmetic for a wedge.
- **How to test**: Demand the beachhead: which specific customers, why they switch, and the theory for winning a dominant share of that narrow segment.

### 6. Instantly applauded strategy

- **Pattern**: Every advisor, journalist, and peer immediately agrees the idea is great. A strategy that triggers zero resistance is usually not novel enough to produce venture-scale returns.
- **How to test**: Ask what informed people disagree with. No credible disagreement = consensus idea = priced-in opportunity.

### 7. Misaligned executive incentives

- **Pattern**: Key executives' compensation rewards something other than long-term value: an outside CEO on a four-year vest is structurally incentivized to sell in year four; restricted stock instead of options selects for preserving value over creating it; every unbalanced target gets gamed (bookings without quality, ship dates without quality).
- **How to test**: Read the actual incentive structure of the top 3–5 people and ask what behavior it pays for. Check each major goal for a paired counter-goal.

## Fundraising and capital red-flag patterns

### 1. Raise without a theory

- **Pattern**: The company cannot state what the round buys in PMF or milestone terms. Correct theory: BPMF, raise at least enough to reach PMF; APMF, enough to fully exploit the opportunity and reach profitability — in both cases with a buffer for bad surprises.
- **How to test**: Ask which evidence gate this money buys and what the next round's story is if the gate is missed.

### 2. No insurance buffer

- **Pattern**: Runway is sized to the default plan with zero slack. Setbacks are near-certain (slipped releases, lost customers, lawsuits, key departures), and funding windows shut without warning — the companies that survived 2001–2003 and similar winters were the ones that over-raised while they could.
- **How to test**: Stress the plan: 6-month delay on the key milestone plus a closed funding window — does the company survive?

### 3. Cultural corrosion from over-raising

- **Pattern**: A raise far beyond the stage's needs produces recognizable symptoms: hiring too many people too fast, management-by-hiring, engineering team bloat, fading product/customer obsession, too many salespeople before PMF, slipping deadlines because "we have cash."
- **How to test**: Headcount plan vs evidence gates; sales hires vs PMF status; deadline discipline since the raise. "Raising money is never an accomplishment in itself" — treat a team celebrating the raise as the milestone as a red flag.

### 4. Liquidation-preference overhang

- **Pattern**: Stacked preferences mean the acquisition price must clear investors' payout before founders and employees see anything — quietly destroying exit optionality for everyone operating the company.
- **How to test**: Compute the realistic exit price floor implied by the preference stack and compare with plausible acquirer prices for this category.

### 5. Repeated VC no's, undiagnosed

- **Pattern**: One no means nothing; three may be coincidence; five to eight no's from qualified investors means something is wrong with the plan — yet the team keeps pitching the same deck. Note VCs rarely say "no" outright; "maybe / not right now" while tracking your progress is usually a no on current facts.
- **How to test**: Ask which risk layer the passes pointed at (founder, market, competition, timing, financing, marketing, distribution, technology, product, hiring, location) and what was changed in response. Pitching harder without retooling is itself a team red flag.

## Market reality checks

1. **Market beats team and product** (Rachleff's law): the #1 company-killer is lack of market. A great team in a nonexistent market loses; diligence weight should follow market evidence, not team charisma.
2. **Market pull is observable**: when the market exists, it pulls product out of the company — customers knock, usage grows ahead of sales capacity, hiring and press and the bank account all get dragged forward. If nothing is being pulled, do not credit the narrative.
3. **Product-creates-market is the exception**: cases like VMware exist but are rare. A thesis that requires the product to conjure its own market deserves a heavy discount.
4. **New-market diffusion resistance**: slow adoption is sometimes inconsistency-avoidance in customers, not product failure. The classic answer is to find users without entrenched habits (non-consumers) rather than fighting to convert incumbents' satisfied users — check whether the GTM targets the former.

## Sources

- Marc Andreessen, pmarca Guide to Startups: "The only thing that matters", "When the VCs say no", "How much funding is too little? Too much?" (pmarchive.com)
- Marc Andreessen, "The Psychology of Entrepreneurial Misjudgment" (Munger biases 1–6, pmarchive.com)
- The Founder's Playbook 2026 — AI-native stage gates, AI-demo-vs-validation, prompt-is-not-moat.
