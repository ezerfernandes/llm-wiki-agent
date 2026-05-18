---
title: "FrontierMath"
type: concept
tags: [benchmark, evaluation, math, epoch-ai]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# FrontierMath

[[EpochAI|Epoch AI]]'s research-mathematics benchmark, tier-stratified by difficulty. **Tier 4** consists of 50 problems crafted as short-term research projects by professors and postdocs, designed to **surpass Tier 3 in difficulty** with some potentially remaining unsolved by AI for decades.

Frontier models and systems from all major providers are tested regularly; the [[2605.06651v2-ai-co-mathematician]] entry reports the latest evaluation: **[[AICoMathematician|AI co-mathematician]] = 23/48 (48%)**, a new high score among all AI systems evaluated, against a 19% baseline for the underlying [[gemini|Gemini 3.1 Pro]]. Two of the public sample problems are excluded from the 48-problem denominator.

Three Tier-4 problems were solved that had not been solved by any previously evaluated system; two prior-solved problems were missed.

Evaluation protocol (per the AI co-mathematician evaluation): **blind**, conducted by Epoch AI via the system's UI; **48-hour wall-clock per problem**; no token/call cap on the system being evaluated (the AI co-mathematician likely consumed more inference than prior evaluations on this benchmark).

Public leaderboard: https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4

## Connections
- [[EpochAI]]
- [[2605.06651v2-ai-co-mathematician]]
- [[IMOProofBench]] / [[PutnamBench]] — peer math benchmarks.
- [[AICoMathematician]]
