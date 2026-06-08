---
title: "Anadromes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anadromes
---

## Summary
An anadrome is a word whose reversal spells a *different* valid word (e.g. "regal" / "lager"), making it a special case of an anagram and a portmanteau of "anagram" and "palindrome". The task is to scan a large English dictionary word list, reverse each word, and report pairs where the reversal is also a dictionary word. The key insight is that a hash set of all words enables O(1) membership tests, so each word's reverse can be checked in a single pass.

## Task Requirements
- Read the `words.txt` dictionary from the dwyl/english-words repository.
- Find all anadrome pairs: words whose character reversal is a different word also present in the list.
- Restrict output to words with more than 6 characters.
- Display each pair only once (avoid listing both `word`/`reverse` and `reverse`/`word`).

## Language Coverage
51 languages implement this task, spanning systems, scripting, functional, and query languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and even the database language DuckDB.

## Connections
- [[StringReversal]] — core operation applied to every candidate word
- [[HashSet]] — enables constant-time dictionary membership lookups
- [[Anagram]] — anadromes are a restricted subset of anagrams
- [[PalindromeDetection]] — closely related string property the task contrasts against

## Solved in (Rosetta Code languages)
Solved in **46** of the wiki's catalogued languages (Rosetta Code shows 51 language sections for this task). (5 further RC language section(s) are outside the wiki's popularity-list language set.)

[[Ada]], [[Agena]], [[ALGOL 68]], [[AppleScript]], [[Arturo]], [[AWK]], [[C]], [[C++]], [[Common Lisp]], [[Crystal]], [[D]], [[DuckDB]], [[Factor]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Lua]], [[M2000 Interpreter]], [[MiniScript]], [[Nim]], [[Objeck]], [[OCaml]], [[Pascal]], [[PascalABC.NET]], [[Perl]], [[Phix]], [[Pluto]], [[Python]], [[Quackery]], [[R]], [[Raku]], [[Ring]], [[Ruby]], [[Rust]], [[Seed7]], [[SETL]], [[Sidef]], [[Swift]], [[Uiua]], [[Wren]]

## Contradictions
- None — reference task page.
