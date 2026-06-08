---
title: "Ackermann function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ackermann_function
---

## Summary
The task is to implement the two-argument Ackermann function A(m, n), a classic example of recursion that is famously total (it always terminates for non-negative arguments) yet is not primitive recursive. The key insight is that its values and the depth of its call tree explode extremely quickly — even modest inputs like A(4, 1) produce enormous numbers — so arbitrary-precision arithmetic is preferred though not required.

## Task Requirements
- Write a function returning the value of A(m, n) for non-negative integer arguments.
- Implement the standard three-case recurrence: n+1 when m=0; A(m-1, 1) when m>0 and n=0; A(m-1, A(m, n-1)) when m>0 and n>0.
- Arbitrary-precision (bignum) output is preferred since the function grows so fast, but not mandatory.

## Language Coverage
261 languages implement this task — one of Rosetta Code's most broadly covered tasks, spanning everything from assembly to functional and esoteric languages. Representative implementations include C, Python, Haskell, Java, Rust, Common Lisp, Prolog, Scheme, Forth, and APL.

## Connections
- [[Recursion]] — the canonical motivating example, with deeply nested recursive calls.
- [[PrimitiveRecursiveFunctions]] — the Ackermann function is the standard example of a total computable function that is not primitive recursive.
- [[ComputabilityTheory]] — central to discussions of what recursive functions can compute beyond primitive recursion.
- [[Memoization]] — a common optimization to tame the redundant call tree.
- [[ConwayChainedArrowNotation]] — relates the function to fast-growing hierarchies and hyperoperations.

## Contradictions
- None — reference task page.
