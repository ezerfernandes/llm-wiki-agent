---
title: "Least m such that n! + m is prime (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Least_m_such_that_n!_+_m_is_prime
---

## Summary
The task asks the programmer to compute, for each n, the smallest positive integer m such that n! + m is prime — equivalently, m is the gap from n! up to the next prime greater than n!. The key insight is that the next prime above a factorial can be found by stepping m upward from 1 and testing n! + m for primality; since factorials grow rapidly, this quickly requires big-integer arithmetic and an efficient primality test (typically Miller-Rabin) for larger n. This sequence is OEIS A033932.

## Task Requirements
- Find and display the first fifty terms of the sequence, i.e. a(n) for 0! through 49!.
- Find and display the position (n) and value (m) of the first m greater than 1000.
- Stretch goal: find and display the position and value of the first m greater than each of 2000, 3000, 4000, ... up to 10,000.

## Language Coverage
20 languages implement this task, spanning systems and low-level languages, scripting languages, and math-oriented tools. Representative implementations include C, Java, Python, Julia, Perl, Raku, Ruby, Nim, Wren, Phix, and Mathematica / Wolfram Language, several of which lean on built-in arbitrary-precision integers and prime utilities.

## Connections
- [[Factorial]] — the base quantity n! whose successor prime is sought
- [[PrimeNumber]] — m is defined by the next prime above n!
- [[PrimalityTest]] — needs an efficient test (e.g. [[MillerRabin]]) for huge n!
- [[ArbitraryPrecisionArithmetic]] — factorials overflow fixed-width integers fast
- [[IntegerSequence]] — corresponds to OEIS A033932

## Contradictions
- None — reference task page.
