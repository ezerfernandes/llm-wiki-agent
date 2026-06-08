---
title: "Blossom algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, matching, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Blossom_algorithm
---

## Summary
The task asks the programmer to implement Edmonds' Blossom algorithm (1965), which finds a maximum matching in a general undirected graph in polynomial time. The key insight is that odd-length cycles ("blossoms") encountered while hunting for augmenting paths can be contracted into a single pseudo-vertex; the search continues in the smaller graph and augmenting paths are then "lifted" back, repeating until no augmenting path remains.

## Task Requirements
- Given a general graph G = (V, E), compute a matching M (a set of edges sharing no common vertex) of maximum size |M|.
- Handle general graphs, including odd-length cycles, not just bipartite graphs.
- Use the augmenting-path approach extended with blossom shrinking/expanding, relying on Berge's lemma (a matching is maximum iff it admits no augmenting path).
- Achieve a polynomial-time solution; Edmonds' original is O(|V|^2·|E|), with an O(|V|^3) variant being easier to implement.

## Language Coverage
16 languages implement this task, spanning systems languages and high-level scripting. Representative implementations include C++, C#, Rust, Go, Java, JavaScript, Python, Julia, Kotlin, Fortran, and Raku.

## Connections
- [[GraphTheory]] — operates on vertices and edges of a general graph
- [[MaximumMatching]] — the optimization problem being solved
- [[AugmentingPath]] — the core search primitive extended to handle odd cycles
- [[BergesLemma]] — the optimality criterion guaranteeing maximality
- [[BreadthFirstSearch]] — underlying traversal used to grow alternating-path forests

## Contradictions
- None — reference task page.
