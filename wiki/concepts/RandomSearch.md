---
title: "Random Search"
type: concept
tags: [hpo, optimization, baseline]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Random Search

Independently sample hyperparameter configurations from a user-specified prior over the configuration space until a budget is exhausted; return the best observed configuration. The universal HPO baseline ([[d2l-hyperparameter-optimization]] §hyperopt-intro).

## Why it works

[[JamesBergstra|Bergstra]] & [[YoshuaBengio|Bengio]] 2012 (*Random Search for Hyper-Parameter Optimization*, JMLR) — the canonical paper. Random search dominates [[GridSearch|grid search]] when validation error depends strongly on a *small subset* of the hyperparameters (the "effective low-dimensional" regime typical of deep learning). Intuition: grid search puts all probe points at $d^k$ corners regardless of which dimensions matter; random search distributes probes uniformly *along each individual dimension*.

## Implementation

```python
config_space = {"learning_rate": stats.loguniform(1e-4, 1)}
for i in range(num_iterations):
    config = {name: domain.rvs() for name, domain in config_space.items()}
    error = objective(config)
```

Trivially parallelizable: each config is independent of the others, so [[AsyncParallelHPO|asynchronous distribution]] gives **linear speed-up** with workers — unlike model-based methods that need synchronization to update the surrogate.

## Shortcomings

1. **Non-adaptive.** Equally likely to sample a known-bad as a known-good configuration; ignores prior trial outcomes.
2. **Uniform resource allocation.** Every config gets the full training budget regardless of early performance.

These two failures define the two axes of HPO improvement: **searcher** (→ [[BayesianOptimization]]) and **scheduler** (→ [[SuccessiveHalving]] / [[ASHA]] / [[Hyperband]]).

## Connections

- [[d2l-hyperparameter-optimization]] — D2L's canonical reference; implements `RandomSearcher(HPOSearcher)`.
- [[JamesBergstra]] / [[YoshuaBengio]] — random-vs-grid paper.
- [[GridSearch]] — the strict baseline random search outperforms.
- [[BayesianOptimization]] — addresses shortcoming (1).
- [[SuccessiveHalving]] / [[ASHA]] / [[Hyperband]] — address shortcoming (2).
- [[SyneTune]] / [[RayTune]] / [[Optuna]] — all ship a `RandomSearch` scheduler.
- [[HyperparameterOptimization]] — parent concept.
