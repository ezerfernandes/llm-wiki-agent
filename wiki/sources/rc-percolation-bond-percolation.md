---
title: "Percolation/Bond percolation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, monte-carlo, graph-traversal, percolation-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Percolation/Bond_percolation
---

## Summary
The task models bond percolation on an M×N grid of cells whose shared edges (horizontal and vertical walls) are each independently present with probability `p`. Fluid poured on the top row flows into any adjacent cell when no wall separates them, and "drips out" if it reaches a bottom cell with a missing bottom wall. By repeating the random trial `t` times, the program estimates the empirical probability that fluid percolates top-to-bottom as a function of `p`.

## Task Requirements
- Build an M×N grid (M=N=10) where each interior wall is present with constant probability `p`, except the outer horizontal walls at m=0 and m=M which are always present.
- Simulate fluid flooding from the top surface (n=0), spreading through any wall-free adjacency, including moving upward within the grid.
- Detect percolation: fluid reaching a bottom cell with a missing bottom wall.
- For each `p` from 0.0 to 1.0 in steps of 0.1, run `t = 100` repetitions and report the fraction of successful percolations.
- Show all output on the page; optionally depict a successful percolation graphically.

## Language Coverage
21 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include C, C++, D, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[PercolationTheory]] — the statistical-physics phenomenon being simulated
- [[MonteCarloSimulation]] — repeated random trials estimate the percolation probability
- [[FloodFill]] — the fluid-spreading step is a connected-component flood traversal
- [[GraphTraversal]] — cells and missing walls form a graph explored via BFS/DFS
- [[PhaseTransition]] — percolation probability exhibits a threshold as `p` varies

## Contradictions
- None — reference task page.
