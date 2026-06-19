<!--
[INPUT]: 依赖目标公司与优先竞品的产品文档、发布记录、采用度和商业证据
[OUTPUT]: 对外提供独立的 AI 功能、产品组合、能力路线与战略比较协议
[POS]: references/research 的 AI 战略专用规则，连接产品事实、商业价值与投资判断
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# AI Product and Capability Strategy

Use this protocol for the target and every priority competitor that offers material AI functionality.

## 1. Build the dated AI product inventory

Record each material AI product, feature, agent, copilot, model, API, workflow automation, or infrastructure capability.

Required fields:

- product or feature name;
- user and workflow;
- release/version/source date;
- status: `live`, `beta/pilot`, `announced`, `retired`, or `unknown`;
- access and packaging;
- underlying model/data/infrastructure when evidenced;
- claimed value;
- observable adoption or outcome evidence;
- source and limitation.

Do not combine announced roadmap items with generally available products.

## 2. Explain the strategy, not just the feature list

Assess six connected choices:

1. **User value** — Which costly, frequent, or risky job improves? What measurable outcome changes?
2. **Portfolio logic** — Is AI a feature, product line, platform, control point, or company-wide operating layer?
3. **Build / buy / partner** — What is proprietary, fine-tuned, retrieved, orchestrated, licensed, or outsourced?
4. **Model route** — Single-provider, multi-model, open-source, proprietary model, edge/on-device, or hybrid; why?
5. **Commercial route** — Included, premium tier, usage-based, seat expansion, outcome pricing, services pull-through, or retention defense?
6. **Compounding advantage** — Does usage improve data, evals, workflow memory, distribution, integrations, trust, or switching cost?

## 3. Separate capability from strategic advantage

For every claimed advantage ask:

- Is the capability available today?
- Is it meaningfully better on the customer's task?
- Is the difference durable if foundation models improve?
- Does the company control data rights, evals, workflow, distribution, or economics?
- Does adoption reinforce the advantage?
- Can an incumbent bundle it or a customer build it?

A feature gap is not automatically a company moat. Feature parity is not automatically strategic parity.

## 4. Verify adoption and monetization

Rank evidence:

1. product telemetry, paid usage, retention, expansion, or customer-owned outcome evidence;
2. named deployment with scope and date;
3. generally available product with pricing or packaging;
4. beta/pilot participation;
5. demo, announcement, waitlist, or roadmap.

Record AI-specific economics where available:

- inference and infrastructure cost;
- gross-margin impact;
- human review/operations burden;
- pricing metric and attach rate;
- cannibalization or seat compression;
- support, liability, and reliability costs.

## 5. Compare companies on the same dimensions

Use dated evidence for:

- AI portfolio and status;
- target workflow and buyer;
- model/data/architecture route;
- eval quality and reliability;
- adoption and customer outcomes;
- monetization and economics;
- distribution and integration;
- proprietary assets and feedback loops;
- platform/provider dependency;
- compliance and safety;
- roadmap direction;
- strategic position.

Never compare the target's roadmap with a competitor's live product without labeling the time/status mismatch.

## 6. Derive the company-level AI strategy

Conclude:

- what role AI plays in the company's strategy today;
- which feature or product is the adoption wedge;
- what is genuinely differentiated;
- what is commodity or partner-dependent;
- whether monetization is additive, defensive, or unproven;
- which dependency can compress margin or erase differentiation;
- the next 2–4 evidence gates;
- what would falsify the strategy.

## 7. Failure behavior

If evidence is sparse:

- retain `unknown` cells;
- distinguish absence of public evidence from absence of capability;
- request product access, roadmap, architecture, eval, telemetry, and unit-economics evidence;
- lower confidence;
- do not infer strategy from marketing language alone.

## 8. Gate — pass only when

- the target and each priority competitor are compared on the same dated dimensions (§5);
- every material AI feature is labeled `live`, `beta/pilot`, `announced`, `retired`, or `unknown` (§1);
- announced roadmap items are never presented as generally available products;
- access failures and `unknown` cells remain visible (§7);
- the conclusion (§6) separates genuine differentiation from commodity or partner-dependent capability and states what would falsify the strategy.
