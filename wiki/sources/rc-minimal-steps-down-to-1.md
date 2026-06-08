---
title: "Minimal steps down to 1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, shortest-path, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Minimal_steps_down_to_1
---

## Summary
Given a starting integer N greater than one, a set of allowed divisors D, and a set of allowed subtractors S, the task is to reduce N to 1 using the fewest possible steps. At each step the number may be divided by any divisor that divides it exactly, or have any subtractor smaller than it subtracted. The key insight is that a greedy "always divide when possible" strategy is not optimal, so the minimal step count is best computed with dynamic programming (memoization or bottom-up tabulation) while recording the move that produced each value to reconstruct one optimal path.

## Task Requirements
- Compute the minimum number of steps to bring N down to 1, given divisor set D and subtractor set S.
- A step divides N by a member of D (only if exactly divisible) or subtracts a member of S (only if N exceeds it).
- Show one concrete sequence of steps achieving that minimum, not just the count.
- For D={2,3}, S={1}: list steps and a path for N = 1..10, then report the count and which numbers in 1..2000 attain the maximum minimal step count.
- Repeat both parts for D={2,3}, S={2}.
- Optional stretch goal: extend the maximum-finding ranges to 1..20000.

## Language Coverage
22 languages implement this task, spanning systems, functional, scripting, and array languages. Representative entries include C++, C#, Go, Rust-adjacent FreeBASIC, Java, Kotlin, Swift, Haskell, Julia, Nim, Perl, Python, Raku, J, jq, Phix, Wren, and Mathematica/Wolfram Language.

## Connections
- [[DynamicProgramming]] — memoization and tabulation give the optimal step count
- [[ShortestPath]] — equivalent to BFS over a graph of reachable integers
- [[Memoization]] — caching minimal steps per value avoids recomputation
- [[GreedyAlgorithm]] — naive greedy division fails, motivating the DP approach

## Contradictions
- None — reference task page.
