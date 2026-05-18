---
title: "Power Method"
type: concept
tags: [linear-algebra, numerical-methods, parallel-computing, eigenvalues]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Power Method

An iterative algorithm for finding the dominant [[Eigenvalue|eigenvalue]] and [[Eigenvector|eigenvector]] of a matrix.

## Algorithm

Given an $n \times n$ matrix A with eigenvalues $|\lambda_1| \geq |\lambda_2| \geq \ldots \geq |\lambda_n|$, start with a nonzero vector $x$ and iterate:

$$x^{(k)} = \frac{A^k x}{\|A^k x\|}$$

Under mild conditions, $x^{(k)}$ converges to $v_1$ (the eigenvector for $\lambda_1$), and $(Ax^{(k)})' x^{(k)}$ converges to $\lambda_1$.

For symmetric matrices (common in statistical applications), eigenvalues are real and eigenvectors are orthogonal.

## Deflation

To find subsequent eigenpairs, form the deflated matrix:

$$B = A - \lambda_1 v_1 v_1'$$

The eigenvalues of B are $\lambda_2, \ldots, \lambda_n, 0$. Apply the power method to B to obtain $\lambda_2$ and $v_2$, and repeat.

## Parallel Computation

The dominant cost per iteration is the matrix-vector product $Ax^{(k)}$, which parallelizes via the methods in §11.3. The "log method" (repeated squaring) from §11.4 can accelerate convergence by computing $A^{2^t}$ rather than stepping by single applications of A.

## Applications

Used in Google's PageRank algorithm, which requires only the dominant eigenvector. The CULA library (CUDA-based) provides SVD routines accessible via R's `gputools` package.

## Connections

- [[Eigenvalue]] — the quantity the power method converges to.
- [[Eigenvector]] — the vector the power method converges to.
- [[MatrixMultiplication]] — the matrix-vector product is the inner loop.
- [[MatrixVectorMultiply]] — the specific operation at each iteration.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6.1 primary source.
