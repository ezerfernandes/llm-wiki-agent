---
title: "Bayesian Linear Regression"
type: concept
tags: [regression, bayesian-inference, foundational]
sources: [mml-book, d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Bayesian Linear Regression

The full-Bayesian counterpart of MLE [[LinearRegression]] ([[mml-book]] §9.3): instead of finding a single $\boldsymbol\theta_{\text{ML}}$, place a prior $p(\boldsymbol\theta) = \mathcal{N}(\mathbf{m}_0, \mathbf{S}_0)$, observe data $\mathcal{D}$, and compute the **posterior** $p(\boldsymbol\theta\mid\mathcal{D})$ in closed form.

## Closed-form posterior

For likelihood $p(y\mid\mathbf{x},\boldsymbol\theta) = \mathcal{N}(y\mid\boldsymbol\phi(\mathbf{x})^\top\boldsymbol\theta, \sigma^2)$ and Gaussian prior $p(\boldsymbol\theta) = \mathcal{N}(\mathbf{m}_0, \mathbf{S}_0)$:

$$p(\boldsymbol\theta\mid\mathcal{D}) = \mathcal{N}(\boldsymbol\theta\mid\mathbf{m}_N, \mathbf{S}_N)$$

with

$$\mathbf{S}_N = \left(\mathbf{S}_0^{-1} + \tfrac{1}{\sigma^2}\boldsymbol\Phi^\top\boldsymbol\Phi\right)^{-1}, \quad \mathbf{m}_N = \mathbf{S}_N\left(\mathbf{S}_0^{-1}\mathbf{m}_0 + \tfrac{1}{\sigma^2}\boldsymbol\Phi^\top\mathbf{y}\right).$$

The closed form exists because the Gaussian likelihood is **conjugate** to the Gaussian prior ([[ConjugatePrior]] / [[ExponentialFamily]]).

## Posterior predictive

For a new input $\mathbf{x}_*$, marginalize over $\boldsymbol\theta$:

$$p(y_*\mid\mathbf{x}_*, \mathcal{D}) = \int \mathcal{N}(y_*\mid\boldsymbol\phi(\mathbf{x}_*)^\top\boldsymbol\theta, \sigma^2)\,\mathcal{N}(\boldsymbol\theta\mid\mathbf{m}_N, \mathbf{S}_N)\,d\boldsymbol\theta = \mathcal{N}(y_*\mid\boldsymbol\phi_*^\top\mathbf{m}_N,\,\sigma^2 + \boldsymbol\phi_*^\top\mathbf{S}_N\boldsymbol\phi_*).$$

The predictive variance has two parts: **observation noise** $\sigma^2$ + **epistemic uncertainty** $\boldsymbol\phi_*^\top\mathbf{S}_N\boldsymbol\phi_*$. As the training set grows, $\mathbf{S}_N\to\mathbf{0}$ and the epistemic term vanishes — the model becomes confident about $\boldsymbol\theta$.

## What Bayesian linear regression buys you over MLE

- **Calibrated predictive uncertainty**: not just $\hat y$, but $\hat y \pm \sigma_*$ at every test point — and the uncertainty *grows* in regions far from training data.
- **Automatic regularization**: the prior plays the same role as $\ell_2$ weight decay (recovers ridge regression as the MAP estimate).
- **Marginal likelihood for model selection**: $p(\mathcal{D}) = \int p(\mathcal{D}\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta$ gives a principled way to compare models (e.g., polynomial-degree selection) without held-out validation data.

## Connection to Gaussian processes

Bayesian linear regression with infinite features $\boldsymbol\phi(\mathbf{x})$ and a Gaussian prior on $\boldsymbol\theta$ recovers a **[[GaussianProcess|Gaussian process]]** — the kernel $k(\mathbf{x},\mathbf{x}') = \boldsymbol\phi(\mathbf{x})^\top\mathbf{S}_0\boldsymbol\phi(\mathbf{x}')$ encodes the prior over functions. This is the bridge from linear regression to non-parametric Bayesian regression, and the weight-space view that [[d2l-gaussian-processes]] lifts to function space. The epistemic / aleatoric variance decomposition of the predictive distribution generalizes directly: $\textrm{Var}[y_*]=\sigma^2$ ([[AleatoricUncertainty|aleatoric]]) $+\,\boldsymbol\phi_*^\top\mathbf{S}_N\boldsymbol\phi_*$ ([[EpistemicUncertainty|epistemic]]).

## Connections

- [[mml-book]] — §9.3 canonical reference.
- [[LinearRegression]] — the MLE counterpart.
- [[MAPEstimation]] — point-estimate halfway-house between MLE and full Bayesian.
- [[GaussianDistribution]] — distribution closure under conjugacy.
- [[ConjugatePrior]] — why the posterior is closed-form.
- [[RidgeRegression]] — emerges as MAP with a Gaussian prior.
- [[GaussianProcess]] — the function-space generalization to infinite-feature priors ([[d2l-gaussian-processes]]).
- [[MarginalLikelihood]] — the model-evidence objective shared with GP regression.
- [[KernelFunction]] / [[RBFKernel]] — implicit features when the basis $\phi$ is taken to be infinite.
