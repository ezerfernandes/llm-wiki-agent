---
title: "Likelihood"
type: concept
tags: [probability, bayesian, estimation, statistics]
sources: [mml-ch06-probability-and-distributions, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Likelihood

The **likelihood** $p(\mathbf{x}\mid\boldsymbol\theta)$ (or, in supervised learning, $p(\mathbf{y}\mid\mathbf{x},\boldsymbol\theta)$) is the probability the model assigns to the observed data as a function of the parameters $\boldsymbol\theta$. It is the bridge between a probabilistic model and the data: the model specifies *how data is generated given parameters*, and the likelihood reads that generative density backwards — fixing the data, varying $\boldsymbol\theta$.

The central conceptual trap: **the likelihood is not a probability distribution over $\boldsymbol\theta$.** As a function of $\boldsymbol\theta$ it does not integrate to 1. It is a distribution over $\mathbf{x}$ for each fixed $\boldsymbol\theta$, viewed as a function of $\boldsymbol\theta$ for fixed $\mathbf{x}$.

## Role in Bayes' theorem

In [[BayesTheorem|Bayes' theorem]] the likelihood is the term that updates the [[Prior|prior]] into the [[Posterior|posterior]]:

$$\underbrace{p(\boldsymbol\theta\mid\mathbf{x})}_{\text{posterior}} = \frac{\overbrace{p(\mathbf{x}\mid\boldsymbol\theta)}^{\text{likelihood}}\;\overbrace{p(\boldsymbol\theta)}^{\text{prior}}}{\underbrace{p(\mathbf{x})}_{\text{evidence}}}.$$

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-ch06-probability-and-distributions|MML Ch 6]] §6.3 introduces the likelihood as the term $p(x\mid y)$ in the [[ProductRule|product rule]] / [[BayesTheorem|Bayes' theorem]] decomposition, and §6.3 explicitly warns against reading it as a density in the conditioned variable. The book's framing (carried into Ch 8) is that the likelihood is the *"probability of the data"* under the model — a **measurement / observation model** connecting latent parameters to observable data.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.3.1 makes the likelihood the object that [[MaximumLikelihoodEstimation|maximum likelihood estimation]] optimizes. For [[IID|i.i.d.]] data the likelihood **factorizes** over examples,

$$p(\mathcal{Y}\mid\mathcal{X},\boldsymbol\theta)=\prod_{n=1}^{N}p(y_n\mid\mathbf{x}_n,\boldsymbol\theta),$$

which is why the [[NegativeLogLikelihood|negative log-likelihood]] turns a product into a numerically stable sum (§8.3.1). §8.4 contrasts the likelihood-only view (frequentist, prone to overfitting) with the fully Bayesian view that also commits to a [[Prior|prior]]; the [[MarginalLikelihood|marginal likelihood]] (§8.6.2) is the likelihood with the parameters integrated out.

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.2.1 instantiates the likelihood as a **Gaussian noise model** $p(y\mid\mathbf{x},\boldsymbol\theta)=\mathcal{N}(y\mid\mathbf{x}^\top\boldsymbol\theta,\sigma^2)$, from which maximizing the (log-)likelihood is shown to be exactly [[LeastSquares|least-squares]] regression — the canonical worked example of likelihood = loss up to a constant.

## Connections

- [[BayesTheorem]] — the likelihood is the data-fit term that reweights the prior.
- [[MaximumLikelihoodEstimation]] — point estimate $\boldsymbol\theta_{\mathrm{ML}}=\arg\max_{\boldsymbol\theta}p(\mathcal{D}\mid\boldsymbol\theta)$.
- [[MAPEstimation]] — adds a [[Prior|prior]]: $\arg\max p(\mathcal{D}\mid\boldsymbol\theta)p(\boldsymbol\theta)$.
- [[NegativeLogLikelihood]] — the log-domain form actually optimized.
- [[Prior]] / [[Posterior]] / [[MarginalLikelihood]] — the other terms in Bayes' theorem.
- [[IID]] — the assumption that lets the likelihood factorize.
- [[LeastSquares]] — Gaussian-likelihood instantiation in regression.
