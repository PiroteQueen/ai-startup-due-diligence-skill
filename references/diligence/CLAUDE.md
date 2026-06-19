# diligence/
> L2 | 父级: ../CLAUDE.md

成员清单
confidence-downgrade-rules.md: 置信度降级规则，处理缺失、二手、冲突与不可访问证据。
coverage-stage-model.md: 加权覆盖与四维阶段模型，定义 P0/P1/P2 和决策就绪度。
decision-rules.md: 确定性裁决规则，将证据映射为 Proceed/Watch/Pass/Need more evidence。
mega-round-sanity-check.md: 超大融资与高估值专项校验，防止融资叙事替代业务证据。
module-questions.md: 八模块问题库，驱动证据台账与 Q&A 缺口。
pattern-library.md: PMF、AI wrapper、融资与组织风险模式库。
red-team-checks.md: 九项反证检查，强制搜索投资论点的破坏性证据。

依赖边界：
- 只消费研究证据，不负责访问外部来源。
- 所有 verdict 必须经过覆盖率、红队和降级规则。

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
