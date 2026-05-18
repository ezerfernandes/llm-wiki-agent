---
title: "Underfitting"
type: concept
tags: [theory, training]
sources: [d2l-linear-regression]
last_updated: 2026-05-16
---

# Underfitting

When a model is **too simple** to capture the pattern in the data: both training error and validation error are high, but the [[GeneralizationGap|generalization gap]] between them is small. The diagnostic mirror image of [[Overfitting|overfitting]].

[[d2l-linear-regression]] §3.6: "If the model is unable to reduce the training error, that could mean that our model is too simple (i.e., insufficiently expressive) to capture the pattern that we are trying to model. Moreover, since the *generalization gap* between our training and generalization errors is small, we have reason to believe that we could get away with a more complex model."

## Remedies

- Increase model capacity (more parameters, deeper architecture, richer feature basis like [[PolynomialRegression]]).
- Reduce regularization strength ([[WeightDecay|weight-decay]] $\lambda$, [[Dropout]] rate).
- Train longer (sometimes loss has not yet converged).
- Add features (engineered or learned via [[RepresentationLearning|representation learning]]).

## The U-curve

On a plot of error vs. model complexity, underfitting is the *left side* (high training + high validation), the minimum-validation point is the "sweet spot," and overfitting is the *right side* (low training, high validation). See [[GeneralizationGap]] for the modern double-descent caveat.

## Connections

- [[d2l-linear-regression]] — canonical introduction (§3.6).
- [[Overfitting]] — symmetric failure mode.
- [[GeneralizationGap]] — what's small under underfitting but large under overfitting.
- [[ModelSelection]] — the procedure for landing between the two.
- [[Regularization]] — too much of it causes underfitting.
