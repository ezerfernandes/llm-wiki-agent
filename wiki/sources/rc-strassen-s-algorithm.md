---
title: "Strassen's algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, divide-and-conquer]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strassen's_algorithm
---

## Summary
The task asks the programmer to implement Strassen's algorithm for matrix multiplication, a divide-and-conquer method named after Volker Strassen. Its key insight is recursively splitting each matrix into four quadrants and computing the product using only seven recursive multiplications (instead of the naive eight), yielding a sub-cubic complexity of roughly O(n^2.807). It is faster than standard matrix multiplication for large matrices but is outperformed by the asymptotically fastest known algorithms on extremely large inputs.

## Task Requirements
- Write a routine/function/procedure that implements the Strassen algorithm for matrix multiplication.
- Unlike practical implementations that switch to standard multiplication for sub-matrices below ~512x512, this task requires recursing all the way down until sub-matrices reach a size of 1 or 2 before switching.

## Language Coverage
35 languages implement this task, spanning systems, functional, scripting, and array-oriented styles. Representative examples include C++, Go, Rust, Java, Haskell, OCaml, Python, Julia, MATLAB, Wolfram Language, Raku, and Fortran.

## Connections
- [[MatrixMultiplication]] — the standard O(n^3) operation that Strassen improves upon
- [[DivideAndConquer]] — the recursive quadrant-splitting strategy underlying the algorithm
- [[LinearAlgebra]] — the mathematical domain of matrix operations
- [[ComputationalComplexity]] — the sub-cubic O(n^2.807) running time that motivates the technique

## Contradictions
- None — reference task page.
