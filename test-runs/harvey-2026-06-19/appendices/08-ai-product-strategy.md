<!--
[INPUT]: 依赖 Harvey 与优先竞品的公开 AI 产品、采用和模型证据
[OUTPUT]: 对外提供独立的 Harvey AI 产品与能力战略
[POS]: appendices 的 AI 战略附录
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Harvey — AI Product and Capability Strategy

- Evidence date：2026-06-19
- Role：operating layer / control point
- Confidence：medium

## Product inventory

| Product | Workflow | Status/date | Model/data route | Adoption/outcome | Limitation |
|---|---|---|---|---|---|
| Assistant | 研究、问答、起草、review tables | live，2026-06 | 多来源检索；模型路由未完整公开 | 官方案例称节时和高采用 | 公司自报 |
| Vault | 文档存储与批量分析 | live | 客户文档 + 模型 | 企业产品组合一部分 | 使用/attach 未公开 |
| Knowledge | 法律、监管、税务研究 | live | premium databases + public/internal sources | 工作流相关 | 内容许可与覆盖未知 |
| Agents | 端到端多步骤法律任务 | live，2026-03 | multi-model + legal engineering | 公司称 25,000+ custom agents | 成功率/人工介入未知 |
| Command Center | AI 采用、benchmark、治理 | live | 平台遥测 | 支持企业 rollout | 商业化与采用未知 |
| Contract Intelligence | 合同洞察与谈判 | live | Harvey + 合作生态 | 与 Docusign 等合作 | 相对竞品效果未知 |
| Mistral models | EU 模型选择 | beta/early access，2026-05-26 | Mistral，多模型路由 | eligible EU customers opt-in | 尚非全球 GA |

## Strategy choices

| Dimension | Current choice | Implication | Unknown |
|---|---|---|---|
| User value | 节省研究、起草、审阅和尽调时间 | 高频高价值工作流 | 财务 ROI |
| Portfolio | 从助手到工作流 OS | 扩大控制面与 ARPU | 产品复杂性 |
| Build/buy/partner | 自建 orchestration/UX/legal engineering；采购模型与内容 | 快速迭代但依赖外部层 | 自研比例 |
| Model route | multi-model，按任务路由 | 降低单一供应商风险 | 路由质量与成本 |
| Commercial | 企业销售，公开定价缺失 | 高 ACV 可能性 | attach、折扣、毛利 |
| Compounding | custom agents、工作流、集成和部署知识 | 潜在锁定和反馈 | 数据权利与自动积累程度 |

## Adoption and economics

| Signal | Evidence | Strength | Implication |
|---|---|---|---|
| Availability | 多产品公开上线 | strong | 已过 demo 阶段 |
| Usage | 100,000+ 律师、25,000+ agents（公司自报） | limited | 规模信号强 |
| Outcomes | Repsol 96% adoption、每周节时 4–6 小时等案例 | limited | 价值存在，需独立验证 |
| Paid expansion | firmwide 部署与客户扩张公告 | limited | 有扩张迹象 |
| Inference cost | 未公开 | none | P0 |
| Gross margin | 未公开 | none | P0 |
| Human review/legal engineering | embedded legal engineers 支持 agents | limited | 可能压低可扩张性 |
| Liability | 未公开事故与保险 | none | P0 |

## Company comparison

| Dimension | Harvey | Legora | CoCounsel/Westlaw | Verdict |
|---|---|---|---|---|
| Live portfolio | broad | broad | broad, content-led | 功能差距缩小 |
| Agent execution | 大规模 custom agents（自报） | Agent live | agentic 产品推进 | Harvey 当前信号最强 |
| Content | 连接 premium sources | 连接数据/知识 | 控制 Westlaw/Practical Law | incumbent 领先 |
| Adoption | 公司自报规模大 | 官方客户增长 | 巨大既有客户基座 | 各有优势 |
| Economics | unknown | unknown | 可捆绑 | 无法判断 |
| Dependency | model/content partners | model/content partners | 模型依赖但内容自有 | Harvey 风险更高 |

## Strategic verdict

- Differentiated：高端法律客户信任、产品广度、agents 部署与法律工程
- Commodity：基础生成、通用检索、简单起草
- Partner-dependent：基础模型、部分法律内容、云和生态集成
- Monetization：已商业化，但 AI 产品级经济性 unknown
- Most important dependency：能否把高人工部署的法律工程转化为可扩张的软件资产
- Falsified if：NRR 和毛利弱、agents 需要持续重人工维护，或 incumbent 同任务达到同等效果并低价捆绑
