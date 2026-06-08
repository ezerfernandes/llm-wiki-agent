---
title: "Hessian"
type: concept
tags: [vector-calculus, optimization, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-preliminaries, d2l-optimization, d2l-appendix-mathematics]
last_updated: 2026-06-04
---

# Hessian

Matrix of second-order [[PartialDerivative|partial derivatives]] of a scalar function. Positive-definite at a strict local minimum; used in Newton's method, [[ConvexOptimization]], and [[LaplaceApproximation]]. [[mml-book]] §5.7.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.7 defines the Hessian as *"the collection of all second-order partial derivatives."* For twice-continuously-differentiable $f:\mathbb{R}^2\to\mathbb{R}$, the order of differentiation does not matter — $\frac{\partial^2 f}{\partial x\partial y}=\frac{\partial^2 f}{\partial y\partial x}$ (Eq. 5.146, **Schwarz / Clairaut symmetry**) — so the Hessian is **symmetric**:

$$\mathbf{H} = \begin{bmatrix}\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x\partial y}\\[4pt] \frac{\partial^2 f}{\partial x\partial y} & \frac{\partial^2 f}{\partial y^2}\end{bmatrix}\quad (5.147).$$

For $\mathbf{x}\in\mathbb{R}^n$, $f:\mathbb{R}^n\to\mathbb{R}$, the Hessian $\nabla^2_\mathbf{x} f$ is an $n\times n$ matrix that **measures the local curvature** of $f$. (Remark: for a vector field $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$ the Hessian is an $(m\times n\times n)$-[[Tensor|tensor]].)

### Role in the multivariate Taylor series (§5.8)

The Hessian is the **second-order coefficient** of the [[TaylorSeries|multivariate Taylor series]]: the $k=2$ term is the quadratic form $D_\mathbf{x}^2 f(\mathbf{x}_0)\boldsymbol\delta^2=\operatorname{tr}(\mathbf{H}(\mathbf{x}_0)\boldsymbol\delta\boldsymbol\delta^\top)=\boldsymbol\delta^\top\mathbf{H}(\mathbf{x}_0)\boldsymbol\delta$ (Eqs. 5.158–5.159). MML Example 5.15 computes it explicitly for $f(x,y)=x^2+2xy+y^3$ at $(1,2)$: $\mathbf{H}(1,2)=\begin{bmatrix}2&2\\2&12\end{bmatrix}$, giving the second-order Taylor term $(x-1)^2+2(x-1)(y-2)+6(y-2)^2$. This quadratic model is what **Newton's method** minimizes at each step and what the [[LaplaceApproximation|Laplace approximation]] (§5.9) uses to build a local Gaussian around a density's mode.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.7 (definition) + §5.8 (Taylor coefficient) canonical reference.
- [[PartialDerivative]] — second partials are its entries.
- [[Jacobian]] — the Hessian is the Jacobian of the gradient.
- [[TaylorSeries]] / [[TaylorPolynomial]] — second-order coefficient.
- [[Linearization]] — the first-order (gradient-only) sibling.
- [[LaplaceApproximation]] — uses the Hessian for a local Gaussian.
- [[ConvexOptimization]] — positive-semidefinite Hessian ⟺ convexity.
