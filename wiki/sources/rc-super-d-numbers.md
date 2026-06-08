---
title: "Super-d numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Super-d_numbers
---

## Summary
A super-d number is a positive integer n such that d × n^d contains at least d consecutive copies of the digit d (for 2 ≤ d ≤ 9). For example, 753 is a super-3 number because 3 × 753^3 = 1280873331, which contains the run "333". The task is to write a routine that finds such numbers, exploiting the fact that the check reduces to searching the decimal string of d × n^d for a run of d repeated d-digits.

## Task Requirements
- Write a function/procedure/routine to find super-d numbers.
- For d = 2 through d = 6, show the first 10 super-d numbers of each.
- Extra credit (optional): show the first 10 super-7, super-8, and/or super-9 numbers.

## Language Coverage
49 languages implement this task, spanning systems and functional languages where the main practical concern is big-integer support for the powers involved. Representative implementations include C, C++, C#, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and REXX.

## Connections
- [[NumberTheory]] — classifies integers by a digit-pattern property of their powers
- [[Exponentiation]] — requires computing n raised to the power d
- [[BigInteger]] — d × n^d quickly exceeds native integer width
- [[StringProcessing]] — detecting a run of d consecutive identical digits
- [[DigitManipulation]] — inspecting the decimal representation of the result

## Contradictions
- None — reference task page.
