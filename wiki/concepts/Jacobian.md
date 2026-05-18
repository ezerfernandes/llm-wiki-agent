---
title: "Jacobian"
type: concept
tags: [vector-calculus, foundational]
sources: [mml-book, d2l-preliminaries]
last_updated: 2026-05-16
---

# Jacobian

For a vector-valued function $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$, the Jacobian is the $m\times n$ matrix of all first-order partial derivatives ([[mml-book]] §5.3):

$$\mathbf{J}\,=\,\frac{d\mathbf{f}}{d\mathbf{x}}\,=\,\begin{bmatrix}
\partial f_1/\partial x_1 & \cdots & \partial f_1/\partial x_n \\
\vdots & \ddots & \vdots \\
\partial f_m/\partial x_1 & \cdots & \partial f_m/\partial x_n
\end{bmatrix}.$$

The gradient of a scalar-valued $f:\mathbb{R}^n\to\mathbb{R}$ ([[PartialDerivative]]) is the $1\times n$ special case.

## What the Jacobian represents

Geometrically: **the best linear approximation** of $\mathbf{f}$ at $\mathbf{x}$. For small $\boldsymbol\delta$,

$$\mathbf{f}(\mathbf{x}+\boldsymbol\delta) \approx \mathbf{f}(\mathbf{x}) + \mathbf{J}(\mathbf{x})\,\boldsymbol\delta.$$

The Jacobian *is* the local linear map between tangent spaces.

## Jacobian determinant

When $m=n$, $|\det(\mathbf{J})|$ is the **local volume-scaling factor** — how much $\mathbf{f}$ stretches an infinitesimal volume element. This appears in:

- **Change of variables** for densities ([[mml-book]] §6.7): $p_Y(\mathbf{y}) = p_X(\mathbf{f}^{-1}(\mathbf{y}))\,|\det\mathbf{J}_{\mathbf{f}^{-1}}(\mathbf{y})|$. Underlies [[NormalizingFlow|normalizing flows]] — invertible neural networks that track the log-determinant exactly.
- **Multivariate integration**: the substitution rule scales $d\mathbf{x} = |\det\mathbf{J}|\,d\mathbf{y}$.

## ML uses

- **[[Backpropagation]]** is iterated Jacobian-vector products: gradients propagate as $\boldsymbol\nabla_{\text{out}}^\top \mathbf{J}_L \mathbf{J}_{L-1}\cdots\mathbf{J}_1$.
- **Normalizing flows** require the **log-determinant** of the Jacobian — invertible architectures (RealNVP, Glow, neural spline flows) constrain $\mathbf{J}$ to be triangular or otherwise structured so $\det\mathbf{J}$ is cheap to compute.
- **Influence functions**: leave-one-out approximations use the Hessian (Jacobian of the gradient).

## Connections

- [[mml-book]] — §5.3 canonical reference.
- [[PartialDerivative]] — scalar-output special case.
- [[Hessian]] — Jacobian of the gradient.
- [[ChainRule]] — Jacobian of a composition is the product of Jacobians.
- [[Backpropagation]] — algorithm that consumes Jacobians.
- [[Determinant]] — used in change-of-variables.
