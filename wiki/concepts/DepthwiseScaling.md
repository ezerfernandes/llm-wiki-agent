---
title: "Depthwise Scaling"
type: concept
tags: [model-merging, model-upscaling, layer-stacking]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Depthwise Scaling

A [[LayerStacking|layer-stacking]] technique that **constructs a deeper model from a shallower pre-trained model**, without training from scratch. Used by [[Kim2023SOLAR|Kim et al. (2023)]] to build [[SOLAR107B|SOLAR 10.7B]] from a 32-layer 7B base. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]] the procedure:

1. **Make a copy of the original pre-trained model.**
2. **Merge the two copies by summing certain layers** (summing two layers into one) **and stacking the rest.** Which layers get summed is chosen to match the target model size.
3. **Further train the upscaled model** toward the target performance.

For [[SOLAR107B|SOLAR 10.7B]], 16 layers were summed (collapsing 32 of the duplicated layers into 16) → final 32 × 2 − 16 = **48 layers**.

## Why it's useful

- **Repurposes pre-training compute** — you don't pay to retrain from scratch.
- **Fits new hardware budgets** — if you have a bigger machine than originally targeted, depthwise scaling fills it.
- **Pre-trained weights are a better starting point than random initialization** — the upscaled model converges faster than a from-scratch 10.7B.

## Connection to [[ModelUpscaling|model upscaling]]

Depthwise scaling is one specific recipe within the broader [[ModelUpscaling|model-upscaling]] category. Other approaches include [[SparseUpcycling|sparse upcycling]] (build an MoE) and width-wise scaling (duplicate channels rather than layers; less common).

## Connections

- [[LayerStacking]] — parent operation.
- [[ModelUpscaling]] — broader category.
- [[SparseUpcycling]] — sibling layer-stacking recipe (produces MoEs).
- [[SOLAR107B]] — the canonical depthwise-scaling example.
- [[Kim2023SOLAR]] — the paper.
- [[ai-engineering-ch07-finetuning]] — primary source.
