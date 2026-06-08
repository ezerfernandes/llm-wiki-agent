---
title: "Kaprekar numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kaprekar_numbers
---

## Summary
The task is to identify Kaprekar numbers: positive integers whose square can be split once into two parts (positive integers) that sum back to the original number. For example, 2223² = 4941729 splits into 494 and 1729, which sum to 2223. The key insight is that checking a candidate reduces to taking its square's decimal digits and trying every left-to-right split point, treating each part as an integer.

## Task Requirements
- Generate and display all Kaprekar numbers less than 10,000.
- A valid split must produce two positive integers; a part consisting entirely of zeros is invalid since 0 is not positive (1 is treated as a special-case Kaprekar number).
- Extra credit: count how many Kaprekar numbers are less than 1,000,000.
- Extra extra credit: find Kaprekar numbers in base 17 between 1 and 1,000,000, displaying each in base 10 (and optionally base 17 with its square and split point).

## Language Coverage
91 languages implement this task, spanning systems, scripting, functional, and assembly families. Representative examples include C, C++, Java, Python, Haskell, Perl, Raku, Go, Rust-adjacent V (Vlang), REXX, and 360 Assembly.

## Connections
- [[NumberTheory]] — Kaprekar numbers are a studied integer sequence
- [[IntegerSquaring]] — each candidate's square is the object under test
- [[PositionalNotation]] — splitting the square depends on its digit representation, generalized to other bases
- [[StringProcessing]] — the split-and-parse approach treats the square as a digit string
- [[OEIS]] — the sequence is catalogued as A006886

## Contradictions
- None — reference task page.
