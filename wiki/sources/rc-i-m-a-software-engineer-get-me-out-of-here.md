---
title: "I'm a software engineer, get me out of here (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-algorithms, shortest-path]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/I'm_a_software_engineer,_get_me_out_of_here
---

## Summary
This task wraps two classic shortest-path problems in a wartime escape narrative built on a 23x23 grid map. Each non-zero cell holds a number giving how many cells a party may travel in a single day in any of eight directions (orthogonal or diagonal); cells marked 0 are safe destinations. The core insight is to model the grid as a weighted graph where moving across a cell costs one day, then apply standard graph algorithms to it.

## Task Requirements
- Part 1: Use Dijkstra's algorithm to find the shortest route(s) from HQ at center (11,11) to any safety cell (value 0).
- Part 2: Use Floyd's (Floyd-Warshall) algorithm to compute all-pairs shortest paths; print the shortest route from (21,11) to (1,11) and from (1,11) to (21,11), plus the longest shortest route between any two points.
- Extra credit: Determine whether any cell is unreachable from HQ, and identify which cells take longest to reinforce from HQ.

## Language Coverage
15 languages implement this task, a moderate spread spanning systems, functional, and scripting tongues. Representative implementations include C++, F#, Go, Java, Julia, Python, Perl, Raku, Nim, and Wren.

## Connections
- [[DijkstrasAlgorithm]] — single-source shortest path for Part 1
- [[FloydWarshallAlgorithm]] — all-pairs shortest path for Part 2
- [[GraphTheory]] — the grid is modeled as a weighted directed graph
- [[ShortestPath]] — the central problem class of the task

## Contradictions
- None — reference task page.
