---
title: "Matrix multiplication (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, numerical-computing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Matrix_multiplication
---

## Summary
The task asks the programmer to multiply two matrices together, where the matrices may be of any dimensions as long as the number of columns of the first matrix equals the number of rows of the second. The key insight is the standard dot-product rule: each entry of the result is the dot product of a row from the first matrix with a column from the second, yielding an m×p result from m×n and n×p inputs.

## Task Requirements
- Multiply two given matrices and produce their product.
- Support arbitrary dimensions, not just square matrices.
- Respect the conformability constraint: columns of the first matrix must equal rows of the second.

## Language Coverage
133 languages implement this task, reflecting very broad coverage spanning systems, scripting, functional, and array-oriented languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, J, APL, MATLAB, Fortran, and Julia.

## Connections
- [[MatrixMultiplication]] — the core operation being implemented
- [[LinearAlgebra]] — the mathematical domain of matrices
- [[DotProduct]] — each result entry is a row-by-column dot product
- [[NumericalComputing]] — performance-sensitive numeric kernel

## Contradictions
- None — reference task page.
