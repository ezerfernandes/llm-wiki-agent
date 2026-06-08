---
title: "Sort three variables (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_three_variables
---

## Summary
The task asks the programmer to sort the values held in exactly three variables (X, Y, Z) into order, where the values may be strings/literals or numbers. The key insight is that with only three elements, idiomatic solutions often skip a general sort: one can collect the values into a 3-element array and sort it, or compute the minimum, maximum, and middle directly (the middle being the sum of all three minus the min and max).

## Task Requirements
- Sort the values of three variables X, Y, and Z; support arbitrary values (strings/literals) if the language allows, otherwise just numbers.
- Note whether numeric sorting handles floating point, integers, or other types, and state any limitations.
- Values may or may not be unique.
- Use the most idiomatic approach in the language; more than one algorithm may be shown.
- Demonstrate with the given string example and the numeric example (77444, -12, 0).

## Language Coverage
88 languages implement this task, spanning systems and scripting languages, functional languages, and low-level assembly. Representative entries include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, Perl, Raku, Fortran, COBOL, Prolog, and assembly targets like 8086 Assembly and Little Man Computer.

## Connections
- [[SortingAlgorithm]] — the task is a member of the sorting algorithm category.
- [[ArraySorting]] — the canonical solution stores the three values in an array and sorts it.
- [[MinMaxMedian]] — the numeric shortcut derives min, max, and the middle value arithmetically.
- [[Comparison]] — sorting strings vs numbers depends on the language's ordering/comparison semantics.

## Contradictions
- None — reference task page.
