---
title: "Vampire number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Vampire_number
---

## Summary
A vampire number is a natural decimal number with an even number of digits that factors into two integers called "fangs". Each fang must have exactly half the digits of the original, the two fangs together must use precisely the same multiset of digits as the original number, and at most one fang may have a trailing zero. The defining example is 1260 = 21 x 60. A single number can have more than one valid pair of fangs.

## Task Requirements
- Print the first 25 vampire numbers together with their fangs.
- Test whether 16758243290880, 24959017348650, and 14593825548650 are vampire numbers and, if so, print them with their fangs.
- Account for the fact that a vampire number may have multiple distinct fang pairs.

## Language Coverage
49 languages implement this task, showing broad coverage from systems and functional languages to scripting and BASIC dialects. Representative implementations include C, C++, C#, Rust, Go, Haskell, Java, Julia, Python, Perl, Raku, Ruby, REXX, and Wren.

## Connections
- [[NumberTheory]] — the task belongs to recreational number theory
- [[IntegerFactorization]] — fangs are found by enumerating factor pairs
- [[DigitManipulation]] — comparing the digit multiset of a number against its fangs
- [[CombinatorialEnumeration]] — searching candidate fang pairs and rejecting invalid trailing-zero cases

## Contradictions
- None — reference task page.
