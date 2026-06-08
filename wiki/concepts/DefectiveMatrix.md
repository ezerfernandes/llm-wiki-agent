---
title: "Defective Matrix"
type: concept
tags: [linear-algebra, eigenvalue, matrix-decomposition]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Defective Matrix

**Definition 4.13** ([[mml-book]] §4.2): a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is **defective** if it possesses **fewer than $n$ linearly independent eigenvectors** — i.e. its eigenvectors do *not* form a basis of $\mathbb{R}^n$.

A defective matrix is precisely the obstruction to [[Diagonalization|diagonalization]]: only non-defective matrices admit an [[Eigendecomposition]] $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ (Thm 4.20), because $\mathbf{P}$ must have full rank.

## Multiplicity characterization

A matrix is defective iff some eigenvalue $\lambda_i$ has

$$\text{geometric multiplicity} < \text{algebraic multiplicity}.$$

Equivalently, at least one eigenvalue with algebraic multiplicity $m>1$ has an [[Eigenspace|eigenspace]] of dimension $<m$. The sum of eigenspace dimensions is then $<n$.

- **Example 4.6** ([[mml-book]] §4.2): $\mathbf{A}=\begin{bmatrix}2&1\\0&2\end{bmatrix}$ has $\lambda=2$ with algebraic multiplicity 2 but only the single eigenvector $[1,0]^\top$ (geometric multiplicity 1) — defective.

## What is *not* defective

- A matrix with **$n$ distinct eigenvalues** is never defective: distinct eigenvalues have linearly independent eigenvectors ([[mml-book]] Thm 4.12). So a defective matrix **cannot** have $n$ distinct eigenvalues — it must have a repeated eigenvalue.
- **Symmetric matrices are never defective**: the [[SpectralTheorem|spectral theorem]] (Thm 4.15) guarantees an orthonormal eigenbasis.

## Defective vs singular

([[mml-book]] §4.7): defectiveness (no eigenbasis) and singularity (zero determinant) are **independent**. A **rotation matrix** is invertible (non-singular) but defective over $\mathbb{R}$ (complex eigenvalues, no real eigenbasis); the matrix $\begin{bmatrix}2&1\\0&2\end{bmatrix}$ above is invertible ($\det=4$) yet defective. The **Jordan normal form** (Lang 1987) provides a decomposition that works even for defective matrices, but is beyond MML's scope.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.2 canonical reference (Def. 4.13).
- [[Diagonalization]] / [[Eigendecomposition]] — defective ⇒ not diagonalizable.
- [[Eigenvalue]] / [[Eigenvector]] / [[Eigenspace]] — defectiveness = geometric < algebraic multiplicity.
- [[SpectralTheorem]] — symmetric matrices are guaranteed non-defective.
- [[MatrixPhylogeny]] — the "defective" branch of the matrix taxonomy.
</content>
