---
title: "Partial Derivative"
type: concept
tags: [vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-06-04
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

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.2 Def 5.5 (Eq. 5.39) defines each partial as a [[DifferenceQuotient|difference-quotient]] limit in one coordinate, the others held fixed: $\frac{\partial f}{\partial x_i}=\lim_{h\to 0}\frac{f(\dots,x_i+h,\dots)-f(\mathbf{x})}{h}$. MML's marginal note frames the practical payoff: *"Each partial derivative is a derivative with respect to a scalar"* — so all the univariate [[DifferentiationRules|differentiation rules]] (§5.1.2) apply directly. The basic multivariate sum/product/chain rules (Eqs. 5.46–5.48) carry over, **but order matters** since gradients are now vectors/matrices (matrix multiplication is non-commutative). Worked: MML Example 5.7, $f(x_1,x_2)=x_1^2x_2+x_1x_2^3$ → $\frac{\partial f}{\partial x_1}=2x_1x_2+x_2^3$, $\frac{\partial f}{\partial x_2}=x_1^2+3x_1x_2^2$. The $n$ partials collect into the row-vector [[Gradient|gradient]] (Eq. 5.40); second partials collect into the symmetric [[Hessian]] (§5.7); for a vector-valued $\mathbf{f}$ they fill the [[Jacobian]] (§5.3).

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.2 Def 5.5 canonical reference.
- [[mml-book]] — umbrella source.
- [[DifferenceQuotient]] — the limit each partial is built from.
- [[Gradient]] — the row vector of partials.
- [[Jacobian]] — partials of vector-valued functions.
- [[Hessian]] — second partials.
- [[ChainRule]] — composition of partial derivatives.
- [[Backpropagation]] — algorithmic application.
- [[GradientDescent]] — the optimization primitive that consumes them.
