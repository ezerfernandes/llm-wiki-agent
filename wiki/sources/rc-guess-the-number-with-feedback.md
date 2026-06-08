---
title: "Guess the number/With feedback (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, games, control-flow]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Guess_the_number/With_feedback
---

## Summary
This task asks the programmer to build a number-guessing game where the computer picks a secret number within fixed limits and the player guesses repeatedly. Unlike the plain "guess the number" task, after each guess the program gives directional feedback — telling the player whether the guess is too high, too low, or correct — which lets a human (or algorithm) converge on the answer via binary search. The key insight is that comparison-based feedback transforms a blind search into a logarithmic one.

## Task Requirements
- The computer chooses a number between given set limits.
- The player is repeatedly prompted for guesses until the target is guessed correctly.
- After each guess the computer reports whether the guess is higher than the target, equal to it, lower than it, or that the input was inappropriate (invalid).

## Language Coverage
132 languages implement this task, spanning systems, scripting, functional, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Ruby, and Perl.

## Connections
- [[BinarySearch]] — directional feedback enables a logarithmic guessing strategy
- [[RandomNumberGeneration]] — the computer picks the secret target at random
- [[InputValidation]] — the program must detect and reject inappropriate input
- [[ControlFlow]] — the guess-feedback loop relies on conditional comparison and iteration

## Contradictions
- None — reference task page.
