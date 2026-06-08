---
title: "Numerical and alphabetical suffixes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numerical_and_alphabetical_suffixes
---

## Summary
This task asks the programmer to parse and "expand" decimal numbers that carry one or more abutted suffix multipliers, then print the resulting value. A number may have an optional sign, comma-grouped digits, a decimal point, and an `E`/`e` exponent, followed by suffixes that scale it. The key insight is that suffixes are heterogeneous and stackable: named alphabetic words, SI metric prefixes (powers of ten), binary prefixes (powers of two), and factorial bangs can all combine on one number.

## Task Requirements
- Parse decimal numbers of the form `{±}{digits}{.}{digits}` optionally with an `E`/`e` exponent, allowing commas as thousands separators.
- Support abbreviated alphabetic multipliers: PAIRs (×2), SCOres (×20), DOZens (×12), GRoss (×144), GREATGRoss (×1728), GOOGOLs (×10^100), including plurals and minimum abbreviations.
- Support metric suffixes K..U (10^3 through 10^36) and binary suffixes Ki..Ui (2^10 through 2^120), case-insensitive, stackable, and intermixable.
- Support an unlimited run of `!` symbols as a multifactorial (single, double, triple, etc.).
- Process the given test-case lists, echoing each input line as-is, then printing the expanded outputs separated by two blanks with commas inserted where appropriate.

## Language Coverage
15 languages implement this task, a moderate set spanning systems, scripting, and niche languages. Representative implementations include Go, Rust, Java, Python, Perl, Raku, Julia, Nim, Factor, Phix, REXX, and Wren.

## Connections
- [[StringParsing]] — tokenizing the numeric mantissa, exponent, and suffix run
- [[Multifactorial]] — the `!`-count multifactorial multiplier
- [[Factorial]] — base case of the factorial suffix family
- [[ArbitraryPrecisionArithmetic]] — needed since GOOGOL and stacked suffixes overflow native numeric types
- [[SIPrefix]] — metric and binary (kibi/mebi) prefix scaling

## Contradictions
- None — reference task page.
