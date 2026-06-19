<!--
[INPUT]: 依赖目标工作流、买方、竞品、替代方案与来源证据
[OUTPUT]: 对外提供六层竞争地图、同维度比较、胜负条件与估值反证
[POS]: references/research 的竞争研究协议，与 AI 战略协议共同支撑差异化判断
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Competitor and Substitute Research Protocol

Use this protocol whenever competition affects differentiation, market entry, pricing, moat, valuation, or exit outcomes.

## 1. Define the competitive job

Start from the customer job or workflow, not the target company's category label.

Record:

- user and buyer;
- job to be done;
- current workflow;
- budget owner;
- success metric;
- switching trigger;
- constraints such as safety, latency, privacy, integration, and procurement.

Two companies are competitors when a buyer could choose one instead of the other to accomplish the same job, even if their technology or category labels differ.

## 2. Map all relevant layers

Check each layer and mark it applicable or not applicable:

1. **Direct product competitors** — same buyer, workflow, and product category.
2. **Adjacent technical approaches** — different architecture or form factor solving the same job.
3. **Platform/model/infrastructure providers** — can commoditize the target, bundle the capability, or capture economics.
4. **Workflow/distribution incumbents** — own customer relationships, systems of record, integration, trust, or procurement.
5. **Customer-built alternatives** — internal engineering, data science, operations, or automation teams.
6. **Manual/non-consumption substitutes** — people, services, spreadsheets, legacy systems, or choosing not to solve the problem.

## 3. Select priority comparables

Choose 4–8 priority competitors or substitutes. Include:

- the closest product/technology comparable;
- the strongest execution or deployment comparable;
- the strongest platform/incumbent threat;
- the most realistic customer substitute;
- a valuation comparable only when stage, evidence and business model are sufficiently comparable.

Do not select companies only because they are prominent or use the same category label.

## 4. Gather source-dated evidence

For each priority competitor, search for:

- product and current version/date;
- workflow and buyer;
- architecture or technical approach;
- benchmark, eval, demonstrated capability, reliability, cost, latency, or safety;
- customer, pilot, deployment, usage, retention, revenue, or commercial agreement;
- data source and feedback loop;
- hardware, model, platform, cloud, or distribution dependencies;
- pricing and business model;
- financing and valuation, only when decision-relevant;
- roadmap, changelog, job postings, partnerships, and evidence of direction.

Use at least two evidence points per priority competitor when public evidence permits:

1. product/technical evidence;
2. traction/deployment/commercial evidence.

## 5. Source hierarchy

Prefer:

1. official product documentation, research papers, model cards, changelogs, filings, pricing, security/legal pages;
2. customer-owned case studies, procurement documents, partner announcements, app stores, repositories and registries;
3. high-quality reporting for financing, stealth companies, hiring, and private transactions;
4. databases, aggregators, social posts, and search snippets only as leads.

Company self-reported benchmarks and deployments must be labeled as self-reported. Do not convert a demo video into production evidence.

## 6. Compare on the same dimensions

Use a common matrix:

- product/workflow;
- buyer and wedge;
- technical approach;
- observable capability/eval;
- deployment/traction;
- data advantage;
- workflow/distribution advantage;
- business model/economics;
- financing/valuation;
- dependency risk;
- relative target position.

Avoid asymmetric comparisons, such as comparing the target's future roadmap with a competitor's current product or comparing one company's valuation with another company's revenue.

## 7. Run contradiction tests

Ask:

- Is the target claiming an empty market where incumbents already operate?
- Is a valuation comparable more mature or better evidenced?
- Can a platform provider bundle the target's core feature?
- Can customers solve the job with existing software plus a general model?
- Is proprietary data truly unavailable through partnerships, simulation, purchase, or customer internal development?
- Does the target's capital intensity create a moat or mostly supplier revenue?
- Is the target's broader scope an advantage or loss of focus?

## 8. Produce an investment conclusion

Conclude:

- where the target leads today;
- where it may lead if unproven assumptions become true;
- where competitors demonstrably lead;
- the most dangerous substitute;
- what evidence would prove the target wins;
- what evidence would falsify the moat;
- whether competitors support or contradict the target valuation.

## 9. Failure behavior

If evidence is sparse:

- keep cells `Unknown`;
- record searches and access failures;
- lower confidence;
- request same-task benchmarks and customer references;
- do not replace missing evidence with market narrative.

## 10. Gate — pass only when

- at least three competitor/substitute layers (§2) are covered, or it is explained why fewer apply;
- 4–8 priority comparables (§3) are selected, including at least one incumbent/platform and one substitute where applicable;
- each priority competitor has at least two evidence points (§4), ideally one product/technical and one traction/deployment/commercial;
- the same dimensions (§6) are used for target and competitors, with product/version/date recorded;
- at least one valuation counterexample is included, or it is explained why no valid comparable exists;
- the conclusion (§8) states what evidence would prove the target wins or loses.

If public evidence is sparse, keep cells `Unknown`; never replace the matrix with generic prose.
