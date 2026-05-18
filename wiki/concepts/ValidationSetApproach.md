---
title: "Validation Set Approach"
type: concept
tags: [resampling, evaluation]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Validation Set Approach

Randomly split data into training and validation sets; fit on training, estimate test error on validation. Simplest form of [[CrossValidation]]. High variance — different splits give different estimates — and trains on less data than $k$-fold CV does on each fold.

## Connections
- [[islr-seventh-printing]] — Ch.5.1.1.
- [[CrossValidation]] — generalization.
- [[KFoldCrossValidation]], [[LeaveOneOutCrossValidation]] — lower-variance alternatives.
