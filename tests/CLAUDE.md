# tests/
> L2 | 父级: ../CLAUDE.md

成员清单
fixtures/: 公司无关的数据驱动行为场景。
test_validator_negative_cases.py: 破坏合法夹具，验证非法失败类型、`Applicable? = no` 与非规范 AI 状态必定失败。

依赖边界：
- 测试验证通用契约，不展示完整尽调示例。
- 测试不得包含真实公司、客户、竞品、日期或固定外部来源。
- 正向场景证明合法输出通过；反向用例证明错误输出不能假通过。

[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
