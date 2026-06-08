---
title: "Graph colouring (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, greedy-algorithm]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Graph_colouring
---

## Summary
The task is to assign colours (integers) to the vertices of an undirected graph so that no edge connects two vertices of the same colour, while trying to minimise the total number of colours used. Since computing the chromatic number exactly is intractable, the task explicitly accepts a heuristic (such as greedy or Welsh-Powell colouring) rather than exhaustive search. A key subtlety it highlights is that the order in which vertices are processed affects how many colours a greedy algorithm ends up using.

## Task Requirements
- Represent graphs as edges written `a-b`, with isolated nodes given alone (e.g. `0-1 1-2 2-0 3`); build an adjacency mapping from node to its neighbours.
- Colour vertices using a heuristic that does better than giving every vertex its own colour, aiming to minimise colour count (exhaustive search is not required).
- For each edge, show the colours assigned to each of its two endpoints.
- Report the total number of nodes, edges, and colours used for each graph.
- Run on the four supplied example graphs (Ex1 through Ex4), where Ex2, Ex3, and Ex4 are the same underlying graph with differing node namings/orderings to expose how input order changes greedy results.

## Language Coverage
20 languages implement this task, spanning systems and functional styles. Representative entries include C++, C#, Rust, Go, Java, JavaScript, Haskell, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[GraphTheory]] — vertices, edges, and adjacency are the core objects.
- [[GreedyAlgorithm]] — the standard heuristic for assigning the smallest available colour per vertex.
- [[GraphColoring]] — the named problem of colouring vertices subject to edge constraints.
- [[WelshPowellAlgorithm]] — a degree-ordered greedy colouring referenced by the task.
- [[NPHardProblems]] — finding the chromatic number exactly is computationally intractable.

## Contradictions
- None — reference task page.
