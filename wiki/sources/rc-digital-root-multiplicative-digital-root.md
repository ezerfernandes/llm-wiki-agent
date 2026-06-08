---
title: "Digital root/Multiplicative digital root (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Digital_root/Multiplicative_digital_root
---

## Summary
This task asks the programmer to compute the multiplicative digital root (MDR) and multiplicative persistence (MP) of a number. Rather than summing digits as in the ordinary digital root, the digits are multiplied together repeatedly until a single digit remains; the MDR is that final digit and the MP is the number of multiplication steps required. The key insight is that this is a simple iterative fixed-point process over the digit-product function.

## Task Requirements
- Implement a routine that, given n, returns its MP (number of steps) and MDR (final single digit), by repeatedly replacing the value with the product of its digits and counting iterations.
- Tabulate the MP and MDR of the numbers 123321, 7739, 893, and 899998.
- Tabulate each MDR value (0 through 9) versus the first five numbers having that MDR (e.g. MDR 0 -> [0, 10, 20, 25, 30]).
- Show all output on the page.

## Language Coverage
61 languages implement this task, giving broad coverage across mainstream, functional, and esoteric languages. Representative implementations include Python, C, C++, Java, JavaScript, Haskell, Rust, Go, Ruby, Perl, and Raku.

## Connections
- [[DigitalRoot]] — the additive counterpart this task is modeled after
- [[NumberTheory]] — the broader mathematical domain
- [[DigitManipulation]] — extracting and combining base-10 digits
- [[FixedPointIteration]] — repeating until a single-digit result stabilizes
- [[Recursion]] — natural recursive formulation of the digit-product reduction

## Contradictions
- None — reference task page.
