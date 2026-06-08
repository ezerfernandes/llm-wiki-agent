---
title: "Pig the dice game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game-simulation, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pig_the_dice_game
---

## Summary
Pig is a multiplayer game played with a single six-sided die where the first player to reach 100 or more points wins. The task asks the programmer to simulate dice throws and score a two-person game. The key mechanic is the push-your-luck tension: on each turn a player may keep rolling to accumulate points, but rolling a 1 wipes out all points banked that turn, while choosing to "hold" makes the turn's total permanently safe.

## Task Requirements
- Simulate dice throws for a two-person game.
- On a player's turn, allow the choice to either roll or hold.
- Rolling a 2-6 adds that value to the turn score and the player keeps the same choice.
- Rolling a 1 forfeits all points accumulated that turn and ends the turn.
- Holding adds the turn score to the player's safe total and ends the turn.
- First player to reach 100 or more points wins.

## Language Coverage
63 languages implement this task, spanning a broad mix of systems, scripting, functional, and BASIC-family languages. Representative implementations include Python, C, C++, Java, Go, Rust, Haskell, Ruby, Perl, JavaScript, and Common Lisp.

## Connections
- [[GameSimulation]] — models turn-based play with random dice events
- [[ProbabilityTheory]] — push-your-luck risk/reward built on die-roll odds
- [[PseudorandomNumberGeneration]] — requires simulating fair six-sided die throws
- [[StateMachine]] — each turn cycles through roll/hold decision states

## Contradictions
- None — reference task page.
