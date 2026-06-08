---
title: "QR decomposition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, numerical-methods, matrix-decomposition]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/QR_decomposition
---

## Summary
The task asks the programmer to factor a rectangular m×n matrix A into the product of an orthogonal matrix Q and an upper-triangular matrix R, using the method of Householder reflections. Each reflection zeroes the subdiagonal entries of one column by reflecting that column onto a standard basis vector; chaining the reflections turns A into R, and their product (in reverse) gives Q. The result is then applied to solve a linear least-squares problem via back substitution.

## Task Requirements
- Decompose the given example matrix A = [[12,-51,4],[6,167,-68],[-4,24,-41]] into Q and R.
- Use Householder reflections, building each reflector H = I − β·v·vᵀ with v = u/u₁ and u = a + sign(a₁)·‖a‖₂·e₁ (the sign chosen to avoid cancellation error).
- Embed each successive reflector into an identity matrix to operate on the trailing submatrix, accumulating Hₙ…H₂H₁·A = R and H₁H₂…Hₙ = Q.
- Use the decomposition to solve a linear least-squares (polynomial/multiple regression) problem A·x = b by solving R·x = Qᵀ·b.
- For non-square R (m > n), drop the zero-padded bottom rows and back-substitute the square upper-triangular system R₁·x = q₁.

## Language Coverage
46 languages implement this task, a broad mix spanning systems, functional, array, and math-oriented languages — representative entries include C, C++, Rust, Go, Java, Haskell, Julia, Python, R, Fortran, J, and Mathematica.

## Connections
- [[QRDecomposition]] — the core matrix factorization being demonstrated.
- [[HouseholderReflection]] — the orthogonal-reflection technique mandated by the task.
- [[LinearLeastSquares]] — the application solving overdetermined systems via QR.
- [[OrthogonalMatrix]] — the property of the Q factor.
- [[BackSubstitution]] — solving the resulting upper-triangular system.

## Contradictions
- None — reference task page.
