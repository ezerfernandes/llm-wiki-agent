---
title: "Non-decimal radices/Convert (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Non-decimal_radices/Convert
---

## Summary
The task asks the programmer to implement two complementary base-conversion functions. The first takes a non-negative integer and a base, returning the string of digits in that base (no leading zeros except for 0 itself), using lowercase letters for digit values above 9 (a = 10, b = 11, and so on). The second takes a digit string and a base and returns the integer it represents. The core insight is repeated division/modulo by the base for encoding and Horner-style positional accumulation for decoding; many languages expose this directly via built-ins.

## Task Requirements
- Write a function passed a non-negative integer and an integer base that returns the digit string for that number in that base.
- Suppress leading zeros, except output "0" for the value zero.
- Use digits 0-9 then lowercase letters a, b, c, ... for values 10 and beyond.
- Example: decimal 26 in base 16 is "1a".
- Write a second function passed a string and an integer base that returns the integer it represents.
- No error handling required for negatives, bases below 2, or invalid digits; word-size limits are acceptable.

## Language Coverage
95 languages implement this task, reflecting how universal base conversion is across both systems and scripting ecosystems. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Common Lisp, Perl, and REXX.

## Connections
- [[RadixConversion]] — the central operation the task implements
- [[PositionalNotation]] — the numeral system underpinning digit strings in arbitrary bases
- [[ModularArithmetic]] — repeated division and remainder drive the integer-to-string direction
- [[HornersMethod]] — positional accumulation drives the string-to-integer direction

## Contradictions
- None — reference task page.
