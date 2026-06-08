---
title: "Sum to 100 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_to_100
---

## Summary
The task is to insert the operators `+`, `-`, or nothing (concatenation) before each digit of the string `123456789` and evaluate the resulting arithmetic expression. The classic goal is to find every combination that evaluates to 100 (e.g. `123 + 4 - 5 + 67 - 89 = 100`). The key insight is that there are only 3^8 = 6561 distinct operator placements to enumerate, since the first digit takes no leading operator, making brute-force enumeration trivially feasible.

## Task Requirements
- Show all operator insertions into `123456789` that sum to exactly 100.
- Identify the target sum that has the maximum number of distinct solutions (over all reachable sums).
- Find the lowest positive sum that cannot be expressed under these rules (e.g. 5074 is an example of an unexpressible sum, though not the smallest).
- Extra credit: show the ten highest sums that can be expressed.

## Language Coverage
53 languages implement this task, spanning systems and scripting languages broadly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Ruby, and Wren.

## Connections
- [[Combinatorics]] — enumerating all 3^8 operator placements
- [[BruteForceSearch]] — the standard exhaustive evaluation strategy
- [[Backtracking]] — an alternative recursive expression-building approach
- [[StringProcessing]] — parsing concatenated digit runs into numeric terms

## Contradictions
- None — reference task page.
