---
title: "Hyperparameter Tuning"
type: concept
tags: [optimization, ml-engineering, hpo]
sources: [d2l-linear-regression, d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# Hyperparameter Tuning

Searching the space of non-learned settings ([[LearningRate]], depth, regularization, [[Dropout]] rate) for configurations that maximize validation performance. Strategies include grid, random, [[BayesianOptimization]], and [[ASHA]]; orchestrated by [[RayTune]], [[Optuna]], or [[Kubeflow]] Katib.

> **See [[HyperparameterOptimization]]** for the full algorithmic treatment from [[d2l-hyperparameter-optimization]] — the searcher / scheduler API, black-box framing, random-vs-grid analysis ([[JamesBergstra|Bergstra]] & [[YoshuaBengio|Bengio]] 2012), and the multi-fidelity family ([[SuccessiveHalving]] / [[Hyperband]] / [[ASHA]]).
