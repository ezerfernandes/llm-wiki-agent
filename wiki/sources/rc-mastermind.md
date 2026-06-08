---
title: "Mastermind (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mastermind
---

## Summary
Implement a simple version of the board game Mastermind, in which the program generates a secret color code and the player repeatedly guesses it, receiving feedback after each attempt. The key challenge is the scoring logic: correctly counting pegs for "right color in the right position" versus "right color in the wrong position" without double-counting duplicated colors.

## Task Requirements
- Let the player configure the number of colors (2–20).
- Let the player configure the code length (4–10).
- Let the player configure the maximum number of guesses (7–20).
- Let the player choose whether colors may repeat within the code.
- Display every player guess and its result; for the text version, mark exact matches with `X`, correct-color/wrong-position with `O`, and absent colors with `-` (e.g. `1. ADEF - XXO-`).

## Language Coverage
28 languages implement this task, spanning systems, scripting, functional, and database languages. Representative entries include C++, Rust, Go, Java, JavaScript, Python, Perl, Raku, Julia, Lua, and even SQL.

## Connections
- [[StringProcessing]] — guesses and codes compared as sequences of color tokens
- [[MultisetMatching]] — counting white pegs requires multiset intersection to avoid double-counting
- [[RandomNumberGeneration]] — generating the secret code
- [[BullsAndCows]] — closely related guess-and-feedback deduction game

## Contradictions
- None — reference task page.
