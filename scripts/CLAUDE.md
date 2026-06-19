# scripts/
> L2 | 父级: ../CLAUDE.md

成员清单
validate_skill.py: 验证技能元数据、文件、链接、模板字段、密钥与 worked-example 标识符泄漏。
validate_test_run.py: 校验 scenario/ledger schema，并结构化验证输出范围、verdict、coverage、来源回退、AI 与竞品契约。

依赖边界：
- 验证器只读项目文件，不修改技能内容。
- 新增强制规则或模板时必须增加对应断言。

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
