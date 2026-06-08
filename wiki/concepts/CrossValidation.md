---
title: "Cross-Validation"
type: concept
tags: [resampling, model-selection, evaluation]
sources: [islr-seventh-printing, mml-book, mml-ch08-when-models-meet-data, d2l-linear-regression]
last_updated: 2026-06-04
---

# Cross-Validation

Resampling procedure for estimating test error: hold out part of the data, fit on the rest, repeat. Variants: [[ValidationSetApproach]] (single split), [[LeaveOneOutCrossValidation|LOOCV]] (each obs. once), [[KFoldCrossValidation|k-fold]] (usually $k\in\{5,10\}$ — a [[BiasVarianceTradeoff|bias-variance compromise]] between the other two). The standard tool for choosing tuning parameters (e.g. $\lambda$ in [[RidgeRegression]] / [[Lasso]], $K$ in [[KNearestNeighbors]]).

[[mml-book]] §8.2.4 introduces $K$-fold CV as the procedure for *constructing predictors from training data that perform well on unseen test data*, then §8.6.1 layers **[[NestedCrossValidation|nested cross-validation]]** on top — outer loop estimates generalization error, inner loop selects hyperparameters. Single-loop CV that's also the hyperparameter-selection criterion overfits to the validation folds.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.2.4 motivates CV as the resolution of a *contradiction*: a small validation set $\mathcal{V}$ gives a noisy (high-variance) performance estimate, but we want to train on as much data as possible. **$K$-fold CV** partitions $\mathcal{D}=\mathcal{R}\cup\mathcal{V}$ ($\mathcal{R}\cap\mathcal{V}=\emptyset$) into $K$ chunks, $K-1$ forming the training set $\mathcal{R}$ and one the validation set $\mathcal{V}$, iterating over all $K$ assignments (Fig. 8.4) and averaging — approximating the expected generalization error $\mathbb{E}_{\mathcal{V}}[R(f,\mathcal{V})]\approx\frac1K\sum_{k=1}^K R(f^{(k)},\mathcal{V}^{(k)})$ (Eq. 8.13). Two approximation sources: the finite training set (suboptimal $f^{(k)}$) and the finite validation set (inaccurate risk). The cost is training $K$ times — burdensome especially when several complexity/regularization hyperparameters require an *exponential* number of runs (motivating [[NestedCrossValidation|nested CV]], §8.6.1) — but CV is **embarrassingly parallel**, so with enough compute it costs no more than a single assessment.

## Connections
- [[islr-seventh-printing]] — Ch.5.1.
- [[mml-book]] — §8.2.4 + §8.6.1 canonical reference.
- [[ValidationSetApproach]], [[LeaveOneOutCrossValidation]], [[KFoldCrossValidation]] — variants.
- [[NestedCrossValidation]] — outer-loop / inner-loop protocol for honest model selection.
- [[ModelSelection]] — the broader problem CV solves.
- [[Bootstrap]] — sibling resampling tool (Ch.5.2).
- [[BiasVarianceTradeoff]] — what CV navigates.
