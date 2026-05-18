---
title: "Quadratic Discriminant Analysis"
type: concept
tags: [classical-ml, classification]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Quadratic Discriminant Analysis (QDA)

[[LinearDiscriminantAnalysis|LDA]] with per-class covariance matrices $\Sigma_k$; the decision boundary becomes *quadratic* in $x$. More flexible than LDA, more parameters to estimate — preferred when $n$ is large and class covariances clearly differ.

## Connections
- [[islr-seventh-printing]] — Ch.4.4.4.
- [[LinearDiscriminantAnalysis]] — restricted (shared-covariance) variant.
- [[BiasVarianceTradeoff]] — QDA trades LDA's bias for variance.
