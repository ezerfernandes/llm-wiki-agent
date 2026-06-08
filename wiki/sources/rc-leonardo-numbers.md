---
title: "Leonardo numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, integer-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Leonardo_numbers
---

## Summary
The Leonardo numbers are an integer sequence defined by L(0)=1, L(1)=1, and L(n)=L(n-1)+L(n-2)+1 for n>1, yielding 1, 1, 3, 5, 9, 15, 25, 41, 67, ... They are closely tied to the Fibonacci numbers via the closed form L(n) = 2·Fib(n+1) − 1, and were used by Edsger Dijkstra as the basis of his smoothsort algorithm. The task asks the programmer to generate the sequence while exposing its parameters so the same generator can also reproduce Fibonacci.

## Task Requirements
- Show the first 25 Leonardo numbers, starting at L(0), using the recurrence L(n) = L(n-1) + L(n-2) + 1.
- Allow the first two values L(0) and L(1) to be specified.
- Allow the "add" constant (default 1) to be configurable.
- Re-run the generator with L(0)=0, L(1)=1, and add=0 to produce the first 25 Fibonacci numbers, demonstrating the parameterized generalization.

## Language Coverage
85 languages implement this task, spanning a broad mix of systems, scripting, functional, and assembly languages. Representative examples include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, Common Lisp, Forth, REXX, and AArch64 Assembly.

## Connections
- [[FibonacciNumber]] — Leonardo numbers equal 2·Fib(n+1) − 1, and the parameterized generator reduces to Fibonacci.
- [[Recurrence]] — the sequence is defined by a two-term additive recurrence relation.
- [[Smoothsort]] — Dijkstra's heap-based sorting algorithm uses Leonardo numbers to size its heaps.
- [[IntegerSequence]] — catalogued as OEIS A001595.

## Contradictions
- None — reference task page.
