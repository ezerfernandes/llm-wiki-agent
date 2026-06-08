---
title: "Algebraic data types (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, type-systems, pattern-matching, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Algebraic_data_types
---

## Summary
This task demonstrates algebraic data types (ADTs) and pattern matching by implementing insertion into a red-black tree. The canonical example follows Okasaki's functional approach, where the tree node — carrying a color attribute of red or black — is modeled as a sum type, and the rebalancing logic is expressed as a handful of pattern-match cases. The key insight is that ADTs plus pattern matching let the balancing algorithm be written almost verbatim from its case analysis, rather than through manual tagging and nested conditionals.

## Task Requirements
- Implement insertion into a red-black tree.
- A red-black tree is a binary tree where each internal node has a color of red or black.
- Enforce the invariants: no red node may have a red child, and every path from the root to an empty node must contain the same number of black nodes.
- These invariants keep the tree balanced, so the tree must be re-balanced after each insertion.
- Where the language supports it, use algebraic data types and pattern matching rather than manual tag-and-conditional simulation.

## Language Coverage
41 languages implement this task, spanning functional languages with native ADT support, Lisps, and procedural languages that simulate the construct. Representative implementations include Haskell, OCaml, Standard ML, F#, Scala, Rust, Erlang, Elixir, Racket, and Common Lisp.

## Connections
- [[AlgebraicDataType]] — the sum-of-products type construct the task showcases
- [[PatternMatching]] — the deconstruction mechanism that makes the rebalancing terse
- [[RedBlackTree]] — the self-balancing binary search tree being implemented
- [[BinarySearchTree]] — the underlying ordered tree structure
- [[FunctionalProgramming]] — the paradigm behind Okasaki's referenced approach

## Contradictions
- None — reference task page.
