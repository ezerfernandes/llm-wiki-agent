---
title: "Grid Search"
type: concept
tags: [hpo, optimization, baseline]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Grid Search

Define an equi-spaced grid over each hyperparameter range, then iterate over the Cartesian product. The strict HPO baseline, almost always dominated by [[RandomSearch|random search]] in deep-learning settings ([[d2l-hyperparameter-optimization]] §hyperopt-intro).

## Why it loses to random search

If only $k$ of the $d$ hyperparameters meaningfully affect validation error (the "effective low-dim" regime), grid search probes each meaningful axis at only $g^{1/d}$ distinct levels (where $g$ is the total budget) — wasting most of the budget on the $d-k$ inert axes. Random search, by contrast, samples each axis at $g$ distinct levels independently ([[JamesBergstra|Bergstra]] & [[YoshuaBengio|Bengio]] 2012).

## When grid search is acceptable

- Very low-dimensional spaces ($d=1$ or $2$).
- Categorical-only spaces where every cell of the grid is meaningful.
- Exhaustive sweeps over a coarse pre-discretized grid as a *sanity check* before random / Bayesian / multi-fidelity search.

## Connections

- [[d2l-hyperparameter-optimization]] — flags grid search as the inferior baseline.
- [[RandomSearch]] — the strict winner in deep-learning HPO.
- [[HyperparameterOptimization]] — parent concept.
