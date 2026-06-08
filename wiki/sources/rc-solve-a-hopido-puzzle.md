---
title: "Solve a Hopido puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, backtracking, puzzle-solving, graph-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Solve_a_Hopido_puzzle
---

## Summary
A Hopido puzzle requires filling a grid of playable tiles with a single consecutive numbered path (1, 2, 3, ...) so every tile is visited exactly once. Unlike Hidato, the only legal moves are hops: diagonally over one tile, or horizontally/vertically over two tiles. The path may start anywhere, has no marked endpoint, and offers no intermediate clues, making it a pure constraint-satisfaction search. The key insight is treating it as a Hamiltonian-path problem over a restricted move graph, solved efficiently with depth-first backtracking.

## Task Requirements
- Solve the given example board (an irregular grid where `.` marks blocked cells and `0` marks empty playable tiles).
- Place consecutive integers covering every playable tile exactly once.
- Allow moves only by hopping: one tile diagonally, or two tiles orthogonally (horizontal/vertical).
- Permit the path to begin at any tile; there is no predetermined start or end and no intermediate filled clues.
- Aim for fast solving (milliseconds), per the task's framing about slow naive solvers.

## Language Coverage
30 languages implement this task, spanning systems, functional, scripting, and logic paradigms. Representative implementations include C++, C#, D, Go, Rust, Java, Python, Perl, Raku, Julia, Prolog, and Wren.

## Connections
- [[Backtracking]] — the standard technique for exploring and pruning candidate paths
- [[HamiltonianPath]] — visiting every node exactly once over the legal-move graph
- [[DepthFirstSearch]] — drives the recursive path exploration
- [[ConstraintSatisfaction]] — the puzzle as a constraint problem with no clues
- [[SolveAHidatoPuzzle]] — the closely related sibling task with different move rules

## Contradictions
- None — reference task page.
