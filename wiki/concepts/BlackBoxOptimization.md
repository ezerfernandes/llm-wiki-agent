---
title: "Black-Box Optimization"
type: concept
tags: [optimization, derivative-free]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Black-Box Optimization

Minimizing a function $f:\mathcal{X}\to\mathbb{R}$ accessible only through queries — no gradients, no Hessians, no structural form, possibly noisy. The optimizer treats $f$ as an oracle, observes $y_i=f(\mathbf{x}_i)+\epsilon_i$, and must choose the next query point $\mathbf{x}_{i+1}$ from $\{\mathbf{x}_1, \dots, \mathbf{x}_i\}$ and $\{y_1, \dots, y_i\}$ alone.

## Why HPO is black-box

[[d2l-hyperparameter-optimization]] §hyperopt-intro is explicit: there is no simple gradient of validation error with respect to hyperparameters (hypergradients exist but are not competitive); observations are noisy because training is stochastic; evaluations are expensive. These are precisely the constraints black-box optimization is designed for.

## Algorithm families

- **Sampling-based:** [[RandomSearch|random search]], [[GridSearch|grid search]], Latin hypercube, Sobol sequences.
- **Model-based / Bayesian:** [[BayesianOptimization]] with [[GaussianProcess|GP]] / TPE / Random-Forest surrogates and EI / UCB / PI acquisition functions.
- **Evolutionary / population-based:** CMA-ES, genetic algorithms.
- **Multi-fidelity:** [[SuccessiveHalving]], [[Hyperband]], [[ASHA]] (when cheap evaluations are available).

## Connections

- [[d2l-hyperparameter-optimization]] — frames HPO as black-box optimization.
- [[HyperparameterOptimization]] — the most prominent ML application.
- [[BayesianOptimization]] / [[RandomSearch]] — the two canonical algorithm families.
- [[MultiFidelityOptimization]] — extension when cheap proxies of the objective exist.
