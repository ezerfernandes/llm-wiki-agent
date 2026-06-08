---
title: "Fraction reduction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recreational-mathematics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fraction_reduction
---

## Summary
The task asks the programmer to find fractions that can be incorrectly "reduced" by crossing out a digit shared between the numerator and denominator, yet still arrive at the correct mathematical value — the classic example being 16/64 reducing to 1/4 by deleting the 6. The key insight is that this so-called anomalous (or accidental) cancellation works only by numerical coincidence, not by any valid arithmetic rule, and the program must verify each candidate against the true reduced value.

## Task Requirements
- Find and show fractions reducible by crossing out a shared digit, grouped separately by digit-count (2-digit, 3-digit, 4-digit, 5-digit and higher optional).
- For each size, show only the first dozen examples, each on one line with the original fraction, the reduced fraction, and the crossed-out digit for numerator and denominator.
- For each size, report a total count of reducible fractions found, plus a per-digit count of which digits were crossed out.
- Restrictions: proper fractions only, positive base-ten integers, no zero digits, numerator and denominator must have equal digit counts, no repeated digit within the numerator or within the denominator, and the crossed-out digit must be shared between both.

## Language Coverage
34 languages implement this task, showing broad coverage across systems, functional, scripting, and constraint-solving paradigms. Representative implementations include C, C++, Go, Rust-adjacent FreeBASIC, Haskell, J, Java, JavaScript, Julia, Python, Perl, Raku, REXX, and the constraint language MiniZinc.

## Connections
- [[NumberTheory]] — the puzzle lives in elementary number theory over base-ten integers.
- [[AnomalousCancellation]] — the named phenomenon this task demonstrates.
- [[ProperFraction]] — only proper fractions and reductions are permitted.
- [[BruteForceSearch]] — most solutions enumerate candidate fractions and test the cancellation.
- [[FareySequence]] — the page's cited related fraction task.

## Contradictions
- None — reference task page.
