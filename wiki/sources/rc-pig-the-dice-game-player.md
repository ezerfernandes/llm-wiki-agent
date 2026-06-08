---
title: "Pig the dice game/Player (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game-ai, simulation, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pig_the_dice_game/Player
---

## Summary
This task extends the basic Pig dice game by adding automated players that follow explicit strategies, then simulating play. The programmer must build a dice simulator and scorer, give at least one player a decision-making strategy (when to roll versus hold), and show a sample game. The key insight is that simple threshold strategies (e.g. "hold once your turn total reaches N") can be compared statistically to find which is stronger and to measure any first-player advantage.

## Task Requirements
- Create a dice simulator and scorer for Pig and add the ability for a player to play according to at least one strategy.
- State the play strategies involved and show actual play during a game.
- Stretch goal: simulate many games between two players of given strategies and report summary statistics, such as the influence of going first or which strategy is stronger.

## Game Rules
- Single six-sided die; first to 100+ points wins.
- On a turn a player may roll (a 2-6 adds to the turn total and the turn continues) or hold (the turn total is banked into the safe score and the turn passes).
- Rolling a 1 forfeits the entire turn total and ends the turn.

## Language Coverage
25 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include Ada, C, C++, Common Lisp, Go, Haskell, Java, Julia, Python, Racket, Raku, Ruby, and Tcl.

## Connections
- [[PigTheDiceGame]] — the base task this builds upon
- [[GameStrategy]] — threshold/hold-at-N decision policies for an automated player
- [[MonteCarloSimulation]] — running many games to gather summary statistics
- [[Probability]] — expected-value reasoning behind optimal hold thresholds
- [[PseudorandomNumberGenerator]] — needed to simulate die rolls

## Contradictions
- None — reference task page.
