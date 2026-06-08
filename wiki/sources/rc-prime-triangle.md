---
title: "Prime triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Prime_triangle
---

## Summary
The task asks for a function f(S) that returns arrangements of the integers 1 through S in which the first element is fixed at 1, the last element is fixed at S, and every pair of adjacent values sums to a prime. The arrangements for S=2 through S=20 are printed stacked to form a triangle, followed by the count of valid arrangements for each S. The key insight is that this is a constrained permutation search best solved by backtracking, since each adjacency must satisfy a primality test; the counts correspond to OEIS sequence A036440.

## Task Requirements
- Implement f(S) returning lists where g₁=1 and g_S=S, with g_n + g_(n+1) prime for n=1..S-1.
- S=1 is undefined and excluded.
- For S=2 to S=20, print one representative arrangement f(S) to build a triangle display.
- For S=2 to S=20, also print the number of valid arrangements meeting the constraints.

## Language Coverage
23 languages implement this task, showing solid breadth across compiled, functional, and array-oriented styles. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, F#, and J.

## Connections
- [[Backtracking]] — the natural search strategy for building valid prime-sum arrangements
- [[PrimalityTest]] — each adjacency check requires testing whether a sum is prime
- [[Permutations]] — the candidate space is permutations of 1..S under constraints
- [[CombinatorialSearch]] — counting all arrangements is a constraint-satisfaction enumeration

## Contradictions
- None — reference task page.
