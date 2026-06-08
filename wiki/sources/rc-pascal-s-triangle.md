---
title: "Pascal's triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pascal's_triangle
---

## Summary
Pascal's triangle is a triangular array where each element is either 1 (at the edges) or the sum of the two elements directly above it. Row n holds the coefficients of the binomial expansion of (x + y)^n. The task asks the programmer to write a function that prints the first n rows. The key insight is that each entry can be computed either by summing the two parents from the previous row or directly as a binomial coefficient C(n, k).

## Task Requirements
- Write a function that prints the first n rows of the triangle.
- Row indexing starts at 0 at the top; f(1) yields the single-element row "1".
- Each interior element equals the sum of the two elements above it; edge elements are 1.
- Implementation may sum elements from previous rows or use a binomial/combination function.
- Behavior for n ≤ 0 need not be uniform but should be noted.

## Language Coverage
150 languages implement this task, spanning low-level assembly to high-level functional and array languages. Representative implementations include C, Python, Java, Haskell, Rust, J, APL, Common Lisp, Forth, and REXX.

## Connections
- [[BinomialCoefficient]] — each row entry equals C(n, k)
- [[Combinatorics]] — the triangle enumerates combinations
- [[Recursion]] — rows are naturally defined recursively from the prior row
- [[DynamicProgramming]] — summing parents reuses previously computed rows
- [[NumberTheory]] — divisibility and patterns within the triangle

## Contradictions
- None — reference task page.
