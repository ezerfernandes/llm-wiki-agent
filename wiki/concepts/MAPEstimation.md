---
title: "MAP Estimation"
type: concept
tags: [bayesian-inference, foundational, parameter-estimation]
sources: [mml-book]
last_updated: 2026-05-16
---

# Maximum A Posteriori (MAP) Estimation

A point estimate of the parameters $\boldsymbol\theta$ that maximizes the **posterior** $p(\boldsymbol\theta\mid\mathcal{D})$ instead of the likelihood $p(\mathcal{D}\mid\boldsymbol\theta)$ ([[mml-book]] §8.3):

$$\boldsymbol\theta_{\text{MAP}} = \arg\max_{\boldsymbol\theta}\,p(\boldsymbol\theta\mid\mathcal{D}) = \arg\max_{\boldsymbol\theta}\,[\log p(\mathcal{D}\mid\boldsymbol\theta) + \log p(\boldsymbol\theta)].$$

## MAP vs MLE

MAP differs from [[MaximumLikelihoodEstimation|MLE]] by the additional $\log p(\boldsymbol\theta)$ term — the log-prior. As prior beliefs become more diffuse (i.e., approach uniform), MAP collapses to MLE.

## MAP ≡ regularized MLE

The most useful reading of MAP for ML practitioners:

| Prior on $\boldsymbol\theta$ | MAP recovers |
|---|---|
| Gaussian $\mathcal{N}(\mathbf{0}, \sigma_0^2\mathbf{I})$ | **Ridge regression** ($\ell_2$ weight decay) |
| Laplace prior | **Lasso** ($\ell_1$ sparsity) |
| Uniform / improper flat | MLE |

The "regularization strength" hyperparameter $\lambda$ is the variance of the prior in disguise (with $\lambda\propto 1/\sigma_0^2$).

## MAP vs full Bayesian inference

MAP is a **point estimate** — it picks a single $\boldsymbol\theta$ and discards the rest of the posterior. Full Bayesian inference instead retains $p(\boldsymbol\theta\mid\mathcal{D})$ and integrates it into predictions:

$$p(\mathbf{x}_*\mid\mathcal{D}) = \int p(\mathbf{x}_*\mid\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathcal{D})\,d\boldsymbol\theta.$$

MAP underestimates predictive uncertainty because it ignores parameter uncertainty. [[BayesianLinearRegression]] ([[mml-book]] §9.3) is the worked example of going beyond MAP to the full integral — analytically tractable when priors are conjugate.

## Connections

- [[mml-book]] — §8.3 canonical reference.
- [[MaximumLikelihoodEstimation]] — MAP collapses to this under uniform prior.
- [[BayesianLinearRegression]] — full-Bayesian alternative.
- [[ConjugatePrior]] — when the full Bayesian integral has a closed form.
- [[RidgeRegression]] — MAP with Gaussian prior.
- [[EmpiricalRiskMinimization]] — MAP can be cast as regularized ERM.
