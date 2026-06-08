---
title: "LU decomposition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrices, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/LU_decomposition
---

## Summary
The task asks the programmer to factor a square n×n matrix A into the product of a lower triangular matrix L and an upper triangular matrix U, a modified form of Gaussian elimination. Because dividing by a small or zero pivot causes numerical instability, the routine must also perform partial pivoting: rows are reordered (captured in a permutation matrix P) so the largest element of each column lands on the diagonal, giving PA = LU. The key insight is that with L's diagonal fixed to 1 (Crout's convention), the 9-unknown 3×3 system becomes uniquely solvable and generalizes to recurrence formulas for u_ij and l_ij.

## Task Requirements
- Implement a routine taking a square n×n matrix A and returning L (lower triangular), U (upper triangular), and a permutation matrix P such that PA = LU.
- Use partial pivoting to move the largest element of each column onto the diagonal before decomposing, ensuring numerical stability.
- Fix the diagonal of L to 1 so the system is uniquely solvable.
- Test on the two provided example matrices (a 3×3 and a 4×4) and include the resulting L, U, and P in the output.

## Language Coverage
48 languages implement this task, spanning systems languages, functional languages, array/math environments, and scripting languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, J, MATLAB / Octave, Fortran, and Mathematica / Wolfram Language.

## Connections
- [[LUDecomposition]] — the matrix factorization the task implements
- [[GaussianElimination]] — the underlying elimination procedure LU decomposition modifies
- [[PartialPivoting]] — row reordering via the permutation matrix P for numerical stability
- [[CroutsAlgorithm]] — the specific derivation fixing L's diagonal to 1
- [[CholeskyDecomposition]] — related but restricted to symmetric positive-definite matrices

## Contradictions
- None — reference task page.
