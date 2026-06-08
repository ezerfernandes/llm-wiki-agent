---
title: "Number reversal game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, interactive-game]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Number_reversal_game
---

## Summary
This task describes an interactive puzzle in which the numbers 1 through 9 are presented in a jumbled (non-ascending) order. On each turn the player chooses how many digits, counting from the left, to reverse; the program flips that prefix and repeats until the list is sorted in ascending order. The score is the total number of reversals taken, making it a hands-on, human-driven variant of the prefix-reversal sort known as pancake sorting.

## Task Requirements
- Start with the digits 1–9 shuffled into an order that is definitely not ascending.
- Display the current list, then prompt the player for a count of leftmost digits to reverse.
- Reverse exactly that prefix of digits and show the new arrangement.
- Repeat the prompt-and-reverse loop until the digits are in ascending order.
- Report the score as the count of reversals performed; input validation is not required.

## Language Coverage
99 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects. Representative examples include C, C++, C#, Java, Python, Ruby, Perl, Haskell, Go, Rust, and Common Lisp.

## Connections
- [[PancakeSorting]] — the same prefix-reversal operation, here driven manually by the player
- [[Topswops]] — a closely related prefix-reversal number puzzle
- [[PrefixReversal]] — the core list-manipulation primitive used each turn
- [[InteractiveGame]] — the prompt/respond loop that scores the player

## Contradictions
- None — reference task page.
