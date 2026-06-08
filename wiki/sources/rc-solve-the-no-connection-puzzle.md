---
title: "Solve the no connection puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-satisfaction, backtracking, graph]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Solve_the_no_connection_puzzle
---

## Summary
The task is to solve a placement puzzle on a fixed board of eight holes (labelled A–H) joined by fifteen straight lines, using eight pegs numbered 1–8. Each peg goes in exactly one hole such that the absolute difference between the numbers at the two ends of every connecting line is strictly greater than one. The key insight is that this is a small constraint-satisfaction problem over the graph's edges, easily handled by brute-force permutation testing or backtracking since there are only 8! = 40320 arrangements.

## Task Requirements
- Model the board: eight holes A–H connected by a specific set of fifteen edges.
- Assign the eight distinct pegs (1–8) to the eight holes.
- Enforce the constraint that for every connected pair of holes, the absolute difference of their peg numbers is greater than one.
- Produce and display one valid solution.

## Language Coverage
47 languages implement this task, showing broad coverage spanning systems languages, functional and logic languages, and scripting tongues. Representative implementations include C, C++, Java, Python, Go, Haskell, Prolog, Julia, Raku, and Rust-adjacent Zig.

## Connections
- [[ConstraintSatisfactionProblem]] — assigning values under per-edge constraints
- [[Backtracking]] — common search strategy to prune invalid partial assignments
- [[Permutation]] — brute-force over the 8! orderings of pegs
- [[GraphTheory]] — the board is a graph of holes (nodes) and lines (edges)

## Contradictions
- None — reference task page.
