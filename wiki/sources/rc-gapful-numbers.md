---
title: "Gapful numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gapful_numbers
---

## Summary
A gapful number is a positive integer (≥ 100, in base ten) that is evenly divisible by the two-digit number formed from its own first and last digits. For example, 187 is gapful because it is divisible by 17 (its leading and trailing digits). The task asks the programmer to generate and display several runs of these numbers. The key insight is that the divisor is built purely from the integer's first and last decimal digits, so the test reduces to digit extraction plus a modulo check.

## Task Requirements
- Consider only numbers ≥ 100 (all one- and two-digit numbers trivially qualify and are excluded).
- A number is gapful if it is evenly divisible (no remainder) by the value `firstDigit * 10 + lastDigit`.
- Show each requested set on one line, horizontally, with a title.
- Show the first 30 gapful numbers.
- Show the first 15 gapful numbers ≥ 1,000,000.
- Show the first 10 gapful numbers ≥ 1,000,000,000.

## Language Coverage
78 languages implement this task, reflecting very broad coverage typical of simple number-theory exercises. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Go, Rust-era systems languages, Perl, Raku, Ruby, and REXX.

## Connections
- [[NumberTheory]] — gapful numbers are a named integer sequence (OEIS A108343)
- [[DigitManipulation]] — extracting the first and last decimal digits
- [[Divisibility]] — the core test is an evenly-divisible (modulo zero) check
- [[IntegerSequences]] — task generates ordered runs of qualifying integers

## Contradictions
- None — reference task page.
