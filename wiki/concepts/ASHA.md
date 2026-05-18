---
title: "ASHA (Async Successive Halving)"
type: concept
tags: [hyperparameter-tuning, optimization, hpo, multi-fidelity]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# ASHA

**Asynchronous Successive Halving Algorithm** ([[LishaLi|Li]], Jamieson, Rostamizadeh, Gonina, Hardt, Recht & Talwalkar 2018, *arxiv 1810.05934*) — the asynchronous version of [[SuccessiveHalving|successive halving]] that eliminates the synchronization barrier and idle-worker pathology of synchronous SH ([[d2l-hyperparameter-optimization]] §sh-async).

## The decision rule

> "The main idea of ASHA is to promote configurations to the next rung level as soon as we collected at least $\eta$ observations on the current rung level." — [[d2l-hyperparameter-optimization]] §sh-async

When a worker becomes free:

1. If a configuration on rung $r_i$ has *not yet been promoted* and at least $\eta$ observations exist on $r_i$ such that it is in the top $1/\eta$ fraction → **promote it to $r_{i+1}$**.
2. Otherwise → **start a new trial at $r_\text{min}$**.

This trades off the *optimality* of synchronous SH's promotion decisions (which see complete rung data) for the *zero idle time* of asynchronous workers. In practice, the trade is overwhelmingly favorable because (a) hyperparameter rankings are fairly consistent across rungs, and (b) rungs grow over time, so later promotion decisions get better.

## Why this beats synchronous SH at distributed scale

Synchronous SH forces all workers to wait until *every* configuration on rung $r_i$ has finished training before any promotion. Heterogeneous training times (configs with more filters / layers take longer) → idle stragglers. Worse, the number of slots in a rung is often not a multiple of the worker count → some workers idle for a full batch. ASHA removes both pathologies.

## Connections

- [[d2l-hyperparameter-optimization]] §sh-async — D2L's canonical reference; uses [[SyneTune]]'s `ASHA` scheduler.
- [[LishaLi]] — first author of the 2018 ASHA paper.
- [[SuccessiveHalving]] — the synchronous baseline ASHA accelerates.
- [[Hyperband]] — the synchronous bracket-hedging cousin; in practice ASHA is deployed instead.
- [[BayesianOptimization]] — the model-based searcher class often combined with ASHA (BOHB).
- [[MultiFidelityOptimization]] / [[HyperparameterOptimization]] — parent concepts.
- [[SyneTune]] / [[RayTune]] — production implementations of ASHA.
