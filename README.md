# AI Startup Due Diligence Skill

A Hermes/Claude skill package for AI startup due diligence.

This repo turns the `ai-startup-due-diligence` skill into a GitHub-trackable source package. It is distilled from the DDyst project logic: modular diligence, key questions, evidence-backed answers, completion status, Q&A gap lists, OnePage summaries, IC memos, and follow-up diligence plans.

The skill also incorporates the user's Obsidian VC / AI-startup synthesis: VC-fit, BPMF/APMF stage gates, risk-onion diagnostics, funding amount sanity checks, and post-raise operating risks. The goal is to distinguish “good business” from “venture-scale investment” instead of treating every polished AI deck as fundable.

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

The skill is designed to prevent six common mistakes:

1. Treating a polished deck as verified evidence.
2. Treating an AI demo or wrapper as durable moat.
3. Turning unknowns into confident narrative.
4. Treating fundraising as an accomplishment by itself.
5. Forcing a good non-VC business into a venture-scale narrative.
6. Ignoring repeated investor no's instead of diagnosing the underlying risk layer.

## What is included

- `SKILL.md` — the agent-facing skill entry point.
- `templates/` — reusable Markdown/YAML templates for diligence outputs.
- `examples/sample-ai-company/` — a minimal fictional example for orientation.
- `scripts/validate_skill.py` — deterministic package checks.
- `.github/workflows/ci.yml` — validates the skill package on push/PR.

## How to use with Hermes

Copy or symlink this package into your Hermes skills directory:

```bash
mkdir -p ~/.hermes/skills/research
ln -s "$PWD" ~/.hermes/skills/research/ai-startup-due-diligence
```

Then ask Hermes:

```text
Use ai-startup-due-diligence to evaluate this AI startup deck.
First produce a Q&A Gap List and evidence ledger; do not write the memo until gaps are explicit.
```

## Recommended diligence sequence

1. Intake user-provided materials.
2. Actively gather external evidence when the company/product/founders are identifiable.
3. Separate provided materials from externally verified evidence.
4. Build module coverage:
   - Basic Info / Thesis
   - Team
   - Product / Technology / AI
   - Traction / Market
   - Financials / Business Model
   - Legal / Compliance / Data Risk
   - Capital Path / VC Fit / Fundability
5. Map stage, VC-fit, capital path, and risk onion.
6. Produce Q&A Gap List.
7. Red-team AI moat and investment thesis.
8. Only then generate OnePage, Risk Register, IC Memo, or follow-up request list.

## Templates

- `templates/evidence-ledger.yaml`
- `templates/qa-gap-list.md`
- `templates/onepage.md`
- `templates/ic-memo.md`
- `templates/risk-register.md`

## Validate locally

```bash
python3 scripts/validate_skill.py
```

This checks:

- `SKILL.md` frontmatter parses.
- Required files exist.
- Templates contain expected sections.
- Obvious secret-like strings are not committed.

## License

MIT.
