---
title: "Test-Time Scaling"
type: concept
tags: [ml-method, reasoning, inference]
sources: [2512.04388-conductor, 2605.02396-heavyskill, 2605.08083-autotts]
last_updated: 2026-05-15
---

# Test-Time Scaling

Improving inference-time performance by spending more compute per query — extra reasoning chains, parallel rollouts, multi-pass self-refinement, adaptive branching. The TTS literature spans three positions in the 2026 corpus:

1. **Externalize via harness orchestration** — the [[2512.04388-conductor|Conductor]]'s recursive topologies introduce an online iterative-adaptation TTS axis with a learned orchestrator.
2. **Internalize via training** — [[2605.02396-heavyskill|HEAVYSKILL]] argues the parallel-reason + deliberation pattern can be folded into a single model's *inner skill* via RLVR, leaving the runtime harness obsolete.
3. **Automate the harness** — [[2605.08083-autotts|AutoTTS]] reframes TTS strategy design as **automatic controller discovery** over a [[WidthDepthSearch|width–depth]] control space. All hand-crafted TTS algorithms ([[selfconsistency|SC@64]], ASC, ESC, ST-BoN, [[2602.03845-parallel-probe|Parallel-Probe]]) are revealed as special cases of a single 2D control space, and an explorer LLM searches the space directly.

## Standard TTS Algorithms

| Algorithm | Strategy |
|---|---|
| [[selfconsistency\|Self-Consistency / SC@64]] (Wang et al. 2022) | Sample $N$ trajectories in parallel, majority vote. |
| ASC (Aggarwal et al. 2023) | Adaptive sampling: stop when consensus reached. |
| ESC (Li et al. 2024) | Early-stopping SC: chunk-based early termination. |
| Answer-Consistency (Liu & Wang 2025) | Adapt depth on single chain. |
| ST-BoN (Wang et al. 2025) | Wide start, prune to best-1, then deepen. |
| [[2602.03845-parallel-probe\|Parallel-Probe]] (Zheng et al. 2026) | Start wide + progressively prune while deepening, with 2D probing. |
| [[ConfidenceMomentumController\|CMC]] (discovered by AutoTTS, 2026) | EMA-momentum gate + coupled width–depth control + alignment-aware depth + conservative abandonment. |

## The Width–Depth Reframing

[[2605.08083-autotts]]'s key conceptual move: define **width** = number of branches and **depth** = per-branch generation budget; treat every TTS algorithm as a path through (width, depth). The control space has admissible actions BRANCH / CONTINUE(i) / PROBE(i) / PRUNE(i) / ANSWER. See [[WidthDepthSearch]].

## Connections

- [[2512.04388-conductor]] — learned external orchestrator approach.
- [[2605.02396-heavyskill]] — RLVR-internalized inner-skill approach.
- [[2605.08083-autotts]] — automated discovery approach.
- [[AutoTTS]] / [[WidthDepthSearch]] / [[ConfidenceMomentumController]] — AutoTTS machinery.
- [[parallelreasoning|Parallel Reasoning]] — the width axis.
- [[chainofthought|Chain-of-Thought]] — the depth axis.
- [[bestofn|Best-of-N]] — width-only degenerate case.
- [[selfconsistency|Self-Consistency]] — width + majority-vote degenerate case.
- [[2402.01817-llm-modulo|LLM-Modulo]] — orthogonal lens: many TTS methods reduce to LLM-Modulo instances when the verifier is implicit (test suite, ground truth, soft critic).
