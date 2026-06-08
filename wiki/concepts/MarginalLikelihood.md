---
title: "Marginal Likelihood"
type: concept
tags: [bayesian, model-selection, gaussian-processes]
sources: [d2l-gaussian-processes, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
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

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] uses the marginal likelihood as the **central quantity for [[ModelSelection|model selection]]**. §8.4.1 identifies it as one of the three things the joint $p(\mathbf{x},\boldsymbol\theta)$ encapsulates: $p(\mathbf{x})$ "can be computed by taking the joint distribution and integrating out the parameters (sum rule)." §8.6.2 frames model selection as hierarchical inference: the **model evidence / marginal likelihood** of model $M_k$ is

$$p(\mathcal{D}\,|\,M_k)=\int p(\mathcal{D}\,|\,\boldsymbol\theta_k)\,p(\boldsymbol\theta_k\,|\,M_k)\,d\boldsymbol\theta_k\qquad(\text{Eq. 8.44}),$$

and under a uniform model prior the MAP model is the one maximizing this evidence (Eq. 8.45). The chapter's **Remark (likelihood vs marginal likelihood)** (§8.6.2, p. 286) is the crux: *"While the likelihood is prone to overfitting, the marginal likelihood is typically not, as the model parameters have been marginalized out (i.e., we no longer have to fit the parameters). Furthermore, the marginal likelihood automatically embodies a trade-off between model complexity and data fit ([[OccamsRazor|Occam's razor]])"* — the same data-fit + complexity-penalty decomposition exhibited above for the GP case (Fig. 8.14). It is the numerator/denominator of the [[BayesFactor|Bayes factor]] (§8.6.3) and — per the Jeffreys–Lindley paradox — a diffuse prior makes a complex model's evidence very small. Computing it generally requires an intractable integral (numerical integration / Monte Carlo), with a closed form only for [[ConjugatePrior|conjugate priors]] (done for [[BayesianLinearRegression|linear regression]] in Ch 9).

## From [[mml-ch09-linear-regression|MML Ch 9]] (the closed-form case)

[[mml-ch09-linear-regression|MML Ch 9]] §9.3.5 is the **one model where the marginal likelihood is computed in closed form** (the conjugate-Gaussian special case Ch 8 promised). For the generative process $\boldsymbol\theta\sim\mathcal{N}(\mathbf{m}_0,\mathbf{S}_0)$, $y_n\mid\mathbf{x}_n,\boldsymbol\theta\sim\mathcal{N}(\mathbf{x}_n^\top\boldsymbol\theta,\sigma^2)$, the evidence is itself a Gaussian in $\mathbf{y}$ (product of Gaussians + linear transform are Gaussian, §6.5.2):
$$p(\mathcal{Y}\mid\mathcal{X})=\int p(\mathcal{Y}\mid\mathcal{X},\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta=\mathcal{N}\big(\mathbf{y}\,\big|\,\mathbf{X}\mathbf{m}_0,\ \mathbf{X}\mathbf{S}_0\mathbf{X}^\top+\sigma^2\mathbf{I}\big)\quad(\text{Eqs. 9.61–9.64}),$$
with mean $\mathbf{X}\mathbf{m}_0$ (Eq. 9.62) and covariance $\mathbf{X}\mathbf{S}_0\mathbf{X}^\top+\sigma^2\mathbf{I}$ (Eq. 9.63). A Remark (p. 309) sharply distinguishes it from the [[PosteriorPredictiveDistribution|posterior predictive]]: both are likelihood expectations, but the **marginal likelihood predicts the *training* targets $\mathbf{y}$ averaged under the *prior*** ($\mathbb{E}_{\boldsymbol\theta}[p(\mathcal{Y}\mid\mathcal{X},\boldsymbol\theta)]$), whereas the predictive predicts *test* targets averaged under the *posterior*. This is the finite-feature analogue of the GP marginal-likelihood objective above (its covariance $\mathbf{X}\mathbf{S}_0\mathbf{X}^\top+\sigma^2\mathbf{I}$ is exactly a linear/dot-product kernel Gram matrix plus noise).

## Connections

- [[mml-ch09-linear-regression]] — §9.3.5 closed-form marginal likelihood for Bayesian linear regression (Eq. 9.64).
- [[mml-ch08-when-models-meet-data]] — §8.4.1 (joint), §8.6.2 (model evidence + Occam's razor), §8.6.3 (Bayes factor).

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
