---
title: "Solve a Holy Knight's tour (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, backtracking, graph-search, puzzle]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Solve_a_Holy_Knight%27s_tour
---

## Summary
The task is to construct a knight's tour over an irregular board where only certain squares are usable, since other squares are blocked (the "pennies"). The program must move a chess knight so that it visits every available square exactly once, given a fixed starting square. The key insight is that this is a constrained Hamiltonian-path search closely related to Hidato-style number-placement puzzles, typically solved by depth-first backtracking with knight-move connectivity.

## Task Requirements
- Read a board layout where zeros mark available squares and missing/blank cells mark blocked squares (not the pennies themselves).
- Begin from the designated starting square (marked 1 in the example) and traverse using legal knight moves.
- Visit every available square exactly once, producing a complete numbered tour as the solution.
- Demonstrate the program on the provided sample board; extra credit for additional interesting boards.

## Language Coverage
35 languages implement this task, giving broad coverage across functional, imperative, scripting, and systems languages. Representative implementations include Python, C++, C#, Java, Haskell, Go, Rust, Julia, Perl, Raku, and Ruby.

## Connections
- [[KnightsTour]] — this is a constrained variant of the classic knight's tour.
- [[Backtracking]] — the standard solution strategy for exploring move sequences.
- [[HamiltonianPath]] — visiting every available square exactly once is a Hamiltonian-path problem.
- [[DepthFirstSearch]] — the search order most implementations use over the move graph.
- [[ConstraintSatisfaction]] — blocked squares and adjacency rules define the constraints.

## Contradictions
- None — reference task page.
