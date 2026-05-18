---
title: "Bootstrap"
type: concept
tags: [resampling, statistics, uncertainty]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Bootstrap

Resampling procedure introduced by [[BradleyEfron|Efron]] (1979): draw $B$ samples *with replacement* from the observed data, compute the statistic of interest on each, and use the empirical distribution as an estimate of the sampling distribution. Provides standard errors and confidence intervals for *any* estimator without a parametric formula. Foundation of [[Bagging]] in ISLR Ch.8.

## Connections
- [[islr-seventh-printing]] — Ch.5.2.
- [[CrossValidation]] — sibling resampling tool.
- [[Bagging]] — applies the bootstrap to decision trees.
- [[RobertTibshirani]] — co-author of *An Introduction to the Bootstrap*.
