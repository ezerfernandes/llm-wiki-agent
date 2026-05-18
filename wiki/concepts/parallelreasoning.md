---
title: "Parallel Reasoning"
type: concept
tags: [ml-method, reasoning, inference]
sources: [2605.02396-heavyskill, 2605.08083-autotts]
last_updated: 2026-05-15
---

# Parallel Reasoning

Producing multiple independent reasoning trajectories from a single base model and aggregating their answers — the **width axis** of [[testtimescaling|test-time scaling]]. Two roles in the wiki:

- **In [[2605.02396-heavyskill|HEAVYSKILL]]**: first phase of the heavy-thinking pattern (K independent trajectories then deliberation). Trajectory quality and diversity are the dominant performance drivers per the ablations.
- **In [[2605.08083-autotts|AutoTTS]]**: the width dimension of the [[WidthDepthSearch|width–depth control space]]. Every TTS algorithm — SC@64, ASC, ESC, [[2602.03845-parallel-probe|Parallel-Probe]] — is a path through (width, depth) that varies *when* to spawn or kill parallel branches.

## Connections

- [[2605.02396-heavyskill]] — inner-skill internalization of parallel reasoning.
- [[2605.08083-autotts]] — automated discovery of when to widen.
- [[testtimescaling|TestTimeScaling]] — parent.
- [[WidthDepthSearch]] — formalization as control axis.
- [[sequentialdeliberation|SequentialDeliberation]] — the contrasting depth axis in HEAVYSKILL's pattern.
- [[2602.03845-parallel-probe|Parallel-Probe]] — most-adaptive prior parallel-reasoning baseline.
- [[selfconsistency|Self-Consistency]] — fixed-width majority-vote degenerate case.
- [[bestofn|Best-of-N]] — width-only degenerate case.
