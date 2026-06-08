---
title: "Guess the number/With feedback (player) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, binary-search, algorithm]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Guess_the_number/With_feedback_(player)
---

## Summary
This task reverses the usual guessing game: the computer is the player and a human scorer secretly picks a number within agreed limits. The program prints a guess, the scorer replies whether the guess is higher than, lower than, or equal to the target, and the loop continues until the program guesses correctly. The key insight is that the program should guess intelligently by exploiting the comparison feedback, with binary search being the canonical approach since it halves the remaining range each turn.

## Task Requirements
- Choose set limits for the target number (an agreed range).
- Have the computer print a guess of the target number.
- Ask the scorer to report whether the guess is higher than, lower than, or equal to the target.
- Loop guess-and-score turns until the computer guesses correctly.
- Guess intelligently based on accumulated feedback (e.g. a binary-search-based algorithm).

## Language Coverage
80 languages implement this task, spanning systems and scripting languages alike. Representative examples include C, C++, C#, Java, Python, Haskell, Rust, Go, Perl, Ruby, Lua, and Scheme, alongside many BASIC dialects and Lisp-family languages.

## Connections
- [[BinarySearch]] — the standard intelligent guessing strategy that narrows the range
- [[DivideAndConquer]] — binary search is the archetypal divide-and-conquer technique
- [[InteractiveInput]] — the loop depends on reading scorer feedback each turn
- [[GuessTheNumber]] — the inverse task where the computer holds the secret number

## Contradictions
- None — reference task page.
