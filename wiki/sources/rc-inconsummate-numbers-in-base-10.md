---
title: "Inconsummate numbers in base 10 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Inconsummate_numbers_in_base_10
---

## Summary
A consummate number is a non-negative integer expressible as N divided by the digital sum of N (e.g. 47 = 846 / (8+4+6)). An inconsummate number is one that can never arise from any such integer ratio; 62 is the smallest example. The task asks the programmer to detect inconsummate numbers in base 10. The key insight is that for a candidate value k, any N producing it satisfies N = k * digitsum(N), and since digit sums grow much slower than N, only a bounded range of multipliers needs checking.

## Task Requirements
- Write a routine to find inconsummate numbers in base 10.
- Use it to find and display the first fifty inconsummate numbers.
- Stretch goal: find and display the one-thousandth inconsummate number.

## Language Coverage
30 languages implement this task, spanning systems, scripting, array, and functional styles. Representative implementations include C++, Java, Python, Perl, Raku, Julia, Nim, APL, J, REXX, Wren, and Phix.

## Connections
- [[NumberTheory]] — the problem is a classic recreational number-theory characterization.
- [[DigitSum]] — the defining operation is dividing a number by the sum of its digits.
- [[OEIS]] — the sequence is cataloged as OEIS A003635.
- [[BruteForceSearch]] — solutions typically test candidates over a bounded multiplier range.

## Contradictions
- None — reference task page.
