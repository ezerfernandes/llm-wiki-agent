---
title: "Poker hand analyser (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, combinatorics, games]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Poker_hand_analyser
---

## Summary
The task is to parse a single five-card poker hand given as a space-separated list of cards and classify it into one of the standard poker rankings. Each card is two characters encoding a face (a, 2–10, j, q, k) and a suit (h/d/c/s or the Unicode suit symbols). The key insight is that ranking reduces to counting face frequencies and checking two structural properties — whether all suits match (flush) and whether the faces form a consecutive run (straight) — rather than enumerating cases by hand.

## Task Requirements
- Parse five cards from a space-separated string, each with a face and a suit character.
- Reject duplicate cards as `invalid` (jokers excepted in the extra-credit variant).
- Output exactly one of: straight-flush, four-of-a-kind, full-house, flush, straight, three-of-a-kind, two-pair, one-pair, high-card, or invalid.
- Display program output for the given example hands.
- Extra credit: support Unicode 6.0 playing-card characters, allow up to two jokers (duplicates permitted for jokers only), and add five-of-a-kind as the highest hand.

## Language Coverage
46 languages implement this task, giving broad coverage across functional, imperative, and scripting paradigms — including C, C++, C#, Java, Python, Ruby, Rust, Go, Haskell, Perl, Raku, and Prolog.

## Connections
- [[StringParsing]] — tokenizing and validating the card notation
- [[FrequencyCounting]] — tallying face counts to detect pairs, trips, and quads
- [[Combinatorics]] — the underlying space of poker hand categories
- [[PatternMatching]] — mapping count signatures to hand rankings

## Contradictions
- None — reference task page.
