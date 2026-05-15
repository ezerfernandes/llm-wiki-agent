---
title: "ODS Ch.12: Graphs"
type: source
tags: [book, data-structures, graphs, bfs, dfs]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 12
pages: "239-256"
---

## Summary
Two graph representations and the two foundational traversal algorithms. **AdjacencyMatrix**: an n×n boolean matrix a[i][j] = (i,j) ∈ E. add_edge / remove_edge / has_edge in O(1); in_edges / out_edges in O(n); space O(n²). Suited to dense graphs. **AdjacencyLists**: an array of lists, one per vertex; add_edge in O(1); has_edge / remove_edge in O(deg); in/out_edges in O(deg). Space O(n+m). Then **breadth-first search** (BFS) using a Queue — visits vertices in non-decreasing order of distance from a source — and **depth-first search** (DFS) using a Stack or recursion. Both run in O(n+m) on adjacency lists, O(n²) on adjacency matrices.

## Key Claims
- **AdjacencyMatrix theorem (12.1)**: edge ops O(1), in/out_edges O(n), space O(n²) bits.
- **Bonus**: matrix-multiplication a² counts paths of length 2; iterating gives all-pairs shortest paths in O(log n) matrix multiplications — connects to algebraic graph algorithms.
- **AdjacencyLists** typically preferred for sparse graphs (m = o(n²)). Lists implemented as ArrayStacks for O(1)-index access; DLLists give O(deg) remove_edge.
- **BFS**: starting at r, mark r visited and enqueue. Repeatedly dequeue u, enqueue every unvisited neighbour. Visits in distance order; computes shortest paths in unweighted graphs.
- **DFS**: visit u, mark visited, recurse on unvisited neighbours (or use explicit stack). Yields a DFS forest with edges classified as tree/back/forward/cross.
- **Both run in O(n + m)** on adjacency-list representation; O(n²) on adjacency-matrix.

## Key Quotes
> "Despite its high memory requirements and poor performance of the in_edges(i) and out_edges(i) operations, an AdjacencyMatrix can still be useful for some applications."
> "Mathematically, a (directed) graph is a pair G = (V, E) where V is a set of vertices and E is a set of ordered pairs of vertices called edges."

## Connections
- [[ods-05-hash-tables]] — adjacency-set implementations rely on hashing for O(1)-expected edge ops.
- [[ods-02-array-based-lists]] — ArrayStack used as the per-vertex list in AdjacencyLists.
- [[ods-01-introduction]] — Queue/Stack interfaces used by BFS and DFS.
- [[matrices]] — algebraic graph operations on adjacency matrices.
- [[ods-06-binary-trees]] — DFS forest is a generalization of binary-tree traversal.

## Contradictions
None.
