---
title: "Best Subset Selection"
type: concept
tags: [model-selection, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Best Subset Selection

For each $k \in \{1,\dots,p\}$ fit *all* $\binom{p}{k}$ models with exactly $k$ predictors, pick the best per-$k$ by RSS, then pick across $k$ by [[CrossValidation]] / Cp / BIC. Exact but $2^p$-many models — infeasible past $p\approx 40$; replaced in practice by [[ForwardStepwiseSelection]] / [[BackwardStepwiseSelection]] or [[Lasso]].

## Connections
- [[islr-seventh-printing]] — Ch.6.1.1.
- [[ForwardStepwiseSelection]], [[BackwardStepwiseSelection]] — greedy approximations.
- [[Lasso]] — convex alternative that does selection implicitly.
