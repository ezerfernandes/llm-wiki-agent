---
title: "Generalized Additive Models"
type: concept
tags: [nonlinear, regression, classification]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Generalized Additive Models (GAMs)

$y_i = \beta_0 + \sum_{j=1}^p f_j(x_{ij}) + \epsilon_i$ — replace each linear term in a [[LinearRegression]] or [[LogisticRegression]] with a smooth function $f_j$ (typically a [[RegressionSplines|spline]] or [[LocalRegression|LOESS]]). Coined by [[TrevorHastie|Hastie]] & [[RobertTibshirani|Tibshirani]] in 1986; preserves the interpretability of additive structure while admitting non-linearity per feature.

## Connections
- [[islr-seventh-printing]] — Ch.7.7.
- [[GeneralizedLinearModels]] — the linear ancestor; GAMs swap linear terms for smooths.
- [[TrevorHastie]], [[RobertTibshirani]] — coined the term.
- [[RegressionSplines]], [[SmoothingSplines]], [[LocalRegression]] — typical per-feature smoothers.
