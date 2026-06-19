<!--
[INPUT]: 依赖 Company Alpha 证据、红队、AI 战略和估值门禁
[OUTPUT]: 对外提供风险、证据状态与下一检查
[POS]: decisions 的风险单一视图
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Company Alpha — Risk Register

| Risk | Category | Severity | Evidence | Status | Mitigation / next check |
|---|---|---:|---|---|---|
| 估值预付成功 | vc_fit | high | 高位后期官方估值 | known | 退出情景与收入质量模型 |
| NRR/续约未知 | pmf_status | high | 公开材料缺失 | unknown | cohort 与合同 |
| AI 推理和法律工程成本 | ai_unit_economics | high | 多模型、embedded legal engineering | inferred | COGS 拆分 |
| 模型供应商依赖 | model_dependency | medium | 已引入第二模型供应商；其他细节有限 | known/unknown | provider agreements、routing |
| 专业内容控制 | distribution_dependency | high | incumbent 掌握专有内容 | known | 许可与替代路线 |
| 幻觉/责任事故 | legal_data | high | 高风险法律输出 | unknown | incident、eval、保险 |
| 竞争快速同质化 | market | high | 新创与 incumbent 功能趋同 | known | win/loss 与 benchmark |
| 超额融资组织腐蚀 | post_raise_org | medium | 累计融资超 10 亿美元 | inferred | headcount、里程碑与 burn |
| 客户集中度 | financial | medium-high | 未公开 | unknown | top-20 ARR |
| ROI 难量化 | ai_adoption | high | 客户自报节时但财务 ROI 未独立核验 | limited | 客户财务案例 |
