---
title: "Knapsack problem/Bounded (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, combinatorial-optimization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knapsack_problem/Bounded
---

## Summary
A tourist must pack a 4 kg (400 dag) knapsack from a list of 22 candidate items, each with a weight, a value, and a limited number of available copies. The goal is to select whole units of items so the total weight stays within the limit while maximizing total value. The "bounded" aspect — each item available in a fixed quantity rather than just once or unlimited — distinguishes it from the 0-1 and unbounded variants and is the key modeling challenge.

## Task Requirements
- Choose a combination of items whose total weight does not exceed 400 dag.
- Respect each item's piece count: an item may be taken zero up to its available number of copies, in whole units only (no cutting).
- Maximize the total value of the chosen items.
- Report which items (and how many of each) the tourist carries.

## Language Coverage
56 languages implement this task, spanning systems and functional languages as well as dedicated constraint/optimization solvers. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Prolog, and the MiniZinc and Mathprog constraint-modeling languages.

## Connections
- [[KnapsackProblem]] — bounded variant of this classic problem family
- [[DynamicProgramming]] — standard exact solution technique
- [[CombinatorialOptimization]] — the broader problem class
- [[IntegerProgramming]] — natural formulation for the bounded constraints

## Contradictions
- None — reference task page.
