---
title: "Solve a Numbrix puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-satisfaction, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Solve_a_Numbrix_puzzle
---

## Summary
The task is to write a solver for Numbrix puzzles, a grid-filling puzzle related to Hidato. Given a square grid pre-seeded with some fixed numbers, the program must fill every cell with consecutive integers (1..N) so each successive number is orthogonally adjacent to the previous one. The defining constraint versus Hidato is that moves are restricted to the Von Neumann neighborhood (up/down/left/right only — no diagonals), and grids typically have no holes.

## Task Requirements
- Place the integers 1 through N (N = number of cells) on the grid so that each value k is orthogonally adjacent (left/right/up/down) to value k+1.
- Honor the pre-filled clue cells given in the problem grid.
- Solve and display the two provided 9x9 example puzzles.
- Extra credit for handling additional interesting example puzzles.

## Language Coverage
35 languages implement this task, spanning systems, scripting, functional, and array languages. Representative entries include C++, C#, D, Go, Rust, Java, Python, Perl, Raku, Ruby, Julia, Prolog, Tcl, and Uiua.

## Connections
- [[BacktrackingSearch]] — the standard approach: recursively place the next number into an adjacent empty cell, backtracking on dead ends.
- [[ConstraintSatisfactionProblem]] — fixed clue cells and adjacency rules define the constraints.
- [[DepthFirstSearch]] — the path of consecutive numbers is explored depth-first through the grid.
- [[HamiltonianPath]] — a valid solution is a Hamiltonian path visiting every cell exactly once via orthogonal steps.
- [[VonNeumannNeighborhood]] — the orthogonal-only move set that distinguishes Numbrix from Hidato.

## Contradictions
- None — reference task page.
