---
title: "Increment a numerical string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, type-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Increment_a_numerical_string
---

## Summary
This task asks the programmer to take a string that represents a number and produce a string representing that number plus one. The core insight is the round-trip between text and numeric types: a numerical string must be parsed into an integer, incremented, and converted back to a string. It highlights how different languages treat the boundary between string and numeric representations, and whether their numeric types overflow at fixed widths or grow arbitrarily large.

## Task Requirements
- Take a numerical string as input (a string whose characters represent a number).
- Increment the value it represents by one.
- Produce the result as a numerical string (not a raw integer).

## Language Coverage
217 languages implement this task, making it one of the most broadly covered text-processing exercises on Rosetta Code, spanning everything from assembly to high-level scripting languages. Representative implementations include C, Python, Java, JavaScript, Haskell, Ruby, Rust, Go, Perl, and REXX.

## Connections
- [[StringProcessing]] — the input and output are both strings rather than native numbers.
- [[TypeConversion]] — the task hinges on parsing a string to a number and formatting it back.
- [[ArbitraryPrecisionArithmetic]] — languages with bignums avoid overflow when incrementing very large numerical strings.
- [[IntegerOverflow]] — fixed-width numeric types may wrap or fail on large inputs.

## Contradictions
- None — reference task page.
