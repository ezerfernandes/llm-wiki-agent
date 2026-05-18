---
title: "Gini Index"
type: concept
tags: [trees, classification, criterion]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Gini Index

Node-impurity criterion used in [[ClassificationTree|classification trees]]: $G = \sum_k \hat p_k (1-\hat p_k)$. Small when one class dominates the node; preferred to misclassification error for split-selection because it is differentiable in $\hat p_k$ and rewards purity more aggressively. Cross-entropy is the close cousin.

## Connections
- [[islr-seventh-printing]] — Ch.8.1.2.
- [[ClassificationTree]] — where it's used.
- [[DecisionTrees]] — parent method.
