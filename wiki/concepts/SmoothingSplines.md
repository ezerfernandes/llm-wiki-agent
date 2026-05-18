---
title: "Smoothing Splines"
type: concept
tags: [nonlinear, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Smoothing Splines

Solution to $\min_g \sum_i (y_i - g(x_i))^2 + \lambda \int g''(t)^2\,dt$. The minimizer is a natural cubic spline with a knot at every distinct $x_i$; the penalty $\lambda$ controls smoothness and is chosen by [[CrossValidation]] (LOOCV has a closed-form shortcut here).

## Connections
- [[islr-seventh-printing]] — Ch.7.5.
- [[RegressionSplines]] — knot-based alternative.
- [[CrossValidation]] — tunes $\lambda$.
