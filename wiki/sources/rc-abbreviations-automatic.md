---
title: "Abbreviations, automatic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, prefix-matching]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abbreviations,_automatic
---

## Summary
The task asks the programmer to automatically determine, for each line in a list of words, the minimum-length prefix that makes every word on that line uniquely abbreviatable. The supplied data is the days-of-the-week names in roughly one hundred languages, one language per line. The key insight is finding the smallest prefix length at which no two words on a line collide; a blank line yields a null string.

## Task Requirements
- Read the days-of-the-week list (one language per line) from a file.
- Write a function that finds the numeric minimum abbreviation length per line so that all abbreviations on that line remain unique.
- A blank (or null) line returns a null string.
- Words are separated by at least one blank; underscores stand in for embedded blanks; the list need not be validated.
- Process and show output for at least the first five lines.

## Language Coverage
67 languages implement this task, spanning systems, scripting, functional, and assembly families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, REXX, and ARM Assembly.

## Connections
- [[StringProcessing]] — the task is fundamentally about manipulating and comparing word strings.
- [[PrefixMatching]] — uniqueness is decided by comparing leading prefixes of each word.
- [[Abbreviation]] — the core domain concept being computed automatically.
- [[Tokenization]] — each line must be split on whitespace into candidate words.

## Solved in (Rosetta Code languages)
Solved in **62** of the wiki's catalogued languages (Rosetta Code shows 67 language sections for this task). (5 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[Amazing Hopper]], [[ARM Assembly]], [[AutoHotkey]], [[AWK]], [[BQN]], [[C]], [[C++]], [[COBOL]], [[Common Lisp]], [[Crystal]], [[D]], [[Delphi]], [[EasyLang]], [[Emacs Lisp]], [[Erlang]], [[Factor]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Groovy]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Ksh]], [[Lua]], [[Nim]], [[Objeck]], [[Perl]], [[Phix]], [[PHP]], [[Picat]], [[Pluto]], [[Prolog]], [[PureBasic]], [[Python]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ruby]], [[Rust]], [[Scala]], [[SenseTalk]], [[Tcl]], [[Transd]], [[TSE SAL]], [[Uiua]], [[V (Vlang)]], [[VBA]], [[VBScript]], [[Visual Basic .NET]], [[Wren]], [[Yabasic]]

## Contradictions
- None — reference task page.
