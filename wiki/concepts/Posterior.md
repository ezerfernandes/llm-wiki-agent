---
title: "Posterior"
type: concept
tags: [probability, bayesian, estimation, inference]
sources: [mml-ch06-probability-and-distributions, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Posterior

The **posterior** $p(\boldsymbol\theta\mid\mathbf{x})$ is the probability distribution over parameters (or latent variables) *after* observing data — the [[Prior|prior]] updated by the evidence in the data through [[BayesTheorem|Bayes' theorem]]:

$$p(\boldsymbol\theta\mid\mathbf{x})=\frac{p(\mathbf{x}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)}{p(\mathbf{x})},\qquad p(\mathbf{x})=\int p(\mathbf{x}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)\,d\boldsymbol\theta.$$

The posterior is the central object of Bayesian inference: it is a *full distribution*, not a point — capturing both the best-guess parameters and the remaining uncertainty about them. A point summary of the posterior (its mode) is the [[MAPEstimation|MAP estimate]].

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-ch06-probability-and-distributions|MML Ch 6]] §6.3 derives the posterior as the output of [[BayesTheorem|Bayes' theorem]] — *"the posterior is what we are interested in because it ... expresses exactly what we know about $\boldsymbol\theta$ after observing $\mathbf{x}$."* The denominator $p(\mathbf{x})$ (the [[MarginalLikelihood|evidence]]) is a normalizing constant obtained by the [[SumRule|sum rule]]. Where the [[Prior|prior]] is [[ConjugatePrior|conjugate]] to the [[Likelihood|likelihood]] (§6.6), the posterior is available in closed form and stays in the same family.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.4 frames Bayesian inference as **computing the posterior** rather than a point estimate: *"Bayesian inference ... is about finding the posterior distribution over the parameters."* The chapter stresses that maintaining the whole posterior (vs. collapsing to [[MAPEstimation|MAP]] or [[MaximumLikelihoodEstimation|MLE]]) is what propagates parameter uncertainty into predictions; §8.4 introduces the **[[PosteriorPredictiveDistribution|posterior predictive distribution]]** $p(\mathbf{x}^*\mid\mathcal{D})=\int p(\mathbf{x}^*\mid\boldsymbol\theta)p(\boldsymbol\theta\mid\mathcal{D})\,d\boldsymbol\theta$ as the posterior averaged over for prediction. §8.5's [[DirectedGraphicalModel|directed graphical models]] make the conditional structure of these posteriors explicit.

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.3.2 computes the **parameter posterior** in closed form for [[BayesianLinearRegression|Bayesian linear regression]] (Gaussian prior × Gaussian likelihood → Gaussian posterior, the conjugate case), giving posterior mean and covariance in terms of the [[DesignMatrix|design matrix]]; §9.3.3 then pushes it through to the [[PosteriorPredictiveDistribution|posterior predictive]], the practical payoff of keeping the full posterior over the [[MAPEstimation|MAP]] point estimate.

## Connections

- [[BayesTheorem]] — the rule that produces the posterior.
- [[Prior]] — the belief before data; [[Likelihood]] — the data-fit update.
- [[MarginalLikelihood]] — the normalizing evidence in the denominator.
- [[MAPEstimation]] — the mode of the posterior (a point summary).
- [[PosteriorPredictiveDistribution]] — predictions averaged over the posterior.
- [[BayesianInference]] — inference centered on the posterior.
- [[ConjugatePrior]] — when the posterior is closed-form.
- [[BayesianLinearRegression]] — Gaussian closed-form posterior over weights.
