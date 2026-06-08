---
title: "Gradient"
type: concept
tags: [math, optimization, vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Gradient

The vector of [[PartialDerivative|partial derivatives]] of a scalar loss with respect to model parameters — points in the direction of steepest increase. [[mml-book]] §5.2 (Eq. 5.40) defines it as the row vector $\nabla_\mathbf{x}f = \text{grad}\,f = \frac{df}{d\mathbf{x}} = [\partial f/\partial x_1\;\cdots\;\partial f/\partial x_n]\in\mathbb{R}^{1\times n}$ — the special case of the [[Jacobian]] for scalar-output functions.

[[mml-book]] uses the **row-vector convention**; many ML texts (Murphy, Goodfellow et al.) use the **column-vector convention**. Same math, transpose-different notation; the row-vector form keeps chain-rule composition $J_{g\circ f} = J_g J_f$ natural.

Computed by [[Autograd]] through [[Backpropagation]] and consumed by [[GradientDescent]] / [[Adam]] to step parameters downhill.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.2 Eq. 5.40 is the canonical definition. Collecting the $n$ [[PartialDerivative|partial derivatives]] (Def 5.5, Eq. 5.39 — each itself a [[DifferenceQuotient|difference-quotient]] limit) gives the **row vector**

$$\nabla_\mathbf{x} f = \operatorname{grad} f = \frac{\mathrm{d}f}{\mathrm{d}\mathbf{x}} = \left[\frac{\partial f}{\partial x_1}\;\cdots\;\frac{\partial f}{\partial x_n}\right]\in\mathbb{R}^{1\times n},$$

where the *input* $\mathbf{x}\in\mathbb{R}^n$ is a column vector. It is the scalar-output special case of the [[Jacobian]] (Def 5.6) and *"points in the direction of steepest ascent."*

### The row-vector convention — MML's deliberate choice

This is the single most-cited notational quirk of the chapter. MML §5.2 Remark (p. 147) defends the row vector *explicitly*: *"It is not uncommon in the literature to define the gradient vector as a column vector... The reason why we define the gradient vector as a row vector is twofold: First, we can consistently generalize the gradient to vector-valued functions $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$ (then the gradient becomes a matrix). Second, we can immediately apply the multi-variate chain rule without paying attention to the dimension of the gradient."* The payoff (§5.2.2, p. 149): the [[ChainRule|chain rule]] becomes a plain left-to-right matrix product $\frac{\mathrm{d}f}{\mathrm{d}(s,t)}=\frac{\partial f}{\partial\mathbf{x}}\frac{\partial\mathbf{x}}{\partial(s,t)}$ (Eq. 5.53) with **no transposes** — and *"when the gradient becomes a tensor... the transpose is no longer a triviality."*

**Contrast with the column-vector camp.** Murphy (*PML*), Goodfellow et al. (*Deep Learning*), and [[d2l-preliminaries|D2L]] / [[d2l-appendix-mathematics]] define $\nabla f$ as a **column** vector $\in\mathbb{R}^n$; D2L states the multivariate chain rule as $\nabla_\mathbf{x}y=\mathbf{A}^\top\nabla_\mathbf{u}y$ *with an explicit transpose*. The math is identical (every disagreement is one transpose), but the matrix shapes printed on the page differ — so cross-referencing MML against those texts requires mentally transposing. MML and [[matrix-calculus-for-deep-learning|Parr & Howard]] agree (both numerator layout / row vector) against that camp.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.2 Eq. 5.40 canonical reference (row-vector convention).
- [[mml-book]] — umbrella source.
- [[PartialDerivative]] — components.
- [[Jacobian]] — generalization to vector-output functions.
- [[Backpropagation]] — algorithmic computation.
- [[GradientDescent]] — primary consumer.
