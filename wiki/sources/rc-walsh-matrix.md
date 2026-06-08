---
title: "Walsh matrix (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrices, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Walsh_matrix
---

## Summary
The task asks for a routine that, given a natural number k, builds a naturally ordered Walsh matrix of order 2^k — a square matrix of +1/-1 entries whose rows and columns are mutually orthogonal. The key insight is the recursive (self-similar) structure: each larger matrix is the Kronecker product of the 2x2 base matrix with the next-smaller Walsh matrix, equivalent to tiling four copies of W(2^(k-1)) and negating the bottom-right block.

## Task Requirements
- Write a routine that, given natural number k, returns a naturally ordered Walsh matrix of order 2^k.
- Display a few sample generated matrices (text using 1/-1, or green/red blocks in image mode).
- Stretch goal: optionally generate sequency ordered Walsh matrices, with rows sorted by the number of sign changes.

## Language Coverage
32 languages implement this task, spanning systems, functional, array, and scripting families. Representative examples include C++, Rust, Go, Haskell, Julia, Python, MATLAB, J, Perl, and Raku.

## Connections
- [[WalshMatrix]] — the central mathematical object being generated.
- [[HadamardMatrix]] — Walsh matrices are a special (reordered) case of Hadamard matrices.
- [[KroneckerProduct]] — the recursive construction is a repeated Kronecker product with the 2x2 base.
- [[Orthogonality]] — the defining property that rows and columns have zero pairwise dot product.
- [[Recursion]] — the natural divide-and-conquer formulation of the matrix.

## Contradictions
- None — reference task page.
