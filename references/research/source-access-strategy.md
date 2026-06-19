<!--
[INPUT]: 依赖公开网页、用户材料与可用研究工具的访问结果
[OUTPUT]: 对外提供按 claim 选源、受阻切换、交叉验证与证据降级规则
[POS]: references/research 的外部研究路由核心，消除 Crunchbase 等单点来源依赖
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Source Access and Fallback Strategy

Use this protocol for every identifiable company. Research starts from the claim to prove, not from a favorite database.

## 1. Universal rules

1. Prefer primary, dated, claim-specific evidence.
2. Treat databases, aggregators, snippets, and social posts as discovery leads unless independently corroborated.
3. Make one reasonable attempt to open a blocked, paywalled, login-only, or robots-restricted source. Log the failure, then move down the fallback ladder.
4. Never make completion depend on Crunchbase, PitchBook, CB Insights, LinkedIn, Tracxn, Dealroom, or any single commercial source.
5. Search by stable identifiers: legal company name, founder name, product name, investor, customer, filing number, repository, domain, and announcement date.
6. For material claims, seek two independent sources when primary evidence is absent. Two articles repeating the same press release count as one evidence origin.
7. Preserve conflicts. A later source does not silently erase an earlier contradictory claim.

## 2. Claim-specific source ladders

| Claim | Preferred evidence | Fallbacks when blocked or absent | Weak leads only |
| --- | --- | --- | --- |
| Legal identity / status | corporate registry, SEC/Companies House/state filing, court or regulator record | official terms/privacy footer, trademark/patent record, government procurement record | databases, directory profiles |
| Funding / investors / date | regulatory filing, company and lead-investor announcements, fund portfolio page | reputable financial/technology reporting, accelerator portfolio, founder interview | Crunchbase/PitchBook/CB Insights snippets, social posts |
| Valuation / round terms | signed term sheet/cap table/data room, regulatory filing, direct company/investor statement | reputable reporting with named sources, multiple independent reports | database estimate, unsourced profile |
| Team / employment | company team page, personal site/CV, GitHub, publications, patents, conference bio | prior employer page, university page, interviews, archived pages | LinkedIn snippet, people-search aggregator |
| Product / AI feature status | product docs, changelog, release notes, pricing, model card, repository, app listing | demo, help center, customer documentation, partner integration page, archived product page | launch article, social post, search snippet |
| Customers / deployments | customer-owned case study, procurement/contract record, customer announcement | company case study with named customer, partner announcement, review/app marketplace evidence | logo wall, anonymous testimonial |
| Usage / revenue / retention | audited/data-room metrics, filings, customer references | named executive statement, reputable reporting with metric/date | traffic estimate, app rank, employee count |
| Pricing / packaging | current pricing page, quote/order form, marketplace listing | archived pricing, reseller page, customer procurement record | review-site estimate |
| Technical performance | reproducible benchmark, paper, model card, eval report, repository | third-party test, customer evidence, detailed technical talk | company demo, generic benchmark claim |
| Security / compliance | certification registry/report, trust center, DPA, subprocessors, security docs | procurement listing, customer security statement | marketing badge |
| Market / competition | buyer workflow evidence, official competitor docs, customer reviews, filings | analyst/reporting evidence, job postings, partner ecosystem | category lists and database tags |

## 3. Search routes

Use several narrow queries instead of one broad company search:

- `"Legal Company Name" funding OR financing OR raised`
- `"Company" site:sec.gov` or the relevant national/state registry
- `"Investor" "Company" portfolio`
- `"Product" changelog OR release notes OR pricing OR docs`
- `"AI feature name" beta OR generally available OR retired`
- `"Company" customer case study` and `"Customer" "Company"`
- `"Company" security OR trust OR subprocessors OR DPA`
- `"Founder Name" GitHub OR scholar OR patent OR conference`
- `"Company" lawsuit OR complaint OR breach OR outage`
- competing claim plus `review`, `benchmark`, `migration`, or `alternative`

Search snippets may reveal a lead but must not carry a high-materiality claim without an opened source or explicit limitation.

## 4. Blocked-source behavior

For every failure record:

- source/domain and claim sought;
- failure type: paywall, login, robots, geo-block, dynamic rendering, missing page, rate limit, or unavailable tool;
- one fallback query or alternate source route;
- evidence impact;
- final status: recovered, partially recovered, or unknown.

Do not repeatedly retry the same blocked page unless a materially different access method is available and permitted.

## 5. Source diversity and confidence

High-confidence material claims normally require:

- one strong primary source; or
- two independent, reputable secondary origins that identify dates and facts.

Downgrade when:

- all sources originate from the company;
- all reporting traces to one press release;
- only snippets or database profiles are available;
- dates or product versions are unclear;
- the source proves announcement but not availability, adoption, revenue, or deployment.

## 6. Research completion test

The source strategy passes when:

- at least three applicable source groups were searched (company-owned, founder/team, product/technical, customer/traction, financing/legal, competitor);
- each material claim has a preferred source, a successful fallback, or an explicit `Unknown`;
- no material claim rests solely on a blocked/paywalled database or a search snippet;
- blocked sources and fallback routes are logged;
- financing evidence does not depend on Crunchbase or another single aggregator;
- product and AI claims use dated first-party artifacts where available;
- disconfirming searches were attempted;
- source diversity is sufficient for the assigned confidence;
- the competitor gate (competitor-research.md §10) also passes when competition is material.
