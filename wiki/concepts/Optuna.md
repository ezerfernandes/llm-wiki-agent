---
title: "Optuna"
type: concept
tags: [library, hpo, bayesian-optimization, tpe, hyperparameter]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Optuna

Open-source [[HyperparameterOptimization|hyperparameter-optimization]] framework (Akiba, Sano, Yanase, Ohta, Koyama 2019, *KDD*). Ships [[TreeStructuredParzenEstimator|TPE]], CMA-ES, and other samplers behind a single `optuna.optimize(objective, n_trials=N)` interface; widely used for ML hyperparameter tuning, NAS, and now (via the [[2406.11695-mipro|MIPRO paper]]) **LM-program prompt optimization**.

## Role in [[MIPROv2|MIPRO]]

The MIPRO paper uses **Optuna's multivariate TPE implementation** (Falkner et al. 2018, BOHB's variant) as the [[BayesianOptimization|Bayesian]] surrogate for the discrete-search stage of MIPRO:

- The categorical variables are **(instruction-index, demo-set-index) per module** across $m$ modules.
- The objective is **mini-batch program score** ($\sigma$) on a $B$-sample mini-batch from the trainset $\mathcal{D}$.
- The acquisition is **multivariate Expected Improvement** — the *multivariate* qualifier is critical because it lets TPE model **joint contributions across modules**, which is what makes [[CreditAssignment|credit assignment]] across modules possible without a per-module label.

The choice of TPE over a [[GaussianProcess|GP]] is consistent with `optuna`'s default sampler — TPE handles **categorical / hierarchical search spaces** more naturally than GP, and the multivariate variant supports the joint modeling MIPRO needs.

## Connections

- [[TreeStructuredParzenEstimator]] — the algorithm Optuna ships and MIPRO uses.
- [[BayesianOptimization]] — parent technique.
- [[HyperOpt]] — predecessor library; also ships TPE.
- [[2406.11695-mipro]] — the canonical wiki source for Optuna's role in LM-program optimization.
- [[MIPROv2|MIPRO]] — the LM-program optimizer that calls into Optuna.
