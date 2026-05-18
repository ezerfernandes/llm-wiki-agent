---
title: "Linear Regression"
type: concept
tags: [classical-ml, regression]
sources: [islr-seventh-printing, mml-book, d2l-linear-regression]
last_updated: 2026-05-16
---

# Linear Regression

A model predicting a continuous target as a linear combination of features ($\hat y = \mathbf{w}^\top\mathbf{x} + b$), fit either by the closed-form normal equation $\mathbf{w}^* = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ (requires full column rank) or by minibatch [[StochasticGradientDescent|SGD]] minimizing [[MeanSquaredError|squared loss]]. The simplest interpretable baseline; foundational to [[statsmodels]], extends to [[LogisticRegression]] for classification.

## Three corpora, one model

- **[[islr-seventh-printing|ISLR]] Ch.3** — "fundamental starting point for all regression methods"; paired with [[KNearestNeighbors]] as the parametric / non-parametric contrast (§3.5).
- **[[mml-book|MML]] §9** — derives the closed form from Gaussian-NLL minimization; explicit gradient-zero derivation (§9.2.1, Eq. 9.12c).
- **[[d2l-linear-regression|D2L]] §3** — the canonical *neural-network-style* introduction: linear regression as a single-layer fully-connected net, motivating [[MinibatchSGD|minibatch SGD]] as the universal DL optimizer even on a problem with a closed-form solution. Introduces D2L's [[Module]] / [[DataModule]] / [[Trainer]] OO scaffold here.

## The probabilistic motivation

Under additive Gaussian noise $y = \mathbf{w}^\top\mathbf{x} + b + \epsilon,\ \epsilon\sim\mathcal{N}(0,\sigma^2)$, minimizing [[MeanSquaredError|MSE]] is exactly [[MaximumLikelihoodEstimation|maximum likelihood estimation]] — the link to [[GeneralizedLinearModels|GLMs]] and the bridge to classification via [[LogisticRegression]].

## Connections
- [[MeanSquaredError]] — the loss function.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — practical optimizer.
- [[MaximumLikelihoodEstimation]] — squared loss as Gaussian MLE.
- [[RidgeRegression]] / [[WeightDecay]] / [[Lasso]] — regularized variants.
- [[BayesianLinearRegression]] — full-posterior counterpart.
- [[PolynomialRegression]] — basis-expanded variant.
