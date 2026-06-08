---
title: "Numbers divisible by their individual digits, but not by the product of their digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisibility]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numbers_divisible_by_their_individual_digits,_but_not_by_the_product_of_their_digits
---

## Summary
This task asks the programmer to find every positive decimal integer below 1,000 that is evenly divisible by each of its individual digits, yet is NOT divisible by the product of those same digits. The dual condition naturally excludes any number containing a zero digit (division by zero and a zero product), so the search space reduces to numbers whose digits are all nonzero and which satisfy the two opposing divisibility tests simultaneously.

## Task Requirements
- Consider positive integers n where n < 1,000.
- Keep n only if it is divisible by every one of its individual digits.
- Reject n if it is also divisible by the product of its digits.
- Display the resulting list of qualifying numbers.

## Language Coverage
69 languages implement this task, spanning low-level assembly, classic procedural languages, functional languages, and modern scripting. Representative implementations include C, C++, Java, Python, Go, Rust, Haskell, Raku, REXX, and 8086 Assembly.

## Connections
- [[Divisibility]] — the core test applied per-digit and against the digit product
- [[DigitManipulation]] — extracting and iterating over a number's decimal digits
- [[NumberTheory]] — broader domain of integer divisibility properties
- [[BruteForceSearch]] — the straightforward enumeration approach over the bounded range

## Contradictions
- None — reference task page.
