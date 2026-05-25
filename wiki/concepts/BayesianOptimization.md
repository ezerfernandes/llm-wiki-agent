---
title: "Bayesian Optimization"
type: concept
tags: [hyperparameter-tuning, optimization, hpo, bayesian]
sources: [d2l-hyperparameter-optimization, 2406.11695-mipro]
last_updated: 2026-05-22
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

## Bayesian Optimization in LM-program prompt search

The [[2406.11695-mipro|MIPRO paper (Opsahl-Ong et al. 2024)]] uses BO **outside the classical HPO setting** — to search over discrete (instruction, demo-set) categorical parameters per module in a multi-stage [[LMProgram|LM program]]. Specifically:

- **Search space**: categorical, $m \times 2$ dimensions (instruction-index × demo-set-index per module), tens to hundreds of candidate values per dimension.
- **Surrogate**: multivariate [[TreeStructuredParzenEstimator|TPE]] via [[Optuna]] (Akiba et al. 2019, Falkner et al. 2018).
- **Objective**: noisy mini-batch program score — *"Bayesian optimization is known for its robustness to noise, as it effectively incorporates uncertainty into the optimization process"* — which justifies mini-batch evaluation over the full trainset for amortized LM-call budget.
- **Why surrogate-based not GP-based**: TPE handles categorical / hierarchical search spaces naturally; categorical inputs are the norm for prompt choice across modules.

The paper's [[CreditAssignment|credit-assignment]] problem (no per-module labels) is what BO is structurally suited for: it learns the joint distribution of program score across per-module parameter choices, attributing credit *implicitly* via the surrogate's posterior over input dimensions.

## Connections

- [[d2l-hyperparameter-optimization]] — the canonical D2L reference comparing BO to random search.
- [[2406.11695-mipro]] — uses BO outside HPO, for LM-program prompt search.
- [[MIPROv2|MIPRO]] — the LM-program optimizer with BO at its core.
- [[TreeStructuredParzenEstimator]] — the specific surrogate MIPRO uses.
- [[Optuna]] — MIPRO's BO implementation.
- [[GaussianProcess]] — the most common BO surrogate; D2L's *Gaussian Processes* chapter ([[d2l-gaussian-processes]]) establishes the relevant math.
- [[RandomSearch]] — the baseline BO outperforms after enough trials.
- [[ASHA]] / [[SuccessiveHalving]] — orthogonal axes of HPO improvement (BO improves the *searcher*, ASHA improves the *scheduler*).
- [[HyperparameterOptimization]] — parent concept.
- [[JasperSnoek]] — author of *Practical Bayesian Optimization of Machine Learning Algorithms* (NIPS 2012), the canonical BO-for-HPO paper.
- [[HyperOpt]] / [[Optuna]] / [[SyneTune]] / [[RayTune]] — production BO implementations.
