---
title: "Narcissistic decimal number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Narcissistic_decimal_number
---

## Summary
A narcissistic (decimal) number is a non-negative integer n that equals the sum of its own digits each raised to the power m, where m is the count of digits in n. For example, 153 has three digits and 1³ + 5³ + 3³ = 153. These are also called Armstrong numbers or Plus Perfect numbers. The task is to generate and display the first 25 such numbers, starting with 0.

## Task Requirements
- Generate and show the first 25 narcissistic decimal numbers.
- Treat 0 as the first in the series (0¹ = 0).
- For each candidate n, split it into decimal digits and check whether the sum of each digit raised to the digit-count power equals n.

## Language Coverage
88 languages implement this task, reflecting very broad coverage across paradigms. Representative implementations include C, C++, Python, Haskell, Java, JavaScript, Rust, Go, Ruby, Perl, and Common Lisp.

## Connections
- [[NumberTheory]] — narcissistic numbers are a classic figurate/digit-property class
- [[DigitManipulation]] — the core operation extracts and processes decimal digits
- [[Exponentiation]] — each digit is raised to the digit-count power
- [[ArmstrongNumbers]] — the alternate name for this number class

## Contradictions
- None — reference task page.
