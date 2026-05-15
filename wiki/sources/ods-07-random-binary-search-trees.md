---
title: "ODS Ch.7: Random Binary Search Trees"
type: source
tags: [book, data-structures, trees, randomization, treap]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 7
pages: "145-164"
---

## Summary
Two ways to use randomization to keep an unbalanced BinarySearchTree balanced in expectation. **Random Binary Search Tree**: insert n distinct keys in a uniformly random permutation order. Lemma 7.1 shows the expected search-path length is H_(x+1) + H_(n−x) − O(1) = 2·ln n + O(1), via the indicator-random-variable trick on harmonic numbers. **Treap**: assign each key a uniformly random priority and maintain heap order on priorities (smallest priority at the root) plus BST order on keys via tree rotations during add/remove. The Treap dynamically simulates a random binary search tree without controlling the input order.

## Key Claims
- **The fundamental observation**: in a BST built from random permutation π, key i is on the search path for x ∈ {0, ..., n−1} iff i appears before any of {i+1, ..., ⌊x⌋} in π. This makes the path-length expectation a sum of harmonic-derived probabilities.
- **Lemma 7.1**: expected search path length is H_(x+1) + H_(n−x) − O(1), bounded by 2·ln n + O(1) = O(log n).
- **Harmonic number bounds**: ln k < H_k ≤ ln k + 1 (provable via integral comparison ∫_1^k (1/x)dx = ln k).
- **Treap**: random priorities make the resulting tree distributed identically to a random BST, regardless of insertion order. add(x) is BST insert + bubble-up by rotations to restore heap order; remove(x) is rotate-to-leaf + delete.
- **Both structures give O(log n) expected time** for find/add/remove. The randomness is over the choice of priorities (treap) or insertion permutation (RBST), not over the input.

## Key Quotes
> "If we choose a random permutation of 0,...,14 and add its elements, one by one, into a BinarySearchTree, then we are more likely to get a very balanced tree than we are to get a very unbalanced tree."
> "The expected length of the search path for x is H_(x+1) + H_(n−x) − O(1)."

## Connections
- [[ods-06-binary-trees]] — base BinarySearchTree class extended.
- [[ods-04-skiplists]] — alternative randomized SSet with similar expected guarantees.
- [[ods-08-scapegoat-trees]] — deterministic alternative balancing via partial rebuild.
- [[ods-09-red-black-trees]] — deterministic worst-case O(log n) alternative.
- [[ods-11-sorting-algorithms]] — quicksort recursion tree analysis re-uses harmonic-number expectation.
- [[logarithms]] — natural-logarithm bounds on H_k used throughout.

## Contradictions
None.
