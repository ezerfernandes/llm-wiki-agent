---
title: "Generalized Linear Models"
type: concept
tags: [statistics, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Generalized Linear Models (GLMs)

Unifying frame coined by Nelder & Wedderburn (1972): the response $Y$ comes from an exponential-family distribution and a *link function* maps its mean to a linear combination of predictors. Special cases: [[LinearRegression]] (identity link, Gaussian), [[LogisticRegression]] (logit link, binomial), Poisson regression (log link).

## Connections
- [[islr-seventh-printing]] — Ch.1 history; subsumes Ch.3 + Ch.4.
- [[LinearRegression]], [[LogisticRegression]] — canonical instances.
- [[GeneralizedAdditiveModels]] — non-linear extension.
