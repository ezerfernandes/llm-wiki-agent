---
title: "Consistency Regularization"
type: concept
tags: [ml-method, semi-supervised, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Consistency Regularization

A [[SemiSupervisedLearning|semi-supervised]] technique that enforces **invariant predictions across augmented versions of the same input** ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Rooted in the smoothness assumption — close inputs should have close labels — it minimizes the divergence between a model's predictions on an input and its perturbed (cropped, rotated, color-shifted) version. Distinct from plain [[DataAugmentation|augmentation]] because it adds an explicit consistency *loss term* even for unlabeled data where the true label is unknown. Systems cost: roughly **doubles forward-pass compute per sample**, a trade-off that favors GPU-rich, label-poor settings. Combined with [[PseudoLabeling|pseudo-labeling]] in [[FixMatch]].

## Connections

- [[SemiSupervisedLearning]] — parent; [[PseudoLabeling]] / [[FixMatch]] — companions.
- [[DataAugmentation]] — the perturbations it relies on (but used as a loss, not extra data).
- [[mlsysbook-ch09-data-selection]] — source.
