---
title: "Fairshare between two and more (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fairshare_between_two_and_more
---

## Summary
This task generalizes the Thue-Morse sequence to a fairer turn-taking scheme among b people. For two people, the standard Thue-Morse sequence (digit sum of n in binary, modulo 2) decides whose turn it is, producing a more equitable distribution than simple alternation. The key insight is that the same idea extends to any base: when counting n in base b, the digit sum modulo b yields a fairshare sequence for b participants.

## Task Requirements
- Implement a routine that expresses an integer count (starting from zero) in an arbitrary base b.
- Sum the base-b digits of each count and take the result modulo b to produce the next term of the fairshare sequence.
- Show the first 25 terms of the fairshare sequence for 2, 3, 5, and 11 people.

## Language Coverage
54 languages implement this task, showing broad coverage across functional, imperative, and array-oriented paradigms. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, Julia, Raku, J, and APL.

## Connections
- [[ThueMorseSequence]] — the base-2 case of this generalized fairshare construction
- [[ModularArithmetic]] — digit sums are reduced modulo the base b
- [[NumberBases]] — expressing the count in an arbitrary radix is the core step
- [[DigitSum]] — the per-term value derives from summing base-b digits

## Contradictions
- None — reference task page.
