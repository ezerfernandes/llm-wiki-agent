---
title: "Floyd-Warshall algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, dynamic-programming, shortest-path]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Floyd-Warshall_algorithm
---

## Summary
This task asks the programmer to implement the Floyd-Warshall algorithm, which finds the shortest path lengths between every pair of vertices in a weighted directed graph that may contain negative edge weights. The key insight is its dynamic-programming structure: a triple-nested loop over an intermediate vertex k progressively relaxes the distance matrix, allowing paths to route through k whenever doing so is shorter. Input is assumed free of loops, parallel edges, and negative cycles.

## Task Requirements
- Compute the shortest-path lengths between all pairs of vertices of a given directed graph.
- Handle positive and negative edge weights (no negative cycles).
- Print each vertex pair and its shortest distance, optionally including the reconstructed path.

## Language Coverage
62 languages implement this task, spanning systems, functional, scripting, and array languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, and Wren.

## Connections
- [[FloydWarshallAlgorithm]] — the named all-pairs shortest-path method this task implements
- [[DynamicProgramming]] — the algorithmic paradigm underlying the k-relaxation
- [[ShortestPath]] — the graph problem being solved
- [[GraphTheory]] — weighted directed graphs and edge weights
- [[PathReconstruction]] — the optional next-vertex matrix used to recover actual paths

## Contradictions
- None — reference task page.
