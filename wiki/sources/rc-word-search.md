---
title: "Word search (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, grid-placement, backtracking, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Word_search
---

## Summary
The task is to generate a 10x10 word search puzzle by packing at least 25 dictionary words into a grid, placing them horizontally, vertically, or diagonally (and optionally reversed) so that they may overlap but never zigzag or wrap. Words are drawn from the unixdict list, restricted to alphabetic strings longer than two characters. The key constraint is that every cell left over after placement must spell the message "Rosetta Code" (uppercase), evenly distributed across the grid, so the puzzle layout and the message are co-designed rather than independent.

## Task Requirements
- Build a 10 by 10 grid of letters.
- Source words from the unixdict word list; use only words longer than 2 chars with no non-alphabetic characters.
- Place words horizontally, vertically, or diagonally, allowing reversed spellings.
- Words may overlap but must not zigzag or wrap around the grid edges.
- Pack a minimum of 25 words.
- Fill unused cells with "Rosetta Code" (uppercase), spread somewhat evenly, read left-to-right, top-to-bottom; hidden words stay lowercase.
- Every cell must hold either a word letter or a message letter.
- Print the finished grid and the solution list (word plus start/end coordinates).

## Language Coverage
22 languages implement this task, spanning systems and scripting languages with the random-placement and backtracking logic this requires. Representative implementations include C++, D, Go, Java, Julia, Kotlin, Nim, Perl, Python, Rust, Raku, and Wren.

## Connections
- [[Backtracking]] — common strategy for fitting overlapping words into the grid
- [[ConstraintSatisfaction]] — placement must satisfy overlap, no-zigzag, and message-cell constraints
- [[RandomNumberGeneration]] — typical placements use randomized positions and orientations
- [[StringProcessing]] — filtering the dictionary and matching letters on overlap
- [[GridAlgorithms]] — directional traversal across a 2D lattice

## Contradictions
- None — reference task page.
