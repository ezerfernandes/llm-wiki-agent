---
title: "Abbreviations, simple (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abbreviations,_simple
---

## Summary
The task asks the programmer to expand abbreviated commands against a fixed command table drawn from the old XEDIT editor. Each command in the table may carry a number specifying the minimum number of leading characters needed to abbreviate it; a command with no number cannot be abbreviated at all. The key insight is that a user word is valid only if it is a case-insensitive prefix of a command whose length falls between that command's minimum abbreviation length and the command's full length.

## Task Requirements
- Treat the supplied command table as one long literal string; preserve word order, tolerate superfluous blanks, and accept any letter case.
- For each user-supplied word, determine validity: its length must be at least the command's minimum abbreviation number, no longer than the full command, and it must match the leading characters of the command (case-insensitively).
- Return the full uppercase command for a valid word, the lowercase string `*error*` (7 chars) for an invalid one, and a null string for blank or null input.
- Words with no trailing number in the table permit no abbreviation (only the exact full word matches).
- Reproduce the given example mapping, e.g. `riG rePEAT copies put mo rest types fup. 6 poweRin` to `RIGHT REPEAT *error* PUT MOVE RESTORE *error* *error* *error* POWERINPUT`.

## Language Coverage
53 languages implement this task, spanning systems languages, scripting languages, functional languages, and several assembly dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, REXX, and AArch64 Assembly.

## Connections
- [[StringProcessing]] — core operation is prefix matching and case folding
- [[Parsing]] — tokenizing the command table and user input into words
- [[PrefixMatching]] — validity hinges on case-insensitive leading-character comparison
- [[CommandLineInterface]] — abbreviations mirror sub-command aliasing in CLIs and editors

## Solved in (Rosetta Code languages)
Solved in **49** of the wiki's catalogued languages (Rosetta Code shows 53 language sections for this task). (4 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[ARM Assembly]], [[AutoHotkey]], [[C]], [[C++]], [[Clojure]], [[Crystal]], [[D]], [[Delphi]], [[EasyLang]], [[Factor]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Lua]], [[M2000 Interpreter]], [[MiniScript]], [[Nim]], [[OCaml]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[Pluto]], [[Python]], [[Racket]], [[Raku]], [[Rebol]], [[REXX]], [[Ruby]], [[Rust]], [[Scala]], [[SNOBOL4]], [[Tcl]], [[V (Vlang)]], [[VBA]], [[VBScript]], [[Wren]], [[Yabasic]]

## Contradictions
- None — reference task page.
