---
title: "Flipping bits game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, puzzle, bit-manipulation, game]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Flipping_bits_game
---

## Summary
Implement a scoring program for a puzzle played on an N×N grid of 0s and 1s. A move inverts an entire numbered row or lettered column at once (every 0 becomes 1 and vice versa), and the player tries to transform a starting configuration into a target configuration in as few moves as possible. The key insight is guaranteeing solvability: generate the start position by applying legal flips to a random target, so the moves are reversible and a path back always exists.

## Task Requirements
- Generate a random target configuration and a starting configuration.
- Ensure the starting position is never identical to the target.
- Guarantee the target is reachable from the start (e.g., derive the start by legal row/column flips from the target so flips are reversible).
- Allow a move to invert a whole row or whole column.
- Track and display the number of moves taken so far.
- Show an example short game on the page for a 3×3 grid.

## Language Coverage
53 languages implement this task, spanning systems, scripting, functional, and array languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Julia, and the array-oriented J, APL, and Uiua.

## Connections
- [[BitManipulation]] — flipping bits via inversion is the core operation
- [[XOR]] — toggling a whole row/column is equivalent to XOR-ing it with all-ones
- [[Involution]] — each flip is its own inverse, which guarantees reversibility
- [[PseudorandomNumberGenerator]] — used to build the random target and starting grids
- [[InteractiveGame]] — the program scores a turn-based player session

## Contradictions
- None — reference task page.
