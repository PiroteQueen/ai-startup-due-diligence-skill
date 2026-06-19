<!--
[INPUT]: 依赖 Harvey 公开证据台账、AI 战略、竞品与裁决规则
[OUTPUT]: 对外提供条件式 IC memo
[POS]: decisions 的深度判断文档，明确不是完成版投资 DD
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Harvey Conditional IC Pre-read — Not decision-ready

## Executive view

- Recommendation：Need more evidence
- Confidence：medium
- Coverage：95 / 160 weighted points = 59.4%，round to 60%；存在多个 recommendation-blocking P0
- Invest reason：法律 AI 中罕见的真实产品广度、企业部署和工作流采用
- Do-not-invest reason：110 亿美元估值下，公开资料无法证明收入质量、单位经济和交易回报
- Reversal：强 NRR、健康毛利、可重复 ROI、可防御的数据/工作流资产及合理条款获得核验

## Thesis

Harvey 的潜在终局不是“律师版聊天机器人”，而是承载研究、起草、文档处理、协作和 agent 执行的法律操作系统。其价值取决于能否长期控制工作流、内容连接、治理与部署，而非是否调用了最强模型。

## Product and AI strategy

公开产品包括 Assistant、Vault、Knowledge、Agents、Command Center、Shared Spaces 和 Contract Intelligence。Assistant 支持引用来源、深度分析、文档生成和结构化 review tables；Agents 被定位为执行端到端复杂法律工作。2026-05 的 Mistral Early Access 证明多模型路线正在落地。

产品状态与广度较强，但独立 eval、错误率、人工复核、模型路由成本及法律工程投入未知。因此，“平台存在”可判定为 known，“平台经济性和 durable moat”只能判定为 inferred。

## Market and traction

Harvey 官方披露超过 100,000 名律师、1,300+ 组织、60+ 国家，多数 AmLaw 100 与 500+ 企业法务团队。Repsol 案例披露 96% adoption 和每名律师每周节省 4–6 小时。这些是强烈采用信号，但主要源自 Harvey 页面，缺乏合同、续约和独立 ROI 验证。

## Business and financials

本轮 2 亿美元融资与 110 亿美元估值有官方公告。若全部为 primary，则隐含 pre-money 约 108 亿美元，新投资人持股约 1.8%。10x 回报需要公司价值约 1,100 亿美元，要求 Harvey 成为大型全球软件/信息服务平台，而非单一法律 AI 工具。

## Stage

| Dimension | State | Basis | Confidence | Next gate |
|---|---|---|---|---|
| Product | scaled_product | 全球多产品企业部署 | medium | 可靠性与使用遥测 |
| PMF | expanding_pmf | firmwide deployments、使用指标、规模 | medium | NRR/续约/合同 |
| GTM | scalable_motion | 全球企业与律所扩张 | medium | CAC、rep productivity |
| Financing | series_b_plus | 累计融资超 10 亿美元 | high | 交易文件 |

## Competition

Legora 在 agentic operating system、Agent、Monitors 和工作流上构成最接近的新创竞争。Thomson Reuters CoCounsel/Westlaw 与 Lexis+ Protégé 控制法律内容和既有分销，是更危险的 incumbent。客户也可用通用模型、内部检索与 DMS 构建局部替代。

## Red-team

1. Pain vs pay：大量部署支持预算存在，但 ROI 仍不透明。
2. Demo vs workflow：通过；已有 firmwide 与日常使用证据。
3. Wrapper vs system：部分通过；工作流和集成较深，但模型/内容依赖仍大。
4. TAM vs wedge：法律是清晰 wedge，专业服务扩张尚需证明。
5. Team vs execution：执行速度强。
6. VC-fit：业务可能 venture-scale，但新投资价格要求极高终局。
7. Plan evolution：从 assistant 转向 agents 合理，但可能扩大焦点。
8. Funding vs stage：资本储备远超普通 SaaS，需要核验用途和组织纪律。
9. Runtime dependency：多模型降低单一供应商风险，但不消除内容和模型依赖。

## Decision gates

| Gate | Threshold | Owner | If missed |
|---|---|---|---|
| Revenue quality | GRR ≥90%、NRR ≥120% 或有充分解释 | CFO | Pass/重定价 |
| Economics | 经核验的健康毛利及明确改善路径 | CFO/CTO | 不按 SaaS 定价 |
| Product moat | 同任务 eval 显著优于通用模型与 incumbent | CTO | Watch/Pass |
| Customer ROI | 多个独立客户确认续约与可量化价值 | CEO/CRO | 下调 PMF |
| Deal economics | 条款支持目标回报且无偏好权陷阱 | Counsel | Pass |
