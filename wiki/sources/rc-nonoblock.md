---
title: "Nonoblock (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nonoblock
---

## Summary
Nonoblock is a simplified single-row variant of the Nonogram puzzle. Given a row of a fixed number of cells and an ordered list of block sizes, the task is to enumerate every legal arrangement of those blocks within the row (blocks keep their order, each pair separated by at least one empty cell). The key insight is a recursive placement: the leftmost block can slide from the left edge up to the rightmost position that still leaves enough room for the remaining blocks, and each remaining block is placed recursively in the space to its right.

## Task Requirements
- Accept the number of cells in a row and a space-separated, left-to-right ordered list of block sizes.
- Show every possible legal positioning of the blocks and report the total count of arrangements.
- Render each arrangement as a neat diagram (e.g. `|#|#|_|#|_|` or `##.#.`), with blocks always separated by at least one space.
- Enumerate five configurations: 5 cells / [2,1]; 5 cells / [] (no blocks); 10 cells / [8]; 15 cells / [2,3,2,3]; and 5 cells / [2,3] (which must indicate it is impossible).

## Language Coverage
38 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative entries include C, C++, C#, Rust, Go, Java, JavaScript, Python, Perl, Raku, Julia, and Racket.

## Connections
- [[Combinatorics]] — counting valid placements of ordered blocks within constrained space.
- [[Recursion]] — the reference algorithm places each block recursively in the remaining space.
- [[Nonogram]] — Nonoblock is a single-row reduction of the full Nonogram puzzle.
- [[ConstraintSatisfaction]] — block ordering and spacing impose placement constraints.

## Contradictions
- None — reference task page.
