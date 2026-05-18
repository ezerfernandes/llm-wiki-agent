---
title: "Partial Least Squares"
type: concept
tags: [dimension-reduction, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Partial Least Squares (PLS)

Supervised dimension-reduction sibling of [[PrincipalComponentsRegression|PCR]]: each new component is the linear combination of predictors that has highest covariance with $Y$. Unlike PCA, the projection uses the response — sometimes better, often comparable to PCR in practice.

## Connections
- [[islr-seventh-printing]] — Ch.6.3.2.
- [[PrincipalComponentsRegression]] — unsupervised counterpart.
