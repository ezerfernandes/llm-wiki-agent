---
title: "Matrix chain multiplication (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, optimization, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Matrix_chain_multiplication
---

## Summary
The task asks the programmer to find the cheapest way to parenthesize a chain of matrix multiplications. Because matrix product is associative but not commutative, the parenthesization can be reordered, and different orders yield wildly different operation counts (multiplying an (n1,n2) by an (n2,n3) matrix costs n1*n2*n3 FMA operations). The key insight is that brute-force enumeration of all parenthesizations grows like a Catalan number, so the optimal solution is the classic O(n^3) dynamic-programming algorithm that memoizes subchain costs.

## Task Requirements
- Write a function taking a list of n+1 successive matrix dimensions (shared dimensions not duplicated) representing a product of n matrices.
- Return both the optimal parenthesization (any sensible description) and its total scalar-multiplication cost.
- The function must handle chains of arbitrary length.
- Test on `[1, 5, 25, 30, 100, 70, 2, 1, 100, 250, 1, 1000, 2]` and `[1000, 1, 500, 12, 1, 700, 2500, 3, 2, 5, 14, 10]`.
- Dynamic programming is the intended approach; full enumeration is allowed but discouraged due to duplicated work.

## Language Coverage
31 languages implement this task, spanning systems languages, functional languages, and scientific computing environments. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Julia, J, MATLAB, Mathematica, and Raku.

## Connections
- [[DynamicProgramming]] — the canonical optimal-substructure technique used to solve it
- [[MatrixMultiplication]] — the underlying operation whose cost is being minimized
- [[CatalanNumbers]] — counts the exponential number of distinct parenthesizations
- [[Memoization]] — caches subchain costs to avoid recomputation
- [[Optimization]] — the task minimizes total FMA operation count

## Contradictions
- None — reference task page.
