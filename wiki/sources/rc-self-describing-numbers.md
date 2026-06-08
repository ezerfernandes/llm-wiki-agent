---
title: "Self-describing numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Self-describing_numbers
---

## Summary
A self-describing number is an integer where the digit at each position (labeled 0 to N-1) equals the count of how many times that position's index appears among all the number's digits. For example, 2020 is self-describing: position 0 holds 2 and there are two 0s, position 2 holds 2 and there are two 2s, while positions 1 and 3 hold 0 matching zero occurrences. The key insight is that the number is a fixed-point of its own digit-frequency tally.

## Task Requirements
- Write a function/routine that checks whether a given positive integer is self-describing.
- Optional stretch goal: generate and display the full set of self-describing numbers (e.g., those below 100,000,000: 1210, 2020, 21200, 3211000, 42101000).

## Language Coverage
83 languages implement this task, reflecting broad coverage across paradigms. Representative implementations include Python, C, C++, Java, Haskell, Go, Rust, Ruby, Perl, and Lua.

## Connections
- [[NumberTheory]] — the task studies a self-referential digit property of integers.
- [[DigitManipulation]] — checking the number requires extracting digits and tallying their frequencies.
- [[FixedPoint]] — a self-describing number is a fixed point of the digit-counting transformation.
- [[FrequencyCounting]] — the core algorithm builds a histogram of digit occurrences.

## Contradictions
- None — reference task page.
