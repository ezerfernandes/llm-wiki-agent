---
title: "Bell numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bell_numbers
---

## Summary
The task asks the programmer to generate the Bell numbers, where B(n) counts the distinct ways to partition a set of n elements (ignoring the order of elements and of the partitions). The recommended approach is to build the Bell triangle (also called Aitken's array or Peirce triangle): each row begins with the last value of the previous row, and each subsequent entry adds the value to its left and the value diagonally above-left. The first entry of each row yields the Bell number sequence.

## Task Requirements
- Write a routine (function, generator, etc.) that produces the Bell number sequence.
- Display at least the first 15 Bell numbers.
- If the language supports big integers, also display the 50th element.
- If using the Bell triangle method, also show the first ten rows of the triangle.

## Language Coverage
79 languages implement this task, spanning mainstream, functional, array, and legacy/historical languages. Representative examples include Python, C, C++, Java, JavaScript, Haskell, Rust, Go, Julia, Common Lisp, and APL.

## Connections
- [[BellNumber]] — the integer sequence being computed (OEIS A000110)
- [[SetPartition]] — Bell numbers count the partitions of a finite set
- [[BellTriangle]] — Aitken's array used as the generating algorithm
- [[Combinatorics]] — the branch of mathematics this enumeration belongs to
- [[ArbitraryPrecisionArithmetic]] — needed for the 50th element, which overflows fixed-width integers

## Contradictions
- None — reference task page.
