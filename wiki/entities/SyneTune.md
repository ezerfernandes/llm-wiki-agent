---
title: "Syne Tune"
type: entity
tags: [tool, hyperparameter-tuning, amazon, hpo]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Syne Tune

[[Amazon]]-developed open-source distributed HPO library (Salinas, Seeger, Klein, Perrone, Archambeau, AutoML 2022). Architectural primitives mirror the D2L `HPOSearcher` / `HPOScheduler` / `HPOTuner` decomposition; pluggable execution back-ends include local processes (`PythonBackend`), SageMaker, and clusters. Implements [[RandomSearch]], [[BayesianOptimization]], [[ASHA]], [[Hyperband]], and constrained / multi-objective extensions.

Used as D2L's preferred distributed-HPO backend in [[d2l-hyperparameter-optimization]] §rs-async (async random search) and §sh-async (ASHA).

## Connections
- [[Amazon]] — institutional backer.
- [[AaronKlein]] / [[MatthiasSeeger]] / [[CedricArchambeau]] — primary authors / contributors.
- [[RayTune]] / [[Optuna]] — peer open-source HPO libraries with the same searcher/scheduler decomposition.
- [[ASHA]] / [[RandomSearch]] / [[BayesianOptimization]] — schedulers / searchers Syne Tune ships with.
- [[d2l-hyperparameter-optimization]] — first source citing Syne Tune.
