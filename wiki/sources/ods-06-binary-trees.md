---
title: "ODS Ch.6: Binary Trees"
type: source
tags: [book, data-structures, trees, traversal]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 6
pages: "127-144"
---

## Summary
Foundational treatment of binary trees: a connected, undirected, finite graph with no cycles where no vertex has degree > 3. Most computer-science applications use **rooted, ordered** binary trees (left vs. right child). The chapter establishes vocabulary (depth, height, ancestor, descendant, subtree, leaf, external nodes) and presents **BinarySearchTree**, an unbalanced binary search tree implementing SSet operations in time proportional to the height of the tree (worst-case O(n) for skewed trees). Covers recursive vs. iterative traversal, including how to traverse without recursion using the parent pointer (avoids stack overflow on tall trees).

## Key Claims
- **Tree terminology.** Depth(u) is the path length from u to root. Height(u) is the longest path from u to any descendant. Height(tree) = height(root). External nodes (n+1 of them in a tree with n real nodes) are useful as algorithmic conveniences.
- **Recursive vs iterative traversal.** Recursion is concise but stack-bounded by tree height. The non-recursive `traverse2()` uses the parent pointer plus a "previous" pointer to compute the next move from any node.
- **BinarySearchTree** stores keys with the BST invariant: all keys in left subtree < u.x < all keys in right subtree. find(x) walks down comparing; insert places new leaf at the search-failure point; remove with two children uses successor-replacement.
- **Performance** is O(height). With adversarial inputs, height can be Θ(n), motivating the balanced trees in [[ods-07-random-binary-search-trees]], [[ods-08-scapegoat-trees]], [[ods-09-red-black-trees]].
- **Breadth-first traversal** uses a Queue; depth-first uses a Stack (or recursion).
- **Size and height computed recursively** in O(n) by recursive descent.

## Key Quotes
> "Mathematically, a binary tree is a connected, undirected, finite graph with no cycles, and no vertex of degree greater than three."
> "Using recursion this way produces very short, simple code, but it can also be problematic. The maximum depth of the recursion is given by the maximum depth of a node in the binary tree."

## Connections
- [[ods-07-random-binary-search-trees]] / [[ods-08-scapegoat-trees]] / [[ods-09-red-black-trees]] — balanced BSTs that bound height to O(log n).
- [[ods-10-heaps]] — implicit binary tree stored in an array (Eytzinger's method).
- [[ods-12-graphs]] — BFS / DFS algorithms generalized.
- [[ods-13-data-structures-for-integers]] — BinaryTrie is a binary tree over bits of integers.
- [[ods-14-external-memory-searching]] — B-trees generalize 2-4 trees to disk-block degree.

## Contradictions
None.
