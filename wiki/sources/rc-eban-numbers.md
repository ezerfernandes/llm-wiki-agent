---
title: "Eban numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Eban_numbers
---

## Summary
An eban number is one whose American-English spelling contains no letter "e" (so any number spelled with "e" is "banned"). The task is to enumerate and count eban numbers below various thresholds up to ten million. The key insight is that only the words for 2, 4, 6, 30, and 60 (and their compounds like sixty-six, two thousand, four million, etc.) avoid the letter "e", which lets the search be done by digit-pattern rules instead of literally spelling every number.

## Task Requirements
- List all eban numbers ≤ 1,000 horizontally, plus a count.
- List all eban numbers between 1,000 and 4,000 inclusive, plus a count.
- Show counts of eban numbers up to and including 10,000; 100,000; 1,000,000; and 10,000,000.
- Use American spelling (e.g. two billion, not two milliard); consider only numbers below one sextillion (10^21).
- Show all output.

## Language Coverage
53 languages implement this task, spanning systems, scripting, functional, and BASIC-family dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, Ruby, and Wren.

## Connections
- [[NumberNames]] — spelling integers in English, the basis for the eban test
- [[NumberTheory]] — integer sequences defined by digit/word properties
- [[StringProcessing]] — detecting the letter "e" in spelled-out numbers
- [[OEIS]] — catalogued as sequence A006933

## Contradictions
- None — reference task page.
