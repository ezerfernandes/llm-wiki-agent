---
title: "Roman numerals/Decode (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Roman_numerals/Decode
---

## Summary
The task asks the programmer to write a function that accepts a Roman numeral string and returns its value as a decimal integer. Validation of the input form is not required. The key insight is the subtractive principle: each symbol's value is added unless a smaller symbol precedes a larger one (e.g. IV, CM), in which case the smaller value is subtracted.

## Task Requirements
- Implement a function taking a Roman numeral as its argument and returning the equivalent decimal integer.
- No need to validate the form of the supplied Roman numeral.
- Correctly handle subtractive notation such as MCMXC (1990) and MMVIII (2008), and additive forms like MDCLXVI (1666).

## Language Coverage
128 languages implement this task, spanning a very broad cross-section from assembly and systems languages to high-level and functional ones. Representative examples include C, C++, C#, Java, Python, Haskell, Rust, Go, Ruby, Perl, Common Lisp, and APL.

## Connections
- [[RomanNumerals]] — the numeral system being decoded.
- [[StringProcessing]] — parsing the symbol sequence character by character.
- [[SubtractiveNotation]] — the rule that governs IV, IX, XC, CM, etc.
- [[LookupTable]] — common implementation mapping each symbol to its value.

## Contradictions
- None — reference task page.
