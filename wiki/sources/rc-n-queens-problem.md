---
title: "N-queens problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, backtracking, combinatorial-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/N-queens_problem
---

## Summary
The task is to solve the classic eight queens puzzle: place 8 queens on a chessboard so that none can attack another, then generalize it to an NxN board. The key insight is that exactly one queen occupies each row and column, so a solution is a permutation of columns that must additionally avoid shared diagonals — making backtracking and constraint search natural fits.

## Task Requirements
- Place N queens on an NxN board so no two share a row, column, or diagonal.
- Solve the standard 8x8 case, and ideally generalize to arbitrary N.
- Solution counts for small N follow OEIS sequence A000170 (1, 0, 0, 2, 10, 4, 40, 92, ... for N = 1, 2, 3, ...).

## Language Coverage
142 languages implement this task, spanning compiled, scripting, functional, logic, and constraint-programming styles — for example C, C++, Rust, Go, Java, Python, Haskell, Prolog, MiniZinc, and J. The breadth highlights how the same constraint problem is expressed via imperative backtracking, declarative logic, and dedicated constraint solvers.

## Connections
- [[Backtracking]] — the canonical algorithm for incrementally placing queens and undoing conflicting placements
- [[ConstraintSatisfaction]] — the puzzle is a textbook constraint-satisfaction problem solved natively by tools like MiniZinc and Prolog
- [[Permutations]] — each candidate solution is a permutation of column indices, one per row
- [[Recursion]] — most implementations explore the search tree recursively row by row
- [[CombinatorialSearch]] — counting all valid arrangements relates to OEIS A000170

## Contradictions
- None — reference task page.
