---
title: "Distribution of 0 digits in factorial series (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Distribution_of_0_digits_in_factorial_series
---

## Summary
The task asks the programmer to compute, for each factorial from 1! up to N!, the proportion of base-10 digits that are the digit 0, then average those proportions across the series. The interesting insight is that this mean drifts from roughly 1/5 toward 1/10 as N grows: trailing zeros accumulate only linearly with N (one per factor of 5), while the total digit count of n! grows much faster, so the overall fraction of zeros approaches the uniform 10% expected for "random" digits.

## Task Requirements
- Write a function returning the mean over 1..N of (count of '0' digits in n!) / (total digits in n!), with each factorial printed as a base-10 integer.
- Verify the worked examples: mean for 1..6 is 0.1111..., and for 1..25 is 0.26787.
- Compute the mean for N = 100, N = 1000, and N = 10000.
- Stretch goal: find the N in (10000, 50000) where the running mean permanently drops below 0.16.

## Language Coverage
30 languages implement this task, spanning systems, scripting, array, and math-oriented languages. Representative examples include C++, C#, Go, Rust, Java, Python, Julia, Raku, Perl, REXX, Wren, and Mathematica/Wolfram Language.

## Connections
- [[Factorial]] — the core sequence whose digits are analyzed
- [[BigInteger]] — arbitrary-precision arithmetic is required since 10000! has tens of thousands of digits
- [[NumberTheory]] — trailing-zero counts derive from factor-of-5 multiplicity
- [[DigitFrequency]] — measuring how often each digit value appears in a number's decimal representation

## Contradictions
- None — reference task page.
