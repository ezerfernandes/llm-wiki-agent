---
title: "Multi-Fidelity Optimization"
type: concept
tags: [hpo, optimization, multi-fidelity]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Multi-Fidelity Optimization

A family of HPO algorithms that exploit **cheap-to-evaluate proxies** of the original objective function. Formally, expand the HPO objective from $f(\mathbf{x})$ to $f(\mathbf{x}, r)$ where $r\in[r_\text{min}, r_\text{max}]$ is a *resource budget* — typically the number of training epochs, the size of a training subset, or the number of cross-validation folds ([[d2l-hyperparameter-optimization]] §sec_mf_hpo).

## Assumptions

1. **Monotone error in resource:** $f(\mathbf{x}, r)$ decreases (or at least doesn't worsen) as $r$ grows.
2. **Monotone cost in resource:** computational cost $c(\mathbf{x}, r)$ increases with $r$.
3. **Predictiveness:** the ranking of configurations on cheap evaluations $f(\mathbf{x}, r_\text{min})$ is reasonably consistent with their ranking on full evaluations $f(\mathbf{x}, r_\text{max})$ — at least for the bottom configurations being early-stopped.

## What multi-fidelity buys

> "Multi-fidelity hyperparameter optimization allows to reduce the overall computation of the HPO instead of just reducing the wall-clock time." — [[d2l-hyperparameter-optimization]] §sh-intro Summary

Where [[AsyncParallelHPO|asynchronous parallel random search]] reduces wall-clock by parallelizing trials but keeps total compute constant, multi-fidelity HPO reduces total compute by aggressively *not running* trials that look poor early.

## Algorithms

- **[[SuccessiveHalving]]** ([[Jamieson]] & Talwalkar 2016; [[Karnin]] et al. 2013) — the foundational synchronous algorithm.
- **[[Hyperband]]** ([[LishaLi|Li]] et al. 2018) — wraps SH in a hedging bracket over $(n, r)$.
- **[[ASHA]]** ([[LishaLi|Li]] et al. 2018) — asynchronous SH; the default production multi-fidelity scheduler.
- **BOHB** (Falkner et al. 2018) — combines Hyperband bracketing with a [[BayesianOptimization|TPE]] surrogate model for the searcher.

## Connections

- [[d2l-hyperparameter-optimization]] — chapter §sec_mf_hpo introduces the multi-fidelity framing.
- [[SuccessiveHalving]] / [[Hyperband]] / [[ASHA]] — the canonical algorithms.
- [[EarlyStopping]] — multi-fidelity HPO operationalizes early stopping at the *trial* level (not just the *epoch* level).
- [[HyperparameterOptimization]] / [[BlackBoxOptimization]] — parent concepts.
