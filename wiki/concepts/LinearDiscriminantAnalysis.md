---
title: "Linear Discriminant Analysis"
type: concept
tags: [classical-ml, classification]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Linear Discriminant Analysis (LDA)

Bayes-rule classifier under the assumption that each class density $f_k(x)$ is multivariate Gaussian with a *common* covariance matrix $\Sigma$. The resulting decision boundaries are linear in $x$. Coined by Fisher (1936); a classical alternative to [[LogisticRegression]] that often outperforms it when classes are well-separated or $n$ is small.

## Connections
- [[islr-seventh-printing]] — Ch.4.4.
- [[QuadraticDiscriminantAnalysis]] — relax the equal-covariance assumption.
- [[LogisticRegression]] — sibling linear classifier with different generative assumptions.
