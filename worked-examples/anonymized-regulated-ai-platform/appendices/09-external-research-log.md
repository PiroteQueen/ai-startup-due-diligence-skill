<!--
[INPUT]: 依赖匿名化后的公司、客户、融资和竞品研究记录
[OUTPUT]: 对外提供来源、访问失败、替代路由与证据限制
[POS]: appendices 的研究审计底稿
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Company Alpha — External Research Log

- Research date：2026-Q2（匿名化）
- Live research：yes
- Gate：public-source preliminary gate passed；completed investment DD gate not passed

## Source groups

| Group | Evidence | Gaps |
|---|---|---|
| Company-owned | company platform, newsroom, security, customers | 自报偏差 |
| Founder/team | 公司融资材料、公开采访和报道 | 内部组织数据 |
| Product/technical | Assistant、Document Workspace、Knowledge Layer、Agents、secondary model | eval、成本、事故 |
| Customer/traction | anonymized customer cases、客户与媒体材料 | 合同、NRR、独立 ROI |
| Financing/legal | company funding announcement、投资方/权威报道 | term sheet/cap table |
| Competitors | Direct Rival A、Content Incumbent B、Workflow Incumbent C、Vertical Rival D | 可比经济数据 |
| AI capabilities | 目标和竞品产品页 | task-level benchmark |

## Key sources

| Source | Date | Supports | Does not prove |
|---|---|---|---|
| Primary source A（URL redacted） | date redacted | late-stage round、high valuation、客户与 agents 自报 | 条款、财务质量 |
| Product source B（URL redacted） | accessed in research period | Assistant live features、公司自报 outcomes | 独立性能与 ROI |
| Product source C（URL redacted） | accessed in research period | Agents 产品与工作流 | 成功率和人工成本 |
| Partnership source D（URL redacted） | date redacted | secondary model Early Access、multi-model route | 全球 GA、经济性 |
| Security source E（URL redacted） | accessed in research period | 安全与企业控制 | 完整审计报告 |
| Customer source F（URL redacted） | accessed in research period | named deployments/cases | 付费、续约、独立验证 |
| Rival source G（URL redacted） | accessed in research period | Agent OS、Monitors、security | 独立 ROI |
| Incumbent source H（URL redacted） | accessed in research period | 专业 copilot、专有内容 grounding | 可比 economics |

## Failed / blocked

| Source/query | Claim | Failure | Fallback | Status |
|---|---|---|---|---|
| Commercial funding database | funding history | robots.txt blocked, non-retryable | company official announcement、投资方/权威报道 | recovered |
| LinkedIn profiles | team roles | login/dynamic，未依赖 | company pages、公开采访和履历 | partial |
| Paywalled reporting | ARR/ROI corroboration | paywall/snippet only | official sources + accessible reporting；标为 limited | partial |

## Disconfirming evidence

- 受监管工作流 AI 的财务 ROI 仍需客户以续约和预算重分配证明。
- Incumbents 拥有专有法律内容、既有采购关系和捆绑能力。
- Company Alpha 不控制 frontier model；moat 必须来自工作流、部署、数据/eval 和信任。
- 高位后期价格对应的目标回报要求公司终局远超单点工具。

## Conclusion

研究充分证明 Company Alpha 是真实、规模化且产品化的受监管工作流 AI 公司，也证明单一商业数据库不是必要来源。公开研究不足以证明当前交易值得投资；财务、合同、单位经济和产品可靠性仍需资料室。
