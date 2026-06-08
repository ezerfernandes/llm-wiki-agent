---
title: "Esthetic numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Esthetic_numbers
---

## Summary
An esthetic number (also called a stepping number) is a positive integer in which every adjacent pair of digits differs by exactly 1. The task asks for a routine that finds such numbers in any base, since the concept generalizes beyond base 10. The key insight is that esthetic numbers can be generated efficiently by a breadth- or depth-first walk: starting from each nonzero leading digit, append only digits that are ±1 from the current last digit, avoiding the cost of testing every integer.

## Task Requirements
- Write a routine to find esthetic numbers in a given base.
- For bases 2 through 16, display the esthetic numbers from index (base × 4) through index (base × 6), inclusive.
- Find and display the base-10 esthetic numbers with magnitude between 1000 and 9999.
- Stretch goal: find and display the base-10 esthetic numbers with magnitude between 1.0e8 and 1.3e8.
- Exclude zero; do not include numbers with leading zeros.

## Language Coverage
44 languages implement this task, giving broad coverage across systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, J, and REXX.

## Connections
- [[NumberTheory]] — the task concerns a digit-defined integer sequence (OEIS A033075).
- [[DigitManipulation]] — esthetic-ness is a property of adjacent base-b digits.
- [[RadixRepresentation]] — the definition generalizes across numeric bases 2–16.
- [[BreadthFirstSearch]] — efficient generation builds candidates by appending ±1 digits, a tree/graph traversal.

## Contradictions
- None — reference task page.
