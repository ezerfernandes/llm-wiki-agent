---
title: "Backward Stepwise Selection"
type: concept
tags: [model-selection, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Backward Stepwise Selection

Greedy variant of [[BestSubsetSelection]]: start with the full $p$-predictor model and at each step drop the predictor whose removal least worsens fit. Requires $n > p$ to start (the full OLS fit must exist).

## Connections
- [[islr-seventh-printing]] — Ch.6.1.2.
- [[ForwardStepwiseSelection]] — bottom-up counterpart.
- [[BestSubsetSelection]] — exact reference.
