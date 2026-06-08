---
title: "Prime conspiracy (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Prime_conspiracy
---

## Summary
This task asks the programmer to empirically verify a 2016 discovery by Soundararajan and Lemke Oliver: that consecutive prime numbers have non-random preferences about their last decimal digits. For every pair of successive primes, you record the transition from the final digit `i` of one prime to the final digit `j` of the next, then tally each transition and report its relative frequency. The key insight is that these frequencies are markedly uneven — for example, a prime ending in 9 is far more likely to be followed by a prime ending in 1 than another ending in 9 — which appears to contradict the assumption that primes behave like random numbers.

## Task Requirements
- Consider the first one million primes (extra credit: one hundred million primes).
- For each pair of successive primes, classify the transition `i -> j` where `i` and `j` are the last decimal digits (modulo 10).
- Count the occurrences of each transition.
- Print each transition with its count and relative frequency as a percentage, sorted by `i`.
- Observe that frequencies are not evenly distributed for a given `i`.

## Language Coverage
48 languages implement this task, spanning systems, scripting, functional, and array languages — including C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and Wren.

## Connections
- [[PrimeNumbers]] — the task operates on the sequence of primes
- [[ModularArithmetic]] — transitions are classified by last digit (mod 10)
- [[SieveOfEratosthenes]] — common method to generate the first N primes
- [[FrequencyDistribution]] — output reports relative frequencies of transitions
- [[NumberTheory]] — the underlying conjecture about prime gaps and digit bias

## Contradictions
- None — reference task page.
