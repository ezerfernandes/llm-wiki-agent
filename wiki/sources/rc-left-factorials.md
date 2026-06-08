---
title: "Left factorials (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Left_factorials
---

## Summary
The task asks the programmer to compute the "left factorial" !n, defined here as the cumulative sum of factorials !n = Σ k! for k from 0 to n-1, with !0 = 0. The key insight is disambiguation: the same "!n" notation is also used for subfactorials (derangements), but this task specifically uses the factorial-sum definition (OEIS A003422). Because the values grow extremely fast, results for large n require arbitrary-precision integers.

## Task Requirements
- Display the left factorials for 0 through 10 inclusive.
- Display the left factorials for 20 through 110 inclusive, stepping by tens.
- Display the number of decimal digits in the left factorials for 1,000 through 10,000 inclusive, stepping by thousands.

## Language Coverage
69 languages implement this task, reflecting broad coverage across paradigms and eras since big-integer arithmetic is the main hurdle. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Julia, Perl, Raku, Scheme, and REXX.

## Connections
- [[Factorial]] — left factorial is built from a running sum of ordinary factorials
- [[Subfactorial]] — the contrasting meaning of the same !n notation, explicitly excluded here
- [[ArbitraryPrecisionArithmetic]] — required since values for n up to 10,000 have thousands of digits
- [[NumberTheory]] — the sequence is catalogued as OEIS A003422
- [[Summation]] — the definition is a cumulative sum of a factorial series

## Contradictions
- None — reference task page.
