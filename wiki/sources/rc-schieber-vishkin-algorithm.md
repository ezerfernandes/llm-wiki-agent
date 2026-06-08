---
title: "Schieber-Vishkin algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, trees, parallel-computing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Schieber-Vishkin_algorithm
---

## Summary
The task asks the programmer to implement the Schieber-Vishkin algorithm, a parallel technique for finding the lowest common ancestor (LCA) of two nodes in a rooted tree. The key insight is that by preprocessing the tree in O(n) time to assign each node a bit-encoded label describing its position in the hierarchy, any subsequent LCA query can be answered in O(1) constant time. It is a foundational result in the CREW PRAM model of parallel computing.

## Task Requirements
- Represent a rooted tree T = (V, E) with n nodes, identifying the root.
- Preprocess the tree (typically via DFS traversal) to assign each node a label encoding its position, achieving O(n) time and O(n) space.
- Given a query pair of nodes (u, v), return the deepest node w that is an ancestor of both — the lowest common ancestor.
- Answer each LCA query in O(1) time using the precomputed labels.

## Language Coverage
21 languages implement this task, giving moderate breadth across systems, scripting, and JVM languages. Representative implementations include C++, C#, Go, Java, JavaScript, Julia, Python, Rust, Swift, and Wren.

## Connections
- [[LowestCommonAncestor]] — the core problem the algorithm solves
- [[TreeDataStructure]] — the input structure being queried
- [[DepthFirstSearch]] — used during the preprocessing traversal
- [[ParallelComputing]] — the algorithm targets the CREW PRAM model
- [[BitManipulation]] — node labels are bit-encoded for constant-time queries

## Contradictions
- None — reference task page.
