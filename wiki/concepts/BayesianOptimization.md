---
title: "Bayesian Optimization"
type: concept
tags: [hyperparameter-tuning, optimization, hpo, bayesian]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Bayesian Optimization

A sample-efficient global-optimization technique for expensive, noisy, derivative-free objectives. Fits a probabilistic **surrogate model** to past observations $\{(\mathbf{x}_i, y_i)\}$ and uses an **acquisition function** to pick the next query point that trades off predicted improvement against epistemic uncertainty.

## Surrogates and acquisitions

| Surrogate | Acquisition examples | Library |
|---|---|---|
| [[GaussianProcess|Gaussian process]] | Expected Improvement (EI), UCB, PI, Thompson sampling | [[SyneTune]], BoTorch, Spearmint |
| Tree-Structured Parzen Estimator (TPE) | Expected Improvement via $p(\mathbf{x}\mid y<y^*)/p(\mathbf{x}\mid y\geq y^*)$ | [[HyperOpt]], [[Optuna]] |
| Random Forest | EI / UCB | SMAC |

## Random search vs Bayesian optimization

[[d2l-hyperparameter-optimization]] §hyperopt-api compares random search and Bayesian optimization on tuning a feedforward NN over 50 seeds. Both algorithms are roughly comparable through ~1000 seconds; afterwards Bayesian optimization's surrogate-model exploitation pulls ahead.

> "We can see that random search and Bayesian optimization perform roughly the same up to ~1000 seconds, but Bayesian optimization can make use of the past observation to identify better configurations and thus quickly outperforms random search afterwards." — [[d2l-hyperparameter-optimization]] §hyperopt-api

## Trade-offs

- **Sample efficiency:** BO dominates random search and grid search on a fixed query budget.
- **Parallelism:** BO must update its surrogate between queries → harder to parallelize than [[RandomSearch|random search]] or [[ASHA]].
- **Cold start:** BO needs ~5–10 initial random points before the surrogate is informative.

Hybrid approaches like BOHB (Falkner et al. 2018) combine BO's sample efficiency with [[Hyperband]]'s multi-fidelity scheduling.

## Connections

- [[d2l-hyperparameter-optimization]] — the canonical D2L reference comparing BO to random search.
- [[GaussianProcess]] — the most common BO surrogate; D2L's *Gaussian Processes* chapter ([[d2l-gaussian-processes]]) establishes the relevant math.
- [[RandomSearch]] — the baseline BO outperforms after enough trials.
- [[ASHA]] / [[SuccessiveHalving]] — orthogonal axes of HPO improvement (BO improves the *searcher*, ASHA improves the *scheduler*).
- [[HyperparameterOptimization]] — parent concept.
- [[JasperSnoek]] — author of *Practical Bayesian Optimization of Machine Learning Algorithms* (NIPS 2012), the canonical BO-for-HPO paper.
- [[HyperOpt]] / [[Optuna]] / [[SyneTune]] / [[RayTune]] — production BO implementations.
