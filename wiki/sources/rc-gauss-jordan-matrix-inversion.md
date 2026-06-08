---
title: "Gauss-Jordan matrix inversion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gauss-Jordan_matrix_inversion
---

## Summary
This task asks the programmer to compute the inverse of an arbitrary n × n matrix A using the Gauss-Jordan elimination method. The key insight is to augment A with the identity matrix and apply row operations until the left block becomes the identity; the right block is then the inverse. This requires handling pivot selection (ideally partial pivoting for numerical stability) to avoid division by zero or amplification of rounding error.

## Task Requirements
- Invert a given square matrix A of dimension n × n.
- Use the Gauss-Jordan elimination method specifically (not other inversion approaches).

## Language Coverage
46 languages implement this task, spanning systems and scientific languages alongside array/math-oriented ones. Representative entries include C, C++, Rust, Go, Java, Python, Fortran, Haskell, Julia, R, MATLAB, and J.

## Connections
- [[GaussianElimination]] — the row-reduction procedure Gauss-Jordan extends to reduced row echelon form
- [[MatrixInverse]] — the result this task computes
- [[LinearAlgebra]] — the broader field of matrix operations
- [[PartialPivoting]] — the pivot-selection strategy that stabilizes the elimination numerically
- [[IdentityMatrix]] — augmented alongside A to drive the reduction

## Contradictions
- None — reference task page.
