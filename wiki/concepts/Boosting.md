---
title: "Boosting"
type: concept
tags: [ensemble, trees]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Boosting

Sequentially fit small (shallow) [[DecisionTrees|trees]], each to the *residuals* of the running ensemble, with a learning-rate shrinkage. Unlike [[Bagging]] / [[RandomForests]] this is *not* trained in parallel and uses small trees on purpose. Tunable via tree depth $d$, number of trees $B$, shrinkage $\lambda$. Practical descendants: XGBoost, LightGBM.

## Connections
- [[islr-seventh-printing]] — Ch.8.2.3.
- [[DecisionTrees]] — base learner.
- [[Bagging]], [[RandomForests]] — parallel-ensemble alternatives.
