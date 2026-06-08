---
title: "First power of 2 that has leading decimal digits of 12 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/First_power_of_2_that_has_leading_decimal_digits_of_12
---

## Summary
Adapted from a Project Euler problem, this task asks for a function p(L, n): the nth-smallest exponent j such that the base-ten representation of 2^j begins with the digit string L. For example, 2^7 = 128 and 2^80 = 1208925819614629174706176 both start with "12", so p(12,1)=7 and p(12,2)=80. The key insight is that the leading digits of 2^j are determined by the fractional part of j·log10(2), so the test can be done with logarithms (or via fast modular/string techniques) without forming the full enormous power.

## Task Requirements
- Implement p(L, n) returning the nth exponent j where 2^j starts with the digits of L.
- Compute and display: p(12, 1), p(12, 2), p(123, 45), p(123, 12345), and p(123, 678910).
- Given checks: p(12,1)=7, p(12,2)=80, p(123,45)=12710.

## Language Coverage
42 languages implement this task, spanning systems and functional languages as well as several BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Perl, Raku, REXX, and Wren.

## Connections
- [[Logarithms]] — leading digits of 2^j come from the fractional part of j·log10(2)
- [[ArbitraryPrecisionArithmetic]] — naive approaches form huge powers of two as big integers
- [[NumberTheory]] — distribution of leading digits relates to equidistribution mod 1
- [[ProjectEuler]] — original source of the problem

## Contradictions
- None — reference task page.
