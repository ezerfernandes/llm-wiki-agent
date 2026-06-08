---
title: "Eigenvalue"
type: concept
tags: [linear-algebra, mathematics, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations, mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Eigenvalue

A scalar $\lambda$ such that $Av = \lambda v$ for some nonzero vector $v$ (the corresponding [[Eigenvector|eigenvector]]). For a symmetric matrix, all eigenvalues are real. The set of eigenvalues is the **spectrum** of A.

In practical parallel computing, eigenvalue problems arise in document retrieval (web search via PageRank), text mining, social network analysis, and statistical methods. The large scale of these problems — matrices with millions of rows — motivates parallel computation.

## Parallel Methods

- **[[PowerMethod|Power method]]:** Iterative; finds the dominant eigenvalue $\lambda_1$ and eigenvector $v_1$; extended to further eigenpairs via deflation.
- **SVD via CULA:** The CULA library (CUDA-based, not NVIDIA) provides singular value decomposition routines. Singular values are related to eigenvalues (they are the square roots of eigenvalues of $A^T A$); for symmetric positive semidefinite A, singular values equal eigenvalues. The R `gputools` package provides an interface to CULA's SVD.

## Note on Singular Values

Matloff (Ch11, footnote 1) writes that "singular value is a synonym for eigenvalue," which holds for symmetric positive semidefinite matrices but is an oversimplification in general. **MML §4.5 makes this precise**: the [[SingularValueDecomposition|singular values]] $\sigma_i$ are the *square roots* of the eigenvalues $\lambda_i$ of $\mathbf{A}^\top\mathbf{A}$ ($\sigma_i^2=\lambda_i$, Eq. 4.75), and the SVD applies to *non-square* matrices where eigenvalues are undefined. Equality $\sigma_i=\lambda_i$ holds only for [[SymmetricPositiveDefiniteMatrix|symmetric positive (semi)definite]] matrices, where the SVD and [[Eigendecomposition]] coincide ([[mml-book]] §4.5.2–4.5.3).

## Appendix B Definition (Matloff)

Section B.6 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) gives the formal definition for square matrices and states two diagonalizability conditions:

1. **Symmetric real case:** if A is symmetric and real, it is diagonalizable — there exists an orthogonal matrix U such that $U'AU = D$ for a diagonal matrix D. The diagonal entries of D are the eigenvalues and the columns of U are the orthogonal eigenvectors.
2. **Distinct eigenvalues:** if all eigenvalues of A are distinct, A is also diagonalizable (though U need not be orthogonal in this case).

Footnote: for nonsquare matrices, the discussion generalizes to *singular value decomposition* (not a simple synonym for eigendecomposition, contrary to a simplified note in Ch11).

## R Syntax

```r
eigen(u)   # returns $values (eigenvalues) and $vectors (eigenvector columns)
```

Note that eigenvalues of a non-symmetric matrix may be complex-valued, as shown in the Appendix B R session output.

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

**Definition 4.6** (§4.2, Eq. 4.25): for square $\mathbf{A}\in\mathbb{R}^{n\times n}$, $\lambda\in\mathbb{R}$ is an *eigenvalue* with corresponding [[Eigenvector|eigenvector]] $\mathbf{x}\in\mathbb{R}^n\setminus\{\mathbf{0}\}$ if $\mathbf{A}\mathbf{x}=\lambda\mathbf{x}$ (the **eigenvalue equation**). The German *eigen* means "characteristic / self / own" (marginal, p. 105). **Four equivalent statements**: $\lambda$ is an eigenvalue ⟺ $(\mathbf{A}-\lambda\mathbf{I})\mathbf{x}=\mathbf{0}$ has a non-trivial solution ⟺ $\operatorname{rk}(\mathbf{A}-\lambda\mathbf{I})<n$ ⟺ $\det(\mathbf{A}-\lambda\mathbf{I})=0$.

- **[[CharacteristicPolynomial|Characteristic polynomial]]** (Thm 4.8): eigenvalues are exactly the roots of $p_\mathbf{A}(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I})$.
- **Algebraic multiplicity** (Def. 4.9): the number of times $\lambda$ appears as a root of $p_\mathbf{A}$.
- **Geometric multiplicity** (Def. 4.11): the number of independent eigenvectors for $\lambda$ = $\dim$ of the [[Eigenspace]] $E_\lambda$. Always $\geq 1$, never exceeds algebraic multiplicity; if strictly less, the matrix is [[DefectiveMatrix|defective]] (Example 4.6).
- **Geometry**: an eigenvector for a nonzero $\lambda$ points in a direction *stretched* by the mapping; $\lambda$ is the stretch factor (negative ⇒ flipped).
- **Properties**: $\mathbf{A}$ and $\mathbf{A}^\top$ share eigenvalues; similar matrices share eigenvalues (basis-invariant — a [[SimilarityTransform]] preserves them); [[SymmetricPositiveDefiniteMatrix|SPD]] matrices have positive, real eigenvalues; the [[SpectralTheorem|spectral theorem]] (Thm 4.15) gives symmetric matrices a *real* spectrum and an orthonormal eigenbasis.
- **Determinant & trace identities** (Thms 4.16–4.17): $\det(\mathbf{A})=\prod_i\lambda_i$ (product) and $\operatorname{tr}(\mathbf{A})=\sum_i\lambda_i$ (sum), with $\lambda_i\in\mathbb{C}$.
- The set of all eigenvalues is the **eigenspectrum / spectrum** (Def. 4.10); descending-order convention is common in software (Remark, p. 105) but not assumed by MML.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.2 canonical reference (Def. 4.6, Thm 4.8).
- [[Eigenvector]] — the associated vector. [[Eigenspace]] — the subspace of all eigenvectors for $\lambda$.
- [[CharacteristicPolynomial]] — roots are the eigenvalues. [[DefectiveMatrix]] — geometric < algebraic multiplicity.
- [[SpectralTheorem]] / [[Eigendecomposition]] / [[Diagonalization]] — what eigenvalues enable.
- [[PowerMethod]] — the iterative algorithm for the dominant eigenvalue.
- [[MatrixMultiplication]] — eigenvalue computation reduces to iterated matrix operations.
- [[Determinant]] — eigenvalues satisfy $\det(A - \lambda I) = 0$ (characteristic polynomial).
- [[MatrixTranspose]] — for symmetric A, the eigenvector matrix U satisfies $U^{-1} = U'$.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6 primary source.
- [[parproc-appB-matrix-algebra]] — §B.6 formal definition and diagonalizability conditions.
