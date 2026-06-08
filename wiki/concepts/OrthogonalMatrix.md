---
title: "Orthogonal Matrix"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Orthogonal Matrix

A square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is an **orthogonal matrix** iff its columns are orthonormal ([[mml-ch03-analytic-geometry|MML Ch 3]] Def. 3.8, §3.4), so that

$$\mathbf{A}\mathbf{A}^\top = \mathbf{I} = \mathbf{A}^\top\mathbf{A} \quad\Longrightarrow\quad \mathbf{A}^{-1} = \mathbf{A}^\top.$$

**The inverse is obtained simply by transposing the matrix** — no Gaussian elimination needed (Eqs. 3.29–3.30).

## A naming quirk

[[mml-book]] flags this in a margin note (p. 78): *"It is convention to call these matrices 'orthogonal' but a more precise description would be 'orthonormal'."* The columns are not merely orthogonal, they are **orthonormal** (orthogonal *and* unit length).

## Why they matter: length and angle preservation

For the dot product, orthogonal transformations leave geometry invariant ([[mml-book]] Eqs. 3.31–3.32):

- **Length preserved**: $\|\mathbf{A}\mathbf{x}\|^2=(\mathbf{A}\mathbf{x})^\top(\mathbf{A}\mathbf{x})=\mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x}=\mathbf{x}^\top\mathbf{x}=\|\mathbf{x}\|^2$.
- **Angle preserved**: $\cos\omega=\dfrac{(\mathbf{A}\mathbf{x})^\top(\mathbf{A}\mathbf{y})}{\|\mathbf{A}\mathbf{x}\|\,\|\mathbf{A}\mathbf{y}\|}=\dfrac{\mathbf{x}^\top\mathbf{y}}{\|\mathbf{x}\|\,\|\mathbf{y}\|}$.

Orthogonal matrices therefore define **distance- and angle-preserving transformations** — the [[Rotation|rotations]] (with the possibility of flips/reflections) developed in §3.9. The determinant of an orthogonal matrix is $\pm 1$ ($+1$ = proper rotation, $-1$ = includes a reflection).

## ML / numerics uses

- **Rotations** in graphics, robotics, and pose estimation ([[Rotation]], [[mml-book]] §3.9).
- **QR / Gram-Schmidt** — the $\mathbf{Q}$ factor is orthogonal; orthonormal columns make [[OrthogonalProjection|projection]] collapse to $\mathbf{B}\mathbf{B}^\top$ (no inverse).
- **Spectral theorem** — a symmetric matrix has an orthogonal eigenbasis ([[Eigendecomposition]]); the $\mathbf{U},\mathbf{V}$ in [[SingularValueDecomposition|SVD]] are orthogonal.
- **Orthogonal weight initialization** in deep nets keeps activation norms stable (related to gradient stability).

## Connections

- [[mml-ch03-analytic-geometry]] — §3.4 canonical reference (Def. 3.8).
- [[Orthogonality]] / [[OrthonormalBasis]] — orthonormal columns form an ONB.
- [[Rotation]] — orthogonal matrices with $\det=+1$ are rotations.
- [[MatrixTranspose]] / [[MatrixInverse]] — $\mathbf{A}^{-1}=\mathbf{A}^\top$.
- [[Eigendecomposition]] / [[SingularValueDecomposition]] — orthogonal factor matrices.
- [[OrthogonalProjection]] — ONB simplifies the projection matrix.
