---
title: "Guess the number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, games, random-number-generation, conditional-loops]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Guess_the_number
---

## Summary
A classic introductory game task: the program picks a secret integer between 1 and 10, then repeatedly prompts the player for a guess. Wrong guesses re-prompt; a correct guess prints "Well guessed!" and the program exits. The key idea is combining random number generation with a conditional loop that runs until the input matches the target.

## Task Requirements
- Have the program choose a number between 1 and 10 (inclusive).
- Prompt the player to enter a guess.
- If the guess is wrong, re-prompt until the player is correct.
- On a correct guess, print a "Well guessed!" message and exit.
- A conditional loop may be used to repeat the prompting.

## Language Coverage
159 languages implement this task, reflecting its popularity as a beginner exercise spanning everything from assembly to high-level scripting. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Ruby, and Lua.

## Connections
- [[RandomNumberGeneration]] — selecting the secret number requires a (pseudo)random source
- [[ConditionalLoops]] — the re-prompt-until-correct structure is a guarded loop
- [[InteractiveInput]] — reading and parsing player guesses from stdin
- [[GuessTheNumberWithFeedback]] — related variant that tells the player higher/lower

## Contradictions
- None — reference task page.
