<!--
[INPUT]: 依赖 Harvey 八模块证据评分和 P0 门禁
[OUTPUT]: 对外提供覆盖率、已知项和后续核验问题
[POS]: decisions 的证据缺口清单
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Harvey — Q&A Gap List

| Module | Weighted points earned / possible | Weighted coverage | P0 resolved / total | Unresolved P0 | Readiness | Confidence |
|---|---:|---:|---:|---|---|---|
| Basic Info / Thesis | 16 / 20 | 80% | 2 / 2 | 无 | decision-ready | high |
| Team | 12 / 20 | 60% | 1 / 2 | 组织效率与关键高管留任 | directional | medium |
| Product / Technology | 14 / 20 | 70% | 2 / 4 | 独立 eval；事故/可靠性 | not decision-ready | medium |
| AI Product & Capability Strategy | 14 / 20 | 70% | 2 / 4 | AI 单位经济；数据/eval 架构 | not decision-ready | medium |
| Traction / Market | 14 / 20 | 70% | 2 / 5 | NRR/续约；客户集中度；独立 ROI | not decision-ready | medium |
| Financials / Business Model | 6 / 20 | 30% | 0 / 4 | ARR bridge、毛利、burn、CAC | sparse | low |
| Legal / Compliance / Data Risk | 10 / 20 | 50% | 1 / 3 | 内容/数据权利；责任事故 | incomplete | medium-low |
| Capital Path / VC Fit / Fundability | 9 / 20 | 45% | 1 / 4 | 交易条款、退出回报、资金计划 | not decision-ready | low |

## Overall readiness

- Weighted points earned / possible：95 / 160
- Weighted coverage：59.4%，round to 60%
- Decision readiness：Not decision-ready
- Blocking P0：交易条款；NRR/续约；毛利与推理成本；客户集中度；内容/数据权利；独立 eval

## 已回答

- 产品真实进入工作流：官方产品和多家客户案例支持，但采用指标主要为公司自报。
- 公开融资存在：Harvey 于 2026-03-25 宣布融资 2 亿美元、估值 110 亿美元；具体条款未知。
- AI 是战略核心：产品组合和 agents 方向表明 Harvey 试图成为法律工作流操作层。

## P0 follow-ups

1. ARR bridge、GRR/NRR、cohort 和客户集中度。
2. 按产品/模型拆分的毛利、推理成本、人工法律工程成本。
3. term sheet、cap table、preference stack、allocation 与 primary/secondary 结构。
4. 独立同任务 benchmark、回归 eval、幻觉/事故与人工复核率。
5. 数据来源、内容许可、客户数据训练规则和输出责任。
6. 5–8 个客户访谈：采购、续约、替代预算、使用深度、可量化 ROI。
