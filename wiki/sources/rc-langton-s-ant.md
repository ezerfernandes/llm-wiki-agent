---
title: "Langton's ant (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Langton's_ant
---

## Summary
Langton's ant is a two-dimensional cellular automaton where an ant traverses a grid of black and white cells, flipping each cell's color and turning based on the color it lands on. Despite the trivially simple ruleset, the ant's path is chaotic for roughly the first 10,000 steps before settling into a periodic "highway" that drifts diagonally away forever. The key insight is the emergence of complex, eventually-ordered behavior from a minimal deterministic rule.

## Task Requirements
- Initialize a 100x100 grid of cells, all white, with the ant placed near the center facing one of four directions.
- Apply the movement rules each step: if on a black cell, set it white and turn left; if on a white cell, set it black and turn right; then move forward one cell.
- Repeat until the ant exits the grid region.
- Display the final pattern of cell colors left behind.

## Language Coverage
94 languages implement this task, reflecting broad appeal as a classic grid-simulation exercise across paradigms. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Lua, Common Lisp, and APL.

## Connections
- [[CellularAutomaton]] — Langton's ant is a canonical example of a Turing-complete cellular automaton.
- [[EmergentBehavior]] — chaotic dynamics resolving into an ordered periodic highway.
- [[TuringCompleteness]] — the system is provably capable of universal computation.
- [[GridSimulation]] — state evolution over a discrete 2D lattice.
- [[ConwaysGameOfLife]] — a related two-dimensional cellular automaton.

## Contradictions
- None — reference task page.
