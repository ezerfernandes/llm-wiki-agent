---
title: "Number names (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Number_names
---

## Summary
This task asks the programmer to spell out an integer in English words — for example, turning 1234 into "one thousand two hundred thirty-four". Implementations must handle inputs at least up to one million (or the language's maximum bounded integer). The key insight is decomposing the number into groups of three digits and mapping each group to ones/tens/hundreds words combined with scale names (thousand, million, billion).

## Task Requirements
- Show how to spell out a number in English.
- Support inputs up to at least one million, or the language's maximum default bounded integer if smaller.
- May use a preexisting implementation or write one from scratch.
- Support for zero, negative integers, and floating-point numbers is optional.

## Language Coverage
100 languages implement this task, reflecting very broad coverage across paradigms — including C, C++, C#, Java, Python, Haskell, Perl, Ruby, Go, Rust, Common Lisp, and Prolog.

## Connections
- [[StringProcessing]] — building the English word output from digit groups
- [[PositionalNumeralSystem]] — grouping digits into thousands/millions scales
- [[Recursion]] — recursive decomposition of number groups in many solutions
- [[LookupTable]] — mapping digit values to their word forms

## Contradictions
- None — reference task page.
