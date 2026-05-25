---
title: "Compute-Optimal"
type: concept
tags: [scaling, pretraining, training]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Compute-Optimal

A model is **compute-optimal** if it achieves the best possible performance given a fixed compute budget. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Given a fixed amount of FLOPs, what model size and dataset size would give the best performance? A model that can achieve the best performance given a fixed compute budget is compute-optimal."

(Ch 2 has a typo: *"compute-optional"* — the correct term is **compute-optimal**.)

## Why the framing matters

Without a compute budget, the question *"how big should the model be?"* has no good answer — bigger is usually better. With a compute budget, the question becomes a constrained optimization: **how should fixed compute be split between model size and dataset size?**

## The Chinchilla answer

The [[ChinchillaScalingLaw|Chinchilla scaling law]] (DeepMind 2022) gives the answer empirically: **≈20 training tokens per parameter**, with model size and dataset size scaling equally with compute.

## Compute-optimal ≠ inference-optimal

Ch 2 flags an important production caveat: **compute-optimal training optimizes training quality, not deployment cost.** [[meta|Meta]]'s [[Llama2_7BChat|Llama]] models are deliberately *smaller* than compute-optimal — making them slightly worse at the same training compute, but **substantially cheaper and easier to deploy**. Sardana et al. (2023) modified the Chinchilla recipe to account for inference demand explicitly.

The lesson:

> "It's important to remember that for production, model quality isn't everything." — Ch 2

## Cost-of-performance trends

Per Stanford HAI's *AI Index Report 2022*: on [[ImageNet]], **the cost to reach 93% accuracy halved from 2019 to 2021**. The cost for a given level of performance is decreasing — but the cost of *improving* performance remains high (last-mile expensive).

## Connections
- [[ChinchillaScalingLaw]] — the rule operationalizing compute-optimal.
- [[scalinglaws]] — the broader power-law framework.
- [[FLOPs]] — the budgeting unit.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[LastMileChallenge]] — the asymmetric improvement cost beyond the optimum.
