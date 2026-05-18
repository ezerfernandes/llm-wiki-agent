---
title: "Bias-Variance Decomposition"
type: concept
tags: [statistics, foundational, learning-theory]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Bias-Variance Decomposition

For any estimator $\hat\theta_n$ of a fixed target $\theta$, the **mean squared error** decomposes cleanly into squared bias and variance ([[d2l-appendix-mathematics]] §statistics):

$$\text{MSE}(\hat\theta_n) = \mathbb{E}\!\big[(\hat\theta_n - \theta)^2\big] = \underbrace{\big(\mathbb{E}[\hat\theta_n] - \theta\big)^2}_{\text{bias}^2} + \underbrace{\text{Var}(\hat\theta_n)}_{\text{variance}}.$$

- **Bias** = how far the estimator's *expected* value is from the truth — systematic error.
- **Variance** = how much the estimator wobbles across different samples — sampling noise.

An estimator with zero bias is called **unbiased**; one whose bias and variance both vanish as $n\to\infty$ is **consistent**.

## Why both terms matter

A constant estimator $\hat\theta_n \equiv c$ has **zero variance** but bias $(c-\theta)^2$ — useless. The empirical mean $\hat\mu = \bar X$ has **zero bias** but variance $\sigma^2/n$ — improves with $n$. The art of estimator design is choosing where on the bias-variance trade-off curve to sit.

## In supervised learning: predictor risk decomposition

For a regression predictor $\hat f$ trained on a sample $\mathcal{D}$, the **expected test loss at a new point** $x$ decomposes (assuming additive Gaussian noise $\epsilon$):

$$\mathbb{E}_{\mathcal{D},\epsilon}\!\big[(y - \hat f(x))^2\big] = \underbrace{\big(\mathbb{E}_\mathcal{D}[\hat f(x)] - f^*(x)\big)^2}_{\text{bias}^2} + \underbrace{\text{Var}_\mathcal{D}(\hat f(x))}_{\text{variance}} + \underbrace{\sigma^2}_{\text{irreducible noise}}.$$

This is *the* classical framing of generalization:

| Regime | Bias | Variance |
|---|---|---|
| **Underfitting** (high regularization / low capacity) | high | low |
| **Sweet spot** (balanced) | moderate | moderate |
| **Overfitting** (low regularization / high capacity) | low | high |

The classical U-shaped test-error curve in capacity is the sum of a monotonically-decreasing bias term and a monotonically-increasing variance term.

## The deep-learning twist: double descent

Modern overparametrized neural networks violate the classical U-shape — the [[DoubleDescent|double-descent]] phenomenon ([[PreetumNakkiran|Nakkiran]] et al. 2021) shows test error rising, falling, *re-rising* at the interpolation threshold, then falling again as capacity grows further. The bias-variance decomposition still holds; what changes is that variance can *decrease* with capacity in the overparametrized regime due to the implicit bias of SGD toward low-norm solutions.

## ML uses

- **[[CrossValidation|Cross-validation]]**: trades variance for bias (smaller train sets give noisier but lower-bias estimates of generalization).
- **Regularization** ([[WeightDecay|$\ell_2$]], [[Lasso|$\ell_1$]], dropout, early stopping): increases bias to reduce variance.
- **Ensembling / [[Bagging]]**: averages many high-variance, low-bias predictors to reduce variance without adding bias.
- **[[Boosting]]**: sequentially reduces bias by fitting residuals of high-bias weak learners.

## Connections

- [[d2l-appendix-mathematics]] — §statistics canonical reference.
- [[MeanSquaredError]] — the loss that admits this decomposition.
- [[Generalization]] — what the decomposition explains.
- [[Overfitting]] / [[Underfitting]] — the two failure modes.
- [[DoubleDescent]] — modern qualification under overparametrization.
- [[CrossValidation]] / [[Bagging]] / [[Boosting]] — algorithms designed against the decomposition.
- [[Statistics]] — parent discipline.
