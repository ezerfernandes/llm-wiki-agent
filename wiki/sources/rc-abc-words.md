---
title: "ABC words (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/ABC_words
---

## Summary
An ABC word is a word in which the letters "a", "b", and "c" all appear in alphabetical order (a before b before c). When a letter occurs more than once, only its first occurrence is considered when checking the ordering. The task is to scan a standard dictionary file and print every word satisfying this property. The key insight is that membership depends only on the relative positions of the first occurrence of each of the three target letters.

## Task Requirements
- Define an ABC word as one where letters "a", "b", and "c" appear in that alphabetical order within the word.
- When a letter occurs multiple times, use only its first occurrence to judge the ordering.
- Read the word list from unixdict.txt.
- Display every ABC word found in that dictionary.

## Language Coverage
79 languages implement this task, reflecting broad coverage typical of simple string-filtering exercises across paradigms. Representative implementations include Python, C, C++, Java, Haskell, Go, Rust, Perl, Raku, Ruby, APL, and REXX.

## Connections
- [[StringProcessing]] — the task is fundamentally substring/character-position filtering
- [[SubsequenceMatching]] — checking that "abc" appears as an ordered subsequence of first occurrences
- [[DictionaryWordlist]] — relies on scanning the unixdict.txt corpus
- [[StringSearching]] — locating the first index of each target character

## Solved in (Rosetta Code languages)
Solved in **70** of the wiki's catalogued languages (Rosetta Code shows 79 language sections for this task). (9 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[Action!]], [[Ada]], [[ALGOL 68]], [[APL]], [[AppleScript]], [[Arturo]], [[AutoHotkey]], [[AWK]], [[Ballerina]], [[BASIC]], [[BCPL]], [[BQN]], [[C]], [[C++]], [[CLU]], [[COBOL]], [[Crystal]], [[D]], [[Delphi]], [[Diego]], [[Draco]], [[DuckDB]], [[EasyLang]], [[Factor]], [[Forth]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Lua]], [[M2000 Interpreter]], [[Modula-2]], [[Nim]], [[Nu]], [[Oberon-07]], [[Objeck]], [[OCaml]], [[Pascal]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[PL-I]], [[Pluto]], [[Processing]], [[Prolog]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Rust]], [[Seed7]], [[Swift]], [[Tcl]], [[Transd]], [[Uiua]], [[V (Vlang)]], [[Wren]], [[XPL0]]

## Contradictions
- None — reference task page.
