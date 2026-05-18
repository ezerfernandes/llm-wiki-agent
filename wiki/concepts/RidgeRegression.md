---
title: "Ridge Regression"
type: concept
tags: [regularization, regression, shrinkage]
sources: [islr-seventh-printing, d2l-linear-regression]
last_updated: 2026-05-16
---

# Ridge Regression

[[LinearRegression]] with an $\ell_2$ penalty: $\min_\beta \|y - X\beta\|_2^2 + \lambda \|\beta\|_2^2$. Shrinks all coefficients toward zero but never to zero — no variable selection. Trades a small increase in bias for a large decrease in variance; particularly effective when $p$ is comparable to $n$ or predictors are collinear. Tuning $\lambda$ via [[CrossValidation]].

## Connections
- [[islr-seventh-printing]] — Ch.6.2.1.
- [[Lasso]] — $\ell_1$ counterpart that performs variable selection.
- [[CrossValidation]] — selects $\lambda$.
- [[LinearRegression]] — the unpenalized base model.
