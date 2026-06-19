# scripts/
> L2 | 父级: ../CLAUDE.md

成员清单
vocab.py: 受控词表的单一事实源（失败类型、AI 状态、阶段维度、证据状态、verdict 等），两验证器共同 import。
validate_skill.py: 验证技能元数据、文件、链接、模板字段、密钥与 worked-example 标识符泄漏；并强制模板选项 ⊆ vocab。
validate_test_run.py: 校验 scenario/ledger schema，并结构化验证输出范围、verdict、coverage、来源回退、AI 与竞品契约。

依赖边界：
- 验证器只读项目文件，不修改技能内容。
- 受控词表只在 vocab.py 定义一次；验证器与模板都以它为准，禁止各写一份。
- 新增强制规则或模板时必须增加对应断言。
- 来源回退只接受 vocab 声明的失败类型；竞争层只接受 `yes` / `applicable` 为已覆盖。

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
