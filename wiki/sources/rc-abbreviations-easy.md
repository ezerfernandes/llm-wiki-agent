---
title: "Abbreviations, easy (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abbreviations,_easy
---

## Summary
The task asks the programmer to validate user-entered words against a fixed command table (derived from the old XEDIT editor) where each command's capitalized prefix defines its minimum required abbreviation length. The key insight is that the count of uppercase letters in a table word sets the shortest acceptable abbreviation, and a valid abbreviation must case-insensitively match the leading characters while not exceeding the full word's length. Valid inputs return the full command uppercased; invalid ones return the literal `*error*`.

## Task Requirements
- Treat the command table as one long string of space-separated words; order must be preserved and the table need not be validated.
- For each user word (case-insensitive), accept it only if its length is at least the number of capital letters in the table word, it matches the leading characters, and it is no longer than the table word.
- Words with no lowercase letters in the table admit no abbreviation (only the exact full word).
- Return the matched command fully uppercased, or the lowercase string `*error*` (7 chars) for invalid words; blank or null input returns a null/empty string.
- Demonstrate output using the provided sample input line.

## Language Coverage
57 languages implement this task, spanning systems and scripting languages broadly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, REXX, and several BASIC dialects such as FreeBASIC and Yabasic.

## Connections
- [[StringProcessing]] — core matching and tokenization work
- [[PrefixMatching]] — abbreviations are case-insensitive leading-substring matches
- [[CaseFolding]] — comparisons ignore case and output is uppercased
- [[Tokenization]] — both the command table and user input are split on whitespace

## Solved in (Rosetta Code languages)
Solved in **53** of the wiki's catalogued languages (Rosetta Code shows 57 language sections for this task). (4 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[ArkScript]], [[ARM Assembly]], [[AutoHotkey]], [[AWK]], [[C]], [[C++]], [[Clojure]], [[Crystal]], [[Delphi]], [[EasyLang]], [[Euphoria]], [[Factor]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Lua]], [[Nanoquery]], [[Nim]], [[OCaml]], [[Pascal]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[PHP]], [[Picat]], [[Pluto]], [[PowerShell]], [[Prolog]], [[Python]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[REXX]], [[Rust]], [[Scala]], [[Tcl]], [[V (Vlang)]], [[VBA]], [[Vedit macro language]], [[Wren]], [[Yabasic]]

## Contradictions
- None — reference task page.
