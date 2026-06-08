---
title: "Determinant and permanent (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, combinatorics, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determinant_and_permanent
---

## Summary
The task asks the programmer to compute both the determinant and the permanent of a square matrix. Both are defined as a sum over all permutations of products of matrix entries; the only difference is that the determinant weights each term by the sign (parity) of the permutation, while the permanent omits the sign entirely. The key insight is that this shared structure makes the two quantities almost identical to define, yet computationally very different: the determinant has fast O(n^3) algorithms (LU decomposition, Bareiss), whereas the permanent is known to be hard (#P-complete) with no comparably efficient general method.

## Task Requirements
- Given a square matrix, return its determinant.
- Given the same matrix, return its permanent.
- The determinant uses the signed sum over permutations (sign = +1 for even number of inversions, -1 otherwise); the permanent uses the unsigned sum.
- Optionally, for a matrix of orthonormal basis vectors, return the Levi-Civita symbol of the permutation.

## Language Coverage
62 languages implement this task, spanning systems and functional languages alongside math-oriented and stack-based ones. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Mathematica/Wolfram Language, J, Racket, and Forth.

## Connections
- [[Determinant]] — the signed permutation sum being computed.
- [[Permanent]] — the unsigned counterpart, #P-complete in general.
- [[ParityOfAPermutation]] — supplies the sign used in the determinant.
- [[LaplaceExpansion]] — a common cofactor-expansion method for both quantities.
- [[LUDecomposition]] — the O(n^3) factorization approach for the determinant.

## Contradictions
- None — reference task page.
