---
title: "Leave-One-Out Cross-Validation"
type: concept
tags: [resampling, evaluation]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Leave-One-Out Cross-Validation (LOOCV)

$n$-fold [[CrossValidation]]: each observation serves once as a singleton validation set. Nearly unbiased estimator of test error but high variance (the $n$ fits are highly correlated). For OLS regression a closed-form leverage shortcut avoids retraining.

## Connections
- [[islr-seventh-printing]] — Ch.5.1.2.
- [[CrossValidation]] — parent.
- [[KFoldCrossValidation]] — typical compromise.
