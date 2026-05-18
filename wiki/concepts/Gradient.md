---
title: "Gradient"
type: concept
tags: [math, optimization, vector-calculus, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Gradient

The vector of [[PartialDerivative|partial derivatives]] of a scalar loss with respect to model parameters — points in the direction of steepest increase. [[mml-book]] §5.2 (Eq. 5.40) defines it as the row vector $\nabla_\mathbf{x}f = \text{grad}\,f = \frac{df}{d\mathbf{x}} = [\partial f/\partial x_1\;\cdots\;\partial f/\partial x_n]\in\mathbb{R}^{1\times n}$ — the special case of the [[Jacobian]] for scalar-output functions.

[[mml-book]] uses the **row-vector convention**; many ML texts (Murphy, Goodfellow et al.) use the **column-vector convention**. Same math, transpose-different notation; the row-vector form keeps chain-rule composition $J_{g\circ f} = J_g J_f$ natural.

Computed by [[Autograd]] through [[Backpropagation]] and consumed by [[GradientDescent]] / [[Adam]] to step parameters downhill.

## Connections

- [[mml-book]] — §5.2 canonical reference.
- [[PartialDerivative]] — components.
- [[Jacobian]] — generalization to vector-output functions.
- [[Backpropagation]] — algorithmic computation.
- [[GradientDescent]] — primary consumer.
