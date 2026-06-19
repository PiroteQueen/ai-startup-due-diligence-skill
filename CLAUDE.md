# AI Startup Due Diligence Skill - 证据驱动的 AI 创业投资尽调系统
Markdown + YAML + Python

<directory>
references/ - 尽调规则与判断协议（2 个子目录：diligence、research）
</directory>

<directory>
templates/ - 可复用交付契约（2 个子目录：decisions、appendices）
</directory>

<directory>
scripts/ - 结构与契约验证（2 个验证器 + 受控词表单一事实源 vocab.py）
</directory>

<directory>
examples/ - 最小示例输入（1 个示例项目）
</directory>

<directory>
tests/ - 公司无关的数据驱动回归场景与验证器反向用例
</directory>

<directory>
worked-examples/ - 去标识化的完整输出示例，不参与测试判定
</directory>

<config>
SKILL.md - 技能入口，定义八模块尽调、研究门禁、判断流程与输出包。
</config>

<config>
README.md - 面向使用者的能力说明与安装入口。
</config>

架构决策：
- 证据台账是单一事实源；报告只从台账派生。
- 外部研究按 claim 路由来源；任何数据库都不是单点门禁。
- AI 产品与能力战略独立于通用产品技术，避免功能清单吞没商业与战略判断。
- 竞争研究和 AI 战略分别维护，再在 IC memo 汇合。
- 规则与模板按“判断核心 / 研究能力”和“决策主文档 / 证据附录”分层，单层不超过 8 个文件。

开发规范：
- 新增或修改规则时同步更新对应模板与验证器。
- 每个业务文件保留 INPUT/OUTPUT/POS 契约。
- 文件增删先更新所属 L2，再检查本文件。

变更日志：
- 2026-06-18：新增来源替代路由与独立 AI 产品战略模块；尽调由七模块升级为八模块。
- 2026-06-19：真实公司前向测试发现并修复 NME/IC memo 冲突和不可复算覆盖率。
- 2026-06-19：SKILL.md 三个 gate 收敛为触发+判据+链接，完整判据下沉至 reference（单一事实源）；压缩 description；修复 README 计数与目录树。
- 2026-06-19：默认产出最小集、全包改 explicit opt-in；mental-model 块去枚举，重申 examples/ 纯输入边界。
- 2026-06-19：拆分匿名 worked example 与数据驱动 tests；验证器移除公司、日期、固定分数和固定九文件硬编码。
- 2026-06-19：场景验证器统一畸形输入为干净错误（缺 key/文件/coverage 不再抛 traceback）；test-runs/ 设为 gitignored 本地草稿区。
- 2026-06-19：消除 validator/fixtures 与 templates 的结构分叉——validator 改读模板真实结构（竞品层级表、Product/feature 列、Failed-or-blocked 表、Readiness 列、可选 bullet 的反转条件），模板补 Verdict/falsifiability/Omitted 锚点；minimal 主决策输出改用 OnePage。负向自检证明 validator 非空过。
- 2026-06-19：统一 `beta/pilot` 状态词，严格验证来源失败类型与竞争层适用性，并将三类假绿灯固化为 CI 反向回归测试。
- 2026-06-19：受控词表收敛到单一事实源 `scripts/vocab.py`，两验证器 import 取代各自硬编码；新增模板选项 ⊆ vocab 的对齐检查与对应负向测试，根治词表多处重复。
