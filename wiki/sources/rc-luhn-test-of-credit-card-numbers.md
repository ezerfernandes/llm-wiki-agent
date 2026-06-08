---
title: "Luhn test of credit card numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksum, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers
---

## Summary
The task asks the programmer to implement the Luhn algorithm, a checksum formula used by some credit card companies to distinguish valid card numbers from random digit sequences. The core insight is a weighted modulo-10 sum: starting from the rightmost digit, alternating digits are doubled (with digit-sums taken when a doubled value exceeds nine), and a number is valid only if the grand total is divisible by ten.

## Task Requirements
- Reverse the order of the digits in the number.
- Sum the digits in odd positions of the reversed number to form partial sum s1.
- For digits in even positions of the reversed number: multiply each by two, take the digit-sum if the result exceeds nine, then sum these to form s2.
- The number is valid if s1 + s2 ends in zero (is divisible by ten).
- Write a reusable function/method and use it to validate the test inputs 49927398716, 49927398717, 1234567812345678, and 1234567812345670.

## Language Coverage
169 languages implement this task, reflecting very broad coverage typical of a fundamental checksum exercise. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Ruby, Perl, and Common Lisp.

## Connections
- [[LuhnAlgorithm]] — the named checksum technique this task implements
- [[Checksum]] — the general category of validation algorithms
- [[ModularArithmetic]] — validity hinges on divisibility by ten (mod 10)
- [[DigitManipulation]] — relies on digit reversal, doubling, and digit-sum operations

## Contradictions
- None — reference task page.
