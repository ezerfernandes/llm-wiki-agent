---
title: "Numbers which are not the sum of distinct squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numbers_which_are_not_the_sum_of_distinct_squares
---

## Summary
The task asks the programmer to find every positive integer that cannot be expressed as a sum of one or more distinct perfect squares (1, 4, 9, 16, ...). The key insight is that this set is finite: although infinitely many integers fail at first, once a long enough run of consecutive representable integers appears, every larger integer is also representable (the next square is small enough relative to the running sum to bridge any gap). This corresponds to OEIS sequence A001422.

## Task Requirements
- Find and display every positive integer that cannot be generated as a sum of distinct integer squares.
- Do not use magic numbers or pre-determined limits — the cutoff must be discovered programmatically.
- Justify the answer mathematically (i.e., prove the set is complete once a sufficient run of representable consecutive integers is found).

## Language Coverage
28 languages implement this task, spanning compiled, scripting, array, and functional styles. Representative implementations include ALGOL 68, C++, Go, Java, Julia, Python, Perl, Raku, Wren, J, and Mathematica/Wolfram Language.

## Connections
- [[NumberTheory]] — the task is a classical additive number theory problem.
- [[SubsetSum]] — determining representability reduces to a subset-sum decision over the squares.
- [[DynamicProgramming]] — typical solutions use a DP/boolean-reachability table over achievable sums.
- [[PerfectSquares]] — the building blocks are the squares of the positive integers.
- [[OEIS]] — the answer is catalogued as sequence A001422.

## Contradictions
- None — reference task page.
