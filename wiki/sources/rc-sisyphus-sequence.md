---
title: "Sisyphus sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequence, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sisyphus_sequence
---

## Summary
The Sisyphus sequence (devised in 2022 by Eric Angelini and Carole Dubois, OEIS A350877) is an infinite sequence of positive integers starting at 1. Each subsequent term is derived from the previous one: if the previous term is even, halve it; if odd, add the smallest prime that has not yet been added. The key bookkeeping insight is that the "smallest unused prime" advances monotonically, so a running prime pointer (with a sieve or incremental primality check) suffices to generate terms efficiently.

## Task Requirements
- Compute and display the first 100 terms, formatted as 10 lines of 10 terms each.
- Report the 1,000th, 10,000th, 100,000th, and 1,000,000th terms, and the highest prime needed to reach each.
- Stretch: report the 10-millionth and 100-millionth terms plus the highest prime for each.
- Stretch: by the 100-millionth term, identify which numbers under 250 have not yet appeared, and which have appeared the most (with counts).
- Extreme stretch: find the index of the first term equal to 36.

## Language Coverage
20 languages implement this task, a moderate spread across systems, scripting, and array languages. Representative implementations include ALGOL 68, C++, Java, JavaScript, Julia, Nim, Python, Perl, Raku, Wren, and Zig.

## Connections
- [[PrimeNumbers]] — terms grow by adding successive smallest-unused primes
- [[IntegerSequences]] — defined as an OEIS sequence (A350877)
- [[SieveOfEratosthenes]] — efficient prime generation for the large-index stretch goals
- [[NumberTheory]] — parity-driven recurrence over the integers

## Contradictions
- None — reference task page.
