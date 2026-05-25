---
title: "Scaling Extrapolation"
type: concept
tags: [scaling, hyperparameters, training]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Scaling Extrapolation

Also called **hyperparameter transferring** — the research subfield that tries to **predict, for large models, what hyperparameters will give the best performance** by studying their impact on much smaller models. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Scaling extrapolation (also called hyperparameter transferring) has emerged as a research subfield that tries to predict, for large models, what hyperparameters will give the best performance. The current approach is to study the impact of hyperparameters on models of different sizes, usually much smaller than the target model size, and then extrapolate how these hyperparameters would work on the target model size."

## Why it exists

For small models, you can train many times with different hyperparameter settings and pick the best. For large models, **one training run is resource-draining enough** — you may only have one shot.

## Key result

A 2022 paper by [[microsoft|Microsoft]] and [[openai|OpenAI]] showed it was possible to **transfer hyperparameters from a 40M-parameter model to a 6.7B-parameter model** — successfully extrapolating across ≈170× model size.

## Why it's hard

1. **Combinatorial explosion.** 10 hyperparameters → 1,024 combinations to study individually, in pairs, in triples, etc.
2. **[[EmergentAbilities|Emergent abilities]]** (Wei et al. 2022) — capabilities only present at scale — make extrapolation less accurate. Behavior at the small-model scale is not always predictive of behavior at the target scale.
3. **Niche expertise.** Few teams have the experience and resources to study large-model training systematically.

## Parameter vs Hyperparameter

Ch 2's mini-glossary, recorded here for the wiki:

- **Parameter** — learned by the model during training (weights, biases).
- **Hyperparameter** — set by users to configure the model and control how it learns. Two sub-classes:
  - *Model configuration*: number of layers, model dimension, vocabulary size.
  - *Training control*: batch size, number of epochs, learning rate, per-layer initial variance.

## Connections
- [[scalinglaws]] / [[ChinchillaScalingLaw]] — the budgeting context.
- [[EmergentAbilities]] — the phenomenon that limits extrapolation accuracy.
- [[pretraining]] — the training stage where hyperparameter choice matters most.
- [[ai-engineering-ch02-foundation-models]] — primary source.
