---
title: "Set consolidation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, set-theory, graph-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Set_consolidation
---

## Summary
The task asks the programmer to consolidate a collection of sets: any two sets that share at least one common element are merged into their union, and this merging is repeated until no two remaining sets overlap. The key insight is that this is exactly the problem of finding connected components in a graph where sets are nodes and a shared element is an edge — overlapping sets belong to the same component and collapse into one.

## Task Requirements
- Given two sets: if they share no element, return both unchanged; if they share an element, return their single union.
- Given N>2 sets: repeatedly replace any pair of sets that share an element with their consolidation until no further merges are possible.
- If N<2, consolidation is undefined and the input is returned as-is.
- Treat sets as unordered (element order is immaterial).

## Language Coverage
60 languages implement this task, giving broad coverage across functional, imperative, and array styles. Representative implementations include Python, Haskell, C, C++, Java, Go, Ruby, Perl, Racket, Clojure, and J.

## Connections
- [[SetTheory]] — operates on set union and intersection (common-element detection)
- [[ConnectedComponents]] — consolidation is equivalent to finding connected components in a graph
- [[GraphTheory]] — sets as nodes, shared elements as edges
- [[UnionFind]] — a natural algorithm for grouping overlapping sets efficiently

## Contradictions
- None — reference task page.
