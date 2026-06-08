---
title: "Noise Model"
type: concept
tags: [regression, probabilistic-modeling, likelihood, foundational]
sources: [mml-ch09-linear-regression, mml-book]
last_updated: 2026-06-04
---

# Noise Model (Observation Noise / Likelihood)

The probabilistic assumption that observed targets are **noise-corrupted function values** $y = f(\mathbf{x}) + \epsilon$, which turns a deterministic function into a [[Likelihood|likelihood]] over data and is what makes [[MaximumLikelihoodEstimation|MLE]] / [[BayesianInference|Bayesian]] estimation possible. [[mml-ch09-linear-regression|MML Ch 9]] §9.1 fixes the noise to **zero-mean Gaussian** throughout:

$$p(y\mid\mathbf{x}) = \mathcal{N}\big(y\mid f(\mathbf{x}),\,\sigma^2\big) \quad\Longleftrightarrow\quad y = f(\mathbf{x}) + \epsilon,\ \ \epsilon\sim\mathcal{N}(0,\sigma^2)\ \text{i.i.d.}$$

(Eqs. 9.1–9.2). The noise is the **only source of uncertainty** in the likelihood (inputs $\mathbf{x}$ and parameters $\boldsymbol\theta$ are treated as known); without it the $\mathbf{x}\!\to\!y$ map would be deterministic and the likelihood would collapse to a **Dirac delta** (a Gaussian in the limit $\sigma^2\to 0$) — MML margin note, p. 291.

## Why the noise model = the loss function

The choice of noise distribution *induces* the training loss — the chapter's "relationship between loss functions and parameter priors" theme (§9.1). The **Gaussian** noise model gives the squared-error / [[LeastSquares|least-squares]] loss (since $-\log\mathcal{N}=\frac{1}{2\sigma^2}(y-f)^2+\text{const}$, MML Eq. 9.9). Different noise → different loss: a **Bernoulli** likelihood gives cross-entropy ([[LogisticRegression]]), **Laplace** noise gives absolute-error loss, **Binomial/Poisson** for count data — all examples of [[GeneralizedLinearModels|GLMs]] (§9.5).

## Estimating the noise variance

$\sigma^2$ need not be assumed known: its MLE is the empirical mean of squared residuals $\sigma^2_{\text{ML}}=\frac{1}{N}\sum_n(y_n-\boldsymbol\phi^\top(\mathbf{x}_n)\boldsymbol\theta)^2$ ([[mml-ch09-linear-regression|MML]] Eq. 9.22, derived by zeroing $\partial\log p/\partial\sigma^2$).

## Aleatoric vs epistemic uncertainty

In [[BayesianLinearRegression|Bayesian linear regression]] the predictive variance separates the noise model's contribution from parameter uncertainty: $\mathbb{V}[y_*]=\underbrace{\sigma^2}_{\text{aleatoric (noise)}}+\underbrace{\boldsymbol\phi_*^\top\mathbf{S}_N\boldsymbol\phi_*}_{\text{epistemic (parameters)}}$ ([[mml-ch09-linear-regression|MML]] Eq. 9.57). The noise term $\sigma^2$ is irreducible ([[AleatoricUncertainty]]); the parameter term shrinks with more data ([[EpistemicUncertainty]]).

## Connections

- [[mml-ch09-linear-regression]] / [[mml-book]] — §9.1 canonical reference (Eqs. 9.1–9.4); §9.2.1 (noise-variance MLE, Eq. 9.22).
- [[GaussianDistribution]] — the assumed noise distribution.
- [[Likelihood]] — what the noise model defines.
- [[LeastSquares]] / [[MaximumLikelihoodEstimation]] — Gaussian noise ⇒ squared-error MLE.
- [[GeneralizedLinearModels]] — other noise models ⇒ other losses.
- [[BayesianLinearRegression]] / [[PosteriorPredictiveDistribution]] — noise as the aleatoric variance term.
- [[Regression]] — the task this noise model underpins.
