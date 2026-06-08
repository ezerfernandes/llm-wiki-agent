---
title: "Superpermutation minimisation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Superpermutation_minimisation
---

## Summary
A superpermutation of N distinct characters is a string that contains every one of the N! permutations of those characters as a substring. The task is to generate superpermutations for N from 1 to 7 using methods that produce strings no longer than the trivial N!*N concatenation, then describe, compare, and pick the algorithm yielding the shortest results. The key insight is that overlapping permutations dramatically shortens the string (e.g. for N=2, "ABA" suffices instead of "ABBA"), and finding the truly minimal length is a hard, possibly NP-complete, problem.

## Task Requirements
- Generate superpermutations of N characters for N = 1 through 7.
- Use only methods that never produce a string longer than the naive N!*N concatenation.
- Show descriptions and comparisons of the algorithms used.
- Select the "best" algorithm as the one generating the shortest superpermutations.
- Note that minimal lengths for small N are known (OEIS A180632: 0, 1, 3, 9, 33, 153 for N=0..5; 872 conjectured for N=6).

## Language Coverage
34 languages implement this task, spanning systems, scripting, functional, and JVM ecosystems. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Perl, Raku, Julia, and Wren.

## Connections
- [[Permutations]] — the task builds strings containing all permutations of a set
- [[Combinatorics]] — superpermutation length is a combinatorial optimization problem
- [[NPCompleteness]] — finding the minimal superpermutation is thought to be NP-complete
- [[GreedyAlgorithm]] — common construction methods extend strings by maximal-overlap greedy choices

## Contradictions
- None — reference task page.
