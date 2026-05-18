---
title: "Best-of-N"
type: concept
tags: [ml-method, inference, test-time-scaling]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# Best-of-N

Generate $N$ independent candidate outputs from a base model and select one (by majority vote, verifier score, or reward model). The simplest [[testtimescaling|test-time scaling]] pattern — degenerate case of the [[WidthDepthSearch|width–depth control space]] where width = $N$ and depth is fixed (each candidate runs to a final answer with no intermediate probing or pruning).

In [[2605.08083-autotts|AutoTTS]]'s formalism, BoN corresponds to: BRANCH × $N$, CONTINUE all to completion, ANSWER with majority vote — no PROBE, no PRUNE. [[selfconsistency|Self-Consistency]] is the BoN instance with majority-vote aggregation.

## Connections

- [[testtimescaling|Test-Time Scaling]] — parent.
- [[parallelreasoning|Parallel Reasoning]] — the width-axis pattern.
- [[selfconsistency|Self-Consistency]] — BoN + majority vote.
- [[WidthDepthSearch]] — formalization that places BoN as a degenerate corner.
- [[2605.08083-autotts]] — uses `get_new_branch_final_answer()` API as the BoN primitive in the AutoTTS environment.
