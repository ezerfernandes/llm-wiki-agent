---
title: "AutoAugment"
type: concept
tags: [ml-method, data-augmentation, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# AutoAugment

A learned [[DataAugmentation|augmentation]] method that treats policy design as a **reinforcement-learning search problem**: a controller selects operations (rotate, translate, shear, equalize), magnitudes, and probabilities to maximize validation accuracy ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Learned policies transfer across datasets and architectures, but the search cost is prohibitive — **~15,000 GPU-hours** for a single policy — so it was largely **displaced by [[RandAugment]]**, which recovers most of the gains with two hyperparameters at negligible search cost.

## Connections

- [[DataAugmentation]] — parent; [[RandAugment]] — its cheaper successor.
- [[mlsysbook-ch09-data-selection]] — source.
