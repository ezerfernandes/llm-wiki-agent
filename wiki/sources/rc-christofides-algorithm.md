---
title: "Christofides algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, approximation-algorithm, optimization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Christofides_algorithm
---

## Summary
This task asks the programmer to implement the Christofides algorithm, a polynomial-time approximation for the metric traveling salesman problem (TSP). Given a complete undirected graph whose non-negative edge weights satisfy the triangle inequality, it produces a Hamiltonian circuit whose total weight is at most 3/2 times the optimal tour. The key insight is combining a minimum spanning tree with a minimum-weight perfect matching over the tree's odd-degree vertices, then shortcutting an Eulerian circuit into a Hamiltonian one without increasing weight (thanks to the triangle inequality).

## Task Requirements
- Build a minimum spanning tree (MST) of the input graph using e.g. Kruskal's or Prim's algorithm.
- Identify the vertices that have odd degree in the MST (always an even count).
- Compute a minimum-weight perfect matching among those odd-degree vertices.
- Combine the MST and the matching into a connected multigraph where every vertex has even degree.
- Find an Eulerian circuit in this multigraph.
- Convert the Eulerian circuit into a Hamiltonian circuit by shortcutting repeated vertices, relying on the triangle inequality so the total weight does not increase.

## Language Coverage
24 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C++, C#, Go, Java, JavaScript, Python, Rust, Julia, Perl, Raku, and Wolfram Language.

## Connections
- [[TravelingSalesmanProblem]] — the NP-hard optimization problem this algorithm approximates
- [[MinimumSpanningTree]] — first structural step of the construction
- [[MinimumWeightPerfectMatching]] — matches odd-degree vertices, the costliest step (O(n^3))
- [[EulerianCircuit]] — traversal used before shortcutting to a tour
- [[ApproximationAlgorithm]] — provides the guaranteed 3/2 ratio for metric TSP

## Contradictions
- None — reference task page.
