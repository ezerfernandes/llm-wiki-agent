---
title: "Principal Components Regression"
type: concept
tags: [dimension-reduction, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Principal Components Regression (PCR)

Pipeline: compute the top $M$ [[PrincipalComponentAnalysis|principal components]] of $X$, then regress $Y$ on those $M$ components by least squares. Reduces variance by collapsing collinear predictors into orthogonal axes; unsupervised (PCA ignores $Y$), in contrast with [[PartialLeastSquares]].

## Connections
- [[islr-seventh-printing]] — Ch.6.3.1.
- [[PrincipalComponentAnalysis]] — the projection step.
- [[PartialLeastSquares]] — supervised counterpart.
