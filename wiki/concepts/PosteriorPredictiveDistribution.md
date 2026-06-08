---
title: "Posterior Predictive Distribution"
type: concept
tags: [bayesian-inference, prediction, uncertainty, foundational]
sources: [mml-ch09-linear-regression, mml-book]
last_updated: 2026-06-04
---

# Posterior Predictive Distribution

The distribution over a new target $y_*$ obtained by **averaging the likelihood over the parameter posterior** — the Bayesian answer to "what do we predict, *and how sure are we*?" Rather than plug in a single $\boldsymbol\theta$ ([[MaximumLikelihoodEstimation|MLE]] / [[MAPEstimation|MAP]]), it marginalizes parameter uncertainty out ([[mml-ch09-linear-regression|MML Ch 9]] §9.3.4):

$$p(y_*\mid\mathbf{x}_*,\mathcal{D}) = \int p(y_*\mid\mathbf{x}_*,\boldsymbol\theta)\,p(\boldsymbol\theta\mid\mathcal{D})\,d\boldsymbol\theta = \mathbb{E}_{\boldsymbol\theta\mid\mathcal{D}}\big[p(y_*\mid\mathbf{x}_*,\boldsymbol\theta)\big].$$

## Closed form for Bayesian linear regression

With Gaussian likelihood and conjugate Gaussian posterior $p(\boldsymbol\theta\mid\mathcal{D})=\mathcal{N}(\mathbf{m}_N,\mathbf{S}_N)$ ([[BayesianLinearRegression]]), the integral is Gaussian ([[mml-ch09-linear-regression|MML]] Eq. 9.57c):

$$p(y_*\mid\mathbf{x}_*,\mathcal{D}) = \mathcal{N}\big(y_*\,\big|\,\boldsymbol\phi^\top(\mathbf{x}_*)\mathbf{m}_N,\ \underbrace{\boldsymbol\phi^\top(\mathbf{x}_*)\mathbf{S}_N\boldsymbol\phi(\mathbf{x}_*)}_{\text{epistemic}}+\underbrace{\sigma^2}_{\text{aleatoric}}\big).$$

- **Predictive mean** $\boldsymbol\phi^\top(\mathbf{x}_*)\mathbf{m}_N$ **coincides exactly with the [[MAPEstimation|MAP]] prediction** (MML margin, p. 308) — the Bayesian win is entirely in the *variance*.
- **Variance splits two ways**: parameter / [[EpistemicUncertainty|epistemic]] uncertainty $\boldsymbol\phi_*^\top\mathbf{S}_N\boldsymbol\phi_*$ (depends on where $\mathbf{x}_*$ sits relative to training data via $\mathbf{S}_N$; *grows* far from data and shrinks as $N\to\infty$) and irreducible measurement / [[AleatoricUncertainty|aleatoric]] [[NoiseModel|noise]] $\sigma^2$. For **noise-free function values** $f(\mathbf{x}_*)$ the $\sigma^2$ term drops (MML Eqs. 9.40, 9.58–9.59).

## Prior vs posterior predictive

The same integral against the **prior** $p(\boldsymbol\theta)$ (before any data) gives the **prior predictive** (MML §9.3.2, Eq. 9.38) — useful for visualizing the [[BayesianLinearRegression|induced distribution over functions]] a model believes in a priori. Swapping prior for posterior gives the posterior predictive; conjugacy keeps both Gaussian.

## Relation to the marginal likelihood

The posterior predictive resembles the [[MarginalLikelihood|marginal likelihood]] (MML §9.3.4 Remark, p. 309): both are likelihood expectations, but the marginal likelihood predicts the **training** targets $\mathbf{y}$ averaging under the **prior**, whereas the posterior predictive predicts **test** targets $y_*$ averaging under the **posterior**.

## Why it matters

The full predictive distribution — not just a point $\hat y$ — is "critical … in a decision-making system, where bad decisions can have significant consequences (e.g., in reinforcement learning or robotics)" ([[mml-ch09-linear-regression|MML]] p. 311). It generalizes directly to [[GaussianProcess|Gaussian processes]] (function-space predictives).

## Connections

- [[mml-ch09-linear-regression]] / [[mml-book]] — §9.3.2 (prior predictive), §9.3.4 (posterior predictive, Eq. 9.57).
- [[BayesianLinearRegression]] — supplies the posterior $\mathcal{N}(\mathbf{m}_N,\mathbf{S}_N)$ that is integrated against.
- [[MAPEstimation]] — its point prediction equals the predictive mean.
- [[NoiseModel]] — contributes the aleatoric $\sigma^2$ variance term.
- [[AleatoricUncertainty]] / [[EpistemicUncertainty]] — the two-way variance split.
- [[MarginalLikelihood]] — the prior-averaged training-target sibling.
- [[ConjugatePrior]] — why the predictive is closed-form Gaussian.
- [[GaussianProcess]] — function-space generalization.
