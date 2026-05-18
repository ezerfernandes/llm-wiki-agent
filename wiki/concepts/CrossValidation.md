---
title: "Cross-Validation"
type: concept
tags: [resampling, model-selection, evaluation]
sources: [islr-seventh-printing, mml-book, d2l-linear-regression]
last_updated: 2026-05-16
---

# Cross-Validation

Resampling procedure for estimating test error: hold out part of the data, fit on the rest, repeat. Variants: [[ValidationSetApproach]] (single split), [[LeaveOneOutCrossValidation|LOOCV]] (each obs. once), [[KFoldCrossValidation|k-fold]] (usually $k\in\{5,10\}$ — a [[BiasVarianceTradeoff|bias-variance compromise]] between the other two). The standard tool for choosing tuning parameters (e.g. $\lambda$ in [[RidgeRegression]] / [[Lasso]], $K$ in [[KNearestNeighbors]]).

[[mml-book]] §8.2.4 introduces $K$-fold CV as the procedure for *constructing predictors from training data that perform well on unseen test data*, then §8.6.1 layers **[[NestedCrossValidation|nested cross-validation]]** on top — outer loop estimates generalization error, inner loop selects hyperparameters. Single-loop CV that's also the hyperparameter-selection criterion overfits to the validation folds.

## Connections
- [[islr-seventh-printing]] — Ch.5.1.
- [[mml-book]] — §8.2.4 + §8.6.1 canonical reference.
- [[ValidationSetApproach]], [[LeaveOneOutCrossValidation]], [[KFoldCrossValidation]] — variants.
- [[NestedCrossValidation]] — outer-loop / inner-loop protocol for honest model selection.
- [[ModelSelection]] — the broader problem CV solves.
- [[Bootstrap]] — sibling resampling tool (Ch.5.2).
- [[BiasVarianceTradeoff]] — what CV navigates.
