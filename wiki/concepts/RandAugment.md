---
title: "RandAugment"
type: concept
tags: [ml-method, data-augmentation, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# RandAugment

A learned-augmentation policy that collapses [[AutoAugment]]'s large RL search space to just **two hyperparameters** — the number of transformations $N$ and their shared magnitude $M$ ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). This works because augmentation policies have low intrinsic dimensionality: a grid search over $N\in[1,3]$ and $M\in[5,15]$ recovers 95–100% of AutoAugment's gains at negligible search cost. It **displaced AutoAugment in production** because the latter's 15,000 GPU-hours of policy search rarely justify the marginal accuracy gain. Especially useful for capacity-constrained models (e.g. MobileNet) where aggressive augmentation substitutes for model capacity.

## Connections

- [[DataAugmentation]] — parent; [[AutoAugment]] — the costly method it replaced.
- [[mlsysbook-ch09-data-selection]] — source.
