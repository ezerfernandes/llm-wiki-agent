---
title: "Cholesky decomposition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, numerical-methods, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cholesky_decomposition
---

## Summary
The task asks the programmer to implement Cholesky decomposition: factoring a symmetric, positive-definite matrix A into the product L·Lᵀ, where L is a unique lower-triangular matrix (a generalized "square root" of A). The key insight is the entries of L can be computed directly with a simple closed-form recurrence — diagonal entries via a square root of the residual, off-diagonal entries via a scaled subtraction — so no iterative solver is needed.

## Task Requirements
- Implement a routine returning the lower Cholesky factor L for any symmetric, positive-definite n×n matrix A.
- Compute diagonal elements as l_kk = √(a_kk − Σ_{j<k} l_kj²).
- Compute sub-diagonal elements as l_ik = (a_ik − Σ_{j<k} l_ij·l_kj) / l_kk.
- Test on the provided 3×3 and 4×4 example matrices and include the output.
- Note: decomposing a Pascal symmetric matrix yields the Pascal lower-triangle matrix.

## Language Coverage
76 languages implement this task, spanning systems and scientific languages, functional languages, and array/math-oriented tools. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Fortran, Julia, J, and MATLAB/Octave.

## Connections
- [[CholeskyDecomposition]] — the matrix factorization being implemented.
- [[LinearAlgebra]] — the broader field this operation belongs to.
- [[PositiveDefiniteMatrix]] — the precondition on the input matrix A.
- [[TriangularMatrix]] — the lower-triangular form of the output factor L.
- [[NumericalMethods]] — used to solve linear systems and in Monte Carlo simulation.

## Contradictions
- None — reference task page.
