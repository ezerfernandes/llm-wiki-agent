---
title: "Nonogram solver (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-satisfaction, puzzle, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nonogram_solver
---

## Summary
The task asks the programmer to solve nonograms (also called Hanjie or Picross), grid puzzles where each row and column is labeled with the lengths of its consecutive runs of filled cells. Given only these run-length clues, the solver must reconstruct a valid grid of filled and empty cells or report failure. The key insight is that the puzzle is a constraint-satisfaction problem: each line's possible fillings are enumerated and intersected against the orthogonal lines until a consistent configuration is found.

## Task Requirements
- Read four sample problems from a `nonogram_problems.txt` file (blank lines separate problems).
- Accept clues in the compact string encoding where each letter denotes a run length (A=1, B=2, etc.).
- Find one valid filling of empty/occupied cells satisfying all row and column run-length constraints, or print a failure message.
- Extra credit: generate nonograms that have unique solutions for a desired height and width.

## Language Coverage
25 languages implement this task, spanning systems and functional languages plus puzzle-oriented logic languages. Representative entries include C++, C#, D, Rust, Go, Haskell, Python, Julia, Common Lisp, Prolog, and Picat.

## Connections
- [[ConstraintSatisfactionProblem]] — the puzzle is naturally modeled as a CSP over cell states.
- [[Backtracking]] — common solving strategy: try line fillings and undo on conflict.
- [[ArcConsistency]] — the AC-3 algorithm is cited for pruning inconsistent line candidates.
- [[RunLengthEncoding]] — clues are run lengths of consecutive filled cells.
- [[LogicProgramming]] — derived from the "99 Prolog Problems" set, suiting declarative solvers.

## Contradictions
- None — reference task page.
