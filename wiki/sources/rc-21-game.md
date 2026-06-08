---
title: "21 game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game-theory, combinatorial-game]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/21_game
---

## Summary
The 21 game is a two-player game (one player being the computer) in which players take turns adding 1, 2, or 3 to a shared running total that starts at zero; the player whose addition brings the total to exactly 21 wins. It is a variant of Nim. The key insight is that it is a solved combinatorial game: a player who leaves the total at a multiple of 4 (e.g. 4, 8, 12, 16, 20) can force a win, so optimal play follows a simple modular strategy.

## Task Requirements
- Prompt the player for input (or provide a button menu).
- Validate input and display appropriate error messages.
- Add the chosen number (1, 2, or 3) to the running total.
- Display the running total after each move.
- Provide a way for the player to quit/exit/halt/stop the program.
- Announce when there is a winner.
- Determine who moves first (random, user choice, or specified at game start).

## Language Coverage
60 languages implement this task, spanning low-level assembly, classic BASIC dialects, functional languages, and mainstream scripting languages. Representative examples include C, C++, Rust, Go, Python, Java, JavaScript, Haskell, Ruby, and AArch64 Assembly.

## Connections
- [[Nim]] — the 21 game is a direct variant of this classic subtraction game.
- [[CombinatorialGameTheory]] — the game is solvable with a winning strategy for one side.
- [[ModularArithmetic]] — optimal play keeps the running total at multiples of four.
- [[GameTree]] — the move space can be searched to determine forced wins.

## Solved in (Rosetta Code languages)
Solved in **55** of the wiki's catalogued languages (Rosetta Code shows 60 language sections for this task). (5 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[AppleScript]], [[Applesoft BASIC]], [[ARM Assembly]], [[Arturo]], [[AutoHotkey]], [[AWK]], [[BASIC]], [[C]], [[C++]], [[Commodore BASIC]], [[Delphi]], [[EasyLang]], [[Factor]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Gambas]], [[GDScript]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Koka]], [[Lua]], [[Nim]], [[Objeck]], [[Pascal]], [[Perl]], [[Phix]], [[PHP]], [[Picat]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Rust]], [[Scala]], [[Uiua]], [[V (Vlang)]], [[Visual Basic .NET]], [[Wren]], [[YAMLScript]]

## Contradictions
- None — reference task page.
