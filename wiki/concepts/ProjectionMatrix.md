---
title: "Projection Matrix"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Projection Matrix

## Projection (Definition 3.10)

A **projection** is a linear mapping $\pi:V\to U$ onto a subspace $U\subseteq V$ that is **idempotent**: $\pi^2=\pi\circ\pi=\pi$ ([[mml-ch03-analytic-geometry|MML Ch 3]] Def. 3.10, §3.8). Since linear maps are transformation matrices, every projection has a **projection matrix** $\mathbf{P}_\pi$ with

$$\mathbf{P}_\pi^2 = \mathbf{P}_\pi \qquad\text{(applying it twice changes nothing).}$$

For *orthogonal* projections (the case relevant to ML), $\mathbf{P}_\pi$ is also **symmetric** (margin note, [[mml-book]] p. 84: *"Projection matrices are always symmetric."*).

## Closed forms (orthogonal projection, dot product)

**Onto a line spanned by $\mathbf{b}$** ([[mml-book]] Eq. 3.46):
$$\mathbf{P}_\pi = \frac{\mathbf{b}\mathbf{b}^\top}{\|\mathbf{b}\|^2} = \frac{\mathbf{b}\mathbf{b}^\top}{\mathbf{b}^\top\mathbf{b}}\qquad(\text{symmetric, rank 1}).$$

**Onto a general subspace** $U$ with basis matrix $\mathbf{B}=[\mathbf{b}_1,\ldots,\mathbf{b}_m]\in\mathbb{R}^{n\times m}$ ([[mml-book]] Eq. 3.59):
$$\mathbf{P}_\pi = \mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top.$$
The 1-D case is the special case $\dim(U)=1$. If $\mathbf{B}$ has **orthonormal columns** ($\mathbf{B}^\top\mathbf{B}=\mathbf{I}$), this collapses to $\mathbf{P}_\pi=\mathbf{B}\mathbf{B}^\top$ — no inverse needed (Eq. 3.65).

The factor $(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ is the **pseudo-inverse** of $\mathbf{B}$, computable for non-square $\mathbf{B}$ when $\mathbf{B}^\top\mathbf{B}$ is positive definite (i.e. $\mathbf{B}$ full rank).

## Spectral reading

A projection matrix has eigenvalues only $0$ and $1$: vectors already in $U$ are fixed (eigenvalue 1, $\mathbf{P}_\pi\pi_U(\mathbf{x})=\pi_U(\mathbf{x})$), vectors in the [[OrthogonalComplement|orthogonal complement]] map to $\mathbf{0}$ (eigenvalue 0) ([[mml-book]] Remark, Example 3.10).

## Rotation matrices: a related orthogonal-transformation matrix

The chapter's other named transformation matrices are the **[[Rotation|rotation matrices]]** $\mathbf{R}(\theta)$ (§3.9) — but note these are [[OrthogonalMatrix|orthogonal]] (length/angle-preserving), *not* idempotent projections. Projections lose information (rank $<n$); rotations are invertible.

## ML uses

- **Least-squares regression** — $\boldsymbol\theta_{\text{ML}}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$; the fitted values $\hat{\mathbf{y}}=\mathbf{X}\boldsymbol\theta_{\text{ML}}=\mathbf{P}_\pi\mathbf{y}$ are the projection of $\mathbf{y}$ onto the column space (the "hat matrix"), [[mml-book]] §9.4.
- **PCA** reconstruction $\tilde{\mathbf{x}}=\mathbf{B}\mathbf{B}^\top\mathbf{x}$ (orthonormal $\mathbf{B}$), Ch 10.
- **Ridge / numerical stability** — adding a jitter $\epsilon\mathbf{I}$ to $\mathbf{B}^\top\mathbf{B}$ keeps the inverse well-conditioned ([[mml-book]] p. 86).

## Connections

- [[mml-ch03-analytic-geometry]] — §3.8 canonical reference (Def. 3.10, Eqs. 3.46, 3.59).
- [[OrthogonalProjection]] — the operation $\mathbf{P}_\pi$ implements.
- [[OrthonormalBasis]] — collapses $\mathbf{P}_\pi$ to $\mathbf{B}\mathbf{B}^\top$.
- [[GramMatrix]] — $\mathbf{B}^\top\mathbf{B}$ is the Gram matrix at the heart of the formula.
- [[Rotation]] / [[OrthogonalMatrix]] — the other named transformation matrices of Ch 3 (invertible, not idempotent).
- [[LinearRegression]] — the "hat matrix" is a projection matrix.
