---
title: "Johnson's algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, shortest-paths]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Johnson's_algorithm
---

## Summary
The task asks the programmer to implement Johnson's algorithm, which finds the shortest paths between all pairs of vertices in a sparse, edge-weighted, directed graph. The key insight is a reweighting technique that transforms every edge weight to be non-negative while preserving shortest-path relationships, allowing Dijkstra's algorithm to run from each source even when the original graph has negative edges. By combining Bellman-Ford (for reweighting) with repeated Dijkstra runs, it beats Floyd-Warshall on sparse graphs.

## Task Requirements
- Take a directed graph G = (V, E) with a real-valued weight function w: E → ℝ that may include negative-weight edges but no negative-weight cycles.
- Produce a |V| × |V| matrix D where D[i,j] is the shortest-path weight from vertex i to vertex j, and ∞ where no path exists.
- Reject or assume the absence of negative-weight cycles.
- Target time complexity O(V² log V + VE) and space complexity O(V²).

## Language Coverage
20 languages implement this task, spanning systems, scripting, and functional families. Representative implementations include C++, C#, Go, Java, JavaScript, Python, Rust, Julia, Raku, and Swift, along with COBOL, Fortran, and Zig.

## Connections
- [[ShortestPath]] — the all-pairs shortest-path problem this task solves
- [[DijkstrasAlgorithm]] — run from each vertex after reweighting
- [[BellmanFordAlgorithm]] — computes the vertex potentials used to reweight edges
- [[FloydWarshallAlgorithm]] — the alternative all-pairs method it outperforms on sparse graphs
- [[GraphTheory]] — directed, edge-weighted graphs are the domain

## Contradictions
- None — reference task page.
