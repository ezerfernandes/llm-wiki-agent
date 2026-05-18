---
title: "Hyperparameter Optimization (HPO)"
type: concept
tags: [hpo, optimization, automl, ml-engineering]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Hyperparameter Optimization (HPO)

Casting the choice of non-learned model / training settings — learning rate, batch size, depth, width, [[Dropout]] rate, [[WeightDecay]], activation function — as a **global [[BlackBoxOptimization|black-box optimization]]** problem. Given an objective function $f:\mathcal{X}\to\mathbb{R}$ that returns validation error for a hyperparameter configuration $\mathbf{x}$, find $\mathbf{x}_\star\in\arg\min_{\mathbf{x}\in\mathcal{X}} f(\mathbf{x})$ ([[d2l-hyperparameter-optimization]] §hyperopt-intro).

## Why this is hard

1. **No usable gradient.** $f$ requires training the model end-to-end; backpropagating through training is feasible only for toy models (hypergradients — Maclaurin et al. 2015 / Franceschi et al. 2017 — not yet state-of-the-art).
2. **Expensive evaluations.** A single $f(\mathbf{x})$ may take hours-to-days of GPU time; even 10 trials on a CIFAR-10 ResNet ≈ a full day on `g4dn.xlarge`.
3. **Noisy observations.** Random initialization, mini-batch ordering → $y\sim f(\mathbf{x})+\epsilon$, $\epsilon\sim\mathcal{N}(0,\sigma)$.
4. **Non-transferable.** Optimal hyperparameters depend on the architecture, dataset, even hardware — must re-run HPO for each new task.
5. **Structured config space.** Some hyperparameters are conditional (number of units in layer $l$ exists only if depth $\geq l+1$); the space is not simply $\mathbb{R}^d$.

## Standard pipeline

1. Define **objective**: typically validation error, can be augmented with secondary objectives (training time, inference latency, model size).
2. Define **configuration space**: per-hyperparameter type + range + prior (log-uniform for things spanning orders of magnitude, uniform otherwise).
3. Pick a **searcher** + **scheduler** ([[d2l-hyperparameter-optimization]] §hyperopt-api decomposition mirrored by [[SyneTune]] / [[RayTune]] / [[Optuna]]).
4. Run the **tuner** for a budget, track the **incumbent** (best config seen).
5. Compare algorithms on **any-time performance**: incumbent error vs cumulative runtime, averaged over many seeds.

## Algorithm families

| Family | Adapts to past observations? | Allocates uneven resources? | Example |
|---|---|---|---|
| [[GridSearch|Grid search]] | No | No | – |
| [[RandomSearch]] | No | No | Bergstra & Bengio 2012 |
| [[BayesianOptimization|Bayesian optimization]] | Yes | No | Snoek et al. 2012, [[HyperOpt]], [[Optuna]] |
| [[SuccessiveHalving]] | No (searcher) | Yes (scheduler) | Jamieson & Talwalkar 2016 |
| [[Hyperband]] | No | Yes | Li et al. 2018 |
| [[ASHA]] | No | Yes (async) | Li et al. 2018 |
| BO + ASHA hybrids | Yes | Yes | BOHB (Falkner et al. 2018) |

## Connections

- [[d2l-hyperparameter-optimization]] — canonical D2L reference.
- [[HyperparameterTuning]] — the earlier, lighter wiki stub; this page is its full elaboration.
- [[BlackBoxOptimization]] — superclass of HPO.
- [[MultiFidelityOptimization]] — the resource-aware extension.
- [[NeuralArchitectureSearch]] — HPO over architectural choices; [[AutoML]] is the umbrella that contains both.
- [[CrossValidation]] / [[ModelSelection]] — HPO inherits the train/validation/test discipline; using the test set during HPO is the model-selection sin [[d2l-linear-classification]] warns against.
- [[SyneTune]] / [[RayTune]] / [[Optuna]] / [[HyperOpt]] — production HPO libraries.
- [[AaronKlein]] / [[MatthiasSeeger]] / [[CedricArchambeau]] — D2L HPO chapter authors.
