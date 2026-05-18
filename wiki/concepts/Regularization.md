---
title: "Regularization"
type: concept
tags: [training, theory]
sources: [madewithml-training, d2l-linear-regression, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Regularization

Techniques that constrain [[ModelComplexity]] to combat [[Overfitting]]: $\ell_1$ / $\ell_2$ penalties, [[Dropout]], early stopping, data augmentation. Trades a small training-loss increase for better generalization.

[[d2l-linear-regression]] §3.7 introduces **[[WeightDecay|weight decay]]** ($\ell_2$ regularization) as "the first practical regularization technique," motivated by the heuristic that "among all functions $f$, the function $f = 0$ is in some sense the *simplest*, and that we can measure the complexity of a function by the distance of its parameters from zero." Replaces the original objective (minimize prediction loss) with the augmented objective (minimize prediction loss + penalty term).

## Common penalty / constraint families

- **[[WeightDecay|Weight decay]] ($\ell_2$ / ridge)** — penalize $\|\mathbf{w}\|_2^2$; spreads weight across features; standard default.
- **[[Lasso|Lasso]] ($\ell_1$)** — penalize $\|\mathbf{w}\|_1$; performs feature selection by zeroing small weights.
- **[[Dropout]]** — randomly zero activations during training.
- **Early stopping** — halt training when validation loss plateaus.
- **Data augmentation** — synthetic perturbations of training examples.

## Connections

- [[d2l-linear-regression]] — §3.7 canonical reference (introduces weight decay).
- [[d2l-multilayer-perceptrons]] — deep-learning angle: [[Dropout]], [[EarlyStopping]], and the caveat that classical regularizers don't actually constrain capacity in the [[InterpolationRegime|interpolation regime]].
- [[WeightDecay]] / [[RidgeRegression]] — $\ell_2$ form.
- [[Lasso]] — $\ell_1$ form.
- [[Overfitting]] — what regularization combats.
- [[Underfitting]] — what too-strong regularization causes.
- [[ModelSelection]] / [[CrossValidation]] — how the regularization strength $\lambda$ is chosen.
- [[MAPEstimation]] / [[BayesianLinearRegression]] — Bayesian interpretation of regularization as prior.
