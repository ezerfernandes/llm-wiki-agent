---
title: "15 puzzle solver (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, search-algorithms, heuristics, puzzles]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/15_puzzle_solver
---

## Summary
The task is to write a program that finds a shortest (fewest-moves) solution to a given scrambled Fifteen Puzzle, sliding numbered tiles on a 4x4 grid into the goal arrangement (1–15 in order with the blank last). The provided start position has a known optimal solution of 52 moves, and the key insight is that producing such a minimal solution requires an informed search (e.g. A* or IDA*) guided by an admissible heuristic rather than brute-force exploration of the enormous state space.

## Task Requirements
- Solve the specified starting board to the ordered goal state in the fewest single moves possible.
- Output the sequence of moves as directions (left, left, down, right, ...).
- Finding either or both of the two known 52-move optimal solutions is acceptable.
- Extra credit: solve a second, harder given board.

## Language Coverage
39 languages implement this task, spanning systems, functional, scripting, and assembly languages. Representative implementations include C, C++, C#, Rust, Go, Java, Python, JavaScript, Julia, Racket, and even ARM/AArch64 Assembly.

## Connections
- [[AStarSearch]] — informed search guiding the solver toward the goal
- [[IDAStar]] — iterative-deepening A* is the standard memory-light approach for optimal 15-puzzle solving
- [[AdmissibleHeuristic]] — Manhattan distance / walking-distance heuristics drive the search
- [[FifteenPuzzle]] — the underlying sliding-tile puzzle and its solvability parity
- [[StateSpaceSearch]] — searching the permutation graph of board configurations

## Contradictions
- None — reference task page.
