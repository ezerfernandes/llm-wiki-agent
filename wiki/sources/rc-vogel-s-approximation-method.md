---
title: "Vogel's approximation method (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, operations-research, optimization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Vogel's_approximation_method
---

## Summary
The task is to implement Vogel's Approximation Method (VAM), a heuristic for finding a good initial feasible solution to a balanced transportation (allocation) problem. Given a cost matrix of contractors against tasks, plus supply and demand totals, VAM iteratively allocates work by exploiting per-row and per-column "penalty" costs. The key insight is that prioritizing the row or column with the largest penalty (the gap between its two cheapest cells) avoids being forced into expensive cells later, often producing the optimal cost (£3100 in the worked example).

## Task Requirements
- Allocate 4 contractors (W, X, Y, Z) with given available hours to 5 tasks (A–E) with given required hours, using a supplied cost-per-hour matrix.
- Assume the model is balanced (total supply equals total demand).
- Compute each row's and column's penalty: the difference between its two lowest cell costs.
- Select the row/column with the highest penalty; break ties by choosing the lowest-cost cell.
- Allocate as much as possible to the cheapest feasible cell in that row/column, then adjust the remaining supply and demand (zeroed rows/columns drop out).
- Repeat until all supply and demand are satisfied, then compute the total transportation cost.
- Ideally keep sorting out of the iterative loop so it scales to large problems.

## Language Coverage
33 languages implement this task, giving broad coverage across systems, scripting, functional, and array languages. Representative examples include C, C++, C#, Java, Go, Rust, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[TransportationProblem]] — VAM produces a starting feasible solution for it.
- [[LinearProgramming]] — the optimal benchmark is computed via an LP solver (GLPK).
- [[GreedyAlgorithm]] — VAM is a penalty-driven greedy heuristic.
- [[CombinatorialOptimization]] — allocation under supply/demand constraints.

## Contradictions
- None — reference task page.
