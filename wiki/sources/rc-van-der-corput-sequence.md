---
title: "Van der Corput sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Van_der_Corput_sequence
---

## Summary
The task asks the programmer to generate the nth term of the van der Corput sequence in base 2. The key insight is that each term is produced by writing n in binary and reflecting its digits about the radix point, so the integer count 0, 1, 10, 11 becomes the fractions .0, .1, .01, .11 (i.e. 0, 1/2, 1/4, 3/4). These terms are a low-discrepancy sequence that fills the interval [0, 1) evenly, making them valuable for Monte Carlo and quasi-random sampling.

## Task Requirements
- Create a function/method that, given n, returns the nth term of the van der Corput sequence in base 2.
- Use it to compute and display the first ten members (the first member corresponds to n = 0).
- Stretch goal: compute and show members of the sequence for bases other than 2.

## Language Coverage
87 languages implement this task, reflecting very broad coverage across paradigms. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Julia, Perl, Raku, and REXX.

## Connections
- [[LowDiscrepancySequence]] — the van der Corput sequence is the canonical 1-D low-discrepancy sequence.
- [[MonteCarloMethod]] — even point distribution makes it useful for quasi-Monte Carlo integration and simulation.
- [[RadixConversion]] — generation reuses base-change/digit-extraction logic with the digits reflected about the radix point.
- [[BinaryNumberSystem]] — relies on negative powers of two for fractional place values.

## Contradictions
- None — reference task page.
