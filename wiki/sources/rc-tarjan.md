---
title: "Tarjan (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tarjan
---

## Summary
The task asks the programmer to implement Tarjan's algorithm for finding the strongly connected components (SCCs) of a directed graph. The key insight is that a single depth-first search, tracking each vertex's discovery index and a "low-link" value (the smallest index reachable via the DFS subtree and back-edges), identifies SCC roots when a vertex's low-link equals its own index; an explicit stack then collects each component. The algorithm runs in linear time, matching alternatives like Kosaraju's and the path-based strong component algorithm.

## Task Requirements
- Implement Tarjan's strongly connected components algorithm for a directed graph.
- Perform a single depth-first traversal, assigning each vertex a discovery index and a low-link value.
- Use a stack of vertices on the current DFS path to detect and extract each SCC when a root vertex is found (low-link equals index).
- Output the strongly connected components of the input graph.

## Language Coverage
26 languages implement this task, spanning systems, scripting, and functional styles. Representative implementations include C, C++, C#, Java, JavaScript, Python, Go, Rust, Julia, Perl, Raku, and Racket.

## Connections
- [[StronglyConnectedComponents]] — the structures the algorithm computes
- [[DepthFirstSearch]] — the traversal at the algorithm's core
- [[GraphTheory]] — the problem domain
- [[KosarajuAlgorithm]] — alternative SCC method referenced as a cross-link
- [[RobertTarjan]] — the algorithm's namesake and discoverer

## Contradictions
- None — reference task page.
