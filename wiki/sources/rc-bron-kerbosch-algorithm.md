---
title: "Bron–Kerbosch algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, recursion, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bron–Kerbosch_algorithm
---

## Summary
The task asks the programmer to find and list all maximal cliques in an undirected graph using the Bron–Kerbosch algorithm. A maximal clique is a fully-connected subset of vertices that cannot be extended by any additional adjacent vertex. The key insight is the recursive backtracking with three working sets (R, P, X) plus pivot selection, which prunes redundant recursive branches and makes enumeration efficient.

## Task Requirements
- Represent the input graph as a list of undirected edges (tuples of two vertices).
- Build an adjacency list (e.g., map of vertex to set of neighbors) from the edge list.
- Implement Bron–Kerbosch with pivoting using three sets: R (current clique), P (candidates), and X (already-processed/excluded vertices).
- Recursion: when P and X are both empty, record R as a maximal clique; otherwise choose a pivot from P ∪ X with maximum degree and recurse only over candidates in P that are not neighbors of the pivot.
- For each chosen vertex, intersect P and X with its neighbors before recursing, then move the vertex from P to X.
- Output all maximal cliques with more than two vertices, each as a comma-separated, lexicographically sorted vertex list.

## Language Coverage
28 languages implement this task, spanning systems languages, functional languages, scripting, and math-oriented tools. Representative implementations include Ada, C++, C#, Go, Java, JavaScript, Julia, Python, Rust, Raku, and Wren.

## Connections
- [[GraphTheory]] — operates on undirected graphs and their vertex/edge structure.
- [[Clique]] — finds maximal cliques, the core combinatorial object of the task.
- [[Backtracking]] — the algorithm is a recursive backtracking search over candidate sets.
- [[Recursion]] — the core procedure calls itself with updated R, P, and X sets.
- [[AdjacencyList]] — the graph representation used to test vertex adjacency.

## Contradictions
- None — reference task page.
