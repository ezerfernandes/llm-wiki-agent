---
title: "Magnanimous numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magnanimous_numbers
---

## Summary
A magnanimous number is an integer for which, at every position where a "+" sign can be inserted between two of its digits, the resulting sum of the two parts is prime. For example, 6425 qualifies because 6+425, 64+25, and 642+5 are all prime, whereas 3538 fails since 353+8 = 361 is composite. The key insight is that the predicate is a conjunction of primality tests over all split points, with single-digit numbers (0-9) trivially included since no split is possible.

## Task Requirements
- Write a routine to test/find magnanimous numbers (sum is prime at every digit-split point).
- Display the first 45 magnanimous numbers.
- Display the 241st through 250th magnanimous numbers.
- Stretch goal: display the 391st through 400th magnanimous numbers.
- Single digits 0-9 count as magnanimous; leading zeros are disallowed except the value 0 itself, while internal zeros (e.g., 1001) are fine.

## Language Coverage
53 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, and REXX.

## Connections
- [[PrimeNumbers]] — every digit-split sum must be prime
- [[PrimalityTesting]] — core operation repeated across split points
- [[NumberTheory]] — the broader domain of integer-property classification
- [[DigitManipulation]] — splitting numbers at each inter-digit position

## Contradictions
- None — reference task page.
