---
title: "Pascal matrix generation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, matrices, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pascal_matrix_generation
---

## Summary
A Pascal matrix is a square matrix whose entries are binomial coefficients (nCr) drawn from Pascal's triangle. The task asks for functions that generate three n-by-n forms: an upper-triangular matrix M[i,j] = C(j,i), a lower-triangular matrix M[i,j] = C(i,j) (the transpose of the upper), and a symmetric matrix M[i,j] = C(i+j,i). The key insight is that all three are just different indexings of the same binomial-coefficient table, and the lower-triangular form is the Cholesky decomposition factor of the symmetric form.

## Task Requirements
- Write functions that generate each of the three forms of n-by-n Pascal matrix (upper-triangular, lower-triangular, symmetric).
- Use those functions to display the upper, lower, and symmetric 5-by-5 Pascal matrices.
- Output must distinguish between the different matrices and between rows of each matrix (rows shown explicitly, not as a flat list of 25 numbers).

## Language Coverage
70 languages implement this task, showing broad coverage across functional, array, and imperative paradigms. Representative implementations include Python, C, C++, Java, Haskell, J, APL, Julia, Go, Raku, and Mathematica/Wolfram Language.

## Connections
- [[BinomialCoefficient]] — every matrix entry is a binomial coefficient nCr
- [[PascalsTriangle]] — the matrices reindex the values of Pascal's triangle
- [[CholeskyDecomposition]] — the lower-triangular Pascal matrix is the Cholesky factor of the symmetric one
- [[MatrixTranspose]] — the lower-triangular form is the transpose of the upper-triangular form

## Contradictions
- None — reference task page.
