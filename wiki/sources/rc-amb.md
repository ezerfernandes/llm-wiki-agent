---
title: "Amb (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, nondeterminism, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Amb
---

## Summary
The task asks the programmer to define and demonstrate the Amb ("ambiguous") operator, which expresses nondeterminism rather than randomness. Conceptually, `Amb(x, y, z)` splits a computation into multiple possible futures and selects the one whose value lets a later constraint succeed, discarding the failing branches. The key insight is that the search is implicit: invocations of Amb look independent and are not visibly wrapped in loops, so the language (or a facsimile built with backtracking/continuations) handles the branch exploration automatically.

## Task Requirements
- Implement the Amb operator (or a close equivalent), where calling it with no arguments denotes failure.
- Amb takes a variable number of values/expressions and yields one that satisfies a future constraint, avoiding failure.
- Demonstrate it by choosing one word from each of four sets to form a four-word sentence: {the, that, a}, {frog, elephant, thing}, {walked, treaded, grows}, {slowly, quickly}.
- Enforce the constraint that the last character of each word (except the last) equals the first character of its successor.
- Produce the unique solution "that thing grows slowly" without using trivial explicit nested iteration as the visible control flow.

## Language Coverage
80 languages implement this task, spanning functional, logic, imperative, and scripting families since nondeterministic choice can be modeled many ways. Representative implementations include Haskell, Scheme, Common Lisp, Prolog, Python, Ruby, OCaml, Racket, Oz, and J.

## Connections
- [[Nondeterminism]] — the core semantics Amb expresses
- [[Backtracking]] — common way to implement the branch search
- [[Continuations]] — used in Scheme/Lisp implementations to capture and resume alternative futures
- [[ConstraintSatisfaction]] — the four-word sentence puzzle is a constraint problem
- [[LogicProgramming]] — Prolog-style search subsumes the Amb behavior natively

## Solved in (Rosetta Code languages)
Solved in **72** of the wiki's catalogued languages (Rosetta Code shows 80 language sections for this task). (8 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[Ada]], [[ALGOL 68]], [[ATS]], [[AutoHotkey]], [[Ballerina]], [[BASIC]], [[Bracmat]], [[C]], [[C++]], [[Clojure]], [[Common Lisp]], [[Crystal]], [[D]], [[E]], [[EasyLang]], [[Egison]], [[Ela]], [[Elena]], [[ERRE]], [[Factor]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[Haxe]], [[Insitux]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Latitude]], [[Lua]], [[M2000 Interpreter]], [[Mercury]], [[NetRexx]], [[Nim]], [[OCaml]], [[OpenEdge-Progress]], [[Oz]], [[PARI-GP]], [[Perl]], [[Phix]], [[Picat]], [[PicoLisp]], [[PL-I]], [[Pluto]], [[Prolog]], [[PureBasic]], [[Python]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ring]], [[Ruby]], [[Rust]], [[Scala]], [[Scheme]], [[Seed7]], [[SETL]], [[Smalltalk]], [[Tcl]], [[TUSCRIPT]], [[TXR]], [[V (Vlang)]], [[VBScript]], [[Wren]], [[Yabasic]]

## Contradictions
- None — reference task page.
