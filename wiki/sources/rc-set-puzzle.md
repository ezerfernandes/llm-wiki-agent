---
title: "Set puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, brute-force]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Set_puzzle
---

## Summary
This task simulates the card game Set, where a deck of 81 cards is built from every combination of four features (color, symbol, number, shading), each having three possible values. Three cards form a "set" when, for every feature, the values are either all identical or all distinct. The program must deal a hand (9 cards in basic mode, 12 in advanced) that contains exactly the required number of valid sets (4 or 6 respectively), then print the dealt cards and the sets found among them.

## Task Requirements
- Build the full deck of 81 cards (4 features × 3 values = 3^4 combinations).
- Shuffle and deal 9 cards (basic) or 12 cards (advanced) depending on the chosen mode.
- Ensure the dealt hand contains exactly 4 sets (basic) or 6 sets (advanced); reshuffle/redeal until the count matches.
- Detect all valid 3-card sets where each feature is uniformly same or uniformly different across the three cards.
- A card may appear in more than one set.
- Print both the dealt cards and the contents of every set found.

## Language Coverage
44 languages implement this task, showing broad coverage across functional, imperative, and array-oriented styles. Representative examples include Python, C, C++, Java, Haskell, Common Lisp, Rust, Ruby, Go, and J.

## Connections
- [[Combinatorics]] — generating the 81 cards and choosing 3-card subsets
- [[BruteForceSearch]] — checking all card triples for the set property
- [[FisherYatesShuffle]] — shuffling the deck before dealing
- [[CartesianProduct]] — the deck is the product of four three-valued feature axes

## Contradictions
- None — reference task page.
