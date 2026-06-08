---
title: "Deal cards for FreeCell (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, random-number-generation, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Deal_cards_for_FreeCell
---

## Summary
The task asks the programmer to reproduce Microsoft FreeCell's numbered deals: given a deal number, deal the 52 cards in exactly the same order as the original Windows implementation. The key insight is that the deal is fully determined by seeding a specific linear congruential generator (from Microsoft C) with the deal number, then repeatedly drawing a card by index = next random number modulo the remaining array length, swapping it to the end, and removing it.

## Task Requirements
- Use the Microsoft C LCG: state_{n+1} = (214013 * state_n + 2531011) mod 2^31, with rand_n = state_n / 2^16 (range 0–32767).
- Seed the RNG with the deal number.
- Build a 52-card array ordered by rank (Ace..King), suit-interleaved (Clubs, Diamonds, Hearts, Spades) so index 0 = Ace of Clubs and index 51 = King of Spades.
- Until the array is empty: pick the card at index = (next random) mod (array length), swap it with the last card, remove it, and deal it.
- Lay all 52 dealt cards face up across 8 columns, filling row by row.
- Output may be ASCII, Unicode, graphics, or any other representation; results must match reference deals (e.g. Game #1, Game #617).

## Language Coverage
68 languages implement this task, a broad spread across systems, scripting, functional, and BASIC-family languages. Representative examples include C, C++, C#, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Ruby, and BBC BASIC.

## Connections
- [[LinearCongruentialGenerator]] — the deal is driven entirely by this specific Microsoft C PRNG.
- [[PseudorandomNumberGeneration]] — deterministic, seed-reproducible randomness underpins the numbered deals.
- [[FisherYatesShuffle]] — the swap-and-remove draw loop is a Fisher–Yates-style shuffle variant.
- [[PlayingCards]] — models a standard 52-card deck with ranks and suits.

## Contradictions
- None — reference task page.
