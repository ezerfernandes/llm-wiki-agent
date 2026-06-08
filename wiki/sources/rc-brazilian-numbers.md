---
title: "Brazilian numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, radix-representation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Brazilian_numbers
---

## Summary
A Brazilian number is a positive integer N for which there exists at least one base B, with 1 < B < N-1, where N written in base B consists entirely of equal digits (e.g. 7 = 111 in base 2, 8 = 22 in base 3). First presented at the 1994 Iberoamerican Mathematical Olympiad in Fortaleza, Brazil. The key insight is that most composites factor as R(S-1)+R = "RR" in base S-1, so the only non-trivial cases are squares of primes; a Brazilian prime can only use the digit 1, typically appearing as an odd-length string of 1s (a repunit).

## Task Requirements
- Write a routine that determines whether a given number is Brazilian.
- Using that routine, print the first 20 Brazilian numbers.
- Print the first 20 odd Brazilian numbers.
- Print the first 20 prime Brazilian numbers.

## Language Coverage
60 languages implement this task, giving very broad coverage across imperative, functional, and scripting families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Raku, Perl, Ruby, REXX, and Wren.

## Connections
- [[NumberTheory]] — the task is rooted in divisibility and prime structure
- [[RadixRepresentation]] — testing digits of N across multiple bases
- [[Repunit]] — Brazilian primes are repunits (strings of 1s) in some base
- [[PrimalityTesting]] — needed to enumerate prime Brazilian numbers
- [[OEIS]] — sequences A125134, A257521, and A085104

## Contradictions
- None — reference task page.
