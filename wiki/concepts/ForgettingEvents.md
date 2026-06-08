---
title: "Forgetting Events"
type: concept
tags: [ml-systems, data-selection, coreset, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Forgetting Events

A [[CoresetSelection|coreset-scoring]] method that ranks samples by how often the model **"forgets"** them — transitions from a correct to an incorrect classification — during training ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Frequently-forgotten samples are the hardest and most valuable; never-forgotten samples are easy and prunable. The cost is high ($\mathcal{O}(\text{full training})$ to compute), but the resulting importance scores **transfer reliably from small proxy models to large targets** (ResNet-18 → ResNet-50), which is what makes inexpensive proxy-based selection viable. Distinct from (though related to) [[CatastrophicForgetting|catastrophic forgetting]] in continual learning.

## Connections

- [[CoresetSelection]] — parent; [[EL2N]] / [[GraNd]] — cheaper gradient-based scorers.
- [[CatastrophicForgetting]] — the related continual-learning phenomenon.
- [[mlsysbook-ch09-data-selection]] — source.
