---
title: "Mind boggling card trick (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, simulation, probability, card-games]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mind_boggling_card_trick
---

## Summary
Simulate Matt Parker's "Stand Up Maths" card trick that produces apparent order from a shuffled deck. From a shuffled 52-card deck (half red, half black), deal cards using each turned-up card's color to route the *next* (unseen) card into a "red" or "black" pile while discarding the turned-up card; then randomly swap X cards between the two piles. The key insight is the invariant: after any such swap the number of black cards in the black pile always equals the number of red cards in the red pile.

## Task Requirements
- Create and shuffle a standard 52-card deck that is half red, half black.
- Deal: turn up the top card; if black, move the next unseen card to the black pile; if red, move it to the red pile; then discard the turned-up card. Repeat over the whole deck.
- Choose a random number X and swap X randomly chosen cards from the red pile with X randomly chosen cards from the black pile.
- Verify the assertion that the count of black cards in the black pile equals the count of red cards in the red pile.
- Optionally repeat the simulation many times to gather evidence; show output on the page.

## Language Coverage
38 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and J.

## Connections
- [[Probability]] — the trick relies on a counting invariant rather than chance.
- [[MonteCarloSimulation]] — repeated random trials gather evidence for the assertion.
- [[FisherYatesShuffle]] — randomizing the deck and selecting cards to swap.
- [[Invariant]] — the equal-count property preserved under any swap of X cards.
- [[PseudorandomNumberGeneration]] — needed for shuffling and choosing X.

## Contradictions
- None — reference task page.
