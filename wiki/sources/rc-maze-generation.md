---
title: "Maze generation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, algorithms, recursion, graph-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Maze_generation
---

## Summary
This task asks the programmer to generate and display a maze using the simple depth-first search (recursive backtracker) algorithm. The key insight is that a maze on a grid is a spanning tree: starting from a random cell, you carve passages by randomly visiting unvisited neighbors, removing the wall between the current cell and the chosen neighbor, then recursing — guaranteeing every cell is reachable with exactly one path between any two cells.

## Task Requirements
- Generate a maze on a grid of cells using the depth-first search maze generation algorithm.
- Start at a random cell and mark the current cell as visited.
- Gather the cell's neighbors and, in random order, recurse into any unvisited neighbor, removing the wall between the two cells.
- Show/render the resulting maze.

## Language Coverage
82 languages implement this task, reflecting very broad coverage across systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Ruby, and Perl.

## Connections
- [[DepthFirstSearch]] — the core algorithm the task specifies
- [[RecursiveBacktracking]] — the implementation strategy for carving passages
- [[SpanningTree]] — the structure a perfect maze forms over the grid graph
- [[GraphTraversal]] — neighbor exploration over a grid-based graph
- [[MazeSolving]] — explicitly listed related task

## Contradictions
- None — reference task page.
