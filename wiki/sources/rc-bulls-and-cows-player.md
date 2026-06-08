---
title: "Bulls and cows/Player (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, games, search-algorithms, constraint-satisfaction]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bulls_and_cows/Player
---

## Summary
The task is to write a *player* (solver) for the Bulls and Cows guessing game rather than the scorer. The player must make guesses and refine them based on the bulls/cows feedback from previous attempts. The key insight is the candidate-elimination strategy: generate every possible secret number, then after each guess prune the candidate set to only those numbers that would have produced the same score for that guess. The next guess is drawn from the surviving candidates, so the player either eventually guesses correctly or exhausts the list, which signals a scoring inconsistency.

## Task Requirements
- Implement a player that guesses the secret rather than scoring guesses.
- Give intermediate guesses that are consistent with the scores received for all prior attempts.
- Suggested method: enumerate all possible answers, then keep only candidates that would yield the same score as the latest guess received.
- The next guess may be any number remaining in the pruned candidate list.
- Terminate by guessing correctly or by running out of candidates (indicating a scoring problem).

## Language Coverage
52 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Go, Rust-adjacent Crystal, Haskell, Python, Ruby, Perl, Raku, Java, Kotlin, Common Lisp, Prolog, and J.

## Connections
- [[ConstraintSatisfaction]] — each score acts as a constraint pruning the candidate space.
- [[GameSolving]] — automated player rather than a human guesser.
- [[CombinatorialSearch]] — enumerating and filtering permutations of digits.
- [[BullsAndCows]] — the companion scorer task this player interacts with.
- [[GuessTheNumber]] — related feedback-driven guessing task.

## Contradictions
- None — reference task page.
