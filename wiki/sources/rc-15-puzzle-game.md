---
title: "15 puzzle game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sliding-puzzle, game]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/15_puzzle_game
---

## Summary
This Rosetta Code task asks for an implementation of the classic Fifteen Puzzle — a 4x4 sliding-tile grid holding tiles numbered 1–15 plus one empty space, where the player slides adjacent tiles into the gap to restore numerical order. The core insight is modeling a shuffled-but-solvable board and processing player moves that swap a tile with the neighboring blank cell. The puzzle is also known as the Gem Puzzle, Boss Puzzle, Game of Fifteen, and Mystic Square.

## Task Requirements
- Implement an interactive 4x4 fifteen-puzzle game (15 numbered tiles plus one blank cell).
- Generate a shuffled starting board (ideally guaranteed solvable, not just randomly permuted).
- Accept player moves that slide a tile adjacent to the blank into the empty space.
- Detect and report the solved/win state (tiles in order 1–15 with the blank at the end).

## Language Coverage
91 languages, spanning low-level assembly (68000, AArch64, ARM, x86-64), systems languages (C, C++, Rust, Zig, Go, Nim), array/functional languages (APL, BQN, J, Haskell, OCaml, Scheme, F#), many BASIC dialects (FreeBASIC, QB64, BBC BASIC, Yabasic), and scripting/mainstream languages. Representative examples: Python, Java, JavaScript, C++, Rust, Go, Haskell, Lua, Ruby, and Perl.

## Connections
- [[SlidingPuzzle]] — the general class of tile-shifting puzzles this task instantiates
- [[BoardGameRepresentation]] — modeling a 4x4 grid and blank-cell state
- [[PermutationParity]] — solvability depends on the parity of the tile permutation plus blank-row position
- [[StateSpaceSearch]] — connects to the related 15 Puzzle Solver task (A* / IDA* search)

## Solved in (Rosetta Code languages)
Solved in **85** of the wiki's catalogued languages (Rosetta Code shows 91 language sections for this task). (6 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[68000 Assembly]], [[AArch64 Assembly]], [[Action!]], [[Ada]], [[Amazing Hopper]], [[APL]], [[ARM Assembly]], [[Arturo]], [[Astro]], [[AutoHotkey]], [[BASIC]], [[BBC BASIC]], [[BQN]], [[C]], [[C++]], [[COBOL]], [[Common Lisp]], [[Craft Basic]], [[Delphi]], [[EasyLang]], [[Factor]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FuncSug]], [[FutureBasic]], [[Gambas]], [[Go]], [[Harbour]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Koka]], [[Kotlin]], [[Liberty BASIC]], [[LiveCode]], [[Lua]], [[M2000 Interpreter]], [[Mercury]], [[MiniScript]], [[MUMPS]], [[Nim]], [[OCaml]], [[Pascal]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[PHP]], [[Picat]], [[Processing]], [[Prolog]], [[PureBasic]], [[Python]], [[QB64]], [[QBasic]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ring]], [[Ruby]], [[Run BASIC]], [[Rust]], [[Scala]], [[Scheme]], [[Scilab]], [[Simula]], [[Standard ML]], [[Tcl]], [[UNIX Shell]], [[VBA]], [[VBScript]], [[Visual Basic .NET]], [[Visual Prolog]], [[Wren]], [[XBasic]], [[XPL0]], [[Yabasic]], [[Zig]]

## Contradictions
- None — reference task page.
