---
title: "Abelian sandpile model (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abelian_sandpile_model
---

## Summary
This task asks the programmer to implement the Abelian sandpile model (also called the Bak–Tang–Wiesenfeld model), a cellular automaton on a 2D grid. Each cell holds a count of "sand particles"; whenever a cell reaches 4 or more, it topples, subtracting 4 from itself and adding 1 particle to each of its four orthogonal neighbors. Toppling repeats until every cell holds fewer than 4 particles, and the key insight is that the final stable configuration is independent of the order in which unstable cells are processed (the "Abelian" property).

## Task Requirements
- Create a 2D grid of arbitrary size on which piles of sand can be placed.
- Implement the toppling rule: any pile with 4 or more particles collapses, losing 4 particles which are distributed one each to its neighbors.
- Iterate until the grid stabilizes (no cell has 4 or more particles).
- Preferably render the result as an image (e.g., a PPM bitmap) rather than terminal text, since interesting configurations grow large.

## Language Coverage
48 languages implement this task, spanning systems languages, functional languages, array languages, and assembly. Representative implementations include C, C++, Rust, Go, Zig, Python, Haskell, Julia, J, APL, BQN, and ARM/AArch64 Assembly.

## Connections
- [[CellularAutomata]] — the sandpile is a discrete dynamical system evolving on a grid by local rules.
- [[SelfOrganizedCriticality]] — the model is the canonical example introduced by Bak, Tang, and Wiesenfeld.
- [[GridSimulation]] — relies on iterating a 2D array until a stable fixed point is reached.
- [[BitmapImageOutput]] — results are typically visualized by writing a PPM/PNG image.

## Solved in (Rosetta Code languages)
Solved in **45** of the wiki's catalogued languages (Rosetta Code shows 48 language sections for this task). (3 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[APL]], [[ARM Assembly]], [[AutoHotkey]], [[BQN]], [[C]], [[C++]], [[Crystal]], [[Delphi]], [[EasyLang]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Fōrmulæ]], [[Go]], [[Haskell]], [[J]], [[Java]], [[Julia]], [[Locomotive Basic]], [[Lua]], [[MiniScript]], [[Nim]], [[OCaml]], [[Pascal]], [[Perl]], [[Phix]], [[PicoLisp]], [[Pluto]], [[Python]], [[R]], [[Raku]], [[RPL]], [[Rust]], [[Scheme]], [[Uiua]], [[V (Vlang)]], [[VBA]], [[Wren]], [[XPL0]], [[Zig]]

## Contradictions
- None — reference task page.
