---
title: "Tree from nesting levels (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, recursion, tree]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tree_from_nesting_levels
---

## Summary
The task asks the programmer to convert a flat list of positive integers — each denoting a nesting depth — into a nested-list tree where every integer appears, in order, at its specified depth. The key insight is that an increase in level opens new sub-lists while equal or decreasing levels place elements back at the appropriate existing depth. The result should be a usable nested data structure, not merely formatted output for printing.

## Task Requirements
- Accept a flat list of integers greater than zero representing nesting levels.
- Build a tree of nested lists so each integer sits at its depth of nesting, preserving input order.
- When the next integer exceeds the previous, nest it inside a sub-list of the prior item's container.
- Produce a real nested-list structure suitable for further computation.
- Generate and show results for the inputs `[]`, `[1, 2, 4]`, `[3, 1, 3, 1]`, `[1, 2, 3, 1]`, `[3, 2, 1, 3]`, and `[3, 3, 3, 1, 1, 3, 3, 3]`.

## Language Coverage
22 languages implement this task, covering functional, imperative, and object-oriented styles. Representative solutions include Python, Haskell, Raku, Perl, Go, Java, C#, C++, Julia, and J.

## Connections
- [[TreeDataStructure]] — the output is a depth-organized tree of nested lists.
- [[Recursion]] — natural approach for descending and ascending nesting levels.
- [[NestedLists]] — the target representation for the constructed tree.
- [[ListProcessing]] — transforming a flat sequence into a structured form.

## Contradictions
- None — reference task page.
