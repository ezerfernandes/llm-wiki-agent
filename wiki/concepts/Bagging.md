---
title: "Bagging"
type: concept
tags: [ensemble, trees]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Bagging

*Bootstrap aggregating*: fit a high-variance model (typically a deep [[DecisionTrees|tree]]) on each of $B$ [[Bootstrap]] samples and average the predictions. Reduces variance without raising bias. Introduced by Breiman (1996); the foundation of [[RandomForests]].

## Connections
- [[islr-seventh-printing]] — Ch.8.2.1.
- [[Bootstrap]] — resampling step.
- [[DecisionTrees]] — typical base learner.
- [[RandomForests]] — bagging with extra per-split randomness.
