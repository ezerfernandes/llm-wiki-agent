---
title: "Fisher Information"
type: concept
tags: [statistics, foundational, mle]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Fisher Information

The variance of the score function — a measure of how much information an observable random variable $X$ carries about an unknown parameter $\theta$ of the distribution that generates it ([[d2l-appendix-mathematics]] §maximum-likelihood):

$$\mathcal{I}(\theta) = \mathbb{E}_{x\sim p(\cdot\mid\theta)}\!\left[\!\left(\frac{\partial}{\partial\theta}\log p(x\mid\theta)\right)^{\!2}\right] = -\mathbb{E}\!\left[\frac{\partial^2}{\partial\theta^2}\log p(x\mid\theta)\right].$$

For vector-valued $\boldsymbol\theta\in\mathbb{R}^d$, $\mathcal{I}(\boldsymbol\theta)\in\mathbb{R}^{d\times d}$ is the Fisher information *matrix* — the (negative) expected Hessian of the log-likelihood.

## Asymptotic theory of MLE

[[d2l-appendix-mathematics]] §maximum-likelihood establishes the three classical guarantees of [[MaximumLikelihoodEstimation|MLE]] under regularity conditions:

1. **Consistency**: $\hat\theta_n \to \theta^*$ in probability.
2. **Asymptotic normality**: $\sqrt n(\hat\theta_n - \theta^*) \xrightarrow{d} \mathcal{N}\!\big(0,\,\mathcal{I}^{-1}(\theta^*)\big)$.
3. **Efficiency**: the MLE achieves the [[CramerRaoBound|Cramér-Rao lower bound]] asymptotically — no unbiased estimator has smaller variance.

This is *why* MLE is the default estimator across classical statistics, modern ML, and LLM pretraining: among regular estimators, no one beats it asymptotically.

## Cramér-Rao lower bound

For any **unbiased** estimator $\hat\theta_n$ of a scalar $\theta$:

$$\text{Var}(\hat\theta_n) \;\geq\; \frac{1}{n\,\mathcal{I}(\theta)}.$$

The Fisher information sets a hard *lower bound* on estimator variance — you cannot estimate $\theta$ better than this from $n$ samples. The MLE achieves it asymptotically.

## ML uses

- **[[LaplaceApproximation|Laplace approximation]]** to a Bayesian posterior: $p(\theta\mid\mathcal{D})\approx \mathcal{N}(\hat\theta_{\text{MAP}}, \mathcal{I}^{-1})$ — the inverse Fisher information is the natural curvature-derived posterior covariance.
- **[[NaturalGradient|Natural gradient descent]]** (Amari 1998): replace the parameter-space gradient with $\mathcal{I}^{-1}\nabla L$ — descend in the *Riemannian* geometry induced by the model, not in raw parameter space. Makes optimization scale-invariant to reparametrization. Foundation of [[KFAC]] and adjacent second-order methods.
- **Information-geometry views of model training**: $\mathcal{I}$ defines the Riemannian metric on parameter manifolds.
- **[[ElasticWeightConsolidation|EWC]]** (continual learning): penalize parameter changes by Fisher curvature — preserve weights important to prior tasks.
- **Active learning / experimental design**: maximize Fisher information of the next sample to minimize estimator variance.
- **Confidence intervals for MLE parameters**: invert the observed Fisher information matrix at the MLE for a Gaussian approximation.

## Score function

The first derivative $s(\theta;x) = \partial_\theta \log p(x\mid\theta)$ is the **score**. Properties: $\mathbb{E}[s] = 0$ and $\text{Var}(s) = \mathcal{I}(\theta)$ — Fisher information is literally the variance of the score.

## Connections

- [[d2l-appendix-mathematics]] — §maximum-likelihood canonical reference.
- [[MaximumLikelihoodEstimation]] — what Fisher information bounds.
- [[CramerRaoBound]] — the lower bound on estimator variance.
- [[Hessian]] — Fisher = $-\mathbb{E}[\text{Hessian of log-likelihood}]$.
- [[LaplaceApproximation]] — Gaussian-posterior approximation that uses $\mathcal{I}^{-1}$.
- [[NaturalGradient]] / [[KFAC]] — preconditioning by the Fisher information matrix.
- [[ElasticWeightConsolidation]] — continual-learning regularizer based on Fisher.
- [[Statistics]] / [[InformationTheory]] — neighboring disciplines (note: Fisher information $\neq$ Shannon entropy / mutual information).
