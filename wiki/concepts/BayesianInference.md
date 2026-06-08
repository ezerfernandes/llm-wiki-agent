---
title: "Bayesian Inference"
type: concept
tags: [bayesian-inference, statistics, foundational, parameter-estimation]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Bayesian Inference

The approach to learning that computes the **full [[Posterior|posterior]] distribution** over parameters and then propagates parameter uncertainty into predictions — rather than committing to a single point estimate ([[mml-book]] §8.4.2). For a dataset $\mathcal{X}$, a parameter [[Prior|prior]] $p(\boldsymbol\theta)$, and a [[Likelihood|likelihood]] $p(\mathcal{X}\,|\,\boldsymbol\theta)$, the posterior is obtained by Bayes' theorem (Eq. 8.22):

$$p(\boldsymbol\theta\,|\,\mathcal{X})=\frac{p(\mathcal{X}\,|\,\boldsymbol\theta)\,p(\boldsymbol\theta)}{p(\mathcal{X})},\qquad p(\mathcal{X})=\int p(\mathcal{X}\,|\,\boldsymbol\theta)\,p(\boldsymbol\theta)\,d\boldsymbol\theta.$$

*"The key idea is to exploit Bayes' theorem to invert the relationship between the parameters $\boldsymbol\theta$ and the data $\mathcal{X}$"* ([[mml-book]] §8.4.2, p. 274).

## Prediction = averaging over all plausible parameters

Predictions integrate the likelihood against the posterior (Eq. 8.23):

$$p(\mathbf{x})=\int p(\mathbf{x}\,|\,\boldsymbol\theta)\,p(\boldsymbol\theta)\,d\boldsymbol\theta=\mathbb{E}_{\boldsymbol\theta}\big[p(\mathbf{x}\,|\,\boldsymbol\theta)\big].$$

The prediction **no longer depends on $\boldsymbol\theta$** (marginalized/integrated out); it is an average over all plausible parameter values, weighted by the posterior's plausibility.

## Optimization vs integration

The defining contrast with point estimation ([[MaximumLikelihoodEstimation|MLE]]/[[MAPEstimation|MAP]]) is computational:

| | Point estimate (MLE/MAP) | Bayesian inference |
|---|---|---|
| Output | single $\boldsymbol\theta^*$ | posterior $p(\boldsymbol\theta\mid\mathcal{X})$ |
| Core problem | **optimization** | **integration** |
| Prediction | $p(\mathbf{x}\mid\boldsymbol\theta^*)$, straightforward | another integral (Eq. 8.23) |

Bayesian inference principled-ly incorporates prior knowledge, side information, and structural knowledge, and propagates parameter uncertainty into predictions — valuable for risk assessment and exploration in data-efficient learning.

## The intractability problem

Without a [[ConjugatePrior|conjugate prior]] (§6.6.1), the integrals in Eqs. 8.22–8.23 are analytically intractable. The standard work-arounds:

- **Stochastic approximations** — Markov chain Monte Carlo (MCMC).
- **Deterministic approximations** — Laplace approximation, **variational inference**, **expectation propagation**.

## Connection to abduction

The posterior is a formal model of [[Abduction|abduction]]: the prior encodes which explanations are *a priori* plausible, the likelihood encodes how well an explanation accounts for the data, and the product picks the best trade-off.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.4.2 canonical reference (Eqs. 8.22–8.23).
- [[mml-book]] — §8.4.
- [[BayesTheorem]] — the inversion mechanism.
- [[Posterior]] / [[Prior]] / [[Likelihood]] / [[MarginalLikelihood]] — the four pieces of the joint.
- [[MaximumLikelihoodEstimation]] / [[MAPEstimation]] — the point-estimate alternatives (optimization, not integration).
- [[ConjugatePrior]] — when the integrals are closed-form.
- [[BayesianLinearRegression]] — the worked tractable example (Ch 9).
- [[LatentVariable]] — Bayesian inference in latent-variable models.
- [[Abduction]] — the posterior as inference-to-the-best-explanation.
