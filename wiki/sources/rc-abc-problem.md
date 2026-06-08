---
title: "ABC problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, backtracking, matching]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/ABC_problem
---

## Summary
Given a fixed collection of twenty two-letter alphabet blocks (like a child's toy set), write a case-insensitive function that decides whether a given word can be spelled out by laying down blocks, where each block can supply only one of its two letters and each block may be used at most once. The key insight is that this is a bipartite matching problem between the word's letters and the available blocks, though for the small fixed set a simple greedy or recursive backtracking search also suffices.

## Task Requirements
- Represent the supplied set of twenty blocks, each carrying two letters.
- Implement a function `can_make_word(word)` returning a boolean.
- Each block, once used for one of its letters, cannot be reused.
- Matching must be case-insensitive.
- Demonstrate the result for the seven sample words: "A" (true), "BARK" (true), "BOOK" (false), "TREAT" (true), "COMMON" (false), "SQUAD" (true), "CONFUSE" (true).

## Language Coverage
164 languages implement this task, an exceptionally broad spread across functional, imperative, assembly, and esoteric families. Representative examples include Python, C, C++, Java, Haskell, Rust, Go, Prolog, Common Lisp, Perl, and even hand-written 8080 Assembly.

## Connections
- [[BipartiteMatching]] — the formal model: words' letters to blocks
- [[Backtracking]] — common recursive strategy for assigning blocks to letters
- [[GreedyAlgorithm]] — a simpler approach that works for the fixed sample set
- [[StringProcessing]] — letter-by-letter consumption of the input word

## Solved in (Rosetta Code languages)
Solved in **154** of the wiki's catalogued languages (Rosetta Code shows 164 language sections for this task). (10 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[360 Assembly]], [[8080 Assembly]], [[8086 Assembly]], [[8th]], [[AArch64 Assembly]], [[ABAP]], [[ABC]], [[Action!]], [[Acurity Architect]], [[Ada]], [[ALGOL 68]], [[ALGOL W]], [[Apex]], [[APL]], [[AppleScript]], [[ARM Assembly]], [[Arturo]], [[Astro]], [[AutoHotkey]], [[AWK]], [[BaCon]], [[Ballerina]], [[BASIC]], [[BASIC256]], [[Batch File]], [[BBC BASIC]], [[BCPL]], [[BQN]], [[Bracmat]], [[C]], [[C++]], [[Ceylon]], [[Clojure]], [[CLU]], [[COBOL]], [[CoffeeScript]], [[Comal]], [[Common Lisp]], [[Component Pascal]], [[Cowgol]], [[Crystal]], [[D]], [[Delphi]], [[Draco]], [[DuckDB]], [[Dyalect]], [[EasyLang]], [[EchoLisp]], [[Ela]], [[Elena]], [[Elixir]], [[Elm]], [[EMal]], [[Erlang]], [[ERRE]], [[Euphoria]], [[Factor]], [[FBSL]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Gambas]], [[Go]], [[Golfscript]], [[Groovy]], [[Harbour]], [[Haskell]], [[Insitux]], [[J]], [[Java]], [[JavaScript]], [[Jsish]], [[Julia]], [[Koka]], [[Kotlin]], [[Lang]], [[Liberty BASIC]], [[Logo]], [[Logtalk]], [[Lua]], [[M2000 Interpreter]], [[MACRO-11]], [[Maple]], [[MAXScript]], [[Mercury]], [[MiniScript]], [[Miranda]], [[Nim]], [[Oberon-2]], [[Objeck]], [[OCaml]], [[Oforth]], [[OpenEdge-Progress]], [[Order]], [[PARI-GP]], [[Pascal]], [[Perl]], [[Phix]], [[PHP]], [[Picat]], [[PicoLisp]], [[PL-I]], [[PL-M]], [[Pluto]], [[PowerBASIC]], [[PowerShell]], [[Prolog]], [[PureBasic]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[RapidQ]], [[Rebol]], [[Red]], [[Refal]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Run BASIC]], [[Rust]], [[Scala]], [[Scheme]], [[Seed7]], [[SenseTalk]], [[SequenceL]], [[SETL]], [[Sidef]], [[Simula]], [[Smalltalk]], [[SNOBOL4]], [[SPAD]], [[Standard ML]], [[SuperCollider]], [[Swift]], [[Tcl]], [[Transd]], [[TUSCRIPT]], [[TXR]], [[Uiua]], [[Ultimate++]], [[UNIX Shell]], [[UTFool]], [[V (Vlang)]], [[VBA]], [[Wren]], [[XPL0]], [[Yabasic]], [[Zig]], [[ZX Spectrum Basic]]

## Contradictions
- None — reference task page.
