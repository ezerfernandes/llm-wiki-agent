---
title: "Roman numerals/Encode (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-systems, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Roman_numerals/Encode
---

## Summary
The task asks for a function that takes a positive integer and returns its representation as a modern Roman numeral string. Each decimal digit is encoded separately from the most significant down, with zero digits skipped. The key insight is using a value-to-symbol mapping that includes the subtractive forms (e.g. 900=CM, 90=XC, 4=IV) so a simple greedy descending subtraction produces correct results.

## Task Requirements
- Accept a positive integer as the parameter.
- Return a string containing its Roman numeral representation.
- Express each digit separately, starting from the leftmost (most significant), skipping any digit with value zero.
- Handle subtractive notation correctly (e.g. 1990 → MCMXC, 2008 → MMVIII, 1666 → MDCLXVI).

## Language Coverage
152 languages implement this task, reflecting its popularity as a beginner-friendly number-formatting exercise. Representative implementations include Python, C, C++, Java, JavaScript, Haskell, Ruby, Rust, Go, and Perl.

## Connections
- [[RomanNumerals]] — the numeral system being encoded
- [[GreedyAlgorithm]] — repeated subtraction of the largest applicable value
- [[NumberFormatting]] — converting integer values to a positional string representation
- [[StringManipulation]] — building the output string from symbol fragments

## Contradictions
- None — reference task page.
