---
title: "Sudoku (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-satisfaction, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sudoku
---

## Summary
The task asks the programmer to solve a partially filled-in standard 9x9 Sudoku grid and print the completed solution in a human-readable form. The puzzle requires that every row, every column, and each of the nine 3x3 boxes contain the digits 1 through 9 exactly once. The core insight is that this is a constraint-satisfaction problem, most commonly solved with recursive backtracking that tries candidate digits and abandons partial fills that violate the row/column/box rules.

## Task Requirements
- Accept a partially filled normal 9x9 Sudoku grid as input.
- Fill in the remaining cells so that each row, column, and 3x3 sub-box contains every digit 1-9 exactly once.
- Display the solved grid in a human-readable format.

## Language Coverage
85 languages implement this task, reflecting broad coverage across general-purpose, functional, logic, and esoteric languages. Representative implementations include C, C++, Java, Python, Haskell, Prolog, Rust, Go, Ruby, and Common Lisp, with logic languages like Prolog and Picat able to express the constraints declaratively.

## Connections
- [[ConstraintSatisfaction]] — Sudoku is a canonical finite-domain constraint-satisfaction problem.
- [[Backtracking]] — the most common solving strategy across implementations.
- [[RecursiveAlgorithms]] — backtracking solvers are typically expressed recursively.
- [[CombinatorialSearch]] — solving explores a constrained search space of digit assignments.

## Contradictions
- None — reference task page.
