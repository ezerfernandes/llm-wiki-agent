---
title: "Forward Stepwise Selection"
type: concept
tags: [model-selection, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Forward Stepwise Selection

Greedy variant of [[BestSubsetSelection]]: start with the null model, then at each step add the single predictor whose inclusion most improves fit. Compares only $1 + p(p+1)/2$ models — feasible at large $p$ — but not guaranteed to find the global best subset.

## Connections
- [[islr-seventh-printing]] — Ch.6.1.2.
- [[BestSubsetSelection]] — exact counterpart.
- [[BackwardStepwiseSelection]] — top-down variant.
