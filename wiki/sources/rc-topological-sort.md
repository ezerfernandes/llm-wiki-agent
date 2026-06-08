---
title: "Topological sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, dependency-resolution]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Topological_sort
---

## Summary
The task asks the programmer to compute a valid topological ordering of items given a mapping of each item to the items it depends on, framed concretely as finding a legal compile order for VHDL libraries where every library must come after the libraries it depends on. The key insight is that such an ordering only exists for a directed acyclic graph; a cycle among genuine dependencies makes the set un-orderable and must be reported.

## Task Requirements
- Write a function that returns a valid compile order of libraries from their dependency list.
- Treat library names as single words.
- Include items that appear only as dependents (with no dependencies of their own) in the output ordering.
- Ignore any self-dependencies.
- Detect and flag any un-orderable (cyclic) dependencies rather than producing a bogus order.
- Demonstrate against the provided VHDL library dependency dataset.

## Language Coverage
65 languages implement this task, spanning system, functional, scripting, and array families. Representative entries include C, C++, Java, Python, Go, Rust, Haskell, Common Lisp, Perl, Raku, J, and Tcl.

## Connections
- [[TopologicalSorting]] — the core ordering this task computes.
- [[DirectedAcyclicGraph]] — a valid order exists only when the dependency graph is a DAG.
- [[KahnsAlgorithm]] — Kahn's 1962 algorithm, one of the two standard approaches noted on the page.
- [[DepthFirstSearch]] — the DFS-based topological sort, the other standard approach.
- [[CycleDetection]] — needed to flag un-orderable dependency sets.

## Contradictions
- None — reference task page.
