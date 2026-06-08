---
title: "Look-and-say sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, integer-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Look-and-say_sequence
---

## Summary
The look-and-say sequence (also called the Morris Number Sequence, after cryptographer Robert Morris) is a recursively defined sequence studied by John Conway: each term is produced by "reading aloud" the previous term, grouping consecutive runs of identical digits and emitting each run as a count followed by the digit. Starting from 1, the sequence runs 1, 11, 21, 1211, 111221, ... (OEIS A005150). The key insight is that the task is essentially run-length encoding applied to the decimal digits of a number.

## Task Requirements
- Take a decimal number as the current term of the sequence.
- Look at the number, visually grouping consecutive runs of the same digit.
- Say the number left to right, group by group, as "how many of that digit there are" followed by the digit itself; this string becomes the next term.
- Write a program to generate successive members of the sequence.

## Language Coverage
138 languages implement this task, reflecting very broad coverage across paradigms thanks to its simple run-length-encoding core. Representative implementations include Python, C, Java, Haskell, Perl, Ruby, Rust, APL, Prolog, and Mathematica.

## Connections
- [[RunLengthEncoding]] — the core operation: counting consecutive identical digits
- [[StringProcessing]] — terms are manipulated as digit strings
- [[IntegerSequence]] — generates a recursively defined OEIS sequence (A005150)
- [[JohnConway]] — mathematician who studied and analyzed the sequence
- [[Recursion]] — each term is defined in terms of its predecessor

## Contradictions
- None — reference task page.
