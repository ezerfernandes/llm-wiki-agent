---
title: "Sub-unit squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sub-unit_squares
---

## Summary
A sub-unit square is a perfect square that remains a perfect square after subtracting 1 from each of its decimal digits. The task is to find and display at least the first five such numbers. A key insight is that a sub-unit square can contain no zero digit (since 0 - 1 would go negative), and every known example apart from 1 ends in the digits "36".

## Task Requirements
- Identify squares that, after decrementing every digit by 1, still form a perfect square.
- Recognize the degenerate case 1 (1 - 1 = 0, also a square) and the worked example 3136 (56²) decrementing to 2025 (45²).
- Find and display at least the first five sub-unit squares.

## Language Coverage
34 languages implement this task, spanning systems, functional, scripting, and array-oriented styles. Representative examples include C++, Rust, Java, Haskell, F#, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[PerfectSquare]] — the core property being tested before and after digit decrement
- [[DigitManipulation]] — subtracting one from each decimal digit of a number
- [[NumberTheory]] — the underlying domain of square-number sequences
- [[OEIS]] — sequence A061844 catalogs these numbers
- [[BruteForceSearch]] — typical approach of iterating squares and testing the condition

## Contradictions
- None — reference task page.
