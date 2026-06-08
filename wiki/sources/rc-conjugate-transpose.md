---
title: "Conjugate transpose (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, complex-numbers, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Conjugate_transpose
---

## Summary
Given a matrix of complex numbers, compute its conjugate transpose (the Hermitian transpose) M^H, formed by transposing the matrix and replacing each entry with its complex conjugate so that (M^H)_ji = conjugate(M_ij). The task then asks the solver to classify a square matrix by checking properties defined in terms of M^H. The key insight is that several important matrix classes are characterized purely by their relationship to the conjugate transpose.

## Task Requirements
- Compute the conjugate transpose M^H of a given matrix of complex numbers (transpose, then conjugate every entry).
- Determine whether the matrix is Hermitian: M^H = M.
- Determine whether the matrix is normal: M^H M = M M^H.
- Determine whether the matrix is unitary: M^H = M^-1, equivalently M^H M = I_n (or M M^H = I_n).

## Language Coverage
43 languages implement this task, spanning numerics-oriented and general-purpose languages. Representative implementations include Python, Julia, R, Fortran, Haskell, J, C++, Go, Rust, Mathematica/Wolfram Language, and APL-style array dialects, several of which lean on built-in complex-number and matrix support.

## Connections
- [[ComplexNumbers]] — entries are complex; the conjugate is taken element-wise.
- [[MatrixTranspose]] — the conjugate transpose extends ordinary transposition.
- [[HermitianMatrix]] — defined as a matrix equal to its own conjugate transpose.
- [[MatrixMultiplication]] — needed to test the normal and unitary conditions.
- [[LinearAlgebra]] — these classifications underpin spectral theory and orthogonality.

## Contradictions
- None — reference task page.
