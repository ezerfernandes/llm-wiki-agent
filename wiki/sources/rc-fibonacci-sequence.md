---
title: "Fibonacci sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, memoization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fibonacci_sequence
---

## Summary
The task asks the programmer to write a function that generates the nth Fibonacci number, where each term is the sum of the two preceding ones starting from F0=0 and F1=1. The key insight is that the same definition can be implemented multiple ways with very different performance: naive recursion is exponentially slow, while iteration, memoization, or Binet's closed-form formula are efficient. The sequence can optionally be extended to negative indices via the identity F(-n) = (-1)^(n+1) F(n).

## Task Requirements
- Implement a function returning the nth Fibonacci number defined by F0=0, F1=1, Fn=Fn-1+Fn-2 for n>1.
- Solutions may be iterative, recursive, or use Binet's algebraic (closed-form) formula.
- Recursive solutions are acceptable mainly as a recursion exercise since they are slow.
- Support for negative n (via the alternating-inverse extension) is optional.

## Language Coverage
336 languages implement this task, reflecting its status as a canonical introductory exercise spanning nearly every paradigm and platform. Representative implementations include C, Python, Haskell, Java, Rust, Lisp, APL, Forth, Prolog, and assembly variants such as 6502 and x86 Assembly.

## Connections
- [[Recursion]] — the classic recursive definition and exercise
- [[Memoization]] — caching subresults to avoid exponential recomputation
- [[DynamicProgramming]] — iterative bottom-up accumulation of terms
- [[GoldenRatio]] — basis of Binet's closed-form formula
- [[NumberTheory]] — Fibonacci and related Lucas number sequences

## Contradictions
- None — reference task page.
