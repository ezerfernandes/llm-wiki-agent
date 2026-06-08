---
title: "War card game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, simulation, card-games]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/War_card_game
---

## Summary
This task asks the programmer to simulate the children's card game War, following the Bicycle playing card company's published rules. A standard 52-card deck is shuffled and split evenly between two players; each round both players flip their top card, the higher rank wins both cards, and ties trigger a "war" in which additional face-down and face-up cards are played until a winner is decided. The key insight is faithfully modeling deck/hand state and the recursive nature of wars, then playing out a full game to completion.

## Task Requirements
- Simulate the card game War using the Bicycle manufacturer's rules.
- Show a game as it is played (display the rounds/progress).
- User input is optional.

## Language Coverage
26 languages implement this task, giving moderate breadth across scripting, systems, and array-oriented styles. Representative implementations include Python, Java, C++, Rust, Go, Perl, Raku, Julia, Lua, and array languages such as J and Uiua.

## Connections
- [[Simulation]] — the task models a stochastic game process end to end.
- [[PlayingCards]] — relies on standard deck representation and ranking.
- [[ShufflingAlgorithm]] — randomized initial deck order drives gameplay.
- [[FiniteStateMachine]] — round/war handling is naturally modeled as state transitions.
- [[Recursion]] — repeated ties chain into nested wars.

## Contradictions
- None — reference task page.
