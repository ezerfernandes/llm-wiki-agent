---
title: "Dynamic Data Selection"
type: concept
tags: [ml-systems, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Dynamic Data Selection

Stage 2 of the [[DataSelection|data-selection]] pipeline ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]): selecting high-value samples **during training**, adapting the data diet to the model's evolving state. The motivating insight is that the optimal training samples change as the model learns — examples that challenge an undertrained model become trivially easy after enough gradient updates, so a fixed [[StaticDataPruning|static]] subset is suboptimal. Early training benefits from diverse coverage; later training benefits from hard, near-boundary examples.

Techniques: [[CurriculumLearning|curriculum learning]] (easy-to-hard ordering), [[ActiveLearning|active learning]] (uncertainty-guided labeling), and [[SemiSupervisedLearning|semi-supervised learning]]. All incur the [[SelectionInequality|Selection Inequality]] cost: $T_{\text{selection}}+T_{\text{train}}(\text{subset})$ must beat $T_{\text{train}}(\text{full})$, and random access to scattered samples triggers the I/O penalty.

## Connections

- [[DataSelection]] — parent; [[StaticDataPruning]] / [[SyntheticDataGeneration]] — pipeline stages 1 and 3.
- [[CurriculumLearning]] / [[ActiveLearning]] / [[SemiSupervisedLearning]] — its techniques.
- [[SelectionInequality]] — the systems gate on dynamic selection.
- [[mlsysbook-ch09-data-selection]] — source.
