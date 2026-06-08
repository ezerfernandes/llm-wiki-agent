---
title: "Stirling numbers of the second kind (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, recurrence-relation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stirling_numbers_of_the_second_kind
---

## Summary
Stirling numbers of the second kind, S2(n, k), count the number of ways to partition a set of n objects into k non-empty subsets. The task is to implement a routine that computes them, most naturally via the recurrence S2(n+1, k) = k·S2(n, k) + S2(n, k-1). They are closely related to Bell numbers, which are the row sums of the Stirling-second-kind triangle.

## Task Requirements
- Write a function (or use a built-in/library) to compute Stirling numbers of the second kind.
- Generate and display a table or triangle of S2(n, k) up to S2(12, 12); showing the n==0/k==0 row/column and the zero cells (where k > n) is optional.
- If the language supports big integers, find and show the maximum value of S2(n, k) for n == 100.

## Language Coverage
38 languages implement this task, spanning systems, scripting, functional, and array languages. Representative entries include C, C++, D, Go, Java, Python, Haskell, J, Julia, Raku, and Wren.

## Connections
- [[Combinatorics]] — counting set partitions into subsets
- [[RecurrenceRelation]] — the defining S2(n+1,k) = k·S2(n,k) + S2(n,k-1) rule
- [[BellNumbers]] — row sums of the Stirling-second-kind triangle
- [[SetPartition]] — the combinatorial object being counted
- [[BigIntegerArithmetic]] — required for the n==100 maximum

## Contradictions
- None — reference task page.
