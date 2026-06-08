---
title: "Four is magic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-to-words, string-processing, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Four_is_magic
---

## Summary
Given an integer, build an English sentence chaining each number to the letter-count of its own spelled-out cardinal form: "N is K, K is M, ... four is magic." The key insight is that the digit four has exactly four letters, so the sequence is self-referential and every starting integer eventually converges to four, making four the unique fixed point that terminates the chain.

## Task Requirements
- Spell an integer as an English cardinal, append " is ", then spell the character count of that word, and repeat using each count as the next term.
- Count all characters of the cardinal string, including spaces and hyphens (e.g. "one hundred fifty-one" = 21).
- Stop at four, ending the sentence with "four is magic." (input 4 yields just "four is magic.").
- Use English short scale; no commas, no "and", and a word separator between tens and units (twenty-three or twenty three, not twentythree).
- Roll-your-own conversion must handle at least 0 to 999999; library-based must support unsigned 64-bit integers; negative numbers optionally supported.
- Display output for a representative sample of 5 to 25 values; write idiomatic, legible code (explicitly not code golf).

## Language Coverage
50 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Perl, Raku, Julia, and APL.

## Connections
- [[NumberToWords]] — converting integers to English cardinal spellings is the core subroutine
- [[Recursion]] — the sequence is naturally expressed as a recursive chain terminating at four
- [[StringProcessing]] — counting characters of spelled-out words drives each step
- [[FixedPoint]] — four is the unique fixed point that all integers converge to

## Contradictions
- None — reference task page.
