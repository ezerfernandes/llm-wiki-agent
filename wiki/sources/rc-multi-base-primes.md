---
title: "Multi-base primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, radix-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multi-base_primes
---

## Summary
A number stays prime regardless of the base it is written in, but its digit-string representation changes from base to base, so distinct primes can share an identical string in different bases (for example 107 in base 6, 173 in base 8, and 353 in base 12 all render as "255"). The task asks the programmer to find, for each string length, which digit-string is produced by a prime in the greatest number of bases. The key insight is to treat a candidate string as fixed and check, across bases 2 through 36, whether interpreting that string in each base yields a prime.

## Task Requirements
- Restrict the bases considered to 2 through 36.
- For each candidate digit-string, count how many of those bases interpret the string as a prime number.
- Separately for 1-, 2-, 3-, and 4-character strings, report the string(s) achieving the maximum base count, along with that count and the enumerated list of qualifying bases.
- (Stretch goal) Do the same for the maximum 5-character string.

## Language Coverage
19 languages implement this task, a moderate cross-section of systems, scripting, functional, and array languages, including C++, Go, Rust, Java, Python, Perl, Raku, Julia, Nim, and Wren.

## Connections
- [[PrimeNumbers]] — every candidate value must be tested for primality
- [[RadixConversion]] — strings are reinterpreted across bases 2–36
- [[PrimalityTest]] — the inner check applied to each base's interpretation
- [[NumberTheory]] — the underlying domain of the problem

## Contradictions
- None — reference task page.
