---
title: "James Bergstra"
type: entity
tags: [researcher, hpo, hyperopt]
sources: [d2l-hyperparameter-optimization]
last_updated: 2026-05-16
---

# James Bergstra

Researcher (formerly Université de Montréal / [[YoshuaBengio|Bengio]] lab, then Waterloo / Kindred). Best known in the HPO literature for:

- **Bergstra & Bengio 2012**, *Random Search for Hyper-Parameter Optimization* (JMLR) — proves random search dominates grid search on the *effective-low-dimensionality* problems typical of deep-learning HPO. Cited as the canonical justification for using [[RandomSearch]] in [[d2l-hyperparameter-optimization]].
- **Bergstra, Bardenet, Bengio & Kégl 2011**, *Algorithms for Hyper-Parameter Optimization* (NeurIPS) — introduces the [[TreeStructuredParzenEstimator|TPE]] surrogate that powers the [[HyperOpt]] library.

## Connections
- [[YoshuaBengio]] — co-author of the random-search and TPE papers.
- [[HyperOpt]] — open-source library implementing Bergstra's TPE.
- [[RandomSearch]] / [[GridSearch]] / [[BayesianOptimization]] — concepts Bergstra's papers define the baseline behavior of.
- [[d2l-hyperparameter-optimization]] — cites Bergstra-Bengio 2012 for the random-vs-grid result.
