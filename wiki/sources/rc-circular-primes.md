---
title: "Circular primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Circular_primes
---

## Summary
A circular prime is a prime that remains prime under every cyclic rotation of its base-10 digits (e.g. 1193 → 1931 → 9311 → 3119 are all prime). The task asks to enumerate these, counting each cyclic family only once via its smallest member, so 13 qualifies but its rotation 31 does not. The key insight is that beyond the small cases, all known larger circular primes are repunits (numbers consisting only of the digit 1), so finding more requires primality testing on R(n) values.

## Task Requirements
- Find the first 19 circular primes.
- If arbitrary-precision integers are available, find the next 4 circular primes (which are all repunits).
- (Stretch) Determine which of the repunits R(5003), R(9887), R(15073), R(25031), R(35317), and R(49081) are probably circular primes, doing as many as feasible.

## Language Coverage
50 languages implement this task, spanning systems, functional, scripting, and array languages — including C, C++, Rust, Go, Java, Haskell, Python, Julia, Raku, Wren, J, and REXX. Solutions vary mainly in whether they reach the big-number repunit stretch goal, which depends on bignum and probabilistic primality support.

## Connections
- [[PrimeNumbers]] — the core objects being tested and enumerated
- [[NumberTheory]] — circular primes and repunits are number-theoretic constructs
- [[Repunit]] — all the larger circular primes in this task are repunits R(n)
- [[PrimalityTest]] — the stretch goal needs probabilistic primality testing (e.g. Miller-Rabin) on huge numbers
- [[ArbitraryPrecisionArithmetic]] — required to handle repunits beyond machine-word size

## Contradictions
- None — reference task page.
