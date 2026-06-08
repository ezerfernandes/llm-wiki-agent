---
title: "Wordle comparison (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, game-logic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wordle_comparison
---

## Summary
Implement the core scoring logic of the word game Wordle: given an answer string and a guess string of equal length, mark each guessed letter as green (correct letter, correct position), yellow (letter present elsewhere in the answer), or grey (not present). The key insight, which many clones get wrong, is handling duplicate letters correctly: a repeated letter in the guess is only colored green/yellow as many times as it appears in the answer, with excess occurrences marked grey. This typically requires a two-pass approach — first mark all exact matches, then allocate remaining answer-letter counts to non-matching positions.

## Task Requirements
- Write a function taking two equal-length strings: the answer and the guess.
- Return an ordered sequence marking each guess letter as green, yellow, or grey (or equivalent codes like 2/1/0).
- Correctly handle multiple instances of the same letter: only color it green/yellow up to its count in the answer; mark excess repeats grey.
- Support printable ASCII/Unicode characters (hex 20 to 7F); case is significant.
- Test with answer `ALLOW` and guess `LOLLY`, yielding `(yellow, yellow, green, grey, grey)`.

## Language Coverage
37 languages implement this task, spanning systems and functional languages alongside scripting and BASIC dialects. Representative implementations include C, C++, C#, Go, Java, Python, Haskell, Julia, Perl, Raku, Scala, and Lua.

## Connections
- [[StringProcessing]] — per-character comparison of two strings
- [[Multiset]] — counting available answer letters to handle duplicates correctly
- [[BullsAndCows]] — closely related deduction/scoring game
- [[Mastermind]] — analogous peg-coloring feedback mechanism

## Contradictions
- None — reference task page.
