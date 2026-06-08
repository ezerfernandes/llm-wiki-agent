---
title: "Upside-down numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Upside-down_numbers
---

## Summary
An upside-down number is a positive base-10 integer whose i-th digit from the left and i-th digit from the right are complements that sum to 10 (e.g., 7165493: 7+3, 1+9, 6+4, 5+5). The key insight is structural: such a number can contain no zeros, and any odd-length number must have a center digit of exactly 5, which makes the integers easy to generate by pairing complementary digits rather than testing every candidate.

## Task Requirements
- Write a routine to find or generate upside-down numbers.
- Find and show the first 50 upside-down numbers.
- Find and show the five hundredth (500th) upside-down number.
- Find and show the five thousandth (5000th) upside-down number.
- Stretch: find and show the fifty thousandth, five hundred thousandth, and five millionth upside-down numbers.

## Language Coverage
30 languages implement this task, spanning systems, functional, scripting, and array-oriented styles. Representative implementations include Ada, ALGOL 68, C++, Go, Haskell, Java, Julia, Perl, Python, Raku, Rust, and Wren.

## Connections
- [[NumberTheory]] — the task is a property defined over base-10 digit positions.
- [[DigitManipulation]] — solving it requires extracting and complementing individual digits.
- [[CombinatorialGeneration]] — efficient solutions enumerate numbers by pairing complementary digit choices rather than brute-force filtering.
- [[IntegerSequences]] — corresponds to OEIS sequence A299539.

## Contradictions
- None — reference task page.
