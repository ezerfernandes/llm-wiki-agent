---
title: "ABC correlation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/ABC_correlation
---

## Summary
Read a string and count how many times the letters "a", "b", and "c" appear in it, ignoring every other character. Return true when all three counts are exactly equal, and false otherwise. The key insight is that the task reduces to tallying three character frequencies and testing them for mutual equality.

## Task Requirements
- Take a string as input and store it in a variable.
- Count the occurrences of the letters "a", "b", and "c" within that string.
- Ignore all other characters when counting.
- Return true if the counts of "a", "b", and "c" are all exactly equal; otherwise return false.

## Language Coverage
58 languages implement this task, spanning mainstream languages, scripting languages, array/concatenative languages, and esoteric ones. Representative examples include Python, C, C++, Java, Go, Rust, Ruby, Perl, JavaScript, BQN, and Brainf***.

## Connections
- [[StringProcessing]] — the task is fundamentally about scanning and analyzing a character string.
- [[FrequencyCounting]] — counting per-character occurrences is the core operation.
- [[CharacterFiltering]] — non-target characters must be excluded from the tally.

## Solved in (Rosetta Code languages)
Solved in **53** of the wiki's catalogued languages (Rosetta Code shows 58 language sections for this task). (5 further RC language section(s) are outside the wiki's popularity-list language set.)

[[ABC]], [[Ada]], [[ALGOL 68]], [[AppleScript]], [[ArkScript]], [[AWK]], [[Ballerina]], [[BASIC]], [[BQN]], [[Brainf***]], [[C]], [[C++]], [[Common Lisp]], [[Crystal]], [[DuckDB]], [[EasyLang]], [[Factor]], [[Forth]], [[Fortran]], [[FutureBasic]], [[Go]], [[Java]], [[JavaScript]], [[Julia]], [[K]], [[LOLCODE]], [[Lua]], [[M2000 Interpreter]], [[Maxima]], [[MiniScript]], [[Nim]], [[Nu]], [[Oberon-07]], [[Objeck]], [[OCaml]], [[Pascal]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[Pluto]], [[Python]], [[Quackery]], [[R]], [[Raku]], [[Rebol]], [[Red]], [[RPL]], [[Ruby]], [[Rust]], [[Uiua]], [[Wren]], [[XPL0]], [[Zig]]

## Contradictions
- None — reference task page.
