---
title: "Orthogonality"
type: concept
tags: [analytic-geometry, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Orthogonality

Two vectors $\mathbf{x},\mathbf{y}$ are **orthogonal** iff their [[InnerProduct]] is zero ([[mml-ch03-analytic-geometry|MML Ch 3]] Def. 3.7, §3.4):

$$\mathbf{x}\perp\mathbf{y} \iff \langle\mathbf{x},\mathbf{y}\rangle = 0.$$

If additionally both are unit vectors ($\|\mathbf{x}\|=1=\|\mathbf{y}\|$), they are **orthonormal**. An immediate implication: the $\mathbf{0}$-vector is orthogonal to *every* vector.

## A generalization of perpendicularity

Orthogonality generalizes the everyday notion of perpendicularity (right angle, $\omega=\pi/2$) to **any** [[BilinearForm|bilinear form]] — it need not be the dot product ([[mml-book]] Remark, p. 77). Geometrically, orthogonal vectors have a right angle *with respect to a specific inner product*.

## Orthogonality is inner-product-relative

A crucial subtlety ([[mml-book]] Example 3.7, p. 78): $\mathbf{x}=[1,1]^\top$ and $\mathbf{y}=[-1,1]^\top$ are orthogonal under the dot product (angle $90°$), but under $\langle\mathbf{x},\mathbf{y}\rangle=\mathbf{x}^\top\begin{bmatrix}2&0\\0&1\end{bmatrix}\mathbf{y}$ the angle is $\approx 109.5°$ — **not** orthogonal. *Vectors orthogonal w.r.t. one inner product need not be orthogonal w.r.t. another.*

## What orthogonality builds

- **[[OrthonormalBasis|Orthonormal bases]]** — mutually orthogonal unit basis vectors (§3.5).
- **[[OrthogonalComplement|Orthogonal complement]]** $U^\perp$ — all vectors orthogonal to a subspace $U$ (§3.6); gives unique decompositions and normal vectors.
- **[[OrthogonalMatrix|Orthogonal matrices]]** — square matrices with orthonormal columns (§3.4 Def 3.8); they preserve lengths and angles.
- **[[OrthogonalProjection]]** — the orthogonality condition $\langle\mathbf{x}-\pi_U(\mathbf{x}),\mathbf{b}\rangle=0$ defines the projection (§3.8).
- **[[InnerProductOfFunctions|Orthogonal functions]]** — $\int_a^b u(x)v(x)\,dx=0$, e.g. $\sin\perp\cos$ on $[-\pi,\pi]$ (§3.7), the Fourier-series substrate.

## ML uses

- **Least-squares / regression** — the normal equations say the residual is orthogonal to every column of the design matrix ([[mml-book]] §9.4).
- **PCA** — principal components are mutually orthogonal directions of maximum variance (Ch 10).
- **Decorrelation / whitening** — transforms features to be mutually orthogonal.

## Connections

- [[mml-ch03-analytic-geometry]] — §3.4 canonical reference (Def. 3.7).
- [[InnerProduct]] — orthogonality = zero inner product.
- [[Angle]] — orthogonality is the angle $\omega=\pi/2$.
- [[BilinearForm]] — orthogonality generalizes to any bilinear form.
- [[OrthonormalBasis]] / [[OrthogonalComplement]] / [[OrthogonalMatrix]] / [[OrthogonalProjection]] — what it builds.
