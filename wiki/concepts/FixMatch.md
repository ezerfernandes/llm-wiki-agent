---
title: "FixMatch"
type: concept
tags: [ml-method, semi-supervised, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# FixMatch

A [[SemiSupervisedLearning|semi-supervised]] method (Sohn et al. 2020) combining [[PseudoLabeling|pseudo-labeling]] and [[ConsistencyRegularization|consistency regularization]] ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]): generate a pseudo-label on a **weakly augmented** image (only when confidence exceeds ~0.95), then train the model to predict that label on a **strongly augmented** version of the same image. Demonstrates extreme label efficiency on CIFAR-10:

- 250 labels (25/class) → **94.9%** (within ~1.2 pp of 96.1% full supervision) = **200× label efficiency**
- 40 labels → 88.6%; 4,000 labels → 95.7%

Trades ~5× more GPU compute (processing 50K unlabeled samples/epoch) for up to ~200× fewer purchased labels — favorable wherever labeling dominates cost.

## Connections

- [[SemiSupervisedLearning]] — parent; [[PseudoLabeling]] / [[ConsistencyRegularization]] — the two ideas it fuses.
- [[CIFAR10]] — the benchmark for its headline numbers.
- [[mlsysbook-ch09-data-selection]] — source.
