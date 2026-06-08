---
title: "Prior"
type: concept
tags: [probability, bayesian, estimation, regularization]
sources: [mml-ch06-probability-and-distributions, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Prior

The **prior** $p(\boldsymbol\theta)$ is the probability distribution over a model's parameters (or latent variables) *before* any data is observed. It encodes assumptions, domain knowledge, or a deliberate inductive bias about which parameter values are plausible. Combined with the [[Likelihood|likelihood]] via [[BayesTheorem|Bayes' theorem]], it yields the [[Posterior|posterior]].

$$p(\boldsymbol\theta\mid\mathbf{x})=\frac{p(\mathbf{x}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)}{p(\mathbf{x})}.$$

## The prior as a regularizer

A key unifying idea: choosing a prior is mathematically equivalent to adding a regularization term. Maximizing the posterior ([[MAPEstimation|MAP estimation]]) equals maximizing $\log p(\mathbf{x}\mid\boldsymbol\theta)+\log p(\boldsymbol\theta)$, where the $\log p(\boldsymbol\theta)$ term penalizes implausible parameters. A zero-mean Gaussian prior gives $L_2$ / [[RidgeRegression|ridge]] regularization; a Laplace prior gives $L_1$.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-ch06-probability-and-distributions|MML Ch 6]] §6.6 develops priors through **[[ConjugatePrior|conjugacy]]**: a prior is *conjugate* to a likelihood when the resulting posterior has the same functional form as the prior (Beta–Binomial, Gaussian–Gaussian, etc.), making Bayesian updating closed-form. The [[ExponentialFamily|exponential family]] (§6.6) is exactly the class of likelihoods that admit conjugate priors with finite-dimensional [[SufficientStatistics|sufficient statistics]].

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.3.2 introduces the prior as the ingredient that turns [[MaximumLikelihoodEstimation|MLE]] into [[MAPEstimation|MAP estimation]] — *"placing a prior $p(\boldsymbol\theta)$ on the parameters ... shifts the estimate away from the maximum-likelihood solution toward values the prior considers plausible,"* combatting overfitting. §8.4 takes the further step to **full Bayesian inference**, where instead of a point estimate one keeps the entire [[Posterior|posterior]] and integrates over it; the prior then propagates uncertainty into the [[MarginalLikelihood|marginal likelihood]] (§8.6.2) used for [[ModelSelection|model selection]].

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.3.1 places a Gaussian parameter prior $p(\boldsymbol\theta)=\mathcal{N}(\mathbf{m}_0,\mathbf{S}_0)$ on the regression weights, yielding [[BayesianLinearRegression|Bayesian linear regression]]; §9.2.2 shows the MAP special case is exactly **regularized least squares**, with the prior precision setting the ridge penalty $\lambda=\sigma^2/b^2$.

## Connections

- [[BayesTheorem]] — prior × likelihood ∝ posterior.
- [[Posterior]] — the updated belief after seeing data.
- [[Likelihood]] / [[MarginalLikelihood]] — the data-dependent terms.
- [[ConjugatePrior]] — priors that keep Bayesian updates closed-form.
- [[MAPEstimation]] — point estimate that incorporates the prior.
- [[Regularization]] — the prior is a regularizer in disguise.
- [[BayesianLinearRegression]] — Gaussian prior on regression weights.
