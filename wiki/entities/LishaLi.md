---
title: "Lisha Li"
type: entity
tags: [researcher, hpo, hyperband, asha]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Lisha Li

Researcher (UC Berkeley / CMU lineage); founder of Rosebud AI. Best known for two foundational [[MultiFidelityOptimization|multi-fidelity HPO]] algorithms:

- **[[Hyperband]]** (Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar, JMLR 2018) — wraps [[SuccessiveHalving]] in a hedging bracket strategy over the choice of $n$ (number of initial configs) vs $r$ (rung budget), eliminating the user-tuning burden.
- **[[ASHA|Asynchronous Successive Halving Algorithm]]** (Li, Jamieson, Rostamizadeh, Gonina, Hardt, Recht & Talwalkar 2018, *arxiv 1810.05934*) — promotes configurations the moment $\eta$ observations land on a rung, eliminating synchronous SH's idle-worker pathology. Used in [[d2l-hyperparameter-optimization]] §sh-async via [[SyneTune]]'s `ASHA` scheduler.

## Connections
- [[Jamieson|Kevin Jamieson]] — co-author of [[Hyperband]] and [[ASHA]].
- [[Hyperband]] / [[ASHA]] / [[SuccessiveHalving]] — concepts Li's papers introduce.
- [[SyneTune]] / [[RayTune]] — production libraries that implement ASHA.
- [[d2l-hyperparameter-optimization]] — cites Li et al. 2018 for [[ASHA]].
