---
title: "Jensen's Inequality"
type: concept
tags: [optimization, convex-optimization, mathematics, probability, foundational]
sources: [mml-ch07-continuous-optimization, mml-book, d2l-optimization]
last_updated: 2026-06-05
---

# Jensen's Inequality

The defining inequality of a [[ConvexFunction|convex function]], named ([[mml-ch07-continuous-optimization|MML Ch 7]] §7.3, Remark p. 239): the convexity condition $f(\theta\mathbf{x}+(1-\theta)\mathbf{y})\leq\theta f(\mathbf{x})+(1-\theta)f(\mathbf{y})$ (Eq. 7.30) "is sometimes called Jensen's inequality. In fact, a whole class of inequalities for taking nonnegative weighted sums of convex functions are all called Jensen's inequality."

## General forms

For a convex $f$ and weights $\alpha_i\ge0$ with $\sum_i\alpha_i=1$:

$$f\!\left(\sum_i\alpha_i x_i\right)\;\leq\;\sum_i\alpha_i\,f(x_i),$$

and, taking the weights as a probability distribution, the **probabilistic form**:

$$f(\mathbb{E}_X[X])\;\leq\;\mathbb{E}_X[f(X)].$$

**The convex function of an expectation is no greater than the expectation of the convex function.** (For concave $f$ the inequality reverses.)

## Where it is used

- **[[StochasticGradientDescent|SGD]] convergence analysis** and variational bounds ([[d2l-optimization]] §convexity / §sgd).
- **Information theory / variational inference** — the ELBO (evidence lower bound) is a Jensen bound on $\log p(\mathbf{x})$; KL divergence non-negativity follows from Jensen applied to $-\log$.
- **Probability** — relating $\mathbb{E}[X^2]$ vs $(\mathbb{E}[X])^2$ (variance $\ge0$ is Jensen for $f(x)=x^2$); AM–GM is Jensen for $\log$.

## Connections

- [[mml-ch07-continuous-optimization]] — §7.3 Remark (the naming) canonical reference.
- [[ConvexFunction]] — Jensen *is* the convexity definition, generalized.
- [[Convexity]] — umbrella concept.
- [[StochasticGradientDescent]] — convergence proofs use Jensen.
- [[d2l-optimization]] — alternative reference with the expectation form.
</content>
