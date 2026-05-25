---
title: "Chinchilla Scaling Laws"
type: concept
tags: [stub, scaling, pretraining]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Chinchilla Scaling Laws

*Earlier stub — see the canonical, Ch-2-grounded version at [[ChinchillaScalingLaw]] (singular form). Kept for backlink compatibility.*

Hoffmann et al. (2022, "Training Compute-Optimal Large Language Models") re-derived [[ScalingLaws|scaling laws]] for compute-optimal LM training, concluding that model size $N$ and training tokens $D$ should scale roughly in 1:1 ratio with compute $C$ — i.e. $N\propto C^{1/2}, D\propto C^{1/2}$ — rather than the $N\propto C^{0.73}, D\propto C^{0.27}$ ratio implied by [[2001.08361-scaling-laws|Kaplan et al. 2020]]. Their flagship "Chinchilla" model (70B params, 1.4T tokens) outperformed much larger contemporaries trained on fewer tokens.

Cited by [[2605.12966-agentic-ai-to-agi]] alongside Kaplan et al. as evidence that monolithic scaling delivers *diminishing* marginal returns — a key motivation for the paper's argument that AGI requires moving from scale to topology.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] supplies the **practitioner-grade restatement**:

> "For compute-optimal training, you need the number of training tokens to be approximately **20 times the model size**. ... The model size and the number of training tokens should be scaled equally: for every doubling of the model size, the number of training tokens should also be doubled."

A 3B-param model therefore needs ≈60B training tokens to be compute-optimal. The full Ch 2 treatment — methodology (400 models, 70M to 16B+ params on 5B to 500B tokens), caveats (dense-models-only; inference-aware revisions), and the Llama compute-suboptimal-by-design counter-pattern — lives at [[ChinchillaScalingLaw]].

## Connections
- [[ChinchillaScalingLaw]] — the canonical, Ch-2-grounded version.
- [[ScalingLaws]]
- [[ComputeOptimal]]
- [[FLOPs]]
- [[2001.08361-scaling-laws]]
- [[2605.12966-agentic-ai-to-agi]]
- [[ai-engineering-ch02-foundation-models]] — primary source for the practitioner-grade version.
