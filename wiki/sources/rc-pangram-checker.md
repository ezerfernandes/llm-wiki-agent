---
title: "Pangram checker (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pangram_checker
---

## Summary
The task is to write a function that determines whether a sentence is a pangram — a sentence containing every letter of the English alphabet at least once, the classic example being "The quick brown fox jumps over the lazy dog." The key insight is that this reduces to a set-membership problem: normalize the text to lowercase, collect its distinct letters, and check whether that set covers all 26 letters a–z.

## Task Requirements
- Write a function or method that takes a sentence and reports whether it is a pangram.
- Show the function in use on example input.
- Case should be ignored so that mixed-case text is handled correctly.

## Language Coverage
125 languages implement this task, reflecting its popularity as a beginner-friendly string exercise. Representative implementations include Python, C, C++, Java, Haskell, Ruby, Rust, Go, Perl, and APL.

## Connections
- [[StringProcessing]] — the task is fundamentally text normalization and scanning.
- [[SetTheory]] — checking that the letters present form a superset of the alphabet.
- [[BitMasking]] — a common idiom uses a 26-bit mask, setting one bit per seen letter.
- [[AlphabetCoverage]] — the underlying notion of covering all 26 letters.

## Contradictions
- None — reference task page.
