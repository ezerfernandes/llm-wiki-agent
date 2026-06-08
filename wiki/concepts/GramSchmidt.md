---
title: "Gram-Schmidt Orthogonalization"
type: concept
tags: [analytic-geometry, linear-algebra, foundational, numerical-methods]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Gram-Schmidt Orthogonalization

The **Gram-Schmidt process** constructively transforms *any* [[Basis]] $(\mathbf{b}_1,\ldots,\mathbf{b}_n)$ of an $n$-dimensional inner-product space into an orthogonal (and, after normalizing, [[OrthonormalBasis|orthonormal]]) basis $(\mathbf{u}_1,\ldots,\mathbf{u}_n)$ spanning the same space ([[mml-ch03-analytic-geometry|MML Ch 3]] §3.8.3, Strang 2003). Such a basis always exists (Liesen & Mehrmann 2015), and $\operatorname{span}[\mathbf{b}_1,\ldots,\mathbf{b}_n]=\operatorname{span}[\mathbf{u}_1,\ldots,\mathbf{u}_n]$.

## The recurrence

It is iterated [[OrthogonalProjection|orthogonal projection]] ([[mml-book]] Eqs. 3.67–3.68):

$$\mathbf{u}_1 := \mathbf{b}_1, \qquad \mathbf{u}_k := \mathbf{b}_k - \pi_{\operatorname{span}[\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}]}(\mathbf{b}_k), \quad k=2,\ldots,n.$$

At step $k$, project $\mathbf{b}_k$ onto the subspace spanned by the already-constructed $\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}$ and **subtract** that projection — the remainder $\mathbf{u}_k$ is orthogonal to that $(k-1)$-dimensional subspace. Normalizing each $\mathbf{u}_k$ ($\|\mathbf{u}_k\|=1$) yields an ONB.

## Example (MML 3.12)

For $\mathbf{b}_1=[2,0]^\top$, $\mathbf{b}_2=[1,1]^\top$ in $\mathbb{R}^2$ (dot product):

$$\mathbf{u}_1 = [2,0]^\top, \qquad \mathbf{u}_2 = \mathbf{b}_2 - \frac{\mathbf{u}_1\mathbf{u}_1^\top}{\|\mathbf{u}_1\|^2}\mathbf{b}_2 = [1,1]^\top - \begin{bmatrix}1&0\\0&0\end{bmatrix}[1,1]^\top = [0,1]^\top,$$

and indeed $\mathbf{u}_1^\top\mathbf{u}_2=0$ (orthogonal).

## Why it matters

- It is the **constructive proof** that orthonormal bases exist, and the standard route to compute them.
- It underlies the **QR decomposition** ($\mathbf{A}=\mathbf{Q}\mathbf{R}$ with $\mathbf{Q}$ orthogonal).
- ONBs in turn make [[OrthogonalProjection|projection]] cheap ($\mathbf{B}\mathbf{B}^\top$, no inverse) and stabilize numerical algorithms.

## ML / numerics uses

- **Krylov subspace solvers** (conjugate gradients, GMRES) maintain orthogonal residual directions ([[mml-book]] §3.10, Stoer & Bulirsch 2002).
- **Orthogonalization in optimization** and in building orthonormal feature bases.
- *Numerical note:* classical Gram-Schmidt is numerically unstable; modified Gram-Schmidt or Householder QR is preferred in practice (the book gives the mathematical form).

## Connections

- [[mml-ch03-analytic-geometry]] — §3.8.3 canonical reference (Eqs. 3.67–3.68).
- [[OrthogonalProjection]] — Gram-Schmidt is iterated projection-and-subtract.
- [[OrthonormalBasis]] — the output (after normalization).
- [[Basis]] — the arbitrary input basis.
- [[OrthogonalMatrix]] — the $\mathbf{Q}$ factor it produces.
