---
title: "Trabb Pardo–Knuth algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numeric-computation, input-output]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Trabb_Pardo–Knuth_algorithm
---

## Summary
The TPK algorithm is a tiny program-comparison exercise (a "chrestomathy") introduced by Donald Knuth and Luis Trabb Pardo in their 1976 Stanford report tracing the early development of programming languages. The task reads 11 numbers, reverses the sequence, applies a function to each, and prints results in reverse order while handling an overflow condition. Its value lies not in difficulty but in exercising the basic features common to most languages: input, arrays, loops, functions, conditionals, and output.

## Task Requirements
- Read 11 numeric inputs into a sequence `S`, printing a prompt beforehand.
- Apply the function `f(x) = |x|^0.5 + 5x^3` to each item.
- Treat any result greater than 400 as an overflow and alert the user, without halting processing of remaining items.
- Output results in reverse order of input (the sequence may be reversed or processed back-to-front; `S` itself need not be shown).
- Optionally print each item alongside its result, and show a typical run.

## Language Coverage
82 languages implement this task, reflecting broad coverage across paradigms and eras given the algorithm's historical role. Representative implementations include ALGOL 60, Fortran, C, C++, Java, Python, Haskell, Common Lisp, Rust, and REXX.

## Connections
- [[NumericalComputation]] — evaluating a real-valued function with a square root and cubic term
- [[ArrayProcessing]] — reading into and traversing a fixed-length sequence
- [[OverflowHandling]] — guarding output against an out-of-range threshold
- [[ProgrammingChrestomathy]] — the comparative-programming tradition this task embodies

## Contradictions
- None — reference task page.
