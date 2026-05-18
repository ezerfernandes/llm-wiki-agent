---
title: "Aleatoric Uncertainty"
type: concept
tags: [uncertainty, bayesian, foundational]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Aleatoric Uncertainty

The **irreducible** component of predictive uncertainty — observation noise inherent to the data-generating process. Cannot be reduced by collecting more data, in contrast to [[EpistemicUncertainty|epistemic uncertainty]] which vanishes in the data-rich limit.

## In Gaussian-process regression

For the additive-noise model $y(x)=f(x)+\epsilon(x)$ with $\epsilon\sim\mathcal{N}(0,\sigma^2)$, the aleatoric component is exactly $\sigma^2$ — added to the latent-function variance to form an observation-space credible set:

$$\textrm{Var}[y_*\mid\mathbf{y}, x_*] = \underbrace{S_*}_{\text{epistemic}} + \underbrace{\sigma^2}_{\text{aleatoric}}.$$

The noise standard deviation $\sigma$ is itself a [[Hyperparameter|hyperparameter]] of the GP, learned by maximizing the [[MarginalLikelihood]].

## Operational distinction from epistemic

[[d2l-gaussian-processes]] gp-inference (Wilson):

> "There are two sources of uncertainty, *epistemic* uncertainty, representing *reducible* uncertainty, and *aleatoric* or *irreducible* uncertainty. The epistemic uncertainty here represents uncertainty about the true values of the noise free function. … The aleatoric uncertainty in this instance is the observation noise, since the data are given to us with this noise, and it cannot be reduced."

Aleatoric uncertainty:

- Stays constant as data grows.
- Lives on a different scale (variance, not standard deviation — *"living on a completely different scale, and is much less interpretable"*).
- Is a property of the measurement instrument / generative process, not the model.

## Common confusions

D2L flags that the field routinely conflates:

- Noise variance vs noise standard deviation,
- Standard deviations vs standard errors,
- Confidence intervals vs credible sets,
- Epistemic vs aleatoric error bars.

The discipline of being explicit about which type of uncertainty an error bar represents is non-trivial — and is one of the few places GPs offer cleaner semantics than typical deep-learning workflows.

## Connections

- [[d2l-gaussian-processes]] — D2L's canonical exposition of the epistemic / aleatoric split.
- [[EpistemicUncertainty]] — the reducible counterpart.
- [[GaussianProcess]] — the model that operationalizes the decomposition cleanly.
- [[BayesianLinearRegression]] — same decomposition at the weight-space level.
- [[MarginalLikelihood]] — the objective that learns $\sigma^2$ alongside the kernel hyperparameters.
