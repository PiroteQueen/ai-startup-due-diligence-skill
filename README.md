<!--
[INPUT]: 依赖 SKILL.md、references/、templates/ 与安装方式
[OUTPUT]: 对外提供项目定位、能力、结构、安装、使用与验证说明
[POS]: 项目公开入口，面向技能使用者与贡献者解释稳定能力
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# AI Startup Due Diligence Skill

An open-source [Agent Skill](https://agentskills.io) for AI startup due diligence. It turns scattered evidence — decks, interviews, demos, public research — into a structured evidence ledger and, when requested, a durable multi-file output package: Chinese Systematic DD, OnePage, Q&A gap list, IC memo, risk register, data-room request, competitor landscape, standalone AI product strategy, and external research log.

Works with any agent that supports the Agent Skills standard (Claude Code, Claude API, Cursor, Codex, and others).

## Core idea

Do **not** start by writing a polished investment memo. Start by building a diligence evidence ledger:

```text
Target company
  → modules
  → key questions
  → evidence-backed answers
  → unanswered gaps
  → confidence / contradiction / red flags
  → four-dimensional stage map / VC-fit / capital path
  → outputs: smallest useful subset by default; full multi-file package on request
```

Diligence is question coverage management, not summarization. The skill is designed to prevent eight common mistakes:

1. Treating a polished deck as verified evidence.
2. Treating an AI demo or wrapper as durable moat.
3. Turning unknowns into confident narrative.
4. Treating fundraising as an accomplishment by itself.
5. Forcing a good non-VC business into a venture-scale narrative.
6. Ignoring repeated investor no's instead of diagnosing the underlying risk layer.
7. Depending on Crunchbase or another blocked/paywalled database as a single point of research failure.
8. Burying a company's AI products and strategic choices inside generic product prose.

## What's inside

```text
ai-startup-due-diligence/
├── SKILL.md                      # Agent-facing entry point (metadata + workflow)
├── references/
│   ├── diligence/                # Questions, scoring, red-team, decision and confidence rules
│   └── research/                 # Source fallbacks, AI strategy, competitors, orchestration
├── templates/
│   ├── decisions/                # Chinese DD, OnePage, Q&A, data room, IC memo, risks
│   └── appendices/               # Evidence ledger, research log, competitors, AI strategy
├── examples/
│   └── sample-ai-company/        # Fictional example for orientation
├── scripts/
│   ├── validate_skill.py         # Deterministic package checks (run in CI)
│   └── validate_test_run.py      # Data-driven behavioral scenario validator
├── tests/
│   └── fixtures/                 # Company-agnostic regression scenarios
└── worked-examples/
    └── anonymized-regulated-ai-platform/ # De-identified full output example
```

By design, `examples/` holds input-only briefs, `worked-examples/` holds human-readable de-identified outputs, and `tests/fixtures/` holds company-agnostic machine checks. To see a full package, browse [`worked-examples/anonymized-regulated-ai-platform/`](worked-examples/anonymized-regulated-ai-platform/).

## Installation

### One command (recommended)

The [Skills CLI](https://github.com/vercel-labs/skills) installs to any supported agent (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Windsurf, and 50+ more) and lets you choose scope and agents interactively:

```bash
# Project-level (interactive: pick agents, scope, symlink/copy)
npx skills add PiroteQueen/ai-startup-due-diligence-skill

# Global, non-interactive, e.g. for Claude Code + Cursor
npx skills add PiroteQueen/ai-startup-due-diligence-skill -g -a claude-code -a cursor -y
```

### Manual install (git clone)

The skill directory name should match the skill name (`ai-startup-due-diligence`), per the Agent Skills spec:

```bash
git clone https://github.com/PiroteQueen/ai-startup-due-diligence-skill.git \
  <skills-dir>/ai-startup-due-diligence
```

Where `<skills-dir>` depends on your agent and scope:

| Agent | Personal (all projects) | Project (committed to repo) |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` or `.agents/skills/` |
| Codex CLI / IDE | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` or `~/.agents/skills/` | `.gemini/skills/` or `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` |
| Windsurf | `~/.codeium/windsurf/skills/` | `.windsurf/skills/` |

Tip: `.agents/skills/` is the emerging cross-agent convention — Cursor, Codex, and Gemini CLI all read it, so one project-level copy can serve several tools.

### As a team default (git submodule)

Pin a version inside your repo so everyone who clones gets the same skill:

```bash
git submodule add https://github.com/PiroteQueen/ai-startup-due-diligence-skill.git \
  .agents/skills/ai-startup-due-diligence
```

### Claude API / Claude.ai / other agents

For the Claude API, bundle the directory as a skill per the [Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview); for Claude.ai, zip the directory and upload it under Settings → Capabilities. On platforms without skill support, paste `SKILL.md` (plus the relevant `references/` and `templates/` files) into context.

## Usage

Ask your agent:

```text
Use ai-startup-due-diligence to evaluate this AI startup deck.
First produce a Q&A gap list and evidence ledger; do not write the memo until gaps are explicit.
```

Recommended sequence (the skill enforces this):

1. Intake provided materials; gather external evidence when the company is identifiable.
2. Separate provided materials from externally verified evidence.
3. Route each material claim through primary and fallback sources; log blocked/paywalled sources instead of repeatedly retrying them.
4. Build weighted module coverage across 8 modules using P0/P1/P2 priority, evidence credit, and gating questions.
5. Produce a standalone AI product and capability strategy for the target and priority competitors.
6. Separately map product maturity, PMF status, GTM maturity, and financing stage; then assess VC-fit, capital path, and the risk onion.
7. Produce the Q&A gap list and red-team the thesis.
8. Only then generate Chinese Systematic DD, OnePage, risk register, IC memo, data-room request, or follow-up request list.

## Output package

For a full diligence run or project-folder workflow, the skill should create a durable multi-file package rather than hiding everything in one memo:

| File | Purpose |
| --- | --- |
| `01-chinese-systematic-dd.md` | Primary Chinese decision narrative: one core question, verdict, five gates, evidence status, next actions |
| `02-onepage.md` | One-page summary for quick investment discussion |
| `03-qa-gap-list.md` | Answered/unanswered questions and evidence gaps |
| `04-data-room-request.md` | Source-document request list tied to unresolved P0 gates |
| `05-ic-memo.md` | Full IC memo for Proceed/Watch/Pass; conditional pre-read for Need more evidence |
| `06-risk-register.md` | Risk register with mitigation and next checks |
| `07-competitor-landscape.md` | Competitor/substitute appendix with same-dimension evidence |
| `08-ai-product-strategy.md` | Standalone target-and-competitor AI product, adoption, monetization, moat, and dependency analysis |
| `09-external-research-log.md` | Auditable research log, blocked-source failures, fallback routes, and source-diversity notes |

For lightweight usage, generate the smallest useful subset and explicitly say which appendices were omitted.

## Validate locally

```bash
python3 -m pip install pyyaml
python3 scripts/validate_skill.py
for scenario in tests/fixtures/*/; do python3 scripts/validate_test_run.py "$scenario"; done
python3 -m unittest tests/test_validator_negative_cases.py
```

This checks package structure plus every declared behavioral scenario. CI runs the same checks on every push and PR.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes are tracked in [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
