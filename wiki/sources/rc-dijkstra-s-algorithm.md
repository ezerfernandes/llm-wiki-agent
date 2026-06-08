---
title: "Dijkstra's algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, shortest-path]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dijkstra's_algorithm
---

## Summary
The task asks the programmer to implement Dijkstra's algorithm, which solves the single-source shortest path problem for a directed graph with non-negative edge weights. Given a start node, the algorithm produces a shortest-path tree (a set of edges describing the cheapest route to every reachable node), without specifying a destination. The key insight is greedily settling the lowest-cost frontier node and relaxing its outgoing edges to update tentative distances.

## Task Requirements
- Implement Dijkstra's algorithm that outputs a set of edges depicting the shortest path to each reachable node from an origin.
- Run the program on a given 6-node directed weighted graph (vertices a–f) starting at node a, using the provided edge/cost table.
- Write code that interprets that output to report the shortest path from node a to nodes e and f.
- Vertices may be identified by numbers or names; inputs are an adjacency matrix/list plus a start node.

## Language Coverage
71 languages implement this task, showing broad coverage across systems, functional, scripting, and niche languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Prolog, and Wren.

## Connections
- [[DijkstrasAlgorithm]] — the named technique being implemented
- [[ShortestPathProblem]] — the single-source problem it solves
- [[GraphTheory]] — directed, weighted graphs are the input domain
- [[PriorityQueue]] — efficient implementations use a min-heap to select the next frontier node
- [[GreedyAlgorithm]] — the algorithm settles the lowest-cost node at each step

## Contradictions
- None — reference task page.
