---
title: "Hyperband"
type: concept
tags: [hpo, multi-fidelity, scheduler]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Hyperband

A multi-fidelity HPO algorithm ([[LishaLi|Li]], Jamieson, DeSalvo, Rostamizadeh & Talwalkar, JMLR 2018) that wraps [[SuccessiveHalving|successive halving]] in an **outer bracket loop** hedging over the trade-off between the number of initial configurations $n$ and the per-config resource budget $r$.

## The $n$ vs $r$ problem Hyperband solves

Plain [[SuccessiveHalving]] requires choosing $r_\text{min}$. Too small and the early-stopping decisions are noisy and a good config might be eliminated. Too large and most of the compute is spent before halving kicks in. Hyperband's answer: don't choose — run several SH rounds (brackets) with different $(n_s, r_s)$ pairs in parallel, each maintaining the same total budget $B$. Bracket $s$ runs SH with more configs and smaller $r_\text{min}$, bracket $s+1$ runs SH with fewer configs and larger $r_\text{min}$, and so on.

This gives Hyperband the property that **at least one bracket matches the optimal SH configuration**, up to a constant factor, without requiring the user to know which bracket that is.

## Connections

- [[d2l-hyperparameter-optimization]] — chapter where Hyperband is introduced via its successor [[ASHA]] (§sh-async).
- [[LishaLi]] — first author of the Hyperband paper.
- [[SuccessiveHalving]] — Hyperband's inner loop.
- [[ASHA]] — Hyperband's asynchronous successor; in practice deployed *instead of* Hyperband.
- [[MultiFidelityOptimization]] / [[HyperparameterOptimization]] — parent concepts.
- [[RayTune]] / [[SyneTune]] / [[Optuna]] — production implementations.
