---
title: "Taylor Series"
type: concept
tags: [vector-calculus, foundational]
sources: [mml-book, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Taylor Series

A representation of a function $f$ as an infinite sum of derivative-weighted polynomial terms ([[mml-book]] §5.1.1, Def 5.4):

$$T_\infty(x) := \sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k.$$

The truncation to degree $n$ is the **Taylor polynomial** $T_n(x)$ — an *approximation* of $f$ near $x_0$.

## Multivariate Taylor

For $f:\mathbb{R}^D\to\mathbb{R}$, the second-order Taylor expansion at $\mathbf{x}_0$ is ([[mml-book]] §5.8):

$$f(\mathbf{x}_0 + \boldsymbol\delta) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)\boldsymbol\delta + \tfrac{1}{2}\boldsymbol\delta^\top \nabla^2 f(\mathbf{x}_0)\,\boldsymbol\delta.$$

First-order Taylor = [[Linearization]] (the local linear approximation of $f$ near $\mathbf{x}_0$). The first-order term is the [[Jacobian]]; the second-order term is the [[Hessian]] $\nabla^2 f$.

## Where Taylor surfaces in ML

- **[[LaplaceApproximation]]**: second-order Taylor of $\log p(\boldsymbol\theta\mid\mathcal{D})$ at the MAP estimate gives the Gaussian approximation to the posterior — variance comes from $-\nabla^2$ of the log-posterior (the Fisher information).
- **Newton's method**: optimization step $\boldsymbol\theta\leftarrow\boldsymbol\theta - [\nabla^2 f]^{-1}\nabla f$ uses the second-order Taylor approximation to find a quadratic-model minimum.
- **Gauss-Newton / Levenberg-Marquardt**: nonlinear least squares = repeated linearization (first-order Taylor) of the residuals.
- **Score matching / diffusion**: log-density gradients live in the first-order Taylor remainder of $\log p$.

## Polynomials are *exact* Taylor

[[mml-book]] §5.1 Example 5.3: the degree-$n$ Taylor polynomial of a degree-$n$ polynomial equals the original polynomial — the Taylor expansion is exact, not an approximation. This is the "obvious" sanity check.

## Connections

- [[mml-book]] — §5.1.1 + §5.8 canonical references.
- [[PartialDerivative]] — building block.
- [[Jacobian]] — first-order coefficient (multivariate).
- [[Hessian]] — second-order coefficient (multivariate).
- [[Linearization]] — first-order truncation.
- [[remarkable-limits]] — algebrica.org's limit-based intro to differentiation.
