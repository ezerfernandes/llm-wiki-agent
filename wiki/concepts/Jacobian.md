---
title: "Jacobian"
type: concept
tags: [vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-preliminaries, matrix-calculus-for-deep-learning]
last_updated: 2026-06-04
---

# Jacobian

For a vector-valued function $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$, the Jacobian is the $m\times n$ matrix of all first-order partial derivatives ([[mml-book]] §5.3):

$$\mathbf{J}\,=\,\frac{d\mathbf{f}}{d\mathbf{x}}\,=\,\begin{bmatrix}
\partial f_1/\partial x_1 & \cdots & \partial f_1/\partial x_n \\
\vdots & \ddots & \vdots \\
\partial f_m/\partial x_1 & \cdots & \partial f_m/\partial x_n
\end{bmatrix}.$$

The gradient of a scalar-valued $f:\mathbb{R}^n\to\mathbb{R}$ ([[PartialDerivative]]) is the $1\times n$ special case.

## Layout conventions

There are two conventions for arranging the partials. [[matrix-calculus-for-deep-learning|Parr & Howard]] adopt **numerator layout** (functions vary down the rows, variables across the columns — the $m\times n$ form above); **denominator layout** is its transpose. Papers mix the two, so the matrix shape depends on the convention — Parr & Howard flag this explicitly so readers can navigate diverse sources.

## Element-wise diagonal condition

When a vector function is **element-wise** — each output element depends only on the correspondingly-indexed input element — its Jacobian is **diagonal** ([[matrix-calculus-for-deep-learning]]). Examples: $\partial(\mathbf{w}+\mathbf{x})/\partial\mathbf{w}=\mathbf{I}$; for the [[HadamardProduct|Hadamard product]] $\partial(\mathbf{w}\odot\mathbf{x})/\partial\mathbf{w}=\operatorname{diag}(\mathbf{x})$. Spotting this collapses chain-rule products from full matrix multiplies to cheap diagonal scalings.

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

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.3 Def. 5.6 (Eqs. 5.57–5.59) is the canonical reference. For $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$ the Jacobian $\mathbf{J}=\nabla_\mathbf{x}\mathbf{f}=\frac{\mathrm{d}\mathbf{f}(\mathbf{x})}{\mathrm{d}\mathbf{x}}$ is the $m\times n$ matrix with entry $J(i,j)=\frac{\partial f_i}{\partial x_j}$ — built by collecting the $n$ column vectors $\frac{\partial\mathbf{f}}{\partial x_i}\in\mathbb{R}^m$ (Eq. 5.55) side by side. The scalar-output case $f:\mathbb{R}^n\to\mathbb{R}^1$ recovers the $1\times n$ [[Gradient|row-vector gradient]] of Eq. 5.40.

**Numerator layout (the convention).** MML §5.3 Remark (pp. 150–151): *"In this book, we use the numerator layout of the derivative... an $m\times n$ matrix, where the elements of $\mathbf{f}$ define the rows and the elements of $\mathbf{x}$ define the columns. There exists also the denominator layout, which is the transpose."* This matches [[matrix-calculus-for-deep-learning|Parr & Howard]] and is what makes the [[ChainRule|chain rule]] a clean left-to-right matrix product $\frac{\mathrm{d}f}{\mathrm{d}(s,t)}=\frac{\partial f}{\partial\mathbf{x}}\frac{\partial\mathbf{x}}{\partial(s,t)}$ (Eq. 5.53) — see Contradictions on [[mml-ch05-vector-calculus|the source page]].

**Dimensions cheat-sheet** (Fig. 5.6): $f:\mathbb{R}\to\mathbb{R}$ → scalar; $f:\mathbb{R}^D\to\mathbb{R}$ → $1\times D$; $f:\mathbb{R}\to\mathbb{R}^E$ → $E\times 1$; $\mathbf{f}:\mathbb{R}^D\to\mathbb{R}^E$ → $E\times D$. MML Example 5.9: the Jacobian of a linear map $\mathbf{f}(\mathbf{x})=\mathbf{A}\mathbf{x}$ is just $\mathbf{A}$ itself.

**Jacobian determinant = volume scaling** (§5.3, Figs. 5.5–5.6): $|\det(\mathbf{J})|$ is the factor by which $\mathbf{f}$ scales an area/volume locally. MML's worked example (Eqs. 5.60–5.66): the map taking the unit square to a parallelogram of area 3 has $\mathbf{J}=\begin{bmatrix}-2&1\\1&1\end{bmatrix}$, $|\det\mathbf{J}|=3$ — recovered identically by a linear-algebra basis change (Approach 1) and by partial derivatives (Approach 2). Exact for linear $\mathbf{f}$, locally approximate for nonlinear $\mathbf{f}$. This is what powers change-of-variables for densities (§6.7) and the **reparametrization trick** in deep generative models.

## Connections

- [[mml-ch05-vector-calculus|MML Ch 5]] — §5.3 Def 5.6 canonical reference (numerator layout, Jacobian determinant).
- [[mml-book]] — umbrella source.
- [[PartialDerivative]] — scalar-output special case.
- [[Gradient]] — the $1\times n$ scalar-output Jacobian (row vector).
- [[Hessian]] — Jacobian of the gradient.
- [[ChainRule]] — Jacobian of a composition is the product of Jacobians.
- [[Backpropagation]] — algorithm that consumes Jacobians.
- [[Determinant]] — used in change-of-variables.
- [[HadamardProduct]] — element-wise op with a diagonal Jacobian.
- [[matrix-calculus-for-deep-learning]] — layout conventions + element-wise diagonal condition.
