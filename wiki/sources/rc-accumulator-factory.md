---
title: "Accumulator factory (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, closures, higher-order-functions, mutable-state]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Accumulator_factory
---

## Summary
Posed by Paul Graham, this task asks for a factory function that takes a number `n` and returns a new accumulator function. Each returned accumulator takes a number `i` and returns the running sum of every value passed to it (including the initial `n`). The natural solution is a closure that captures a private piece of mutable state, which is why purely functional languages cannot satisfy the task without escaping their purity.

## Task Requirements
- Factory takes a number `n` and returns a function `g` that takes `i` and returns `n` plus the accumulation of all `i` values seen across every call to `g`.
- Must support numeric polymorphism: handle both ints and floats, and an accumulator that has only seen integers should still return integers (no blanket conversion to float).
- The accumulated value must persist across calls (a stored, mutable piece of state), not reset to the most recent input.
- The returned object must be a real, first-class function usable anywhere a normally-defined function could be used.
- State must be private — no global variables or anything that lets other code inadvertently modify it. Multiple accumulators must be independent.

## Language Coverage
122 languages implement this task, spanning functional, object-oriented, scripting, and assembly families — broad coverage that highlights how each language exposes (or works around) closures and mutable capture. Representative examples include Python, JavaScript, Haskell, Common Lisp, Scheme, Clojure, C, Java, Rust, Go, OCaml, and Smalltalk.

## Connections
- [[Closures]] — the canonical mechanism for capturing private accumulator state
- [[HigherOrderFunctions]] — a function that returns another function
- [[MutableState]] — required to retain the running sum between calls
- [[Polymorphism]] — handling both integer and floating-point inputs without forced coercion
- [[LexicalScope]] — how the inner function retains access to the enclosing variable

## Solved in (Rosetta Code languages)
Solved in **113** of the wiki's catalogued languages (Rosetta Code shows 122 language sections for this task). (9 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[8th]], [[ABAP]], [[ActionScript]], [[Ada]], [[Aikido]], [[Aime]], [[ALGOL 68]], [[AppleScript]], [[Argile]], [[Astro]], [[Ballerina]], [[BBC BASIC]], [[BQN]], [[Bracmat]], [[Brat]], [[C]], [[C++]], [[Ceylon]], [[Clay]], [[Clojure]], [[CoffeeScript]], [[Common Lisp]], [[Crystal]], [[D]], [[Dart]], [[Delphi]], [[Déjà Vu]], [[E]], [[EchoLisp]], [[Elena]], [[Elixir]], [[EMal]], [[Erlang]], [[ERRE]], [[Factor]], [[Fantom]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[Go]], [[Golo]], [[Groovy]], [[Haskell]], [[Io]], [[J]], [[Java]], [[JavaScript]], [[Jsish]], [[Julia]], [[Kotlin]], [[Lambdatalk]], [[Lang]], [[LFE]], [[Lua]], [[M2000 Interpreter]], [[Maple]], [[Mercury]], [[MiniScript]], [[Nemerle]], [[NGS]], [[Nim]], [[Nit]], [[Objeck]], [[Objective-C]], [[OCaml]], [[Octave]], [[Oforth]], [[OxygenBasic]], [[Oz]], [[PARI-GP]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[PHP]], [[PicoLisp]], [[Pluto]], [[Pony]], [[PostScript]], [[PowerShell]], [[Prolog]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[Retro]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Rust]], [[Scala]], [[Scheme]], [[Sidef]], [[Simula]], [[Smalltalk]], [[Standard ML]], [[Swift]], [[Tcl]], [[TXR]], [[Unicon]], [[UNIX Shell]], [[Ursalang]], [[V (Vlang)]], [[VBScript]], [[Wart]], [[Wren]], [[XLISP]], [[Yabasic]], [[Yorick]]

## Contradictions
- None — reference task page.
