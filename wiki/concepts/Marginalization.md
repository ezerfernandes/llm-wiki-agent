---
title: "Marginalization"
type: concept
tags: [probability, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Marginalization

**Marginalization** ("summing out" / "integrating out") recovers the distribution of a subset of random variables from a [[JointProbability|joint]] distribution by eliminating the others. It is exactly the content of the **[[SumRule|sum rule]]** ([[mml-book]] §6.3, which calls it the *marginalization property*):

$$p(\mathbf x)=\sum_{\mathbf y\in\mathcal{Y}} p(\mathbf x,\mathbf y)\quad(\text{discrete}),\qquad p(\mathbf x)=\int_{\mathcal{Y}} p(\mathbf x,\mathbf y)\,d\mathbf y\quad(\text{continuous})\qquad(\text{Eq. 6.20}).$$

The result $p(\mathbf x)$ is the **marginal distribution** of $\mathbf x$. For a vector, marginalize all-but-one coordinate: $p(x_i)=\int p(x_1,\dots,x_D)\,d\mathbf x_{\setminus i}$ (Eq. 6.21).

## Discrete table view

For a discrete joint pmf laid out as a table (Example 6.2), the marginal of $X$ is the **column sum** $P(X=x_i)=c_i/N=\sum_j n_{ij}/N$ and the marginal of $Y$ is the **row sum** $P(Y=y_j)=r_j/N$ ([[mml-book]] Eqs. 6.10–6.11) — hence the name "marginal" (the sums written in the margins of the table).

## Computational hardness

When there are many variables, marginalization becomes a high-dimensional sum/integral with no known exact polynomial-time algorithm ([[mml-book]] §6.3 Remark) — the root cause of why the **evidence** $p(\mathbf y)$ in [[BayesTheorem]] is usually intractable, and why approximate inference exists.

## Where it stays tractable

- **[[GaussianDistribution|Gaussians]]**: the marginal of a joint Gaussian is Gaussian and is obtained by simply reading off the relevant mean/covariance block (§6.5.1, Eq. 6.68) — no integral needed.
- **Conjugate / [[ExponentialFamily|exponential-family]]** models give closed-form marginals.

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.3 deep dive.
- [[mml-book]] — §6.3 canonical reference.
- [[SumRule]] — marginalization *is* the sum rule.
- [[JointProbability]] — the object marginalized.
- [[ConditionalProbability]] — the complementary operation (ratio against a marginal).
- [[BayesTheorem]] — its evidence term is a marginalization.
- [[GaussianDistribution]] — closed-form marginalization.
