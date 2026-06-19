<!--
[INPUT]: 依赖 2026-06-19 对 Harvey、客户、融资和竞品的公开检索
[OUTPUT]: 对外提供来源、访问失败、替代路由与证据限制
[POS]: appendices 的研究审计底稿
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Harvey — External Research Log

- Research date：2026-06-19
- Live research：yes
- Gate：public-source preliminary gate passed；completed investment DD gate not passed

## Source groups

| Group | Evidence | Gaps |
|---|---|---|
| Company-owned | Harvey platform, newsroom, security, customers | 自报偏差 |
| Founder/team | 公司融资材料、公开采访和报道 | 内部组织数据 |
| Product/technical | Assistant、Vault、Knowledge、Agents、Mistral | eval、成本、事故 |
| Customer/traction | Harvey customer cases、客户与媒体材料 | 合同、NRR、独立 ROI |
| Financing/legal | Harvey 2026 funding announcement、投资方/权威报道 | term sheet/cap table |
| Competitors | Legora、TR CoCounsel、Lexis+、Luminance official | 可比经济数据 |
| AI capabilities | 目标和竞品产品页 | task-level benchmark |

## Key sources

| Source | Date | Supports | Does not prove |
|---|---|---|---|
| [Harvey $11B funding announcement](https://www.harvey.ai/blog/harvey-raises-at-dollar11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises) | 2026-03-25 | $200m、$11b、GIC/Sequoia、客户与 agents 自报 | 条款、财务质量 |
| [Harvey Assistant](https://www.harvey.ai/platform/assistant) | accessed 2026-06-19 | Assistant live features、公司自报 outcomes | 独立性能与 ROI |
| [Harvey Agents](https://www.harvey.ai/agents) | accessed 2026-06-19 | Agents 产品与工作流 | 成功率和人工成本 |
| [Mistral live in Harvey](https://www.harvey.ai/blog/mistral-now-live-in-harvey) | 2026-05-26 | Mistral Early Access、multi-model route | 全球 GA、经济性 |
| [Harvey Security](https://www.harvey.ai/security) | accessed 2026-06-19 | 安全与企业控制 | 完整审计报告 |
| [Harvey Customers](https://www.harvey.ai/customers) | accessed 2026-06-19 | named deployments/cases | 付费、续约、独立验证 |
| [Legora](https://legora.com/) | accessed 2026-06-19 | aOS、Agent、Monitors、security | 独立 ROI |
| [Thomson Reuters CoCounsel](https://legal.thomsonreuters.com/en/products/cocounsel-legal) | accessed 2026-06-19 | CoCounsel、Westlaw grounding、客户案例 | 可比 economics |
| [Lexis+ Protégé](https://www.lexisnexis.com/en-us/products/lexis-plus-protege.page) | accessed 2026-06-19 | 产品与内容整合 | adoption/ROI comparison |
| [Luminance](https://www.luminance.com/) | accessed 2026-06-19 | legal AI competitor product | same-task benchmark |

## Failed / blocked

| Source/query | Claim | Failure | Fallback | Status |
|---|---|---|---|---|
| crunchbase.com/organization Harvey | funding history | robots.txt blocked, non-retryable | Harvey official announcement、投资方/权威报道 | recovered |
| LinkedIn profiles | team roles | login/dynamic，未依赖 | company pages、公开采访和履历 | partial |
| Paywalled reporting | ARR/ROI corroboration | paywall/snippet only | official sources + accessible reporting；标为 limited | partial |

## Disconfirming evidence

- 法律 AI 的财务 ROI 仍需客户以续约和预算重分配证明。
- Incumbents 拥有专有法律内容、既有采购关系和捆绑能力。
- Harvey 不控制 frontier model；moat 必须来自工作流、部署、数据/eval 和信任。
- 110 亿美元价格对应的 10x 终局约为 1,100 亿美元，要求远超单点工具。

## Conclusion

公开研究充分证明 Harvey 是真实、规模化且产品化的法律 AI 公司，也证明 Crunchbase 不是必要来源。公开研究不足以证明当前交易值得投资；财务、合同、单位经济和产品可靠性仍需资料室。
