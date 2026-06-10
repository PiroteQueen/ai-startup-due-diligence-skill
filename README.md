# AI Startup Due Diligence Skill

An open-source [Agent Skill](https://agentskills.io) for AI startup due diligence. It turns scattered evidence — decks, interviews, demos, public research — into a structured evidence ledger, Q&A gap list, OnePage, IC memo, risk register, and follow-up diligence plan.

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
  → stage gate / VC-fit / capital path
  → outputs: Q&A List, OnePage, IC memo, risk register, follow-up plan
```

Diligence is question coverage management, not summarization. The skill is designed to prevent six common mistakes:

1. Treating a polished deck as verified evidence.
2. Treating an AI demo or wrapper as durable moat.
3. Turning unknowns into confident narrative.
4. Treating fundraising as an accomplishment by itself.
5. Forcing a good non-VC business into a venture-scale narrative.
6. Ignoring repeated investor no's instead of diagnosing the underlying risk layer.

## What's inside

```text
ai-startup-due-diligence/
├── SKILL.md                      # Agent-facing entry point (metadata + workflow)
├── references/
│   ├── module-questions.md       # Full key-question bank for 7 diligence modules
│   └── red-team-checks.md        # Nine contradiction checks, risk onion, post-raise risks
├── templates/
│   ├── evidence-ledger.yaml      # Per-claim evidence schema
│   ├── qa-gap-list.md            # Coverage table + answered/unanswered questions
│   ├── onepage.md                # One-page investment summary
│   ├── ic-memo.md                # Full IC memo skeleton
│   └── risk-register.md          # Risk register with AI-specific categories
├── examples/
│   └── sample-ai-company/        # Fictional example for orientation
└── scripts/
    └── validate_skill.py         # Deterministic package checks (run in CI)
```

## Installation

The skill directory name should match the skill name (`ai-startup-due-diligence`), per the Agent Skills spec.

### Claude Code

```bash
git clone https://github.com/PiroteQueen/ai-startup-due-diligence-skill.git \
  ~/.claude/skills/ai-startup-due-diligence
```

### Cursor

```bash
git clone https://github.com/PiroteQueen/ai-startup-due-diligence-skill.git \
  ~/.cursor/skills/ai-startup-due-diligence
```

### Claude API / other agents

Bundle the directory as a skill per your platform's docs, or just paste `SKILL.md` (plus the relevant `references/` and `templates/` files) into context.

## Usage

Ask your agent:

```text
Use ai-startup-due-diligence to evaluate this AI startup deck.
First produce a Q&A gap list and evidence ledger; do not write the memo until gaps are explicit.
```

Recommended sequence (the skill enforces this):

1. Intake provided materials; gather external evidence when the company is identifiable.
2. Separate provided materials from externally verified evidence.
3. Build module coverage across 7 modules (thesis, team, product/AI, traction, financials, legal, capital path).
4. Map stage (BPMF/APMF), VC-fit, capital path, and the risk onion.
5. Produce the Q&A gap list.
6. Red-team the thesis with nine contradiction checks.
7. Only then generate OnePage, risk register, IC memo, or follow-up request list.

## Validate locally

```bash
python3 -m pip install pyyaml
python3 scripts/validate_skill.py
```

This checks frontmatter against the [Agent Skills spec](https://agentskills.io/specification) (name format, description length), required files, template sections, relative file references, and obvious secret-like strings. CI runs the same checks on every push and PR.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes are tracked in [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
