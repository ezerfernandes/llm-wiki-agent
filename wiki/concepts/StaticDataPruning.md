---
title: "Static Data Pruning"
type: concept
tags: [ml-systems, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Static Data Pruning

Stage 1 of the [[DataSelection|data-selection]] pipeline ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]): removing low-value samples **before training begins**, without modifying the training loop or model architecture. It typically reduces a dataset by **30–50%** while preserving (sometimes improving) final accuracy. Three families:

1. **[[CoresetSelection|Coreset selection]]** — keep the smallest subset preserving the data's statistical structure (k-Center, Herding, [[GraNd]], [[EL2N]], [[ForgettingEvents|forgetting events]]).
2. **[[DataDeduplication|Deduplication]]** — remove exact (hash) and near ([[MinHash]]/[[LocalitySensitiveHashing|LSH]]/[[CLIP]]) duplicates.
3. **Quality pruning** — drop samples that actively harm learning: label-error detection ([[Cleanlab]]), outlier removal, [[Perplexity|perplexity]]/low-information filtering.

Because the decision is fixed, every epoch trains on the same subset — contrasted with [[DynamicDataSelection|dynamic selection]], which adapts the data diet as the model learns.

## Connections

- [[DataSelection]] — parent; [[DynamicDataSelection]] / [[SyntheticDataGeneration]] — pipeline stages 2 and 3.
- [[CoresetSelection]] / [[DataDeduplication]] / [[DataPruning]] — its three techniques.
- [[InformationComputeRatio]] — pruning raises ICR by removing redundant/noisy samples.
- [[mlsysbook-ch09-data-selection]] — source.
