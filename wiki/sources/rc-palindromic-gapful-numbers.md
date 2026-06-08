---
title: "Palindromic gapful numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, palindromes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Palindromic_gapful_numbers
---

## Summary
The task asks the programmer to find numbers that are simultaneously palindromic (reading the same forwards and backwards in base ten) and gapful. A gapful number (>= 100) is one that is evenly divisible by the two-digit number formed by concatenating its first and last decimal digits. The key insight noted on the page is that every palindromic gapful number is divisible by eleven, since a palindrome begins and ends with the same digit, making the divisor a multiple of 11.

## Task Requirements
- Consider only numbers >= 100 (all one- and two-digit numbers are trivially gapful).
- A number is gapful if it is evenly divisible (no remainder) by the integer formed from its first digit followed by its last digit.
- For each ending digit 1 through 9 (nine sets), show the first 20 palindromic gapful numbers ending in that digit.
- For each ending digit 1 through 9, show the last 15 palindromic gapful numbers out of the first 100 found.
- Optionally, for each ending digit, show the last 10 out of the first 1,000 found.

## Language Coverage
36 languages implement this task, giving broad coverage across systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and REXX.

## Connections
- [[PalindromeDetection]] — testing whether a number reads the same reversed
- [[NumberTheory]] — divisibility and digit-based number properties
- [[DivisibilityRules]] — the divisibility-by-eleven property of these numbers
- [[GapfulNumbers]] — the base property this task specializes
- [[DigitManipulation]] — extracting first and last digits to form the divisor

## Contradictions
- None — reference task page.
