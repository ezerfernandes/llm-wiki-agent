---
title: "Knapsack problem/0-1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, combinatorial-optimization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knapsack_problem/0-1
---

## Summary
The task frames the classic 0-1 knapsack problem as a tourist packing for a day trip: given a fixed list of 22 items, each with a weight and a value, choose a subset whose total weight stays within a 400-dag (4 kg) capacity while maximizing total value. The "0-1" qualifier means each item is either taken whole or left behind — no partial items and no duplicates. The standard solution is dynamic programming over a capacity table, which runs in pseudo-polynomial time (O(n × capacity)).

## Task Requirements
- Use the given fixed table of 22 items, each with a weight (in dag) and a value.
- Select a subset of items whose combined weight does not exceed 400 dag.
- Maximize the total value of the selected subset.
- Each item may be taken at most once and only as a whole unit (no cutting or partial items).
- Show which items the tourist carries (the chosen subset, not just the optimal value).

## Language Coverage
90 languages implement this task, reflecting its status as a canonical optimization exercise. Representative implementations include C, C++, C#, Java, Python, Haskell, Rust, Go, Julia, Common Lisp, Prolog, and MiniZinc — the last few showing constraint/logic-programming and dedicated optimization-solver approaches alongside the usual dynamic-programming code.

## Connections
- [[DynamicProgramming]] — the standard approach builds a value table over remaining capacity
- [[KnapsackProblem]] — this is the canonical 0-1 variant of the broader family
- [[CombinatorialOptimization]] — selecting an optimal subset under a constraint
- [[NPComplete]] — the decision version of the knapsack problem is NP-complete
- [[Memoization]] — the page is categorized under memoization, a top-down DP technique

## Contradictions
- None — reference task page.
