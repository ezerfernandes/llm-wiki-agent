---
title: "N'th (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/N'th
---

## Summary
This task asks the programmer to write a routine that, given a non-negative integer, returns the number followed by its English ordinal suffix (e.g. `1st`, `2nd`, `3rd`, `11th`). The key insight is the special-casing of the teens: numbers ending in 11, 12, and 13 always take the `th` suffix despite ending in 1, 2, or 3, so the suffix must be chosen from the last two digits rather than just the last digit.

## Task Requirements
- Implement a function that maps an integer ≥ 0 to its ordinal string representation.
- Correctly select the suffix `st`, `nd`, `rd`, or `th` based on the final digit(s), handling the 11/12/13 exception.
- Demonstrate output for at least the ranges 0..25, 250..265, and 1000..1025.
- The apostrophe shown in early examples (`1'st`) is optional, allowing standard apostrophe-less English.

## Language Coverage
116 languages implement this task, spanning a very broad range from assembly and esoteric languages to mainstream and functional ones. Representative implementations include C, Python, Java, JavaScript, Haskell, Rust, Go, Perl, Ruby, and Common Lisp.

## Connections
- [[StringProcessing]] — building the output by concatenating digits with a suffix
- [[OrdinalNumbers]] — the linguistic concept the task encodes
- [[ModularArithmetic]] — suffix selection via remainders modulo 10 and 100
- [[ConditionalLogic]] — branching on the teens exception

## Contradictions
- None — reference task page.
