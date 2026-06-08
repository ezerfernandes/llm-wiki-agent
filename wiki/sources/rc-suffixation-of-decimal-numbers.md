---
title: "Suffixation of decimal numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-formatting, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Suffixation_of_decimal_numbers
---

## Summary
The task is to write a function that appends a metric or "binary" metric suffix to a decimal number, compressing large magnitudes into a short human-readable form (e.g. 456,789,100,000,000 becomes 456.7891T). The key insight is to divide the input by the largest applicable power (10^3n for metric, 2^10n for binary) and attach the matching suffix letter, optionally rounding to a requested number of fractional digits while preserving the sign.

## Task Requirements
- Add (if possible) a metric or binary suffix to a number, with an optional count of decimal digits past the point (with rounding); default shows all significant digits.
- Preserve the sign if present; strip optional commas; accept decimal points and exponents (e.g. -123.7e-01).
- Emit the suffix in uppercase, but the binary 'i' marker in lowercase.
- Support metric suffixes K M G T P E Z Y X W V U (10^3 through 10^36) and binary suffixes Ki Mi Gi Ti Pi Ei Zi Yi Xi Wi Vi Ui (2^10 through 2^120); optionally the full name "googol" (1e100).
- Argument validation is optional but recommended; display the original number, digit count, suffix type, and the converted result with identifying text for a fixed set of test cases.

## Language Coverage
19 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative entries include C#, Go, Java, Julia, Nim, Perl, Python, Raku, Rust, REXX, Wren, and Mathematica/Wolfram Language.

## Connections
- [[NumberFormatting]] — converting raw magnitudes into suffixed human-readable strings
- [[StringProcessing]] — parsing signs, commas, decimal points, and exponents from the input
- [[Rounding]] — shortening to a specified number of fractional digits
- [[SiPrefixes]] — the underlying metric and binary (IEC) prefix system

## Contradictions
- None — reference task page.
