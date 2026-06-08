---
title: "Penney's game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, game-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Penney's_game
---

## Summary
Penney's game is a coin-tossing wager where two players each pick a length-three sequence of heads/tails, then a fair coin is flipped repeatedly until one player's chosen sequence appears in consecutive tosses, winning the round. The key insight is that the game is intransitive (non-transitive): the second player, after seeing the first player's pick, can always choose a sequence with a better-than-even chance of winning, so going second is an advantage.

## Task Requirements
- Implement a program that tosses a fair coin, keeps score, and plays Penney's game against a human opponent.
- Randomly decide who chooses (and reveals) their three-toss sequence first.
- If the computer goes first, it picks its sequence of three randomly.
- If the computer goes second, it must automatically play the optimum counter-sequence against the human's pick.
- Display the successive coin tosses as they occur.
- Show sample output for both a game where the computer chooses first and one where the user chooses first.

## Language Coverage
47 languages implement this task, spanning systems and scripting languages alike. Representative entries include C, C++, C#, Go, Rust, Java, Python, Haskell, Perl, Raku, Ruby, Julia, Lua, and Clojure.

## Connections
- [[ProbabilityTheory]] — analyzing win likelihoods over coin-toss sequences
- [[NonTransitiveGames]] — the optimal second-player strategy exploits intransitivity
- [[GameTheory]] — adversarial sequence selection and expected outcomes
- [[PseudorandomNumberGeneration]] — simulating fair coin tosses

## Contradictions
- None — reference task page.
