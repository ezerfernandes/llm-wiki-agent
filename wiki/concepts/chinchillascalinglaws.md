---
title: "Chinchilla Scaling Laws"
type: concept
tags: [stub, scaling, pretraining]
sources: []
last_updated: 2026-05-15
---

# Chinchilla Scaling Laws

*Stub — referenced by other wiki pages but not yet ingested as a primary source.*

Hoffmann et al. (2022, "Training Compute-Optimal Large Language Models") re-derived [[ScalingLaws|scaling laws]] for compute-optimal LM training, concluding that model size $N$ and training tokens $D$ should scale roughly in 1:1 ratio with compute $C$ — i.e. $N\propto C^{1/2}, D\propto C^{1/2}$ — rather than the $N\propto C^{0.73}, D\propto C^{0.27}$ ratio implied by [[2001.08361-scaling-laws|Kaplan et al. 2020]]. Their flagship "Chinchilla" model (70B params, 1.4T tokens) outperformed much larger contemporaries trained on fewer tokens.

Cited by [[2605.12966-agentic-ai-to-agi]] alongside Kaplan et al. as evidence that monolithic scaling delivers *diminishing* marginal returns — a key motivation for the paper's argument that AGI requires moving from scale to topology.

## Connections
- [[ScalingLaws]]
- [[2001.08361-scaling-laws]]
- [[2605.12966-agentic-ai-to-agi]]
