---
title: "Set (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, discrete-math]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Set
---

## Summary
This task asks the programmer to demonstrate the core operations of a mathematical set — an unordered collection of distinct elements with no duplicates. Implementations must show creation, membership testing, and the standard algebraic operations (union, intersection, difference, subset, equality). The key insight is that the underlying representation (associative array, hash table, balanced binary search tree, or bit array) determines the cost of membership testing, ranging from O(n) for a sequential list to O(1) average-case for a hash table.

## Task Requirements
- Set creation.
- Membership test: m ∈ S ("m is an element of set S").
- Union (A ∪ B): all elements in either A or B.
- Intersection (A ∩ B): all elements in both A and B.
- Difference (A \ B): all elements in A that are not in B.
- Subset (A ⊆ B): true if every element of A is also in B.
- Equality (A = B): true if A and B contain exactly the same elements.
- Optional: proper subset (A ⊂ B, where A ⊆ B but A ≠ B), other set operations, and mutating a mutable set.

## Language Coverage
97 languages implement this task, reflecting that sets are a near-universal data structure with built-in or library support across paradigms. Representative implementations include Python, Java, C++, Haskell, Clojure, Ruby, Rust, Scala, Common Lisp, and Wren.

## Connections
- [[SetTheory]] — the mathematical foundation of the operations
- [[HashTable]] — common O(1) average-case backing store for membership
- [[BinarySearchTree]] — alternative O(log n) ordered representation
- [[AssociativeArray]] — keys-as-elements implementation strategy
- [[BitwiseOperations]] — bit-array representation for small universes

## Contradictions
- None — reference task page.
