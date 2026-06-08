---
title: "Colorful numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Colorful_numbers
---

## Summary
A colorful number is a non-negative base-10 integer in which the product of every contiguous subgroup of its digits is distinct. The task is to write a routine that tests whether a number is colorful, then use it to enumerate all colorful numbers below 100 and to find the largest one. The key insight is a tight bound: any colorful number above 9 cannot repeat a digit and cannot contain 0 or 1, so no colorful number can exceed 8 digits.

## Task Requirements
- Write a routine that tests whether a given number is a colorful number.
- Use it to find all colorful numbers less than 100.
- Use it to find the largest possible colorful number.
- Stretch: count colorful numbers per order of magnitude.
- Stretch: report the total count of all colorful numbers.

## Language Coverage
37 languages implement this task, spanning systems languages, functional languages, array languages, and scripting languages. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, and J.

## Connections
- [[NumberTheory]] — framed (humorously) as a recreational number-theory puzzle.
- [[Combinatorics]] — enumerating contiguous digit subgroups and their products.
- [[BruteForceSearch]] — the bounded digit space (no 0/1, no repeats, max 8 digits) makes exhaustive search tractable.
- [[DigitManipulation]] — decomposing integers into digits to compute subgroup products.

## Contradictions
- None — reference task page.
