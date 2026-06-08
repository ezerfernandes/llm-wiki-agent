---
title: "Uncertainty Sampling"
type: concept
tags: [ml-method, active-learning, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Uncertainty Sampling

The simplest and most common [[ActiveLearning|active-learning]] query strategy: select the unlabeled samples on which the model is **least confident** (e.g. predictions near 0.5 probability for binary classification) for human labeling ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). Computationally cheap and effective in practice. Related strategies: **query-by-committee** (label where an ensemble disagrees most, capturing epistemic uncertainty), **expected model change** (theoretically grounded but expensive), and **diversity sampling** (pick samples dissimilar to the labeled set to cover the input space). In the Smart Doorbell "hard negative" example, querying low-confidence predictions (a statue scored "Person 51%") converts the labeling loop from a random walk into a guided search for the decision boundary.

## Connections

- [[ActiveLearning]] — the parent loop this strategy drives.
- [[EL2N]] — shares the uncertainty-near-boundary intuition for static coresets.
- [[SelectionInequality]] — scoring the pool must stay cheap (proxy models).
- [[mlsysbook-ch09-data-selection]] — source.
