---
title: "Rock-paper-scissors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rock-paper-scissors
---

## Summary
Implement the classic two-player game Rock-paper-scissors where the computer plays against a human operator. The key twist beyond the basic win rules (rock beats scissors, scissors beat paper, paper beats rock) is that the computer must not pick uniformly at random: it records the frequency of the player's past choices and makes a weighted random choice that anticipates and counters the player's most likely next move.

## Task Requirements
- Implement the win/lose/tie rules: rock beats scissors, scissors beat paper, paper beats rock; identical choices are a draw.
- Let the operator select rock, paper, or scissors each round.
- Have the computer track the frequency of the player's historical choices.
- Use that frequency to make a weighted random choice aimed at defeating the opponent (not a uniform random pick).
- Extra credit: support additional weapons (e.g., the rock-paper-scissors-lizard-Spock variant).

## Language Coverage
83 languages implement this task, a very broad cross-section spanning systems, scripting, functional, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Clojure, Ruby, and Racket.

## Connections
- [[ProbabilisticChoice]] — the weighted-random selection at the core of the task
- [[WeightedRandomSelection]] — picking a counter-move proportional to observed frequencies
- [[FrequencyAnalysis]] — recording and counting the player's past choices
- [[PredictiveModeling]] — using history to anticipate the opponent's next move
- [[FiniteStateGame]] — the fixed move set and cyclic dominance structure

## Contradictions
- None — reference task page.
