---
title: "Knapsack problem/Unbounded (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorial-optimization, dynamic-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knapsack_problem/Unbounded
---

## Summary
A traveler in Shangri La may take unlimited quantities of three items (panacea, ichor, gold), each with a value, weight, and volume, but his knapsack is bounded by 25 weight units and 0.25 cubic-length volume units. The task is to choose how many of each item to take so as to maximize total value subject to both constraints. The defining feature versus the bounded/0-1 variants is that supply is effectively infinite, so each item count is an unbounded non-negative integer; multiple optimal solutions (e.g. 0/15/11 or 9/0/11 panacea/ichor/gold, all worth 54500) tie for the maximum.

## Task Requirements
- Maximize the total value carried given fixed per-item value, weight, and volume.
- Respect two simultaneous constraints: total weight no more than 25 and total volume no more than 0.25.
- Take only whole (integer) units of each item; supply of each item is unlimited.
- Report how many of each item is taken; only one of the four maximal solutions need be given.

## Language Coverage
68 languages implement this task, showing broad coverage across imperative, functional, and constraint-solving paradigms. Representative implementations include C, C++, Java, Python, Haskell, Go, Rust-adjacent BASICs like FreeBASIC, plus constraint/optimization tools such as MiniZinc, Mathprog, and SAS alongside Lisp dialects like Common Lisp and Racket.

## Connections
- [[KnapsackProblem]] — the unbounded variant of this classic optimization problem.
- [[DynamicProgramming]] — the standard exact technique for solving knapsack instances.
- [[CombinatorialOptimization]] — the broader field this maximization problem belongs to.
- [[IntegerProgramming]] — the constraint-based formulation used by solvers like MiniZinc and Mathprog.
- [[BruteForceSearch]] — feasible here because the small item set and bounds limit the search space.

## Contradictions
- None — reference task page.
