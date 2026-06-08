---
title: "Flatten a list (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Flatten_a_list
---

## Summary
The task asks the programmer to write a function that collapses an arbitrarily nested list of values into a single flat list, preserving the left-to-right order of the leaf elements. The canonical example transforms `[[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]` into `[1, 2, 3, 4, 5, 6, 7, 8]`. The key insight is that flattening is naturally expressed by recursion (or an explicit stack): recurse into sublists and discard empty ones, while emitting scalar leaves.

## Task Requirements
- Implement a function that accepts an arbitrarily deeply nested list of values.
- Return a single list containing all the leaf (non-list) values in order.
- Handle empty sublists at any depth correctly (they contribute nothing to the output).
- Work for the given test list and yield exactly `[1, 2, 3, 4, 5, 6, 7, 8]`.

## Language Coverage
134 languages implement this task, reflecting how universal nested-list handling is across paradigms. Representative implementations include Python, Haskell, Common Lisp, Scheme, Prolog, Ruby, Clojure, J, Rust, and JavaScript, spanning functional, logic, array, and imperative styles.

## Connections
- [[Recursion]] — the standard technique for descending into nested sublists.
- [[TreeTraversal]] — flattening is a depth-first traversal that collects leaf nodes; the task itself links to Tree traversal.
- [[NestedDataStructures]] — the input is a tree-like arbitrarily nested list.
- [[HigherOrderFunctions]] — many solutions use fold/reduce or concatMap to assemble the flat result.

## Contradictions
- None — reference task page.
