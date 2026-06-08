---
title: "Held–Karp algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, graph-algorithms, optimization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Held–Karp_algorithm
---

## Summary
Implement the Held–Karp dynamic programming algorithm to solve the Traveling Salesperson Problem (TSP) exactly. Given an n-city cost matrix C, find the minimum-cost Hamiltonian cycle that starts at city 0, visits every city exactly once, and returns to city 0. The key insight is that bitmask subsets of cities serve as DP states `dp(S, j)` — the cheapest path covering set S and ending at city j — yielding O(n²·2ⁿ) time, far better than the O(n!) brute-force permutation search though still exponential.

## Task Requirements
- Represent the problem with an n×n cost matrix C where `C[i][j]` is the travel cost from city i to city j.
- Define DP state `dp(S, j)` = minimum cost of a path from city 0 through all cities in subset S, ending at j (with 0 ∈ S, j ∈ S).
- Base case: `dp({0, j}, j) = C[0][j]` for each j ≠ 0.
- Recurrence: `dp(S, j) = min over i ∈ S, i ≠ j of { dp(S \ {j}, i) + C[i][j] }`, computed by increasing subset size.
- Final answer: `min over j ≠ 0 of { dp(V, j) + C[j][0] }`, the shortest cycle returning to city 0.
- Achieve the O(n²·2ⁿ) time and O(n·2ⁿ) space characteristic of the method.

## Language Coverage
23 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative entries include C++, C#, Rust, Go, Java, JavaScript, Python, Julia, Fortran, Raku, and Wren.

## Connections
- [[DynamicProgramming]] — the algorithm's core paradigm of solving overlapping subproblems
- [[TravelingSalespersonProblem]] — the NP-hard problem this gives an exact solution to
- [[Bitmasking]] — subsets of cities are encoded as integer bitmasks for DP indexing
- [[HamiltonianCycle]] — the route sought is a minimum-cost Hamiltonian cycle
- [[CombinatorialOptimization]] — broader class of exact optimization over discrete structures

## Contradictions
- None — reference task page.
