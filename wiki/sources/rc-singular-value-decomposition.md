---
title: "Singular value decomposition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrix-decomposition, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Singular_value_decomposition
---

## Summary
The task asks the programmer to compute the singular value decomposition (SVD) of an arbitrary m-by-n matrix A, factoring it as A = U·Σ·Vᵀ where U and V are orthogonal matrices and Σ is a diagonal matrix of non-negative singular values. The key insight is that SVD succeeds where eigendecomposition fails: it produces orthogonal singular vectors, always exists, and works for rectangular (non-square) matrices, making it a universal diagonalization tool.

## Task Requirements
- Read two integers m and n (the matrix dimensions).
- Read the m-by-n matrix A.
- Output the three factors U, Σ, and V corresponding to A.
- Handle the general rectangular case, not just square matrices.
- Implementing the algorithm yourself is encouraged, though using a library is acceptable.
- Output sign/values may legitimately vary with data-type and convention choices.

## Language Coverage
16 languages implement this task. Coverage spans systems and numeric languages plus array/math specialists; representative implementations include C, C++, Go, Java, Julia, Python, Perl, Raku, Scheme, and Wolfram Language (Mathematica), with J and Phix among the more specialized entries.

## Connections
- [[SingularValueDecomposition]] — the matrix factorization this task directly implements.
- [[LinearAlgebra]] — the broader field providing the orthogonal-matrix and diagonalization machinery.
- [[Eigendecomposition]] — the related decomposition SVD generalizes by avoiding its limitations.
- [[MatrixDecomposition]] — the family of factorizations to which SVD belongs.
- [[OrthogonalMatrix]] — the structure of the U and V factors produced.

## Contradictions
- None — reference task page.
