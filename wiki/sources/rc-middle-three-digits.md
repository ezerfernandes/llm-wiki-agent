---
title: "Middle three digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Middle_three_digits
---

## Summary
Write a function that takes an integer and returns its middle three digits, or a clear error indication when that is impossible. The key insight is that "middle three" is only defined when the number of digits (ignoring the sign) is odd and at least three; the sign must be stripped first, and the original order of the extracted digits must be preserved.

## Task Requirements
- Accept an integer value and return its middle three digits.
- Preserve the order of the middle digits.
- Return a clear error indication when the operation is not possible (too few digits, or an even digit count with no well-defined middle).
- Ignore the sign of the number when counting/extracting digits.
- Test with the valid set (123, 12345, 1234567, 987654321, 10001, -10001, -123, -100, 100, -12345) and the error set (1, 2, -1, -10, 2002, -2002, 0), showing output on the page.

## Language Coverage
119 languages implement this task, giving very broad coverage across imperative, functional, and scripting families. Representative implementations include C, C++, Java, Python, Haskell, Go, Rust, Ruby, Perl, Raku, JavaScript, and REXX.

## Connections
- [[StringProcessing]] — most solutions stringify the absolute value and slice the central three characters.
- [[IntegerArithmetic]] — alternative approaches use division and modulo to isolate middle digits without string conversion.
- [[InputValidation]] — the task centers on detecting and signaling the error cases (even or fewer-than-three digit counts).
- [[NumberTheory]] — reasoning about digit counts via base-10 magnitude (logarithms / powers of ten).

## Contradictions
- None — reference task page.
