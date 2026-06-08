---
title: "Matrix Phylogeny"
type: concept
tags: [linear-algebra, matrix-decomposition, taxonomy, foundational]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Matrix Phylogeny

A **taxonomy of real matrices** — a "family tree" of matrix types and the factorizations / operations each admits ([[mml-book]] §4.7, Fig. 4.13). Marginal note: *"The word 'phylogenetic' describes how we capture the relationships among individuals or groups and derived from the Greek words for 'tribe' and 'source.'"* Black arrows mean "is a subset of"; the covered operations are annotated in blue.

## The tree (Fig. 4.13)

Starting from all real matrices $\mathbf{A}\in\mathbb{R}^{n\times m}$ (every one has a pseudo-inverse and an [[SingularValueDecomposition|SVD]]):

- **Non-square** ($m\neq n$): only the SVD applies.
- **Square** $\mathbb{R}^{n\times n}$: gains a [[Determinant]] and a [[Trace]]. Two orthogonal splits:
  - **By determinant**: $\det=0$ → **singular** (no inverse); $\det\neq0$ → **regular / invertible** ($\exists\mathbf{A}^{-1}$).
  - **By eigenvector basis**: no basis of eigenvectors → **[[DefectiveMatrix|defective]]**; basis of eigenvectors → **non-defective / [[Diagonalization|diagonalizable]]** ($\exists$ [[Eigendecomposition]], Thm 4.12/4.20).
- **Non-defective** splits by whether $\mathbf{A}^\top\mathbf{A}=\mathbf{A}\mathbf{A}^\top$:
  - holds → **normal**;
  - fails → **non-normal**.
- **Normal** ⊃ **symmetric** ($\mathbf{S}=\mathbf{S}^\top$, eigenvalues $\in\mathbb{R}$ by the [[SpectralTheorem|spectral theorem]]) ⊃ **[[SymmetricPositiveDefiniteMatrix|positive definite]]** ($\mathbf{x}^\top\mathbf{P}\mathbf{x}>0$; unique [[CholeskyDecomposition]]; eigenvalues $>0$; always invertible).
- **Symmetric** ⊃ **diagonal** matrices (closed under +/×; a group only if all diagonal entries are nonzero) ⊃ the **identity matrix**.
- **Orthogonal** matrices ($\mathbf{A}^\top\mathbf{A}=\mathbf{A}\mathbf{A}^\top=\mathbf{I}$, so $\mathbf{A}^\top=\mathbf{A}^{-1}$; columns are orthonormal eigenvectors) are a subset of the **regular (invertible)** matrices; **rotations** are a subset of the orthogonal matrices.

## The key non-equivalence

**Non-singular ≠ non-defective** ([[mml-book]] §4.7): invertibility (governed by the determinant) and diagonalizability (governed by the eigenvector basis) are *independent* axes. A rotation matrix is invertible ($\det\neq0$) but not diagonalizable over $\mathbb{R}$ (its eigenvalues are complex). Conversely a defective matrix can still be invertible.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.7 canonical reference (Fig. 4.13).
- [[MatrixDecomposition]] — the broader topic; this is its organizing taxonomy.
- [[Determinant]] / [[Trace]] — the square-matrix characteristic numbers.
- [[DefectiveMatrix]] / [[Diagonalization]] / [[Eigendecomposition]] — the non-defective branch.
- [[SymmetricPositiveDefiniteMatrix]] / [[CholeskyDecomposition]] / [[SpectralTheorem]] — the symmetric/SPD branch.
- [[OrthogonalMatrix]] / [[Rotation]] — the orthogonal branch of the invertible matrices.
- [[SingularValueDecomposition]] — the one factorization available at the root (all matrices).
- [[Rank]] — full rank ⟺ regular/invertible.
</content>
