---
title: "Partition function P (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, memoization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Partition_function_P
---

## Summary
The task is to implement P(n), the partition function counting the distinct ways an integer n can be written as a sum of non-increasing positive integers (e.g. P(4) = 5). The key insight is Euler's pentagonal number theorem, which turns the naive exponential count into an efficient recurrence: P(n) = P(n-1) + P(n-2) - P(n-5) - P(n-7) + P(n-12) + ..., where the offsets are generalized pentagonal numbers and the signs follow a ++--++ pattern. Memoizing the recurrence yields fast computation even for large n.

## Task Requirements
- Write a function returning PartitionsP(n), counting partitions of n into non-increasing positive integers.
- Solutions may be iterative or recursive.
- The offsets in the recurrence increase by the pattern 1, 3, 2, 5, 3, 7, 4, 9, ... (generalized pentagonal numbers).
- Bonus: measure and report how long it takes to compute PartitionsP(6666).

## Language Coverage
43 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, C#, Rust, Go, Java, Haskell, Julia, Python, Perl, Raku, J, and Wren.

## Connections
- [[PartitionFunction]] — the number-theoretic function P(n) being computed
- [[EulersPentagonalNumberTheorem]] — the recurrence relation underlying efficient solutions
- [[PentagonalNumbers]] — generalized pentagonal numbers give the recurrence offsets
- [[Memoization]] — caching subresults makes the recursion tractable
- [[Recursion]] — the natural structure for evaluating the recurrence

## Contradictions
- None — reference task page.
