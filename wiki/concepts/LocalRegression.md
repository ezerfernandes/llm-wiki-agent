---
title: "Local Regression"
type: concept
tags: [nonlinear, regression, nonparametric]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Local Regression

LOESS / LOWESS: at each target point $x_0$, fit a low-degree polynomial weighted toward training points near $x_0$. Span parameter $s$ controls the neighborhood size — a classic [[BiasVarianceTradeoff|bias-variance]] knob.

## Connections
- [[islr-seventh-printing]] — Ch.7.6.
- [[KNearestNeighbors]] — sibling nonparametric approach.
- [[GeneralizedAdditiveModels]] — can use LOESS as the per-feature smoother.
