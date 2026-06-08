---
title: "Dominoes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, backtracking, tiling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dominoes
---

## Summary
Given a 7-row by 8-column tableau of pip values formed by laying a shuffled set of dominoes into a rectangle, the task is to recover where each individual domino sits — that is, partition the 56 cells into 28 adjacent pairs that match a valid placement of the tiles. The key insight is that this is a perfect-matching / exact-cover problem over the grid, typically solved with backtracking that pairs each cell with a horizontal or vertical neighbor.

## Task Requirements
- Parse the given 7x8 tableau of face values and identify the position and orientation of each domino.
- Demonstrate the solver on the supplied example tableau and on a second tableau of the programmer's own construction.
- Extra credit: count the number of ways to arrange dominoes in an 8x7 rectangle — first ignoring values, then considering values, and finally considering values but ignoring value symmetry (treating 5 and 4 as interchangeable when transposed).

## Language Coverage
14 languages implement this task, a moderate spread across systems, functional, and scripting families. Representative implementations include C++, Java, JavaScript, Julia, Python, Perl, Raku, F#, Nim, Phix, FreeBASIC, and Wren.

## Connections
- [[Backtracking]] — the natural strategy for partitioning the grid into adjacent domino pairs
- [[ExactCover]] — recovering the tiling is a cover of all 56 cells by 28 dominoes
- [[Combinatorics]] — the extra-credit counting of distinct arrangements
- [[GraphMatching]] — pairing adjacent cells is a perfect matching on the grid graph
- [[Tiling]] — placing dominoes over a rectangular board is a classic tiling problem

## Contradictions
- None — reference task page.
