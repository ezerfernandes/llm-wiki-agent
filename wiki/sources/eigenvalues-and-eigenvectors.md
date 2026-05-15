---
title: "Eigenvalues and Eigenvectors"
type: source
tags: [math, vectors-and-matrices]
date: 2026-05-10
source_file: raw/vectors-and-matrices/eigenvalues-and-eigenvectors.md
---

## Summary
A linear transformation, represented by a square [[matrices|matrix]] \\(A\\), acts on vectors by moving them in space. It can stretch, compress, rotate, or reflect them, and in general the image of a [[vectors|vector]] points in a different direction from the original. Among all vectors however there are those for which the action of \\(A\\) is particularly simple. The transformation scales them by a constant factor, leaving their direction unchanged. Such vectors are called eigenvectors of \\(A\\), and the corresponding scaling factors are called eigenvalues.

## Key Claims
- **The characteristic equation** — Rewriting the eigenvalue equation as \\((A - \lambda I)\mathbf{v} = \mathbf{0}\\), where \\(I\\) is the identity matrix of order \\(n\\), it is clear that a non-zero solution \\(\mathbf{v}\\) exists precisely when the matrix \\(A - \lambda…
- **Eigenspaces** — For each eigenvalue \\(\lambda_0\\), the [[sets|set]] of all vectors satisfying \\(A\mathbf{v} = \lambda_0\mathbf{v}\\) is a subspace of \\(\mathbb{R}^n\\) or \\(\mathbb{C}^n\\).
- **Example 1** — Consider the following [[matrices|matrix]]:
- **Example 2** — Consider the matrix
- **Linear independence of eigenvectors** — Eigenvectors corresponding to distinct eigenvalues are always linearly independent.
- **Diagonalization** — A matrix \\(A\\) of order \\(n\\) is called diagonalizable if it can be written in the form
- **Trace, determinant and eigenvalues** — Let \\(\lambda_1, \lambda_2, \ldots, \lambda_n\\) be the eigenvalues of \\(A\\) counted with algebraic multiplicity.

## Key Quotes
> Source page: algebrica.org — see `source_file`.

## Connections
- [[matrices|Matrices]] — matrix
- [[vectors|Vectors]] — vector
- [[unit-circle|UnitCircle]] — unit circle
- [[Ellipse]] — ellipse
- [[sets|Sets]] — set
- [[polynomials|Polynomials]] — polynomial
- [[determinant-of-a-square-matrix|Determinant]] — determinant
- [[rank-of-a-matrix|RankOfAMatrix]] — linearly independent

## Contradictions
None.
