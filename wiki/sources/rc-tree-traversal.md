---
title: "Tree traversal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, recursion, trees]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tree_traversal
---

## Summary
The task asks the programmer to build a binary tree whose nodes each hold an integer, then implement the four standard tree traversal orders: pre-order, in-order, post-order, and level-order. The first three are naturally expressed by depth-first recursion that varies only in when the node is visited relative to its children, while level-order is a breadth-first walk typically driven by a queue.

## Task Requirements
- Define a binary tree where each node carries an integer value.
- Implement pre-order traversal (visit node, then left subtree, then right subtree).
- Implement in-order traversal (left, node, right).
- Implement post-order traversal (left, right, node).
- Implement level-order (breadth-first) traversal.
- Populate a specific 9-node sample tree and print all four traversals, matching the expected output (e.g. preorder `1 2 4 7 5 3 6 8 9`, level-order `1 2 3 4 5 6 7 8 9`).

## Language Coverage
109 languages implement this task, spanning functional, imperative, object-oriented, and assembly paradigms — reflecting how foundational tree traversal is. Representative implementations include Haskell, OCaml, Scheme, Python, Java, C, C++, Rust, Go, and Prolog.

## Connections
- [[BinaryTree]] — the data structure being traversed
- [[Recursion]] — the natural mechanism for depth-first orders
- [[DepthFirstSearch]] — pre/in/post-order are DFS visit orderings
- [[BreadthFirstSearch]] — level-order is BFS, usually queue-driven
- [[Queue]] — supports the level-order traversal

## Contradictions
- None — reference task page.
