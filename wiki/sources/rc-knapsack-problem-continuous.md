---
title: "Knapsack problem/Continuous (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, optimization, greedy-algorithm]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knapsack_problem/Continuous
---

## Summary
A thief must fill a 15 kg knapsack from a list of butcher's-shop items (each with a weight and price) so as to maximize the total value carried. Unlike the 0-1 variant, items are divisible: a fractional cut yields a proportional fraction of the price, so half an item is worth half its price. This divisibility makes the problem solvable optimally with a simple greedy approach rather than dynamic programming.

## Task Requirements
- Select items (whole or fractional) totaling at most 15 kg.
- Maximize the combined value of the selected items.
- Report which items the thief carries, including any partial amounts.
- Use the given table of nine items with their weights (kg) and prices.

## Language Coverage
71 languages implement this task, indicating broad coverage across functional, imperative, and constraint-solving paradigms. Representative implementations include C, C++, Python, Java, Haskell, Go, Rust, Julia, Perl, and the constraint solver MiniZinc.

## Connections
- [[GreedyAlgorithm]] — sorting by value-to-weight ratio yields the optimal continuous solution
- [[KnapsackProblem]] — the fractional/continuous variant of the classic family
- [[CombinatorialOptimization]] — maximizing value under a capacity constraint
- [[LinearProgramming]] — the continuous relaxation can be framed as an LP

## Contradictions
- None — reference task page.
