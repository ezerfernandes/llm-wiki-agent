---
title: "Topswops (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Topswops
---

## Summary
Topswops is a card game invented by John Conway: starting from a permutation of cards numbered 1..n (leftmost on top), each round reverses the first m cards where m is the value of the topmost card, repeating until card 1 reaches the top while counting the reversals. The task is to compute topswops(n), the maximum number of swaps needed over all starting permutations, for n in 1..10. The key insight is that this is equivalent to the worst-case "pancake flipping" deck-prefix-reversal process, and the answers form a known integer sequence requiring an exhaustive search over all n! permutations.

## Task Requirements
- Implement the round operation: reverse the first m cards where m is the current top card's value.
- Repeat rounds until the top card is 1, counting the number of reversals (swaps).
- Define topswops(n) as the maximum swap count across every permutation of n cards.
- Generate and display a table of n vs topswops(n) for n from 1 to 10 inclusive.

## Language Coverage
47 languages implement this task, giving broad coverage across mainstream, functional, and niche languages. Representative implementations include C, C++, Java, Python, Go, Rust, Haskell, J, Julia, Raku, and REXX.

## Connections
- [[Permutations]] — the search ranges over all n! orderings of the cards
- [[Combinatorics]] — counting and exhaustive enumeration of arrangements
- [[PancakeSorting]] — the prefix-reversal mechanic mirrors pancake flipping (Fannkuch)
- [[BruteForceSearch]] — finding the maximum requires checking every permutation
- [[OEIS]] — sequence A000375 records the known topswops values

## Contradictions
- None — reference task page.
