---
title: "Count in octal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, radix-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Count_in_octal
---

## Summary
This task asks the programmer to print a sequential count starting at zero, incrementing by one each step, with every value displayed in octal (base 8) on its own line. The count continues until the program is terminated or the numeric type overflows. The key insight is separating the underlying integer increment from the output radix, which most languages expose either through built-in octal formatting or a manual base-8 conversion.

## Task Requirements
- Produce a sequential count beginning at zero.
- Increment by one for each consecutive number.
- Display each number in octal, one value per line.
- Run until terminated by the user or until the numeric type reaches its maximum value.

## Language Coverage
155 languages implement this task, spanning a very broad range from low-level assembly to high-level scripting and esoteric languages. Representative examples include C, Python, Java, Rust, Go, Haskell, Perl, Ruby, COBOL, and Brainf***.

## Connections
- [[RadixConversion]] — converting an integer into base-8 representation
- [[NumberBases]] — octal is a positional base-8 numeral system
- [[Iteration]] — the count is driven by a simple incrementing loop
- [[IntegerOverflow]] — the loop terminates at the numeric type's maximum value

## Contradictions
- None — reference task page.
