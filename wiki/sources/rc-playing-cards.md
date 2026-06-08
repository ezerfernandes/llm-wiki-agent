---
title: "Playing cards (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Playing_cards
---

## Summary
The task asks the programmer to design a data structure for a standard 52-card deck and the methods to operate on it. Each card is modeled as a combination of a pip value (rank) and a suit, giving it a unique identity within the deck. The key insight is choosing a representation for cards and a deck that makes building, randomizing, and dealing natural — often the suit/rank pair is the cross product of two small sets.

## Task Requirements
- Define a data structure for a deck containing 52 unique cards.
- Provide a method to make a new (ordered) deck.
- Provide a method to shuffle/randomize the deck.
- Provide a method to deal cards from the deck.
- Provide a method to print the current contents of a deck.
- Each card must carry a pip (rank) value and a suit value that together form its unique value.

## Language Coverage
94 languages implement this task, spanning functional, object-oriented, and procedural styles as well as many BASIC dialects. Representative implementations include Python, C++, Java, Haskell, Common Lisp, Ruby, Rust, Go, Scala, and Perl.

## Connections
- [[DataStructures]] — modeling a card as a rank/suit record and a deck as a collection.
- [[FisherYatesShuffle]] — the standard in-place algorithm for randomizing the deck.
- [[CartesianProduct]] — a fresh deck is the cross product of ranks and suits.
- [[EnumeratedTypes]] — suits and pip values are naturally expressed as enumerations.

## Contradictions
- None — reference task page.
