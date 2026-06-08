---
title: "Cartesian product of two or more lists (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, list-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cartesian_product_of_two_or_more_lists
---

## Summary
This task asks the programmer to generate the Cartesian product of two arbitrary lists, producing every ordered pair drawn one element from each list. The key insight is that ordering matters (A × B differs from B × A) and that pairing with an empty list yields an empty result. For extra credit, the solution should generalize to an n-ary product over an arbitrary number of lists, typically by accepting a list of lists.

## Task Requirements
- Show an idiomatic way to compute the Cartesian product of two lists, e.g. {1,2} × {3,4} = {(1,3),(1,4),(2,3),(2,4)}.
- Demonstrate non-commutativity: {3,4} × {1,2} = {(3,1),(3,2),(4,1),(4,2)}.
- Show that a product involving an empty list is empty: {1,2} × {} = {} and {} × {1,2} = {}.
- Extra credit: implement an n-ary product over an arbitrary number of lists of arbitrary length.
- Use the n-ary function on the provided multi-list test cases, including one containing an empty list (which must yield an empty result).

## Language Coverage
77 languages implement this task, spanning functional, imperative, array, and stack-based paradigms. Representative implementations include Python, Haskell, J, APL, Java, C++, Rust, Clojure, Raku, and Prolog.

## Connections
- [[CartesianProduct]] — the core set-theoretic operation being implemented
- [[Combinatorics]] — enumeration of all combinations across sets
- [[Recursion]] — common strategy for the n-ary generalization
- [[ListComprehension]] — idiomatic expression used in many functional languages
- [[FoldOperation]] — reducing a list of lists into their product

## Contradictions
- None — reference task page.
