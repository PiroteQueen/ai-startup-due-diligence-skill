<!--
[INPUT]: 依赖已完成且可验证的技能能力变化
[OUTPUT]: 对外提供版本化的新增、变更与修复记录
[POS]: 项目发布记忆，连接技能版本与可观察行为
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Changelog

All notable changes to this skill are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Slimmed `SKILL.md` toward progressive disclosure: the external-research, competitor, and AI-strategy gates now state only their trigger, a one-line pass criterion, and a link, with the full pass checklists living solely in their reference files (`source-access-strategy.md` §6, `competitor-research.md` §10, `ai-product-strategy.md` §8). Numeric thresholds are no longer duplicated between `SKILL.md` and the references.
- Tightened the skill `description` to a what-plus-when trigger, removing internal jargon while preserving the use-case cues.
- Made the smallest useful output the default and the full multi-file package an explicit opt-in, and de-enumerated the deliverable list in both mental-model blocks so the output-package table is its single source of truth.
- Split human-readable outputs into `worked-examples/` and machine checks into company-agnostic `tests/fixtures/`.
- Replaced the company/date/score-specific test validator with a data-driven `scenario.yaml` contract.
- Added separate regression scenarios for the default minimal output and a full `Need more evidence` package.
- Hardened the scenario validator: a malformed `scenario.yaml` (missing required key, missing referenced file, or `modules` without `coverage`) now fails with a single clean error instead of a traceback.
- Added ledger schema validation for priority, coverage credit, and evidence status; malformed ledgers now also fail with one clean error.
- Replaced keyword-presence assertions with structured Markdown field, table, and bullet-row validation for verdicts, coverage, modules, source fallback, AI status, and competitor layers.
- Aligned the structured validator with the real template output contract so it verifies what the skill actually produces: it now reads the competitor "Competition layers" table, the `Product / feature` AI inventory column, the "Failed or blocked research" table, and the coverage `Readiness` column, and accepts a bulleted `- This verdict reverses if:` line. Added `- Verdict:` / falsifiability anchors to the Chinese DD and IC memo templates and an `Omitted appendices:` line to OnePage.
- Made OnePage the default minimal decision output (it carries verdict, falsifiability, and the omitted-appendices notice); the Q&A gap list is the accompanying coverage/gap inventory.
- Expanded worked-example leak checks beyond URLs to email addresses, exact calendar dates, and currency amounts.
- Unified the AI lifecycle status as `beta/pilot`, rejected fake blocked-source recoveries with invalid failure types, and stopped treating `Applicable? = no` competitor layers as covered.
- Centralized every controlled vocabulary (failure types, AI status, evidence status, stage dimensions, verdicts, weights/credits) in a single `scripts/vocab.py`; both validators import it instead of hardcoding their own copies, and a new `validate_skill` check fails if any template's spelled-out option list drifts outside the vocab.
- Gitignored `test-runs/` as a private scratch area so real-company runs are never committed; de-identify into `worked-examples/` before sharing.

### Fixed

- Corrected the README to say it prevents "eight" common mistakes and updated the project tree for the behavioral validator, fixtures, and worked examples.
- De-identified the full worked example by removing real entity, customer, product, competitor, financing, scale and URL identifiers.

## [1.4.0] - 2026-06-18

### Added

- Added `references/research/source-access-strategy.md` with claim-specific source ladders, one-attempt blocked-source handling, fallback routes, origin-aware corroboration, and a completion test that does not depend on Crunchbase or any single commercial database.
- Added `references/research/ai-product-strategy.md` and `templates/appendices/ai-product-strategy.md` for standalone, dated analysis of AI feature portfolios, user value, build/buy/model choices, adoption, monetization, economics, moat, and platform dependency.
- Added L1/L2/L3 architecture documentation and validation coverage for the new research and AI strategy contracts.

### Changed

- Expanded diligence from seven to eight modules by separating Product / Technology from AI Product & Capability Strategy.
- Split flat rule and template folders into `diligence/`, `research/`, `decisions/`, and `appendices/` responsibility boundaries.
- Expanded the output package with `08-ai-product-strategy.md` and renumbered the external research log to `09-external-research-log.md`.
- Upgraded the research log and evidence ledger to retain access failures, fallback sources, shared evidence origins, and source-diversity limits.
- Updated the OnePage, IC memo, Chinese systematic DD, competitor landscape, Q&A list, data-room request, risk register, orchestration, and public README to preserve the new module boundaries.
- Forward-tested on a real company and fixed two discovered rule gaps: `Need more evidence` now permits only a conditional, non-recommendation IC pre-read, and coverage tables must expose weighted points earned / possible.

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

## [1.3.2] - 2026-06-10

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
