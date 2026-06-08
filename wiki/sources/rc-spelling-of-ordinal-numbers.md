---
title: "Spelling of ordinal numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Spelling_of_ordinal_numbers
---

## Summary
This task asks the programmer to write a routine that converts a positive integer into its English-spelled ordinal form (e.g. 1 → "first", 100 → "one hundredth", 1000000000 → "one billionth"). The key insight is that ordinal spelling is mostly the cardinal-number spelling with the final word given an ordinal suffix or substituted by an irregular form ("one" → "first", "two" → "second", "twenty" → "twentieth"). The short-scale numbering system is mandated (2,000,000,000 is "two billion", not "two milliard").

## Task Requirements
- Write a driver plus a function that returns the English-spelled ordinal version of a specified positive integer.
- Use the short-scale numbering system.
- Optionally accept multiple numeric forms of the same integer (e.g. `123`, `00123.0`, `1.23e2`).
- Handle the test cases: 1, 2, 3, 4, 5, 11, 65, 100, 101, 272, 23456, 8007006005004003.
- Show all output.

## Language Coverage
38 languages implement this task, showing broad coverage across functional, imperative, and scripting paradigms. Representative implementations include Python, Java, C, C++, C#, Go, Rust, Haskell, Common Lisp, Perl, Raku, and REXX.

## Connections
- [[NumberNames]] — ordinal spelling builds directly on spelling cardinal numbers in English.
- [[StringProcessing]] — assembling and suffixing spelled-out word fragments.
- [[ShortScale]] — the mandated naming convention for large numbers (billion, trillion, ...).
- [[NumberToWords]] — the general technique of mapping integers to natural-language text.

## Contradictions
- None — reference task page.
