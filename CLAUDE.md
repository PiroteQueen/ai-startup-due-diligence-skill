# AI Startup Due Diligence Skill - 证据驱动的 AI 创业投资尽调系统
Markdown + YAML + Python

<directory>
references/ - 尽调规则与判断协议（2 个子目录：diligence、research）
</directory>

<directory>
templates/ - 可复用交付契约（2 个子目录：decisions、appendices）
</directory>

<directory>
scripts/ - 结构与契约验证（1 个验证器）
</directory>

<directory>
examples/ - 最小示例输入（1 个示例项目）
</directory>

<directory>
test-runs/ - 真实公司前向测试与回归证据（按公司和日期隔离）
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
- 2026-06-19：Harvey 真实公司前向测试；修复 NME/IC memo 冲突和不可复算覆盖率。
- 2026-06-19：SKILL.md 三个 gate 收敛为触发+判据+链接，完整判据下沉至 reference（单一事实源）；压缩 description；修复 README 计数与目录树。
