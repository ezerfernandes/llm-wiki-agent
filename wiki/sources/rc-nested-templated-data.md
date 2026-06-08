---
title: "Nested templated data (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, recursion, tree-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nested_templated_data
---

## Summary
The task asks the programmer to expand a template — an arbitrarily nested tree of integer indices — by substituting each index with its corresponding payload string drawn from a flat index-to-data mapping. The key insight is that the solution must hierarchically traverse the nested structure using the language's native lists/tuples and recursion, rather than treating the data as text to be string-replaced or regex-matched.

## Task Requirements
- Given a nested template `t` of integer indices and a flat list/mapping of payloads `p` ('Payload#0' ... 'Payload#6'), produce a new structure with identical nesting where each index is replaced by its payload.
- Preserve the nesting and ordering of the template (exact spacing/linefeeds may vary).
- Avoid simple string replacement or regular expressions; use native list/tuple structures and recursive traversal.
- Optional: report which payloads remain unused, and handle indices that have no corresponding payload.

## Language Coverage
29 languages implement this task, spanning functional, imperative, and array-oriented paradigms. Representative implementations include Python, Haskell, Julia, Racket, Raku, J, Go, C++, Java, and Wren.

## Connections
- [[Recursion]] — the natural mechanism for traversing arbitrarily deep nesting
- [[TreeTraversal]] — the template is a tree of indices walked depth-first
- [[DataStructures]] — relies on native nested lists/tuples rather than text manipulation
- [[Mapping]] — payloads are looked up via an index-to-string association

## Contradictions
- None — reference task page.
