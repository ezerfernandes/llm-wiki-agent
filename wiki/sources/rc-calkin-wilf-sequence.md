---
title: "Calkin-Wilf sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, rational-numbers, continued-fractions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Calkin-Wilf_sequence
---

## Summary
The task implements the Calkin-Wilf sequence, an enumeration that lists every nonnegative rational number exactly once via the recurrence a₁ = 1 and aₙ₊₁ = 1/(2⌊aₙ⌋ + 1 − aₙ). The key insight is that any rational's position in the sequence can be recovered without iterating it: the continued-fraction expansion of the rational, taken as a run-length encoding of a binary numeral (read from the tail), yields the term index — provided the continued fraction has an odd number of terms.

## Task Requirements
- Print terms 1 through 20 of the Calkin-Wilf sequence (rational arithmetic recommended to avoid floating-point error).
- Determine a rational's position by computing its continued fraction, normalizing to an odd term count, and treating the terms as run-lengths of a binary number read from the end.
- Find the position of 83116/51639 in the sequence (worked example: 9/4 has continued fraction [2;3,1] → binary 100011 → term 35).

## Language Coverage
50 languages implement this task, spanning mainstream languages, esoteric/assembly targets, and array/functional dialects. Representative entries include Python, C++, Java, Haskell, Rust, Go, Julia, Raku, J, BQN, and even low-level targets like EDSAC order code and Little Man Computer.

## Connections
- [[RationalNumbers]] — sequence is defined over exact rationals to avoid floating-point drift
- [[ContinuedFractions]] — the position-finding procedure relies on continued-fraction expansion
- [[RunLengthEncoding]] — continued-fraction terms encode the binary term index as run lengths
- [[CalkinWilfTree]] — the sequence is the breadth-first traversal of this binary tree of fractions
- [[FuscSequence]] — the related Stern-Brocot / fusc function generates the same numerators and denominators

## Contradictions
- None — reference task page.
