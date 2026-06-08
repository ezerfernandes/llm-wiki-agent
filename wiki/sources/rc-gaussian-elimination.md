---
title: "Gaussian elimination (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gaussian_elimination
---

## Summary
The task is to solve the linear system Ax = b, where A is an n-by-n matrix and x and b are n-by-1 vectors, by applying Gaussian elimination followed by back substitution. The key insight is that to maintain numerical accuracy, the implementation should employ partial pivoting (swapping rows so the largest available element becomes the pivot) along with scaling, rather than naively eliminating in place.

## Task Requirements
- Solve Ax = b for the unknown vector x.
- A is an n-by-n matrix; x and b are n-by-1 vectors.
- Use forward elimination to reduce A to upper-triangular form, then perform backward substitution to recover x.
- Apply partial pivoting and scaling to improve numerical accuracy.

## Language Coverage
59 languages implement this task, spanning systems languages, array/math languages, and assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Fortran, Haskell, J, MATLAB, Julia, and 360 Assembly.

## Connections
- [[GaussianElimination]] — the core algorithm the task names.
- [[LinearAlgebra]] — solving systems of linear equations.
- [[PartialPivoting]] — the row-selection strategy required for numerical stability.
- [[BackSubstitution]] — the final step that extracts the solution from the triangular system.
- [[NumericalStability]] — the motivation for pivoting and scaling.

## Contradictions
- None — reference task page.
