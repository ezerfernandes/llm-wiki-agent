---
title: "Padovan n-step number sequences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Padovan_n-step_number_sequences
---

## Summary
This task generalizes the Padovan sequence the way the Fibonacci n-step sequences generalize Fibonacci. For each step count n, the recurrence sums the previous n terms but skips the immediately preceding term: R(N, x) = R(N, x-2) + R(N, x-3) + ... + R(N, x-N-1). The key insight is the bootstrapping rule: the base case n=2 starts with 1,1,1, and each higher n-step sequence seeds itself with the first N+1 terms of the (N-1)-step sequence before applying its own recurrence.

## Task Requirements
- Write a function that generates the first t terms of each Padovan n-step sequence for n in the range 2..max_n.
- For n == 2: start 1,1,1 and use R(n,x) = R(n,x-2) + R(n,x-3).
- For n == N: seed with the first N+1 terms of the (N-1)-step sequence, then use R(N,x) = sum of R(N,x-2) through R(N,x-N-1).
- Print at least the first t=15 values for each of the 2..8 step sequences (OEIS column omitted).

## Language Coverage
34 languages implement this task, spanning systems and functional languages to scripting and array-oriented ones. Representative implementations include C, C++, Rust, Go, Java, Haskell, J, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[PadovanSequence]] — the base sequence this task generalizes
- [[FibonacciNStepNumberSequences]] — the analogous Fibonacci generalization that motivates the construction
- [[RecurrenceRelation]] — each sequence is defined by a linear recurrence over the prior n terms
- [[DynamicProgramming]] — terms are built bottom-up from earlier computed values
- [[IntegerSequences]] — the rows correspond to OEIS entries such as Narayana's cows sequence

## Contradictions
- None — reference task page.
