---
title: "Cyclops numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cyclops_numbers
---

## Summary
A cyclops number is a base-10 number with an odd number of digits that has a single zero in the exact center and no other zeros anywhere. The task asks the programmer to generate several related sequences, exploiting the fact that valid cyclops numbers always have an odd digit count with the middle position fixed to zero.

## Task Requirements
- Find and display the first 50 cyclops numbers in base 10.
- Find and display the first 50 prime cyclops numbers (cyclops numbers that are prime).
- Find and display the first 50 blind prime cyclops numbers (prime cyclops numbers that stay prime when the central zero is removed, i.e. "blinded").
- Find and display the first 50 palindromic prime cyclops numbers (prime cyclops numbers that are palindromes).
- Stretch: for each of the four variants, find the first one greater than ten million and report its index (place) in the series.

## Language Coverage
40 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C++, C#, Go, Rust, Haskell, F#, Java, JavaScript, Python, Perl, Raku, Julia, Nim, and REXX.

## Connections
- [[PrimeNumbers]] — three of the four variants require primality testing
- [[NumberTheory]] — classification of integers by digit structure
- [[PalindromicNumbers]] — the palindromic prime cyclops variant
- [[DigitManipulation]] — examining and removing center digits in base 10

## Contradictions
- None — reference task page.
