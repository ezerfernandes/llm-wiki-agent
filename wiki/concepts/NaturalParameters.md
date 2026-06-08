---
title: "Natural Parameters"
type: concept
tags: [probability, distributions, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Natural Parameters

The **natural parameters** are the parameter vector $\boldsymbol\theta\in\mathbb{R}^D$ that pairs with the [[SufficientStatistics|sufficient statistics]] $\boldsymbol\phi(\mathbf x)$ inside the canonical form of an [[ExponentialFamily|exponential-family]] distribution ([[mml-book]] §6.6.3):

$$p(\mathbf x\mid\boldsymbol\theta)=h(\mathbf x)\exp\big(\langle\boldsymbol\theta,\boldsymbol\phi(\mathbf x)\rangle-A(\boldsymbol\theta)\big)\qquad(\text{Eq. 6.107}),$$

or, stripping the base measure and log-partition for intuition, $p(\mathbf x\mid\boldsymbol\theta)\propto\exp(\boldsymbol\theta^\top\boldsymbol\phi(\mathbf x))$ (Eq. 6.108). The name *natural parameters* attaches to $\boldsymbol\theta$ in this parametrization (margin / p. 212).

## Relation to the "usual" parameters

The natural parameters are usually a *transformation* of the familiar parameters:

- **Gaussian** $\mathcal{N}(\mu,\sigma^2)$ (Example 6.13): $\boldsymbol\theta=\big[\tfrac{\mu}{\sigma^2},\,-\tfrac{1}{2\sigma^2}\big]^\top$ with $\boldsymbol\phi(x)=[x,x^2]^\top$.
- **Bernoulli** $\mathrm{Ber}(\mu)$ (Example 6.14): the natural parameter is $\theta=\log\frac{\mu}{1-\mu}$ (the **log-odds / logit**) with $\phi(x)=x$, $A(\theta)=\log(1+\exp\theta)$, $h(x)=1$.

## The Bernoulli natural parameter is the logit; its inverse is the sigmoid

Inverting the Bernoulli relationship ([[mml-book]] Eq. 6.118):

$$\mu=\frac{1}{1+\exp(-\theta)},$$

which is the **[[Sigmoid|sigmoid / logistic function]]** — it squeezes a real-valued natural parameter $\theta\in\mathbb{R}$ into a probability $\mu\in(0,1)$. This is exactly the link function used in logistic regression and the sigmoid activation in neural networks ([[mml-book]] §6.6.3 Remark, citing Bishop 2006 and Goodfellow et al. 2016).

## Why "natural"

In this form, modeling and inference become convenient: $A(\boldsymbol\theta)$ (the log-partition function) normalizes the distribution, and the conjugate prior for an exponential family has sufficient statistics $[\boldsymbol\theta, -A(\boldsymbol\theta)]^\top$ (Eq. 6.120), so conjugate pairs can be *derived* (Example 6.15 derives the Beta as the Bernoulli's conjugate prior).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.6.3 deep dive.
- [[mml-book]] — §6.6.3 canonical reference.
- [[ExponentialFamily]] — the form natural parameters parametrize.
- [[SufficientStatistics]] — paired with $\boldsymbol\theta$ in the dot product.
- [[ConjugatePrior]] — derivable from the natural-parameter form.
- [[GaussianDistribution]] — natural-parameter example.
