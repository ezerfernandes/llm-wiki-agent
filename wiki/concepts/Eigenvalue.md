---
title: "Eigenvalue"
type: concept
tags: [linear-algebra, mathematics, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Eigenvalue

A scalar $\lambda$ such that $Av = \lambda v$ for some nonzero vector $v$ (the corresponding [[Eigenvector|eigenvector]]). For a symmetric matrix, all eigenvalues are real. The set of eigenvalues is the **spectrum** of A.

In practical parallel computing, eigenvalue problems arise in document retrieval (web search via PageRank), text mining, social network analysis, and statistical methods. The large scale of these problems — matrices with millions of rows — motivates parallel computation.

## Parallel Methods

- **[[PowerMethod|Power method]]:** Iterative; finds the dominant eigenvalue $\lambda_1$ and eigenvector $v_1$; extended to further eigenpairs via deflation.
- **SVD via CULA:** The CULA library (CUDA-based, not NVIDIA) provides singular value decomposition routines. Singular values are related to eigenvalues (they are the square roots of eigenvalues of $A^T A$); for symmetric positive semidefinite A, singular values equal eigenvalues. The R `gputools` package provides an interface to CULA's SVD.

## Note on Singular Values

Matloff (Ch11, footnote 1) writes that "singular value is a synonym for eigenvalue," which holds for symmetric positive semidefinite matrices but is an oversimplification in general.

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

## Connections

- [[Eigenvector]] — the associated vector.
- [[PowerMethod]] — the iterative algorithm for the dominant eigenvalue.
- [[MatrixMultiplication]] — eigenvalue computation reduces to iterated matrix operations.
- [[Determinant]] — eigenvalues satisfy $\det(A - \lambda I) = 0$ (characteristic polynomial).
- [[MatrixTranspose]] — for symmetric A, the eigenvector matrix U satisfies $U^{-1} = U'$.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6 primary source.
- [[parproc-appB-matrix-algebra]] — §B.6 formal definition and diagonalizability conditions.
