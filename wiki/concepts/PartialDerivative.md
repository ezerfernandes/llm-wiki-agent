---
title: "Partial Derivative"
type: concept
tags: [vector-calculus, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Partial Derivative

For $f:\mathbb{R}^n\to\mathbb{R}$, the partial derivative w.r.t. $x_i$ measures the rate of change of $f$ when only $x_i$ varies and the other coordinates are held fixed ([[mml-book]] §5.2, Def. 5.5):

$$\frac{\partial f}{\partial x_i} = \lim_{h\to 0}\,\frac{f(\dots, x_i+h, \dots) - f(\dots, x_i, \dots)}{h}.$$

Collected into a row vector, partials form the **gradient** (or [[Jacobian]] in the scalar-output case):

$$\nabla_{\mathbf{x}}f \;=\;\frac{df}{d\mathbf{x}} \;=\;\begin{bmatrix}\partial f/\partial x_1 & \partial f/\partial x_2 & \cdots & \partial f/\partial x_n\end{bmatrix}\in\mathbb{R}^{1\times n}.$$

[[mml-book]] uses the **row-vector convention** (Eq. 5.40) — opposite to the column-vector convention common in Murphy / standard ML texts. This is a notational convenience for chain-rule composition ($J_{g\circ f} = J_g\,J_f$ works with neighboring dimensions matching).

## Why it matters for ML

- **Gradient descent** ([[mml-book]] §7.1): the direction of steepest descent is $-\nabla f^\top$.
- **[[Backpropagation]]** ([[mml-book]] §5.6): repeated application of the chain rule on partials computes gradients through deep computational graphs. This is the math behind every neural-network training loop.
- **[[Hessian]]**: the matrix of *second* partials, used in Newton-style optimization and to determine whether a stationary point is a minimum / maximum / saddle.
- **[[Linearization]]** ([[mml-book]] §5.8): the first-order Taylor expansion $f(\mathbf{x}+\boldsymbol\delta)\approx f(\mathbf{x}) + \nabla f(\mathbf{x})\boldsymbol\delta$ uses the gradient of partials.

## Connections

- [[mml-book]] — §5.2 canonical reference.
- [[Jacobian]] — partials of vector-valued functions.
- [[Hessian]] — second partials.
- [[ChainRule]] — composition of partial derivatives.
- [[Backpropagation]] — algorithmic application.
- [[GradientDescent]] — the optimization primitive that consumes them.
