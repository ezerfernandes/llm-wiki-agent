---
title: "Cutout"
type: concept
tags: [ml-method, data-augmentation, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Cutout

An image [[DataAugmentation|augmentation]] technique that **randomly masks square regions** of input images during training, forcing the model to recognize objects from partial information ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Unlike dropout (which zeroes *neurons* in feature space), Cutout operates in *input* space. Yields ~1–2 pp gains on CIFAR-10/100 with negligible compute overhead — a high-[[InformationComputeRatio|ICR]] augmentation when occlusion-style invariance matches the task. Improved upon by [[CutMix]], which fills the masked region with real content from another image.

## Connections

- [[DataAugmentation]] — parent; [[CutMix]] / [[MixUp]] — related advanced augmentations.
- [[InformationComputeRatio]] — Cutout adds information per sample at near-zero cost.
- [[mlsysbook-ch09-data-selection]] — source.
