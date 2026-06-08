---
title: "Hamiltonian Cycle via Chvátal Closure (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, graph-algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hamiltonian_Cycle_via_Chvátal_Closure
---

## Summary
The task asks the programmer to decide whether a simple undirected graph contains a Hamiltonian cycle (a cycle visiting every vertex exactly once) using the Bondy–Chvátal closure test. The closure cl(G) is built by repeatedly adding an edge between any two non-adjacent vertices u, v whenever deg(u) + deg(v) ≥ n, until no more edges can be added. The key insight is that if this closure is the complete graph Kₙ, the original graph is guaranteed Hamiltonian; otherwise the test is inconclusive. This is a sufficient (not necessary) condition, so it sidesteps the NP-hardness of the general Hamiltonian cycle problem.

## Task Requirements
- Accept a simple undirected graph G = (V, E) with |V| = n.
- Compute the closure cl(G): repeatedly add edge (u, v) for non-adjacent u, v whenever deg(u) + deg(v) ≥ n until no further edges qualify.
- If the closure equals the complete graph Kₙ, report that G is Hamiltonian (by the Bondy–Chvátal theorem).
- Otherwise report that no definitive conclusion can be drawn.
- A naive implementation is O(n⁵); with suitable data structures it can be reduced to O(n³).

## Language Coverage
15 languages implement this task, giving moderate breadth across systems, scripting, statistical, and BASIC-family languages. Representative implementations include C#, C++, Go, Java, JavaScript, Julia, Python, R, Rust, and Wren.

## Connections
- [[GraphTheory]] — the task operates on simple undirected graphs and graph closures.
- [[HamiltonianCycle]] — the central object the test reasons about.
- [[BondyChvatalTheorem]] — the theorem that justifies the closure test as a sufficient condition.
- [[VertexDegree]] — the deg(u) + deg(v) ≥ n criterion drives edge addition.
- [[NPHardness]] — context: the general Hamiltonian cycle problem is NP-complete, motivating sufficient-condition shortcuts.

## Contradictions
- None — reference task page.
