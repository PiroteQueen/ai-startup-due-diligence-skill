<!--
[INPUT]: 依赖 SKILL.md 的工作流、模块问题库与证据台账结构
[OUTPUT]: 对外提供可选的多代理研究、红队、合并与裁决职责拓扑
[POS]: references/research 的执行编排规则，保证并行研究不污染最终判断
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
-->

# Multi-Agent Orchestration (Optional)

Use this topology when the host environment supports spawning subagents or parallel tasks (e.g. Claude Code tasks, Cursor subagents). If it does not, run the standard workflow in `SKILL.md` sequentially — every step works single-agent; this file only changes who executes it.

## Why split this way

- Module research is parallel because the eight modules are independent at evidence-gathering time.
- Red-teaming runs in a **separate context** because the agent that drafted the narrative has sunk cost in it (the same doubt-avoidance bias the pattern library flags in founders applies to analysts, including AI ones). The red-team agent must see only the evidence ledger, never the draft narrative.
- The verdict is **never delegated**: decision rules require the full merged ledger and global caps.

## Topology

```text
Orchestrator (main agent)
├── Research agents × 2–4 (parallel, fan-out by module)
├── Red-team agent × 1 (independent context, runs after merge)
└── Verdict + outputs (orchestrator itself, single-threaded)
```

## Role contracts

### Orchestrator

- Loads: `SKILL.md`, [coverage-stage-model.md](../diligence/coverage-stage-model.md), [decision-rules.md](../diligence/decision-rules.md).
- Does: Step 1 intake; assigns modules to research agents; merges ledgers; scores coverage; applies decision rules; writes final outputs (Step 6).
- Never: outsources the verdict or lets a subagent's prose bypass the ledger.

### Research agents

- Each owns 1–2 modules. Suggested split for 4 agents: (1) Basic Info + Team, (2) Product/Technology + AI Product & Capability Strategy, (3) Traction/Market + Financials, (4) Legal/Compliance + Capital Path.
- Loads: its module sections from [module-questions.md](../diligence/module-questions.md), plus the schema in `templates/appendices/evidence-ledger.yaml`.
- Input: the intake materials plus the module assignment and P0/P1/P2 priorities from the orchestrator.
- Output: **evidence ledger entries only**, in the `evidence-ledger.yaml` schema — no narrative, no recommendations, no stage claims. External research follows the Step 1 source list; every entry carries `source_type`, `source_url`/`source_title`, and `source_date`.

### Red-team agent

- Loads: [pattern-library.md](../diligence/pattern-library.md), [red-team-checks.md](../diligence/red-team-checks.md).
- Input: the merged evidence ledger **only** — never the draft narrative, OnePage, or memo.
- Output: per-claim findings — pattern matches, the nine contradiction-check results, and proposed downgrades (`evidence_status`, `confidence`, `red_flag`, `next_check`) with one-line reasons. No verdict.

## Merge rules (orchestrator)

1. Deduplicate by claim: same fact from two agents becomes one entry; keep the stronger source, note corroboration.
2. Conflicting entries on the same fact become a single entry with `evidence_status: contradiction` — never silently pick one side.
3. Apply red-team downgrades before scoring coverage. If a downgrade is rejected, record why in the ledger; rejecting a downgrade because it hurts the narrative is forbidden.
4. After merge: score coverage (coverage-stage-model), apply verdict caps and eligibility (decision-rules), then write outputs.

## Failure handling

- A research agent that returns narrative instead of ledger entries: re-run with the schema; do not paraphrase its prose into entries yourself.
- A module with no usable evidence still gets ledger entries marked `unknown` — absence of evidence must be visible in coverage, not skipped.
- If subagents are unavailable mid-run, fall back to sequential execution; the artifacts and rules are identical.
