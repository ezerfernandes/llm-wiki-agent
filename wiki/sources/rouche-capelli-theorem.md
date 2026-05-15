---
title: "Rouché-Capelli Theorem"
type: source
tags: [math, linear-systems]
date: 2026-05-10
source_file: raw/linear-systems/rouche-capelli-theorem.md
---

## Summary
The Rouché-Capelli theorem characterizes the solvability of a [[SystemsOfLinearEquations|linear system]] in terms of two matrix invariants: the [[rank-of-a-matrix|rank]] of the coefficient matrix and the rank of the augmented matrix. Consider a linear system of \\(m\\) equations in \\(n\\) unknowns written in matrix form:

## Key Claims
- **Statement of the theorem** — The Rouché-Capelli theorem characterizes the solvability of a [[SystemsOfLinearEquations|linear system]] in terms of two matrix invariants: the [[rank-of-a-matrix|rank]] of the coefficient matrix and the rank of the augmented…
- **Geometric interpretation** — The condition \\(r(A) = r(A \mid \mathbf{b})\\) admits a transparent geometric reading in terms of [[linear-combinations|linear combinations]] of the columns of \\(A\\).
- **Proof of the consistency criterion** — The consistency part of the theorem can be proved by reducing the system to row echelon form via [[SolvingLinearSystemsUsingGaussianElimination|Gaussian elimination]] and analyzing the position of the pivots in the reduced matrix.
- **Example 1** — The following system illustrates the case of a unique solution:
- **Example 2** — The following system illustrates the case of a infinitely many solution:
- **Example 3** — The following system illustrates the case of an inconsistent system:
- **Discussion of a parametric system** — The role of the rank in the classification of solutions becomes especially transparent for systems whose coefficients depend on a parameter.
- **Homogeneous systems** — A homogeneous linear system has the form:

## Key Quotes
> Source page: algebrica.org — see `source_file`.

## Connections
- [[SystemsOfLinearEquations]] — linear system
- [[rank-of-a-matrix|RankOfAMatrix]] — rank
- [[matrices|Matrices]] — matrix
- [[SolvingLinearSystemsUsingGaussianElimination]] — gaussian elimination
- [[linear-combinations|LinearCombinations]] — linear combinations

## Contradictions
None.
