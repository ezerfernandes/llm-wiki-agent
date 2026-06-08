---
title: "Gabow's algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, strongly-connected-components]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gabow's_algorithm
---

## Summary
The task asks the programmer to implement Gabow's algorithm, a single-pass depth-first-search method for finding all strongly connected components (SCCs) of a directed graph. An SCC is a maximal vertex set in which every pair of vertices is mutually reachable. The key insight is that Gabow's approach uses two stacks during DFS — one path stack and one "boundary" stack tracking potential SCC roots — to collapse cycles without computing the explicit low-link values that Tarjan's algorithm requires.

## Task Requirements
- Accept a digraph of V vertices (0 to V-1) with directed edges given as (v, w) pairs in an adjacency list.
- Compute the total number of SCCs in the graph.
- Assign each vertex a unique component identifier (integer >= 0).
- Provide a query to test whether two vertices belong to the same SCC.
- Return the component ID for any given vertex.
- Handle edge cases: empty graphs (V >= 0), cycles, self-loops, and parallel edges.
- Verify against the worked 13-vertex example digraph and pairwise connectivity checks (e.g., vertices 0 and 3, 0 and 7).

## Language Coverage
23 languages implement this task, spanning systems, scripting, and functional ecosystems. Representative entries include C++, C#, Go, Rust, Java, Python, JavaScript, Julia, Kotlin, Swift, and Raku.

## Connections
- [[StronglyConnectedComponents]] — the structures this algorithm computes
- [[DepthFirstSearch]] — the traversal Gabow's algorithm is built on
- [[TarjansAlgorithm]] — the closely related single-pass SCC algorithm using low-links
- [[DirectedGraph]] — the input data structure
- [[GraphTheory]] — the broader domain

## Contradictions
- None — reference task page.
