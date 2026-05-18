---
title: "Lasso"
type: concept
tags: [regularization, regression, shrinkage, variable-selection]
sources: [islr-seventh-printing, d2l-linear-regression]
last_updated: 2026-05-16
---

# Lasso

[[LinearRegression]] with an $\ell_1$ penalty: $\min_\beta \|y - X\beta\|_2^2 + \lambda \|\beta\|_1$. Proposed by [[RobertTibshirani]] (1996). Unlike [[RidgeRegression]], the geometry of the $\ell_1$ ball forces some coefficients to *exactly zero* — performing simultaneous shrinkage and variable selection. Workhorse for high-dimensional ($p \gg n$) regression.

## Connections
- [[islr-seventh-printing]] — Ch.6.2.2.
- [[RidgeRegression]] — $\ell_2$ counterpart that keeps all variables.
- [[RobertTibshirani]] — proposer.
- [[CrossValidation]] — selects $\lambda$.
