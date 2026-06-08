---
title: "Bulls and cows (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bulls_and_cows
---

## Summary
Implement the classic pencil-and-paper code-breaking game "Bulls and Cows" as a program. The computer generates a secret four-digit number drawn from the digits 1–9 with no repeats, then repeatedly accepts the player's guesses and scores them. The key insight is the scoring rule: a "bull" is a correct digit in the correct position, while a "cow" is a correct digit that exists in the secret but sits in the wrong position.

## Task Requirements
- Generate a random four-digit secret number using digits 1 through 9 with no duplicate digits.
- Prompt the player for guesses against this secret number.
- Validate and reject malformed guesses (wrong length, non-digits, duplicates, out-of-range).
- Score each guess: one bull per digit matching in value and position; one cow per digit present but positioned wrongly.
- End the game when the guess exactly matches the secret (the player wins).

## Language Coverage
124 languages implement this task, reflecting wide popularity as an interactive game exercise spanning systems, scripting, and functional languages. Representative implementations include C, C++, Python, Java, Haskell, Ruby, Go, Rust, Common Lisp, and Prolog.

## Connections
- [[Mastermind]] — generalized variant of the same deduction game with colored pegs
- [[GuessTheNumber]] — sibling Rosetta Code guessing task with simpler scoring
- [[RandomNumberGeneration]] — needed to pick the secret without duplicates
- [[InputValidation]] — rejecting malformed guesses is a core requirement
- [[CombinatorialGames]] — the deductive guessing structure underlying play

## Contradictions
- None — reference task page.
