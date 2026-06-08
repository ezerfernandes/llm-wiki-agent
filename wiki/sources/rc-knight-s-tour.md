---
title: "Knight's tour (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, backtracking, graph-traversal, chess]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knight's_tour
---

## Summary
The task asks the programmer to find a sequence of legal knight moves on a standard 8x8 chessboard such that the knight visits every square exactly once, starting from a given square. The tour need not be "closed" (the knight does not have to end adjacent to its start). The key insight is that this is a Hamiltonian-path problem on the knight's-move graph, which naive backtracking solves slowly but Warnsdorff's heuristic (always move to the square with the fewest onward moves) solves almost instantly.

## Task Requirements
- Begin with a single knight on a specified starting square of an 8x8 board.
- Emit a series of legal knight moves visiting every square exactly once.
- A closed tour is not required.
- Input: the starting square; Output: the move sequence.
- Output may be textual (algebraic notation, or a numbered board diagram) or graphical/animated.

## Language Coverage
72 languages implement this task, spanning systems languages, scripting languages, functional languages, and constraint/logic solvers. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Prolog, Julia, and Mathematica/Wolfram Language.

## Connections
- [[KnightsTour]] — the chess puzzle this task formalizes
- [[HamiltonianPath]] — visiting every vertex exactly once on the knight's-move graph
- [[WarnsdorffsRule]] — greedy heuristic that makes the search tractable
- [[Backtracking]] — the baseline exhaustive search strategy
- [[GraphTraversal]] — underlying model of board squares as graph nodes

## Contradictions
- None — reference task page.
