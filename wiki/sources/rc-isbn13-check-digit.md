---
title: "ISBN13 check digit (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksum, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/ISBN13_check_digit
---

## Summary
The task asks the programmer to validate the check digit of a 13-digit ISBN code. The key insight is a simple weighted modular checksum: digits in alternating positions are weighted by 1 and 3, summed, and the total must be divisible by 10 for the ISBN to be valid. This same weighting scheme underlies the EAN-13 barcode standard.

## Task Requirements
- Multiply every other digit by 3.
- Add these weighted numbers together with the remaining (weight-1) digits.
- Take the remainder of the total after division by 10.
- If the remainder is 0, the ISBN-13 check digit is correct; otherwise it is invalid.
- Handle/ignore separators such as hyphens, and validate the provided test codes (e.g. 978-0596528126 good, 978-0596528120 bad).

## Language Coverage
93 languages implement this task, showing broad reach across systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Perl, Raku, COBOL, and several assembly dialects (8080/8086 Assembly).

## Connections
- [[Checksum]] — the validation is a checksum verification
- [[ModularArithmetic]] — relies on the remainder after division by 10
- [[WeightedSum]] — alternating digit weights of 1 and 3
- [[StringProcessing]] — parsing and stripping the ISBN string before computation

## Contradictions
- None — reference task page.
