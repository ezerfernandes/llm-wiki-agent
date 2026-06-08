---
title: "Borůvka algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, greedy, minimum-spanning-tree]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Borůvka_algorithm
---

## Summary
The task asks the programmer to implement Borůvka's algorithm, a greedy method for finding a minimum spanning tree (MST) of a connected, undirected, weighted graph. The algorithm starts with each vertex as its own single-node tree and repeatedly adds, for every tree, the cheapest edge linking it to another tree, merging trees together. Because every stage at least halves the number of trees, it terminates in at most log(V) stages with an overall time complexity of O(E log V). Published in 1926, it is the oldest known MST algorithm and is notable for parallelizing better than Kruskal's or Prim's.

## Task Requirements
- Build an MST of a connected, undirected, weighted graph using Borůvka's algorithm.
- Begin with a forest of single-vertex trees (one per vertex).
- In each stage, find for every current tree the minimum-weight edge connecting it to a different tree.
- Add all those selected minimum-weight edges to the MST, merging the corresponding trees.
- Repeat the stages until only one tree remains; that tree is the minimum spanning tree.

## Language Coverage
23 languages implement this task, giving broad coverage across systems, scripting, functional, and BASIC-family languages. Representative implementations include C++, C#, Java, Rust, Go, Python, JavaScript, Julia, Raku, Fortran, and Wolfram Language.

## Connections
- [[MinimumSpanningTree]] — the structure the algorithm computes.
- [[GreedyAlgorithm]] — the design paradigm Borůvka's algorithm follows.
- [[GraphTheory]] — operates on connected, undirected, weighted graphs.
- [[DisjointSetUnion]] — typical structure for tracking which vertices belong to which tree/component.
- [[KruskalsAlgorithm]] — alternative MST algorithm with the same asymptotic complexity.

## Contradictions
- None — reference task page.
