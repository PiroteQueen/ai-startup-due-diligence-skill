# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.0] - 2026-06-10

### Changed

- Aligned `SKILL.md` frontmatter with the [Agent Skills spec](https://agentskills.io/specification): added `license` and `metadata` (author, version) fields, rewrote `description` with explicit trigger keywords.
- Restructured for progressive disclosure: `SKILL.md` now holds the workflow and links to `references/` and `templates/` via relative paths instead of inlining everything.
- Removed private project paths and personal-vault references from the skill body and README.
- Rewrote `README.md` for open-source distribution with installation instructions for Claude Code, Cursor, and other Agent Skills-compatible products.
- Upgraded `scripts/validate_skill.py` to check spec-level name format rules and relative file references.

### Added

- `references/module-questions.md` — full key-question bank for the seven diligence modules.
- `references/red-team-checks.md` — nine contradiction checks, risk onion layers, post-raise operating risks, investor-no diagnostics.
- `CONTRIBUTING.md` and `CHANGELOG.md`.

## [1.0.0] - 2026-06-10

### Added

- Initial release: seven-module diligence framework, evidence ledger, Q&A gap list, OnePage, IC memo, risk register templates, VC fundability lens, CI validation.
