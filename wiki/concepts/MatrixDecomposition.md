---
title: "Matrix Decomposition"
type: concept
tags: [linear-algebra, foundational, factorization]
sources: [mml-book, mml-ch04-matrix-decompositions]
last_updated: 2026-06-04
---

# Matrix Decomposition

Factoring a matrix $\mathbf{A}$ into a product of simpler / more interpretable matrices — analogous to factoring the integer 21 into primes $7\cdot 3$ ([[mml-book]] Ch 4, p. 98).

## The MML Ch 4 taxonomy

Six related operations are framed together (Fig. 4.1 mind map):

| Operation | What it does | Section |
|---|---|---|
| [[Determinant]] | Signed volume of column parallelepiped; tests invertibility | §4.1 |
| [[Trace]] | Sum of diagonal; basis-invariant via cyclic permutation | §4.1 |
| [[CharacteristicPolynomial]] | $p_\mathbf{A}(\lambda) = \det(\mathbf{A}-\lambda\mathbf{I})$ — bridge to eigenvalues | §4.1 |
| [[Eigendecomposition]] | $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ for diagonalizable square matrices | §4.4 |
| [[CholeskyDecomposition]] | $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$ for symmetric positive-definite | §4.3 |
| [[SingularValueDecomposition]] | $\mathbf{A} = \mathbf{U}\boldsymbol\Sigma\mathbf{V}^\top$ for **any** matrix | §4.5 |

SVD generalizes eigendecomposition to non-square / non-diagonalizable matrices and is "considered one of the fundamental concepts in linear algebra" (Ch 4 intro, p. 98).

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

The full chapter deep dive develops the three threads — *summarize* ([[Determinant]], [[Trace]], [[CharacteristicPolynomial]], [[Eigenvalue|eigenvalues]]/[[Eigenvector|eigenvectors]], [[Eigenspace]]), *decompose* ([[CholeskyDecomposition]], [[Eigendecomposition]] via [[Diagonalization]] and the [[SimilarityTransform|similarity transform]], [[SingularValueDecomposition]]), and *approximate* ([[LowRankApproximation]] with the [[EckartYoung|Eckart–Young theorem]] in the [[SpectralNorm|spectral norm]]). Key cross-cutting results: the [[SpectralTheorem|spectral theorem]] (symmetric ⇒ orthonormal real eigenbasis), the [[DefectiveMatrix|defective-matrix]] obstruction to diagonalization, and the [[MatrixPhylogeny|matrix phylogeny]] (§4.7) organizing every matrix type into one taxonomy. The [[LaplaceExpansion|Laplace expansion]] computes determinants recursively (§4.1).

## Why decomposition matters for ML

- **[[CholeskyDecomposition]]** is the cheap factorization that makes Gaussian-density sampling tractable ($\boldsymbol\Sigma = \mathbf{L}\mathbf{L}^\top \Rightarrow \mathbf{L}\mathbf{z}$ samples from $\mathcal{N}(\mathbf{0}, \boldsymbol\Sigma)$).
- **[[Eigendecomposition]]** is the engine of [[PrincipalComponentAnalysis]] (Ch 10): the principal components are eigenvectors of the [[DataCovarianceMatrix]].
- **[[SingularValueDecomposition]]** is the engine of low-rank matrix approximation (§4.6) — the basis for compressed embeddings, [[LoRA]]-style adapters, and the optimal rank-$k$ Frobenius-norm approximation (Eckart-Young).

## Connections

- [[mml-book]] — Ch 4 canonical reference.
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — the full exhaustive deep dive.
- [[MatrixPhylogeny]] — the §4.7 taxonomy of matrix types and factorizations.
- [[matrix-diagonalization]] — algebrica.org's restricted version (square + diagonalizable only).
- [[determinant-of-a-square-matrix]] — algebrica.org's determinant page.
- [[eigenvalues-and-eigenvectors]] — algebrica.org's eigenvalue page.
- [[PrincipalComponentAnalysis]] — eigendecomposition application.
- [[SymmetricPositiveDefiniteMatrix]] — characterizes which matrices admit Cholesky.
