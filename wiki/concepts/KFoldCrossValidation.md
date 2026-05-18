---
title: "k-Fold Cross-Validation"
type: concept
tags: [resampling, evaluation]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# k-Fold Cross-Validation

Randomly partition data into $k$ folds; for each fold, fit on the other $k-1$ folds and validate on the held-out fold; average the $k$ errors. $k\in\{5,10\}$ is the standard [[BiasVarianceTradeoff|bias-variance]] compromise: lower variance than [[LeaveOneOutCrossValidation|LOOCV]] (less correlated fits), lower bias than the [[ValidationSetApproach]].

## Connections
- [[islr-seventh-printing]] — Ch.5.1.3.
- [[CrossValidation]] — parent.
- [[LeaveOneOutCrossValidation]], [[ValidationSetApproach]] — the bracketing extremes.
