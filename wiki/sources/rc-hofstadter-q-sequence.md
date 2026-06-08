---
title: "Hofstadter Q sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, memoization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hofstadter_Q_sequence
---

## Summary
The task is to implement Hofstadter's Q sequence, defined by Q(1)=Q(2)=1 and Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2)) for n>2. Unlike the Fibonacci sequence, where each term is the sum of the two preceding terms, the two previous Q terms instead tell you how far back to reach to find the two values that are summed. This self-referential (meta-Fibonacci) definition produces chaotic, unpredictable behavior despite its simple recurrence.

## Task Requirements
- Confirm and display that the first ten terms are: 1, 1, 2, 3, 3, 4, 5, 5, 6, 6.
- Confirm and display that the 1000th term is 502.
- Optional extra credit: count how many times a term is less than its preceding term, for terms up to and including the 100,000th.
- Optional: ensure the extra-credit solution safely handles a large initial n, correctly managing caching and/or recursion limits.

## Language Coverage
109 languages implement this task, spanning a very broad mix of assembly, classic, scripting, and functional languages. Representative examples include C, C++, Python, Java, Haskell, Common Lisp, Rust, Go, Ruby, and REXX.

## Connections
- [[Recursion]] — the sequence is defined by a self-referential recurrence
- [[Memoization]] — caching computed terms is the practical way to reach large n
- [[MetaFibonacciSequence]] — Q is a canonical chaotic meta-Fibonacci sequence
- [[FibonacciSequence]] — explicitly contrasted in the task definition
- [[NumberTheory]] — integer sequence with studied combinatorial properties

## Contradictions
- None — reference task page.
