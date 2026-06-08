---
title: "Self numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Self_numbers
---

## Summary
A self number (also called a Colombian number) is a positive integer n for which no integer g exists such that g plus the sum of g's decimal digits equals n. For example, 18 is not a self number because 9 + 9 = 18, but a self number has no such "generator." The task asks the programmer to produce these numbers, with the key insight that they are most efficiently found by sieving: marking every n + digitsum(n) as "not self" rather than testing each candidate independently.

## Task Requirements
- Display the first 50 self numbers.
- Confirm or dispute the conjecture that the 100,000,000th self number is 1,022,727,208.
- Extra credit: prove that the Mersenne prime 2^24036583 - 1 is also a self number.

## Language Coverage
33 languages implement this task, spanning systems languages, scripting languages, and functional languages. Representative implementations include C, C++, C#, Go, Java, Python, Haskell, Julia, Perl, Raku, and REXX.

## Connections
- [[NumberTheory]] — self numbers are a classification of integers studied in number theory
- [[DigitSum]] — the defining operation is adding an integer to the sum of its digits
- [[SieveAlgorithm]] — the efficient solution marks generated values rather than testing each candidate
- [[MersennePrime]] — the extra-credit clause concerns 2^24036583 - 1
- [[OEIS]] — catalogued as sequence A003052

## Contradictions
- None — reference task page.
