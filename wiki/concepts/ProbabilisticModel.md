---
title: "Probabilistic Model"
type: concept
tags: [probabilistic-modeling, modeling, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Probabilistic Model

The second of the two senses of "model" in [[mml-book]] (§8.1.3 / §8.4.1): instead of a single [[Predictor|predictor function]], a model that **describes the distribution of possible outputs** and so expresses *uncertainty*. Data are treated as **noisy observations of some true underlying effect** (§8.1.3, p. 256), and we want predictors that quantify confidence — e.g. a Gaussian predictive distribution at a test point (Fig. 8.3).

[[mml-book]] limits itself to distributions with **finite-dimensional parameters** (no stochastic processes / random measures), which lets us treat probabilistic models as **multivariate probability distributions** — already a rich class.

## Specified by the joint distribution

§8.4.1 (p. 273): "A probabilistic model is specified by the joint distribution of all its random variables." The **joint** $p(\mathbf{x},\boldsymbol\theta)$ over observed data $\mathbf{x}$ and hidden parameters $\boldsymbol\theta$ is the central object — only the joint encapsulates all three of:

- the **[[Prior|prior]]** and **[[Likelihood|likelihood]]** (product rule, §6.3);
- the **[[MarginalLikelihood|marginal likelihood]]** $p(\mathbf{x})$ (sum rule — integrate out the parameters; key to [[ModelSelection|model selection]]);
- the **[[Posterior|posterior]]** (joint ÷ marginal likelihood).

Probabilistic models offer "a unified and consistent set of tools from probability theory (Chapter 6) for modeling, inference, prediction, and model selection."

## What it enables that a bare predictor does not

- **[[MaximumLikelihoodEstimation|Maximum likelihood]]** / **[[MAPEstimation|MAP]]** point estimation.
- **[[BayesianInference|Bayesian inference]]** — a full posterior over parameters, propagating uncertainty into predictions (a function-predictor admits only a point estimate).
- **[[LatentVariable|Latent-variable]]** structure and **[[DirectedGraphicalModel|graphical-model]]** representations.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.1.3 / §8.4.1 canonical reference.
- [[mml-book]] — §8.1.3 / §8.4.
- [[Predictor]] — the alternative "model-as-function" view.
- [[Prior]] / [[Likelihood]] / [[Posterior]] / [[MarginalLikelihood]] — the components of the joint.
- [[BayesianInference]] — what a probabilistic model uniquely enables.
- [[ProbabilisticGraphicalModel]] — its graphical representation.
- [[GaussianDistribution]] — the workhorse finite-parameter distribution.
