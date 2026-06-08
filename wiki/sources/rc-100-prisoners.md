---
title: "100 prisoners (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, monte-carlo, probability, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/100_prisoners
---

## Summary
The task models the classic "100 prisoners" puzzle: 100 prisoners each numbered 1–100 must find their own number among 100 drawers holding randomly shuffled cards, opening at most 50 drawers each; all are pardoned only if every prisoner succeeds. The key insight is that the optimal "cycle-following" strategy — starting at the drawer matching one's own number and chasing the card it reveals — raises the group success probability from a vanishingly small ~0.0000000000000000000000000000003 (random) to roughly 31%, because it ties failure to the existence of a permutation cycle longer than 50.

## Task Requirements
- Simulate several thousand games where each prisoner opens drawers at random.
- Simulate several thousand games using the optimal cycle-following strategy: open the drawer matching your own number, then follow each revealed card number to the next drawer, up to 50 openings.
- All 100 prisoners must individually find their own number for the group to win.
- Compute and compare the success probability of both strategies on the page.

## Language Coverage
97 languages; coverage spans the usual systems and scripting tiers plus a notably deep BASIC/assembly long tail, reflecting how cheap a Monte Carlo simulation is to express. Representative examples: Python, C, C++, Rust, Go, Haskell, Java, JavaScript, Julia, Raku, and several BASIC dialects (FreeBASIC, QB64, Yabasic) and assembly targets (ARM, AArch64).

## Connections
- [[MonteCarloSimulation]] — both strategies are estimated by repeated random trials.
- [[Permutations]] — the drawer arrangement is a random permutation; success hinges on its cycle structure.
- [[ProbabilityTheory]] — the optimal strategy's ~31% bound derives from harmonic-number analysis of cycle lengths.
- [[RandomNumberGeneration]] — each trial requires shuffling cards uniformly at random.

## Solved in (Rosetta Code languages)
Solved in **89** of the wiki's catalogued languages (Rosetta Code shows 97 language sections for this task). (8 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[ABC]], [[Ada]], [[ALGOL 68]], [[APL]], [[Applesoft BASIC]], [[ARM Assembly]], [[Arturo]], [[AutoHotkey]], [[BASIC]], [[BCPL]], [[C]], [[C++]], [[CLIPS]], [[Clojure]], [[CLU]], [[Commodore BASIC]], [[Common Lisp]], [[Cowgol]], [[Crystal]], [[D]], [[Dart]], [[Delphi]], [[EasyLang]], [[Ecstasy]], [[Elixir]], [[Factor]], [[FOCAL]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Gambas]], [[GDScript]], [[Go]], [[Groovy]], [[Haskell]], [[J]], [[Janet]], [[Java]], [[JavaScript]], [[Julia]], [[Koka]], [[Kotlin]], [[Lua]], [[Maple]], [[MATLAB]], [[MiniScript]], [[Nim]], [[Pascal]], [[Perl]], [[Phix]], [[Phixmonti]], [[PicoLisp]], [[PL-M]], [[Pluto]], [[Pointless]], [[PowerShell]], [[Processing]], [[Prolog]], [[PureBasic]], [[Python]], [[QB64]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ruby]], [[Rust]], [[Sather]], [[Scala]], [[SETL]], [[SuperCollider]], [[Swift]], [[Tcl]], [[Transact-SQL]], [[Transd]], [[V (Vlang)]], [[VBScript]], [[Visual Basic .NET]], [[Wren]], [[XPL0]], [[Yabasic]], [[YAMLScript]], [[Zig]]

## Contradictions
- None — reference task page.
