---
title: "Width–Depth Search"
type: concept
tags: [test-time-scaling, reasoning, control-space]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# Width–Depth Search

Two-dimensional control space spanning the [[testtimescaling|test-time scaling]] design landscape:

- **Width** = how many reasoning branches are explored in parallel.
- **Depth** = how far each active branch is developed (number of fixed-length generation intervals).

[[2605.08083-autotts]] argues that essentially every TTS algorithm proposed since 2022 — [[selfconsistency|SC@64]], ASC, ESC, Answer-Consistency, ST-BoN, [[2602.03845-parallel-probe|Parallel-Probe]] — is a *hand-designed path* through this space, not a fundamentally distinct algorithm:

| Algorithm | Path through width–depth |
|---|---|
| SC@64 (2022) | Fixed full-budget corner (max width, max depth). |
| ASC (2023) | Adapt width only at max depth, single chain. |
| ESC (2024) | Adapt width only at max depth, chunked. |
| Answer-Consistency | Adapt depth on single chain. |
| ST-BoN (2025) | Wide start, prune to one, then deepen. |
| Parallel-Probe (2026) | Start wide, progressively prune while deepening. |

The reframing motivates **[[AutoTTS]]**: rather than design more paths, define the control space + an [[OfflineReplayEnvironment|offline replay environment]] and *discover* the path automatically via an explorer LLM. A discovered controller can be **genuinely 2D-adaptive** — both widening and deepening based on current state — rather than committing in advance to a hand-tuned schedule.

## Action Set

Admissible actions at decision step $t$: `BRANCH` / `CONTINUE(i)` / `PROBE(i)` / `PRUNE(i)` / `ANSWER`. Width = $|m_t|$; per-branch depth = $\ell_{t,i}$.

## Connections

- [[2605.08083-autotts]] — origin paper for the formalism.
- [[AutoTTS]] — instantiates the framework over this space.
- [[testtimescaling|Test-Time Scaling]] — parent concept.
- [[parallelreasoning|Parallel Reasoning]] — width axis.
- [[chainofthought|Chain-of-Thought]] — depth axis.
- [[bestofn|Best-of-N]] — degenerate (width-only, depth-fixed) case.
- [[selfconsistency|Self-Consistency]] / SC@64 — fixed-corner baseline.
- [[2602.03845-parallel-probe|Parallel-Probe]] — most-adaptive prior baseline.
