---
title: "Untouchable numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Untouchable_numbers
---

## Summary
An untouchable (or nonaliquot) number is a positive integer that cannot be expressed as the aliquot sum — the sum of all proper divisors — of any positive integer. The task asks the programmer to find every untouchable number up to 2,000 and to count how many exist below successive powers of ten. The key implementation insight is that detecting whether a value n is "touched" requires sieving aliquot sums over a sufficiently large range above n (commonly up to roughly 2n or more) so that no generating number is missed.

## Task Requirements
- Show, in a grid format, all untouchable numbers ≤ 2,000.
- Show the count of untouchable numbers ≤ 2,000.
- Show the cumulative count of untouchable numbers from 1 up to 10, 100, 1,000, 10,000, 100,000 (or as high as is practical).
- Display all output on the page.

## Language Coverage
19 languages implement this task, spanning systems languages, functional languages, and array/CAS environments. Representative implementations include C, C++, Go, Java, Python, Julia, Perl, Raku, REXX, F#, Nim, Phix, J, and Mathematica/Wolfram Language.

## Connections
- [[NumberTheory]] — the task is grounded in divisor-based integer properties
- [[AliquotSum]] — untouchable numbers are precisely those outside the image of this function
- [[ProperDivisors]] — the building block summed to test each candidate
- [[SieveOfEratosthenes]] — efficient solutions sieve aliquot sums over a range, analogous to prime sieving
- [[GoldbachsConjecture]] — whether 5 is the only odd untouchable number follows from a strengthened form of it

## Contradictions
- None — reference task page.
