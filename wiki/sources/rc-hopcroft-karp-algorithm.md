---
title: "Hopcroft-Karp Algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, matching, bipartite]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hopcroft-Karp_Algorithm
---

## Summary
The task is to implement the Hopcroft-Karp algorithm, which finds a maximum cardinality matching in a bipartite graph — a graph whose vertices split into two disjoint sets U and V, with every edge crossing between them. The key insight is that the algorithm repeatedly finds, via BFS, the shortest augmenting paths and then augments along many vertex-disjoint such paths at once via DFS, yielding O(E·√V) running time, faster than the naive O(V·E) augmenting-path approach.

## Task Requirements
- Given a bipartite graph G = (U ∪ V, E), compute a matching M ⊆ E whose size |M| is maximized.
- Ensure no vertex is incident to more than one matched edge (no two edges share a U-vertex or a V-vertex).
- Implement the phased structure: an outer loop driven by BFS that layers vertices by distance, then a DFS pass that augments along shortest augmenting paths.
- Use the standard supporting structures: pair_u, pair_v matching arrays, a dist array, and a NIL sentinel for unmatched vertices.

## Language Coverage
23 languages implement this task, giving solid breadth across systems, scripting, and functional styles. Representative entries include C++, C#, Java, Go, Rust, Python, JavaScript, Julia, Perl, Raku, Kotlin, and Wren.

## Connections
- [[BipartiteGraph]] — the input structure the algorithm operates on
- [[MaximumMatching]] — the optimization objective being solved
- [[AugmentingPath]] — the core technique for improving a matching each phase
- [[BreadthFirstSearch]] — layers vertices to find shortest augmenting paths
- [[DepthFirstSearch]] — augments along the discovered layered paths

## Contradictions
- None — reference task page.
