---
title: "Set, the card game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, card-game]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Set,_the_card_game
---

## Summary
The task models the card game *Set*, whose 81-card deck encodes every combination of four attributes — number (1/2/3), symbol (diamond/oval/squiggle), colour (red/green/purple), and shading (solid/striped/open) — taken across three values each (3^4 = 81). A program must build and shuffle the deck, deal a specified number of cards, and find all "sets": triples where, for each of the four attributes independently, the three values are either all identical or all distinct.

## Task Requirements
- Create a representation of a 81-card Set pack (every combination of number, symbol, colour, shading).
- Shuffle the pack and select a specified number of cards, listing them in the output.
- Identify and list all valid sets among the selected cards, where a set is three cards that are all-same-or-all-different in each of the four attributes.

## Language Coverage
22 languages implement this task, spanning systems, functional, and scripting families. Representative implementations include C++, Rust, Zig, Go, Nim, Java, JavaScript, Python, Ruby, Raku, Common Lisp, Factor, and the array language Uiua.

## Connections
- [[Combinatorics]] — enumerating the 81-card space and choosing triples
- [[CartesianProduct]] — the deck is the product of four 3-valued attribute domains
- [[FisherYatesShuffle]] — randomizing the pack before dealing
- [[BruteForceSearch]] — checking all C(n,3) candidate triples for the set condition

## Contradictions
- None — reference task page.
