---
title: "Minkowski question-mark function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, continued-fractions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Minkowski_question-mark_function
---

## Summary
The task is to implement Minkowski's question-mark function ?(x), which maps a number's continued-fraction representation [a0; a1, a2, ...] to a binary expansion where the integer part a0 is unchanged and each subsequent term becomes an alternating run of binary 0s and 1s of that length. Its defining property is that it sends quadratic irrationals (which have eventually periodic continued fractions) to rationals (which have eventually periodic binary expansions). The function is continuous and strictly increasing, so the inverse ?⁻¹(x) is well defined and must also be implemented.

## Task Requirements
- Implement ?(x). Handle the ambiguity that rationals have two continued-fraction forms ([..., an] and [..., an−1, 1]); pick the one whose binary expansion ends in a 1.
- Implement the inverse function ?⁻¹(x).
- Verify ?(φ) = 5/3, where φ is the golden ratio.
- Verify ?⁻¹(−5/9) = (√13 − 7)/6.
- Demonstrate the two are mutual inverses: ?⁻¹(?(x)) = x and ?(?⁻¹(y)) = y for chosen x, y.
- Precision error in the last few digits is acceptable.

## Language Coverage
20 languages implement this task, spanning systems and functional languages alongside math-oriented and scripting environments. Representative implementations include C++, C#, Go, Java, Haskell, F#, Julia, Python, Perl, Raku, Nim, and Wren.

## Connections
- [[ContinuedFractions]] — the function operates directly on continued-fraction expansions
- [[GoldenRatio]] — φ is a required verification input (?(φ) = 5/3)
- [[QuadraticIrrational]] — periodic continued fractions mapped to periodic binary expansions
- [[NumberTheory]] — the broader domain of the task
- [[InverseFunction]] — the task requires constructing and validating ?⁻¹

## Contradictions
- None — reference task page.
