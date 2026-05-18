---
title: "Gaussian Distribution"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-book, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Gaussian Distribution

The univariate Gaussian (or normal) density:

$$p(x\mid\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).$$

The multivariate Gaussian on $\mathbb{R}^D$:

$$p(\mathbf{x}\mid\boldsymbol\mu,\boldsymbol\Sigma) = (2\pi)^{-D/2}\,|\boldsymbol\Sigma|^{-1/2}\,\exp\!\left(-\tfrac{1}{2}(\mathbf{x}-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu)\right).$$

Parameterized by mean $\boldsymbol\mu\in\mathbb{R}^D$ and symmetric positive-definite covariance $\boldsymbol\Sigma\in\mathbb{R}^{D\times D}$ ([[mml-book]] §6.5).

## Why Gaussians are everywhere in ML

- **Closure under marginalization, conditioning, and linear transformations**: every operation a probabilistic ML algorithm needs on a Gaussian yields another Gaussian in closed form. This is the property that makes Bayesian linear regression, Kalman filters, and Gaussian processes analytically tractable.
- **Conjugate to itself for the mean**: Gaussian likelihood × Gaussian prior on the mean = Gaussian posterior (§6.6) — see [[ConjugatePrior]].
- **Maximum-entropy distribution** given a fixed mean and variance: the "least committal" choice under those constraints.
- **Central limit theorem**: sums of independent RVs converge to a Gaussian — the empirical justification for using it as a noise model.

## Standard ML uses

- **[[LinearRegression]]** ([[mml-book]] Ch 9): the noise model $\epsilon\sim\mathcal{N}(0,\sigma^2)$ makes least-squares = MLE.
- **[[GaussianMixtureModel|GMM]]** (Ch 11): mixtures of Gaussians give multimodal density estimates.
- **[[BayesianLinearRegression]]** (§9.3): Gaussian prior + Gaussian likelihood ⇒ closed-form Gaussian posterior.
- **[[VariationalAutoencoder|VAE]]** prior + posterior ansatz.
- **Score matching / diffusion models**: Gaussian noise schedule with closed-form perturbation kernels.

## Sampling and density evaluation

- **Sampling**: factor $\boldsymbol\Sigma = \mathbf{L}\mathbf{L}^\top$ via [[CholeskyDecomposition]]; sample $\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$; return $\boldsymbol\mu + \mathbf{L}\mathbf{z}$.
- **Log-density** is quadratic in $\mathbf{x}$ ⇒ minimizing NLL = solving a least-squares / quadratic problem.

## Connections

- [[mml-book]] — §6.5 canonical reference.
- [[ConjugatePrior]] — Gaussians are self-conjugate.
- [[ExponentialFamily]] — Gaussian is the prototypical exponential-family member.
- [[CholeskyDecomposition]] — sampling primitive.
- [[GaussianMixtureModel]] — multimodal extension.
- [[BayesianLinearRegression]] — Gaussian-conjugacy application.
