---
title: "Two identical strings (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, binary]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Two_identical_strings
---

## Summary
Find and display all positive integers n below 1,000 whose base-2 representation is the concatenation of two identical binary strings (e.g. a value whose binary form looks like XX for some bit string X). For each qualifying integer, the decimal and binary forms must be shown. The key insight is that such numbers have an even number of binary digits, where the top half equals the bottom half — equivalently n = m·(2^k + 1) where the high half is an k-bit value m with its leading bit set.

## Task Requirements
- Consider positive integers n with n < 1,000 (decimal).
- A number qualifies if its base-2 representation is exactly two copies of the same binary string concatenated.
- For each qualifying n, display both its decimal value and its binary representation.

## Language Coverage
81 languages implement this task, showing very broad coverage spanning assembly, classic, and modern languages. Representative implementations include C, C++, Java, Python, Rust, Go, Haskell, Ruby, Perl, APL, COBOL, and Fortran.

## Connections
- [[BinaryRepresentation]] — the task is defined purely over base-2 digit strings
- [[StringProcessing]] — detecting a string that is its own first-half repeated
- [[NumberTheory]] — qualifying values factor as m·(2^k + 1)
- [[BitManipulation]] — checking the high and low halves of a fixed-width bit pattern

## Contradictions
- None — reference task page.
