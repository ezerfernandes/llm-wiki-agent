---
title: "Conway's Game of Life (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Conway's_Game_of_Life
---

## Summary
Implement Conway's Game of Life, the best-known cellular automaton, devised by mathematician John Horton Conway in 1970. The universe is a square grid where each cell is alive or dead, and each generation is computed simultaneously from the previous one: a cell's fate depends only on the count N of live cells in its eight-cell Moore neighbourhood. The key insight is that this zero-player game produces complex emergent behaviour (oscillators, gliders) from four simple birth/survival/death rules applied in lockstep.

## Task Requirements
- Represent cells as 1 (alive) or 0 (dead) in an m-by-m square grid.
- For each cell C, compute N = sum of live cells in its eight-location Moore neighbourhood.
- Apply the transition rules: a live cell survives only with N = 2 or 3 (dies of loneliness at 0-1, of overcrowding at 4+); a dead cell becomes alive only with exactly N = 3.
- Treat cells beyond the grid boundary as always dead.
- Demonstrate the blinker pattern (three adjoining live cells in a row) evolving over three generations in a 3x3 grid; ideally also test richer cases like the glider in a larger universe.

## Language Coverage
134 languages implement this task, spanning low-level assembly (6502, 68000, AArch64, ARM, Z80), systems languages (C, C++, Rust, Zig, Go), functional languages (Haskell, OCaml, Scheme, Clojure, F#), array languages (APL, J, BQN, Uiua), and scripting/general-purpose languages (Python, Ruby, JavaScript, Perl, Lua). Even esoteric languages like Brainf*** and INTERCAL appear, reflecting the task's popularity as a programming exercise.

## Connections
- [[CellularAutomaton]] — Game of Life is the canonical example of this discrete computational model.
- [[MooreNeighborhood]] — the eight surrounding cells used to compute each cell's neighbour count.
- [[JohnHortonConway]] — the mathematician who devised the game in 1970.
- [[EmergentBehavior]] — complex patterns (oscillators, gliders) arise from simple local rules.
- [[LangtonsAnt]] — a related, well-known cellular automaton task.

## Contradictions
- None — reference task page.
