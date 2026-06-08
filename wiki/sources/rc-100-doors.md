---
title: "100 doors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, simulation, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/100_doors
---

## Summary
A row of 100 doors starts fully closed. Over 100 passes, pass *n* toggles every *n*-th door (open if closed, close if open), so pass 1 touches all doors, pass 2 every other door, and so on. The task is to report each door's final state. The key insight is that a door is toggled once per divisor of its number, and only perfect squares have an odd number of divisors — so the doors left open are exactly the perfect-square-numbered ones (1, 4, 9, 16, …, 100).

## Task Requirements
- Model 100 doors, all initially closed.
- Perform 100 passes; on pass *n*, visit and toggle every *n*-th door (doors *n*, 2n, 3n, …).
- After the final pass, report which doors are open and which are closed.
- Alternate / extra-credit: directly open only the perfect-square doors as an optimization (noted to defeat the cross-language comparison intent, so usually shown alongside the naive simulation).

## Language Coverage
378 languages implement this task. Coverage spans the full spectrum — from low-level assembly (6502, 8080, x86, ARM, MMIX) through mainstream procedural and OO languages, functional languages, query/markup languages, and esoteric entries. Representative examples: C, Python, Java, Haskell, Rust, Go, COBOL, APL, Scheme, SQL, Forth, and Befunge.

## Connections
- [[PerfectSquares]] — only perfect-square-numbered doors stay open, the mathematical heart of the task.
- [[DivisorCounting]] — a door's toggle count equals its divisor count; odd divisor counts (squares) leave it open.
- [[NumberTheory]] — the result follows from properties of divisors and integer factorization.
- [[Simulation]] — the naive solution simulates each pass over the array of doors.
- [[AlgorithmicOptimization]] — the O(√n) direct perfect-square approach versus the O(n²) brute-force simulation.

## Solved in (Rosetta Code languages)
Solved in **356** of the wiki's catalogued languages (Rosetta Code shows 379 language sections for this task). (23 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[360 Assembly]], [[4DOS Batch]], [[6502 Assembly]], [[68000 Assembly]], [[8080 Assembly]], [[8086 Assembly]], [[8th]], [[AArch64 Assembly]], [[ABAP]], [[ABC]], [[ACL2]], [[Action!]], [[ActionScript]], [[Acurity Architect]], [[Ada]], [[Adina]], [[Agena]], [[Aikido]], [[ALGOL 60]], [[ALGOL 68]], [[ALGOL W]], [[ALGOL-M]], [[AmigaE]], [[APL]], [[AppleScript]], [[Arbre]], [[Argile]], [[ArkScript]], [[ARM Assembly]], [[Arturo]], [[Astro]], [[Asymptote]], [[ATS]], [[AutoHotkey]], [[AutoIt]], [[AutoLISP]], [[AWK]], [[Axiom]], [[B]], [[BabyCobol]], [[BaCon]], [[Bait]], [[Ballerina]], [[BASIC]], [[Batch File]], [[BBC BASIC]], [[BCPL]], [[Befunge]], [[Binary Lambda Calculus]], [[Blade]], [[BlitzMax]], [[BlooP]], [[BQN]], [[Bracmat]], [[Burlesque]], [[C]], [[C++]], [[C1R]], [[Caché ObjectScript]], [[Ceylon]], [[Clarion]], [[Clio]], [[CLIPS]], [[Clojure]], [[CLU]], [[COBOL]], [[Coco]], [[CoffeeScript]], [[ColdFusion]], [[Comal]], [[Commodore BASIC]], [[Common Lisp]], [[Component Pascal]], [[Cowgol]], [[Craft Basic]], [[Crystal]], [[D]], [[Dafny]], [[Dart]], [[Dc]], [[DCL]], [[Delphi]], [[Draco]], [[DuckDB]], [[DUP]], [[DWScript]], [[Dyalect]], [[Dylan]], [[Déjà Vu]], [[E]], [[EasyLang]], [[EchoLisp]], [[ECL]], [[Ecstasy]], [[EDSAC order code]], [[Eero]], [[Egel]], [[EGL]], [[Eiffel]], [[Ela]], [[Elena]], [[Elixir]], [[Elm]], [[Emacs Lisp]], [[EMal]], [[Erlang]], [[ERRE]], [[Euler]], [[Euphoria]], [[Excel]], [[Factor]], [[Falcon]], [[FALSE]], [[Fantom]], [[FBSL]], [[Fe]], [[Fennel]], [[Fhidwfe]], [[Fish]], [[FOCAL]], [[Forth]], [[Fortran]], [[Free Pascal]], [[FreeBASIC]], [[Frink]], [[FTCBASIC]], [[FunL]], [[Futhark]], [[FutureBasic]], [[FUZE BASIC]], [[Fōrmulæ]], [[Gambas]], [[GAP]], [[GDScript]], [[Genie]], [[Glee]], [[GML]], [[Go]], [[Goboscript]], [[Golfscript]], [[Gosu]], [[Groovy]], [[GW-BASIC]], [[Harbour]], [[Haskell]], [[Haxe]], [[HicEst]], [[HolyC]], [[Hoon]], [[Huginn]], [[Hy]], [[I]], [[Idris]], [[Inform 7]], [[Informix 4GL]], [[Insitux]], [[Io]], [[Ioke]], [[Isabelle]], [[J]], [[Janet]], [[Java]], [[JavaScript]], [[Julia]], [[K]], [[Klingphix]], [[Klong]], [[Koka]], [[KonsolScript]], [[Kotlin]], [[KQL]], [[LabVIEW]], [[Lambdatalk]], [[Lang]], [[Lasso]], [[Latitude]], [[Lhogho]], [[Liberty BASIC]], [[Lily]], [[LiveCode]], [[Logo]], [[LOLCODE]], [[Lua]], [[M2000 Interpreter]], [[M4]], [[MACRO-11]], [[MAD]], [[Maple]], [[Maxima]], [[MAXScript]], [[Mercury]], [[Metafont]], [[Microsoft Small Basic]], [[MiniScript]], [[MIPS Assembly]], [[Mirah]], [[Miranda]], [[ML-I]], [[MMIX]], [[Modula-2]], [[Modula-3]], [[MontiLang]], [[MOO]], [[MoonScript]], [[MUMPS]], [[Myrddin]], [[MySQL]], [[Nanoquery]], [[NetRexx]], [[Nial]], [[Nim]], [[Oberon-07]], [[Objeck]], [[Objective-C]], [[OCaml]], [[Octave]], [[Odin]], [[Oforth]], [[Ol]], [[OmniMark]], [[Onyx]], [[OpenEdge-Progress]], [[OPL]], [[OxygenBasic]], [[Oz]], [[PARI-GP]], [[Pascal]], [[PascalABC.NET]], [[Pebble]], [[Perl]], [[Perl5i]], [[Phix]], [[Phixmonti]], [[PHL]], [[PHP]], [[Picat]], [[PicoLisp]], [[Piet]], [[Pike]], [[PL-I]], [[PL-M]], [[PL-SQL]], [[Plain English]], [[Pluto]], [[Pointless]], [[Polyglot:PL-I and PL-M]], [[Pony]], [[Pop11]], [[PostScript]], [[Potion]], [[PowerShell]], [[Processing]], [[ProDOS]], [[Prolog]], [[PROMAL]], [[Pure]], [[Pure Data]], [[PureBasic]], [[Pyret]], [[Python]], [[Q]], [[QB64]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[RapidQ]], [[Rebol]], [[Red]], [[Refal]], [[Relation]], [[Retro]], [[REXX]], [[Ring]], [[Rocq]], [[RPL]], [[Ruby]], [[Run BASIC]], [[Rust]], [[S-BASIC]], [[S-lang]], [[Salmon]], [[SAS]], [[Sather]], [[Scala]], [[Scheme]], [[Scilab]], [[Scratch]], [[Seed7]], [[SenseTalk]], [[SequenceL]], [[SETL]], [[SheerPower 4GL]], [[Sidef]], [[Simula]], [[Slate]], [[Smalltalk]], [[SNOBOL4]], [[SparForte]], [[Sparkling]], [[Spin]], [[SQL]], [[SQL PL]], [[Standard ML]], [[Stata]], [[Stax]], [[Stringle]], [[SuperCollider]], [[Swift]], [[Tailspin]], [[Tcl]], [[TI-83 BASIC]], [[TI-89 BASIC]], [[TorqueScript]], [[Transact-SQL]], [[Transd]], [[True BASIC]], [[TSE SAL]], [[TUSCRIPT]], [[TXR]], [[TypeScript]], [[Uiua]], [[Uniface]], [[Unison]], [[UNIX Shell]], [[Ursa]], [[Ursala]], [[UTFool]], [[V (Vlang)]], [[Vala]], [[VAX Assembly]], [[VBA]], [[VBScript]], [[Vedit macro language]], [[Verilog]], [[VHDL]], [[Visual Basic]], [[Visual Basic .NET]], [[VTL-2]], [[Wart]], [[WDTE]], [[Wortel]], [[Wrapl]], [[Wren]], [[X86 Assembly]], [[XBasic]], [[Xojo]], [[XPL0]], [[XSLT 1.0]], [[XSLT 2.0]], [[Yabasic]], [[YAMLScript]], [[Yorick]], [[Zig]], [[ZX Spectrum Basic]]

## Contradictions
- None — reference task page.
