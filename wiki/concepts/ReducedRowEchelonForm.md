---
title: "Reduced Row-Echelon Form"
type: concept
tags: [linear-algebra, numerical-methods]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Reduced Row-Echelon Form

A matrix is in *reduced row-echelon form* (RREF; also *row-reduced echelon form* or *row canonical form*) if ([[mml-ch02-linear-algebra|MML Ch 2]] §2.3.2 Remark, p. 31):

1. it is in [[RowEchelonForm|row-echelon form]];
2. every [[Pivot|pivot]] is **1**;
3. each pivot is the **only non-zero entry in its column**.

RREF is the canonical target of [[GaussianElimination|Gaussian elimination]] — indeed, MML *defines* Gaussian elimination as "an algorithm that performs elementary transformations to bring a system of linear equations into reduced row-echelon form."

## Why RREF matters

- It makes reading off the **general solution** of a system straightforward (MML §2.3.3): non-pivot columns are directly expressible as combinations of the pivot columns to their left.
- It enables the **Minus-1 Trick** (Eqs. 2.51–2.55): augment the RREF matrix with rows $[0\cdots0\,{-1}\,0\cdots0]$ so the diagonal holds 1 or $-1$; the columns with $-1$ on the diagonal form a [[Basis|basis]] of the [[NullSpace|kernel/null space]] (the general solution of $\mathbf{A}\mathbf{x}=\mathbf{0}$).
- It computes the [[MatrixInverse|inverse]]: $[\mathbf{A}\,|\,\mathbf{I}_n]\rightsquigarrow[\mathbf{I}_n\,|\,\mathbf{A}^{-1}]$ (Eq. 2.56).

## Example (MML Eq. 2.49)

$\mathbf{A}=\begin{bmatrix}\mathbf{1}&3&0&0&3\\0&0&\mathbf{1}&0&9\\0&0&0&\mathbf{1}&-4\end{bmatrix}$ is in RREF (pivots in bold); columns 1, 3, 4 are pivot columns, columns 2 and 5 are non-pivot columns expressible via the pivots on their left.

## Connections

- [[RowEchelonForm]] — the weaker prerequisite form.
- [[GaussianElimination]] — defined as producing RREF.
- [[NullSpace]] — read off the kernel via the Minus-1 Trick.
- [[MatrixInverse]] — augmented-matrix inversion targets RREF.
- [[Pivot]] — every RREF pivot is 1 and column-unique.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.3.2–2.3.3 canonical reference.
