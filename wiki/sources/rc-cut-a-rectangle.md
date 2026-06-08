---
title: "Cut a rectangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, graph-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cut_a_rectangle
---

## Summary
Given an m × n grid of unit squares, the task is to count the number of distinct cuts along square edges that split the rectangle into two connected pieces of identical shape (one being the 180°-rotation of the other). Such a halving cut is only possible when m and n are not both odd. The key insight is that every valid cut is a self-symmetric path through the grid's center, so the problem reduces to counting paths from the center to the boundary via a depth-first traversal, exploiting the 180° rotational symmetry to avoid double counting.

## Task Requirements
- Compute the number of different ways to cut an m × n rectangle into two congruent, connected halves.
- A cut is a path along the square edges; the two resulting pieces must have the same shape after rotating one by 180°.
- Note that a halving cut exists only when m and n are not both odd.
- Optionally, display each of the individual cuts.

## Language Coverage
36 languages implement this task, spanning systems and functional languages alongside scripting and array-oriented ones. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Perl, Raku, J, and Wren.

## Connections
- [[Combinatorics]] — counting the distinct valid cut paths
- [[DepthFirstSearch]] — enumerating paths from the grid center outward
- [[GridGraph]] — the rectangle modeled as a lattice of edges and vertices
- [[Symmetry]] — exploiting 180° rotational symmetry of the two halves
- [[MazeGeneration]] — related path-carving traversal noted on the task page

## Contradictions
- None — reference task page.
