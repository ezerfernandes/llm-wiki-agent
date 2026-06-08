---
title: "Subtractive generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, random-number-generator, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Subtractive_generator
---

## Summary
The task asks the programmer to implement a subtractive random number generator, a lagged-difference PRNG where each output is the modular difference of two earlier outputs: r_n = r_(n-i) − r_(n-j) mod m. The key insight is that subtraction (plus adding m to negative results) replaces multiplication and division entirely, giving a fast generator with a long period that holds more state than a linear congruential generator. The specific target is to replicate the sequence produced by the *xpat2* generator (Bentley's implementation from Knuth's TAOCP Algorithm A).

## Task Requirements
- Implement the recurrence r_n = r_(n-55) − r_(n-24) mod 10^9 (popular lags i=55, j=24).
- Seed using Bentley's scheme: set s_0 = seed, s_1 = 1, then fill s_2..s_54 via s_n = s_(n-2) − s_(n-1) mod 10^9.
- Reorder the 55 state values by the permutation r_n = s_(34*(n+1) mod 55), exploiting that 34 and 55 are coprime.
- Advance the generator 165 more steps (r_55 through r_219), discarding them to avoid early-sequence bias.
- Output starts at r_220; for seed 292929 the sequence must begin 467478574, 512932792, 539453717.

## Language Coverage
50 languages implement this task, spanning systems languages, functional languages, and array/stack languages. Representative implementations include C, C++, C#, Java, Rust, Go, Python, Haskell, OCaml, Common Lisp, Perl, and J.

## Connections
- [[RandomNumberGenerator]] — this is a specific PRNG algorithm
- [[LinearCongruentialGenerator]] — the alternative PRNG it is contrasted with and outperforms in reputation
- [[ModularArithmetic]] — outputs are computed modulo 10^9
- [[RingBuffer]] — the ideal data structure for storing the last 55 state values
- [[KnuthTAOCP]] — the source of Algorithm A on which this generator is based

## Contradictions
- None — reference task page.
