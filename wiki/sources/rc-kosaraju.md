---
title: "Kosaraju (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, depth-first-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kosaraju
---

## Summary
The task asks the programmer to implement Kosaraju's algorithm (also called Kosaraju–Sharir), a linear-time method for finding the strongly connected components (SCCs) of a directed graph. The key insight is that the transpose graph — the same graph with every edge reversed — has exactly the same SCCs as the original, so two depth-first search passes (one to order vertices by finish time, one over the transpose in that order) suffice to recover all components.

## Task Requirements
- Implement Kosaraju's algorithm to find strongly connected components of a directed graph.
- Use the specific 8-node directed graph given (nodes 0–7 with edges such as 0→1, 1→2, 2→0, 3→{1,2,4}, 4→{3,5}, 5→{2,6}, 6→5, 7→{4,6,7}).
- Report the strongly connected component for each node.

## Language Coverage
34 languages implement this task, spanning systems, functional, scripting, and array-oriented styles. Representative implementations include C++, Rust, Go, Java, Python, OCaml, Standard ML, Racket, Perl, Raku, J, K, and Wren.

## Connections
- [[KosarajuAlgorithm]] — the specific two-pass SCC algorithm being implemented
- [[StronglyConnectedComponents]] — the graph property the task computes
- [[DepthFirstSearch]] — the traversal used in both passes
- [[DirectedGraph]] — the input data structure, including its transpose
- [[GraphAlgorithms]] — the broader family this task belongs to

## Contradictions
- None — reference task page.
