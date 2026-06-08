---
title: "Kronecker product (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kronecker_product
---

## Summary
This task asks the programmer to implement the Kronecker product of two arbitrary-sized matrices, producing a block matrix. The key insight is that the Kronecker product of an m×n matrix A with a p×q matrix B yields an (mp)×(nq) matrix in which each scalar entry A[i][j] is replaced by the entire submatrix A[i][j]·B. It is a generalization of the outer product to matrices.

## Task Requirements
- Compute the Kronecker product of two matrices of arbitrary dimensions.
- The result must be a block matrix where block (i,j) equals A[i][j] times B.
- Demonstrate correctness on two given test cases: a 2×2 with a 2×2 (from Wikipedia), and a 3×3 with a 3×4 binary matrix.

## Language Coverage
65 languages implement this task, spanning array/matrix-oriented languages, general-purpose languages, and assembly. Representative implementations include APL, J, Julia, Python, Mathematica/Wolfram Language, Octave, R, C, Go, Haskell, and Rust.

## Connections
- [[KroneckerProduct]] — the matrix operation being implemented
- [[MatrixMultiplication]] — related but distinct matrix combination
- [[OuterProduct]] — the Kronecker product generalizes it to matrices
- [[LinearAlgebra]] — the mathematical domain
- [[BlockMatrix]] — the structural form of the result

## Contradictions
- None — reference task page.
