# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.3.1] - 2026-06-10

### Changed

- Documented full multi-file output package behavior in `SKILL.md` and `README.md`, including Chinese Systematic DD, OnePage, Q&A gap list, data-room request, IC memo, risk register, competitor landscape, and external research log.
- Clarified that full diligence runs or project-folder workflows should create durable files, while lightweight requests should generate the smallest useful subset and explicitly state omitted appendices.

## [1.3.0] - 2026-06-10

### Added

- Added `templates/chinese-systematic-dd.md` for Chinese-facing, coherent decision narratives organized around one core question, one verdict, five gates, evidence status, and next actions instead of exposing all internal modules.
- Added `templates/data-room-request.md` to convert risk-onion gaps and unresolved P0 gates into source-document requests grouped by transaction, allocation, governance, team, technology, customers, competition, and financing milestones.
- Added `references/mega-round-sanity-check.md` for pre-revenue, stealth, pre-product, unusually large financing, or unusually high valuation cases; includes ownership, capital-intensity, valuation, next-round, governance, and use-of-funds checks.
- Added `references/confidence-downgrade-rules.md` to cap conclusion strength when external research, transaction documents, founder-role evidence, product demo, benchmarks, customer proof, competitor research, data rights, or SPV rights are incomplete.

### Changed

- Wired the Chinese systematic DD, data-room request, mega-round sanity check, and confidence downgrade rules into `SKILL.md` Step 6 and the README file tree.
- Clarified that risk-onion output should lead to the next evidence request, interview, or external verification action, not just another abstract risk list.

## [1.2.0] - 2026-06-10

### Added

- Mandatory external-research gate with source-group coverage, high-materiality claim audit, disconfirming-evidence search, and explicit incomplete/blocked behavior.
- Dedicated competitor and substitute research protocol covering direct products, adjacent approaches, platforms, incumbents, customer-built alternatives, and manual/non-consumption.
- `templates/external-research-log.md` for auditable active-research records.
- `templates/competitor-landscape.md` for source-dated, same-dimension competitor evidence and valuation counterexamples.

### Changed

- Competition coverage now counts as answered only after the competitor gate passes.
- IC Memo and OnePage templates retain competitor evidence and link to a dedicated landscape appendix.
- Quality bar now prohibits completed-DD language when external research was possible but not attempted.

## [Unreleased]

### Changed

- Replaced raw answered-question coverage with weighted P0/P1/P2 coverage, evidence credits, readiness bands, and recommendation-blocking gating rules.
- Replaced the mixed stage label with separate product maturity, PMF status, GTM maturity, and financing stage dimensions.

### Added

- Added `references/coverage-stage-model.md` as the canonical scoring and stage-classification reference.
- Added `references/decision-rules.md` — deterministic verdict mapping: eligibility thresholds for Proceed/Watch/Pass/Need-more-evidence, a confirmed deal-breaker list, red-flag arithmetic that caps verdicts on pattern-library matches, mandatory Watch re-engagement triggers, a falsifiability statement for every verdict, and a decision-gates table format. Wired into Step 6, the quality bar, and the OnePage / IC memo templates.
- Added `references/orchestration.md` — optional multi-agent topology: parallel module-research agents constrained to evidence-ledger output, an independent red-team agent that sees the ledger but never the draft narrative, single-threaded verdict in the orchestrator, merge/dedup rules, and sequential fallback when subagents are unavailable.
- Added `references/pattern-library.md` — calibration examples: nine false-PMF patterns, six AI-wrapper death patterns, six true-PMF signals plus absent-PMF texture and the Sean Ellis cross-check, seven founder/team red flags, five fundraising red flags, and four market reality checks, each with a concrete verification test. Sourced from the pmarca startup guides (PMF, risk onion, funding amount), Munger/Andreessen misjudgment biases, and AI-native stage-gate playbooks. Wired into the stage-gate (Step 3) and red-team (Step 5) workflow so pattern matches force evidence-ledger downgrades.

### Fixed

- Added the missing Capital Path / VC Fit / Fundability module to the Q&A gap list coverage table and validator checks.

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
