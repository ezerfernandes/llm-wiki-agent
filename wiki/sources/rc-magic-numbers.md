---
title: "Magic numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magic_numbers
---

## Summary
"Magic numbers" are base-10 polydivisible numbers: an m-digit number whose first n digits form a value divisible by n for every n from 1 to m. For example, 1868587 qualifies because 1÷1, 18÷2, 186÷3, ... 1868587÷7 are all exact. The key insight is that the set is finite — extending a polydivisible prefix becomes impossible past a point — so the count can be found by digit-by-digit breadth-first growth rather than brute-force scanning.

## Task Requirements
- Write a routine to find magic numbers.
- Find and display how many magic numbers exist in total.
- Find and display the largest possible magic number.
- Count and display how many magic numbers have 1 digit, 2 digits, 3 digits, etc.
- Find and display all magic numbers that are minimally pandigital across digits 1 through 9 (each digit exactly once).
- Find and display all magic numbers that are minimally pandigital across digits 0 through 9.
- Treat zero (0) as an included magic number for this task.

## Language Coverage
19 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C++, Rust, Java, Python, Julia, Nim, Perl, Raku, F#, J, and Wren.

## Connections
- [[PolydivisibleNumbers]] — the formal name for the property defining magic numbers
- [[NumberTheory]] — divisibility constraints over digit prefixes
- [[PandigitalNumbers]] — the 1-through-9 and 0-through-9 subtasks
- [[BreadthFirstSearch]] — efficient generation by extending valid prefixes one digit at a time

## Contradictions
- None — reference task page.
