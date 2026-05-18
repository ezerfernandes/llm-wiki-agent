---
title: "ParProcBook Appendix B: Review of Matrix Algebra"
type: source
tags: [textbook, parallel-computing, matrix-algebra, linear-algebra, r]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
sources: []
last_updated: 2026-05-17
---

## Summary

Appendix B (book pp. 313–320) of *Programming on Parallel Machines* by [[NormMatloff]] is a self-contained review of matrix algebra intended as a primer for readers whose background is thin. It covers eight topics in tight succession: notation and basic operations, transpose, linear independence, determinants, matrix inverse, eigenvalues and eigenvectors, rank, and R syntax for all of the above. The appendix is explicitly a reference rather than a novel contribution; its role in the book is to ground the parallel algorithms in Chapters 11–14 in formal definitions.

## Key Claims

- A matrix is a rectangular array; a vector is a single-row or single-column matrix. The (i,j) element of product C = AB equals the inner product of row i of A and column j of B: $c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$.
- Matrix multiplication is associative and distributive but not commutative in general: $AB \neq BA$.
- The transpose of A, written $A'$ or $A^T$, exchanges rows and columns; key identities: $(A+B)' = A'+B'$ and $(AB)' = B'A'$.
- Vectors $X_1, \ldots, X_k$ are linearly independent if $a_1 X_1 + \cdots + a_k X_k = 0$ implies all $a_i = 0$.
- The determinant of an $n \times n$ matrix is computed recursively: $\det(A) = \sum_{m=1}^{n} (-1)^{k+m} \det(A_{-(k,m)})$, where $A_{-(k,m)}$ is the submatrix with row k and column m deleted. Base case: $\det\begin{pmatrix}s&t\\u&v\end{pmatrix} = sv - tu$.
- $A^{-1}$ exists if and only if $\det(A) \neq 0$, equivalently iff the rows (or columns) of A are linearly independent. For conformable invertible square A and B: $(AB)^{-1} = B^{-1}A^{-1}$.
- A matrix U is orthogonal if its rows all have norm 1 and are mutually orthogonal (inner product 0); this implies $UU' = I$, i.e. $U^{-1} = U'$.
- QR decomposition: for any A, write $A = QR$ with Q orthogonal and R upper-triangular; then $A^{-1} = R^{-1}Q'$. This is the practical alternative to direct inversion and is accessible in R via `qr()` and `qr.solve()`.
- A scalar $\lambda$ and nonzero vector X satisfying $AX = \lambda X$ are an eigenvalue and eigenvector of A. If A is symmetric and real it is diagonalizable: there exists an orthogonal U such that $U'AU = D$ (diagonal), where D's diagonal entries are the eigenvalues and U's columns are the eigenvectors.
- A sufficient condition for diagonalizability (even without symmetry) is that the eigenvalues of A are all distinct; in that case U need not be orthogonal.
- The rank of A is the maximal number of linearly independent columns in A. Because $\text{rk}(A') = \text{rk}(A)$, this equals the maximal number of linearly independent rows. For an $r \times s$ matrix, $\text{rk}(A) \leq \min(r, s)$. Also $\text{rk}(A'A) = \text{rk}(A)$.
- In R, matrix multiplication uses `%*%`; transpose is `t()`; inverse is `solve()`; eigenvalues/eigenvectors are `eigen()`; QR decomposition is `qr()`. Column-major storage means extracting a single row yields a plain vector unless `drop = FALSE` is specified.

## Key Quotes

> "Generally, determinants are mainly of theoretical importance, but they often can clarify one's understanding of concepts." — §B.4

> "Typically one does not compute matrix inverses directly." — §B.5

> "Note however that although rank is clearly defined in theory, the presence of roundoff error in computation make may rank difficult to determine reliably." — §B.8

## Connections

- [[MatrixMultiplication]] — §B.1.1 gives the formal definition ($c_{ij} = \sum_k a_{ik} b_{kj}$) and the non-commutativity property.
- [[MatrixInversion]] — §B.5 introduces the identity matrix, the inverse definition, the QR route, and the back-substitution shortcut for triangular matrices.
- [[Determinant]] — §B.4 provides the recursive cofactor expansion (Eq. B.15–B.16) as a computational procedure.
- [[Eigenvalue]] — §B.6 gives the formal definition $AX = \lambda X$ and the diagonalizability conditions.
- [[Eigenvector]] — §B.6 defines the associated nonzero vector and the orthogonality property for symmetric real matrices.
- [[Rank]] — §B.7 formalizes rank as the maximal number of linearly independent columns, with the key properties $\text{rk}(A') = \text{rk}(A)$ and $\text{rk}(A'A) = \text{rk}(A)$.
- [[MatrixTranspose]] — §B.2 introduces transpose notation and the product-reversal identity $(AB)' = B'A'$.
- [[LinearIndependence]] — §B.3 defines the concept as the only-trivial-solution condition for linear combinations.
- [[NormMatloff]] — author; this appendix is the math-primer companion to Chs 11–14.
- [[parproc-ch11-parallel-matrix-operations]] — the main chapter that applies all of these definitions in parallel settings.

## Contradictions

None identified. The appendix is consistent with all prior wiki content on these topics. Note that [[Eigenvalue]] (from Ch11) carries a footnote that "singular value is a synonym for eigenvalue," which the appendix implicitly refines: §B.6 footnote 1 clarifies that for nonsquare matrices the discussion generalizes to *singular value decomposition*, not a synonym relationship.
