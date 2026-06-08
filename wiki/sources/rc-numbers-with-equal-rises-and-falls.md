---
title: "Numbers with equal rises and falls (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numbers_with_equal_rises_and_falls
---

## Summary
The task asks for numbers whose decimal digits contain an equal count of "rises" (a digit less than its right neighbor) and "falls" (a digit greater than its right neighbor). For example, 83,548 has 2 rises and 2 falls so it qualifies, while 726,169 (3 rises, 2 falls) does not. The key insight is that single-digit numbers trivially have zero rises and zero falls, so they all belong to the sequence (OEIS A296712).

## Task Requirements
- Print the first 200 numbers in the sequence.
- Demonstrate that the 10,000,000th (10 millionth) number in the sequence is 41,909,002.

## Language Coverage
52 languages implement this task, showing broad coverage across compiled, scripting, functional, and assembly languages. Representative examples include C, C++, Java, Python, Haskell, Go, Rust-adjacent languages, Perl, Raku, REXX, APL, and 8080 Assembly.

## Connections
- [[NumberTheory]] — the sequence is defined by a digit-based property of integers.
- [[DigitManipulation]] — comparing adjacent base-10 digits drives the rise/fall classification.
- [[OEIS]] — the sequence is cataloged as A296712.
- [[EstheticNumbers]] — a related Rosetta Code task also based on relationships between adjacent digits.

## Contradictions
- None — reference task page.
