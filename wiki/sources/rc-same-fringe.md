---
title: "Same fringe (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, trees, recursion, concurrency]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Same_fringe
---

## Summary
The task is to write a routine that compares the leaves (the "fringe") of two binary trees and decides whether they form the same left-to-right sequence of values, ignoring tree shape or balance. The key insight is that an elegant solution interleaves the two traversals rather than fully flattening either tree first, so it can short-circuit and report inequality the moment the fringes diverge — a classic showcase for concurrency, coroutines, or lazy evaluation.

## Task Requirements
- Compare the ordered list of leaf values of two binary trees for equality.
- Only the number, order, and value of leaves matter; internal structure and balance are irrelevant.
- Any binary tree representation is allowed, provided nodes are orderable and only downward links are used (no parent or sibling pointers to circumvent recursion).
- Preferred (though not mandatory) is a solution that does the minimum work to falsify equivalence, short-circuiting once the fringes differ rather than collecting an entire fringe up front.

## Language Coverage
33 languages implement this task, spanning functional, imperative, and concurrent paradigms, with idiomatic lazy or coroutine-based approaches common. Representative implementations include Haskell, OCaml, F#, Clojure, Racket, Scheme, Python, Go, C++, Java, and Raku.

## Connections
- [[BinaryTree]] — the data structure whose leaves are compared
- [[TreeTraversal]] — in-order/left-to-right leaf enumeration drives the comparison
- [[Coroutines]] — interleaving the two traversals to avoid full flattening
- [[LazyEvaluation]] — produces fringe elements on demand for short-circuiting
- [[Recursion]] — natural way to walk each tree's downward links

## Contradictions
- None — reference task page.
