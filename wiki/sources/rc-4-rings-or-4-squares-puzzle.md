---
title: "4-rings or 4-squares puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-satisfaction, brute-force, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/4-rings_or_4-squares_puzzle
---

## Summary
Assign the decimal digits a, b, c, d, e, f, g to four overlapping rings (drawn as squares) so that the four ring sums are all equal: a+b, b+c+d, d+e+f, and f+g must share a common value. The key insight is that the chained/overlapping structure means each interior letter is shared between two rings, which constrains the search; once a, b, and d are chosen the remaining letters are forced, making a small brute-force search sufficient.

## Task Requirements
- Place digits in letters a–g so the sum inside each of the four large squares is identical.
- Show all unique-letter solutions for LOW=1, HIGH=7.
- Show all unique-letter solutions for LOW=3, HIGH=9.
- Show only the count of solutions when letters may repeat, for LOW=0, HIGH=9.
- Print all output.

## Language Coverage
77 languages implement this task, showing broad coverage across systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Prolog, and several assembly variants (AArch64, ARM, X86).

## Connections
- [[ConstraintSatisfaction]] — the equal-sum rings form a small constraint system.
- [[BruteForceSearch]] — most solutions enumerate digit assignments exhaustively.
- [[Permutations]] — unique-letter variants are essentially permutations of a digit subset.
- [[Backtracking]] — pruning shared interior letters early reduces the search space.

## Solved in (Rosetta Code languages)
Solved in **72** of the wiki's catalogued languages (Rosetta Code shows 77 language sections for this task). (5 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Action!]], [[Ada]], [[ALGOL 68]], [[ALGOL W]], [[AppleScript]], [[Applesoft BASIC]], [[ARM Assembly]], [[AutoHotkey]], [[AWK]], [[BASIC256]], [[Befunge]], [[C]], [[C++]], [[Chipmunk Basic]], [[Clojure]], [[Common Lisp]], [[Crystal]], [[D]], [[Delphi]], [[EasyLang]], [[Factor]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Groovy]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Koka]], [[Kotlin]], [[Lua]], [[MiniScript]], [[Modula-2]], [[Nim]], [[OCaml]], [[PARI-GP]], [[Pascal]], [[Perl]], [[Phix]], [[Picat]], [[PL-M]], [[PL-SQL]], [[Prolog]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[REXX]], [[Ruby]], [[Rust]], [[Scala]], [[Scheme]], [[Sidef]], [[Simula]], [[SQL PL]], [[Stata]], [[Tcl]], [[Uiua]], [[V (Vlang)]], [[VBA]], [[Visual Basic .NET]], [[Wren]], [[X86 Assembly]], [[XPL0]], [[Yabasic]], [[Zig]]

## Contradictions
- None — reference task page.
