---
title: "Marginal Likelihood"
type: concept
tags: [bayesian, model-selection, gaussian-processes]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Marginal Likelihood

The probability of the observed data $\mathbf{y}$ under a model with hyperparameters $\theta$, **marginalizing over** all model parameters (or latent functions):

$$p(\mathbf{y}\mid\theta, X) = \int p(\mathbf{y}\mid f, X)\, p(f\mid X, \theta)\, df.$$

Also called the **model evidence** or **type-II likelihood**. The standard Bayesian objective for [[ModelSelection|model selection]] and hyperparameter learning ([[MacKay2003|MacKay]] Ch 28; [[d2l-gaussian-processes]] gp-inference).

## GP regression case

For a [[GaussianProcess|GP]] with kernel $k_\theta$ and Gaussian noise variance $\sigma^2$, $\mathbf{y}\sim\mathcal{N}(\boldsymbol\mu, K_\theta(X,X)+\sigma^2 I)$, so:

$$\log p(\mathbf{y}\mid\theta, X) = \underbrace{-\tfrac{1}{2}\mathbf{y}^\top[K_\theta+\sigma^2 I]^{-1}\mathbf{y}}_{\text{data fit}}\;\underbrace{-\tfrac{1}{2}\log|K_\theta+\sigma^2 I|}_{\text{model complexity}}\;\underbrace{-\tfrac{n}{2}\log 2\pi}_{\text{constant}}.$$

The three terms decompose into:

- **Data fit** — quadratic in $\mathbf{y}$; rewards $\theta$ that explains the data well.
- **Complexity penalty** — $\log\det$ of the kernel matrix; *automatically* penalizes flexible models that don't need their flexibility.
- **Normalizing constant.**

## Occam's razor, automatically

The complexity term implements [[OccamsRazor|Occam's razor]] without any held-out validation: maximizing the marginal likelihood selects $\theta$ that produces the **simplest model still consistent with the data**. *"The marginal likelihood compartmentalizes into model fit and model complexity terms, and automatically encodes a notion of Occam's razor for learning hyperparameters."* ([[d2l-gaussian-processes]] gp-inference)

[[AndrewGordonWilson|Wilson]] notes the marginal likelihood is *"much better at learning length-scale hyperparameters than conventional approaches in spatial statistics, which involve fitting empirical autocorrelation functions (covariograms)."*

## Local optima

The marginal likelihood is **not convex** in $\theta$. Different local optima encode interpretably different explanations:

- *Large $\ell$ + large $\sigma^2$* — slowly varying function with high observation noise.
- *Small $\ell$ + small $\sigma^2$* — rapidly varying function with little observation noise.

Both can be plausible for the same data; the choice between them is a **prior commitment** that the marginal likelihood alone cannot resolve.

## Practical optimization

- The marginal likelihood **does not factorize** over data instances — so [[MinibatchSGD|mini-batch SGD]] *cannot* be used. Full-batch [[Adam]] or L-BFGS are the standard optimizers ([[d2l-gaussian-processes]] gp-inference and [[GPyTorch]]).
- *"Unlike in standard deep learning, doing a good job of optimizing the marginal likelihood corresponds strongly with good generalization, which often inclines us towards powerful optimizers like L-BFGS, assuming they are not prohibitively expensive."* — D2L

## Connections

- [[d2l-gaussian-processes]] — canonical D2L reference; the GP regression objective.
- [[GaussianProcess]] — the model whose hyperparameters this objective trains.
- [[KernelFunction]] / [[RBFKernel]] / [[MaternKernel]] — what parameterizes $\theta$.
- [[BayesianLinearRegression]] — finite-feature special case of the same machinery.
- [[ModelSelection]] — broader use of marginal likelihood across Bayesian model families.
- [[OccamsRazor]] — encoded automatically via the log-det complexity term.
- [[Adam]] — the canonical full-batch optimizer in [[GPyTorch]].
- [[GPyTorch]] — `gpytorch.mlls.ExactMarginalLogLikelihood`.
