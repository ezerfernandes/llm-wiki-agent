---
title: "Minesweeper game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, recursion, grid]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Minesweeper_game
---

## Summary
The task asks the programmer to implement a playable version of the classic Minesweeper game on an n-by-m grid (specifically 6 by 4) seeded with a random number of hidden mines (10%–20% of tiles). The player marks suspected mines with '?' or clears suspected free space by coordinate; clearing a safe cell reveals either a count of adjacent mines or a blank, and recursively flood-fills outward across all connected mine-free cells. The key insight is the recursive flood-fill reveal of empty regions, mirroring the real game. Input validation may be skipped and a text UI is acceptable.

## Task Requirements
- Build a grid (6 by 4) with a random count of mines between 10% and 20% of total tiles, placed at random positions unknown to the player.
- Display the total mine count at game start.
- Render the grid as a character rectangle between moves: '.' for obscured cells, '?' for marked mines, a space ' ' for free cells with no adjacent mines, and an integer for free cells adjacent to mines.
- Let the player address cells by 1-indexed coordinates (horizontal then vertical), with 1,1 at top-left and n,m at bottom-right.
- Support marking a suspected mine and clearing suspected free space; clearing a free cell recursively clears adjacent free cells.
- Lose if the player clears a hidden mine; win when all mines are correctly identified.
- Input may be assumed well-formed; GUI may be omitted in favor of text I/O.

## Language Coverage
40 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, and Ruby.

## Connections
- [[FloodFill]] — the recursive clearing of connected empty cells
- [[Recursion]] — the reveal step expands outward recursively
- [[GridTraversal]] — addressing cells and scanning the 8-cell neighborhood
- [[RandomNumberGeneration]] — placing mines at random positions
- [[GameOfMinesweeper]] — the game being modeled

## Contradictions
- None — reference task page.
