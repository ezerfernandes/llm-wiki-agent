---
title: "Pentomino tiling (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, exact-cover, backtracking, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pentomino_tiling
---

## Summary
The task is to tile an 8x8 grid using the 12 distinct free pentominoes (each a shape of 5 connected squares), using every shape exactly once with no overlaps, while leaving 4 randomly chosen cells uncovered. This is a classic instance of the exact cover problem, since 12 pentominoes cover 60 of the 64 cells. The key insight is that not every choice of the 4 uncovered cells yields a solvable board, so the solver must backtrack and may need to retry with different gaps.

## Task Requirements
- Build an 8 by 8 grid (64 cells).
- Cover 60 cells with all 12 pentomino shapes, each used exactly once, allowing rotations and reflections of each piece.
- No two pieces may overlap.
- Leave exactly 4 cells uncovered, chosen at random.
- Account for the fact that not all gap configurations are solvable.
- Print the resulting tiling.

## Language Coverage
18 languages implement this task, giving moderate breadth across systems, functional, and scripting languages. Representative implementations include C++, C#, Go, Java, Python, Julia, Kotlin, Nim, Perl, Raku, Racket, and Wren.

## Connections
- [[ExactCover]] — the problem is a canonical exact cover instance
- [[Backtracking]] — the standard solving technique for placing/removing pieces
- [[Polyomino]] — pentominoes are the order-5 polyominoes used as tiles
- [[DancingLinks]] — Knuth's Algorithm X / DLX is a common efficient solver
- [[Combinatorics]] — enumerating orientations and placements of the 12 shapes

## Contradictions
- None — reference task page.
