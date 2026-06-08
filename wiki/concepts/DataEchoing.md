---
title: "Data Echoing"
type: concept
tags: [ml-systems, data-selection, training-efficiency, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Data Echoing

A training-pipeline technique (Choi et al. 2020) that **reuses each batch $e$ times before fetching new samples**, recovering GPU cycles wasted when the CPU data pipeline (reading, decoding, augmenting) is the bottleneck ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). It trades sample diversity for GPU utilization. Benefit depends on the ratio $R=T_{\text{pipeline}}/T_{\text{GPU}}$: echoing helps only when $R>1$.

Key subtlety: **upstream echoing** (echo *before* augmentation) applies different random augmentations to each repetition, preserving diversity; **downstream echoing** (after augmentation) feeds identical tensors and gives no benefit. Choi et al. measured a **3.25× speedup** on ResNet-50/ImageNet when reading over a network; echoed samples are worth ~70–90% of fresh ones, and above ~4× the model starts memorizing. Also interacts with batch normalization (repeated samples skew batch statistics).

## Connections

- [[DataSelection]] — the systems-engineering toolkit it belongs to.
- [[MixUp]] / [[DataAugmentation]] — heavy augmentations that make the CPU pipeline the bottleneck echoing fixes.
- [[SelectionInequality]] — both are about keeping data-side overhead from negating gains.
- [[mlsysbook-ch09-data-selection]] — source.
