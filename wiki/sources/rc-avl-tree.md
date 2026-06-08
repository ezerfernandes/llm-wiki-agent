---
title: "AVL tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, binary-search-tree, balancing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/AVL_tree
---

## Summary
The task asks the programmer to implement an AVL tree — a self-balancing binary search tree — in the language of choice, providing at least the basic operations. The defining invariant is that the heights of any node's two child subtrees differ by at most one; whenever an insertion or deletion violates this, the tree is rebalanced via one or more rotations. This guarantees O(log n) lookup, insertion, and deletion in both the average and worst cases.

## Task Requirements
- Implement an AVL tree in the chosen language.
- Provide at least the basic operations (lookup, insertion, deletion).
- Maintain the height-balance invariant: sibling subtree heights differ by at most one, restored through tree rotations after modifications.
- Treat node keys as a set — duplicate keys are not allowed.

## Language Coverage
46 languages implement this task, spanning low-level assembly, systems, functional, and scripting families. Representative implementations include C, C++, C#, Java, Python, Rust, Go, Haskell, Common Lisp, Scheme, and even AArch64/ARM Assembly.

## Connections
- [[BinarySearchTree]] — an AVL tree is a self-balancing specialization of this structure.
- [[TreeRotation]] — the rebalancing operation used to restore the height invariant.
- [[RedBlackTree]] — the page contrasts AVL trees against this alternative balanced BST.
- [[BinaryTree]] — the underlying recursive node structure.
- [[BigONotation]] — characterizes the O(log n) cost of the supported operations.

## Contradictions
- None — reference task page.
