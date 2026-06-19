<!--
[INPUT]: 依赖未解决的 P0 门禁、风险洋葱、AI 战略与交易结构缺口
[OUTPUT]: 对外提供按优先级、责任和结论影响组织的资料室请求
[POS]: templates/decisions 的证据补全入口，把未知项转换为可执行文件请求
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# 资料室请求模板

> Purpose: convert evidence gaps and risk-onion layers into a concrete data-room request list. Use when the current materials are pitch decks, teasers, memos, or second-hand introductions and the next step is evidence verification.

## 使用原则

- 资料室不是“多要材料”，而是把投资判断从故事推进到证据。
- 只请求能改变结论的文件；不要堆无关清单。
- P0 缺失时不得写 Proceed。
- 如果对方只能提供截图、转发 PDF、口头说明，应保持 Watch / Need more evidence。

## 0. 请求说明，可直接发送

> 我们对项目方向有兴趣，但在进入投资判断前，需要先完成基础资料室核验。请问是否可以开放正式 Data Room？我们希望先查看交易条款、股权结构、领投方确认、公司治理、团队角色、技术产品证据、客户/部署证据、数据/IP/合规材料和融资用途里程碑。在资料室开放前，我们只能把当前 memo 视为初步介绍材料，暂不能形成投资结论。

## 1. 交易与股权

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | 本轮 term sheet | 本轮是否真实、价格和条款是否一致 | 不能 Proceed |
| P0 | cap table，含 fully diluted 口径 | 当前股权结构、稀释、期权池、优先权 | 估值和回报无法判断 |
| P0 | subscription agreement / SPA / SAFE / note 文件 | 投资工具与权利 | 无法确认法律权利 |
| P0 | primary / secondary / SPV 结构说明 | 买的是公司新股、老股还是中间层份额 | 进入权和权利需降级 |
| P1 | 历史融资文件 | liquidation stack、优先权、反稀释 | 退出回报不清 |

## 2. 领投方与 allocation

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | lead investor confirmation | 谁真实领投 | 领投叙事不能采信 |
| P0 | allocation letter / allocation email from authorized party | 我方是否有真实份额 | 交易可进入性不成立 |
| P1 | closing timetable | 是否仍在窗口期 | 时间和机会成本不清 |
| P1 | 投资委员会/董事会批准状态 | 是否已批准还是仅讨论 | 交易确定性降级 |

## 3. 公司治理与信息权

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | legal entity chart | 投资主体、运营主体、IP 主体 | 法律结构不清 |
| P0 | charter / investor rights agreement | 信息权、投票权、保护性条款 | 投后权利无法判断 |
| P1 | side letters | 是否存在不平等待遇 | 经济权利可能被稀释 |
| P1 | transfer restrictions | 二级转让限制 | 流动性和退出受限 |

## 4. 团队与关键人员

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | founder employment / role confirmation | 创始人是否全职、实质角色 | 团队结论不能高于 medium |
| P0 | org chart + core team roster | 核心能力是否在团队内 | 执行能力待核验 |
| P1 | key hires offer letters / LinkedIn / bios | 人才来源与真实性 | 团队叙事降级 |
| P1 | advisor vs employee distinction | 是否把顾问包装成团队 | 团队质量可能被夸大 |

## 5. 技术、产品、数据

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | product demo / prototype access | 是否有可运行产品 | 只能视为叙事或原型 |
| P0 | benchmark / eval methodology | 性能是否可复现 | 技术结论不能高于 low |
| P0 | architecture / model / data pipeline overview | 技术路线与依赖 | moat 无法判断 |
| P1 | data rights / licensing | 数据是否合法、可持续 | 合规和 moat 风险 |
| P1 | compute contracts / infrastructure plan | 成本与规模化能力 | 资本强度无法判断 |

## 6. AI 产品与能力战略

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | AI 产品/功能清单，含 live、beta、announced、retired 状态与日期 | 实际能力与路线图是否混淆 | AI 战略 coverage incomplete |
| P0 | AI 功能使用、留存、付费 attach、客户结果数据 | AI 是否产生真实采用与商业价值 | 不能声称 AI 产品已验证 |
| P0 | build/buy/partner、模型供应商、数据与 eval 架构 | 差异化和供应商依赖 | moat 与依赖无法判断 |
| P1 | AI 定价、推理成本、人工审核、毛利影响 | AI 商业化与单位经济 | AI 盈利能力未知 |
| P1 | AI roadmap 与 feature retirement 记录 | 战略方向和执行纪律 | 只能判断当前快照 |

## 7. 客户、部署、收入

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | signed customer contracts / paid pilots | 是否有真实付费需求 | 不能声称 PMF |
| P0 | usage / retention / expansion data | 是否嵌入工作流 | workflow lock-in 未证实 |
| P1 | LOI / design partner agreements | 是否有需求线索 | 只能算弱证据 |
| P1 | customer references | 客户痛点与替代方案 | 市场判断不稳 |

## 8. 竞品与替代方案

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | management view of direct competitors | 公司是否理解直接竞争 | 竞争判断 incomplete |
| P0 | substitute / incumbent comparison | 客户为什么不自建、不用现有方案 | moat 待核验 |
| P1 | win/loss notes | 真实胜负原因 | GTM 判断不稳 |
| P1 | pricing comparison | 价值捕获是否合理 | 商业模式待核验 |

## 9. 融资用途与里程碑

| 优先级 | 文件/证据 | 要验证的问题 | 缺失时的结论影响 |
|---|---|---|---|
| P0 | use of funds | 本轮资金买什么证据 | 融资合理性不清 |
| P0 | next milestone plan | 下一轮/盈利前必须证明什么 | capital path 不成立 |
| P1 | hiring plan and burn forecast | 是否有组织腐蚀风险 | post-raise 风险升高 |
| P1 | downside plan | 资金不顺时能否收缩 | 生存风险不清 |

## 10. 输出要求

在 DD 报告中把请求结果写成：

| P0 请求 | 状态 | 结果 | 结论影响 |
|---|---|---|---|
| ... | 已收到 / 未收到 / 被拒绝 / 不适用 | ... | Proceed / Watch / Pass / 降级 |
