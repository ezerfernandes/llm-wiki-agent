---
title: "24 game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, expression-parsing, arithmetic, games]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/24_game
---

## Summary
The task implements the 24 Game, a mental-arithmetic puzzle. The program randomly selects four single digits (each 1–9, repetitions allowed) and prompts the player to enter an arithmetic expression that uses all four digits exactly once and evaluates to 24. The program must parse and evaluate the player's input rather than generate the solution, so the core engineering challenge is building a constrained expression evaluator and validating that the digits used match the ones offered.

## Task Requirements
- Randomly choose and display four digits, each from 1 to 9 inclusive, with repetitions allowed.
- Prompt the player for an arithmetic expression using only those four digits, each used exactly once.
- Only the operators multiplication, division, addition, and subtraction are allowed.
- Division must use floating-point or rational arithmetic to preserve remainders.
- Brackets are allowed when using an infix evaluator; an RPN evaluator is equally acceptable.
- Forming multi-digit numbers from the supplied digits is disallowed (e.g. 12+12 from 1,2,2,1 is invalid).
- The order of the displayed digits need not be preserved.
- The program must check and evaluate the expression; it does not need to generate it or test solvability.

## Language Coverage
117 languages implement this task, reflecting wide breadth across systems, scripting, functional, and even assembly languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Scheme, Common Lisp, Perl, and ARM Assembly.

## Connections
- [[ExpressionParsing]] — the program must parse the player's arithmetic input.
- [[RecursiveDescentParser]] — a common technique for evaluating infix arithmetic expressions.
- [[ReversePolishNotation]] — an explicitly sanctioned alternative evaluation strategy.
- [[OperatorPrecedence]] — multiplication/division must bind tighter than addition/subtraction.
- [[RationalArithmetic]] — needed (alongside floating point) to preserve division remainders.

## Solved in (Rosetta Code languages)
Solved in **107** of the wiki's catalogued languages (Rosetta Code shows 117 language sections for this task). (10 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[8th]], [[AArch64 Assembly]], [[ABAP]], [[Ada]], [[ALGOL 68]], [[APL]], [[Applesoft BASIC]], [[Argile]], [[ARM Assembly]], [[Arturo]], [[AutoHotkey]], [[AutoIt]], [[BBC BASIC]], [[Befunge]], [[Bracmat]], [[C]], [[C++]], [[Ceylon]], [[Clojure]], [[COBOL]], [[CoffeeScript]], [[Commodore BASIC]], [[Common Lisp]], [[D]], [[Delphi]], [[EasyLang]], [[EchoLisp]], [[Elena]], [[Elixir]], [[Erlang]], [[Factor]], [[Falcon]], [[Fortran]], [[FreeBASIC]], [[Frink]], [[FutureBasic]], [[GAP]], [[Go]], [[Gosu]], [[Groovy]], [[Haskell]], [[HicEst]], [[Huginn]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Koka]], [[Kotlin]], [[Lasso]], [[Liberty BASIC]], [[LiveCode]], [[Locomotive Basic]], [[Logo]], [[Lua]], [[Maple]], [[MiniScript]], [[Modula-2]], [[MUMPS]], [[Nanoquery]], [[Nim]], [[Nit]], [[Objeck]], [[OCaml]], [[Oforth]], [[OpenEdge-Progress]], [[PARI-GP]], [[Perl]], [[Phix]], [[PHP]], [[Picat]], [[PicoLisp]], [[PL-I]], [[Potion]], [[PowerShell]], [[ProDOS]], [[Prolog]], [[PureBasic]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Rust]], [[Scala]], [[Scheme]], [[Sidef]], [[Simula]], [[Swift]], [[Tcl]], [[TorqueScript]], [[TUSCRIPT]], [[UNIX Shell]], [[V (Vlang)]], [[VBA]], [[Wren]], [[XPL0]], [[Yabasic]], [[Zig]], [[ZX Spectrum Basic]]

## Contradictions
- None — reference task page.
