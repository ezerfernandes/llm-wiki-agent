---
title: "Solve a Hidato puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, backtracking, constraint-satisfaction, puzzle-solving]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Solve_a_Hidato_puzzle
---

## Summary
The task is to write a program that solves Hidato (also called Hidoku) puzzles: given a grid pre-seeded with some numbers, fill every blank square so the full sequence of natural numbers from 1 upward forms a connected path. Each consecutive pair of numbers must lie in each other's Moore neighborhood, meaning a chess king could walk the path in numerical order. The core insight is that this is a Hamiltonian-path / constraint-satisfaction problem usually solved by depth-first backtracking from cell "1".

## Task Requirements
- Accept a grid that may be non-rectangular, contain holes, but is always connected.
- The numbers 1 and N (where N equals the number of fillable squares) are always present, plus additional clues that force a unique solution.
- The difference between any two clue numbers given on the grid is at most 13.
- Place a natural number in every blank square so numbers 1..N form a path where each step moves to a Moore-neighbor (king move) of the previous square.
- Each square holds exactly one number; a proper puzzle has a unique solution.

## Language Coverage
42 languages implement this task, spanning systems and functional languages, scripting languages, and even a constraint/LP modeling language (Mathprog). Representative examples include C, C++, C#, Java, Python, Haskell, Prolog, Rust, Go, Julia, and Raku.

## Connections
- [[Backtracking]] — the standard recursive search technique for filling the path
- [[HamiltonianPath]] — the solution is a Hamiltonian path through the grid cells
- [[ConstraintSatisfaction]] — pre-placed clues constrain the search space
- [[DepthFirstSearch]] — backtracking explores candidate moves depth-first
- [[MooreNeighborhood]] — defines the legal king-move adjacency between consecutive numbers

## Contradictions
- None — reference task page.
