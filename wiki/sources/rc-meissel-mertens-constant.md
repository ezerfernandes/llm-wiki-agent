---
title: "Meissel-Mertens constant (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, mathematical-constants]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Meissel-Mertens_constant
---

## Summary
The task asks the programmer to compute the Meissel–Mertens constant (M ≈ 0.26149...) to whatever precision the language supports. The constant is the prime-number analogue of the Euler–Mascheroni constant: just as the partial sum of reciprocal naturals grows like log(n) + γ, the partial sum of reciprocal primes 1/2 + 1/3 + 1/5 + ... + 1/p grows like log(log(p)) + M. The key insight is that M quantifies the limiting offset between that prime-reciprocal sum and the double logarithm.

## Task Requirements
- Calculate the Meissel–Mertens constant to a precision the language can handle.
- Recognize it as the limiting difference between the sum of prime reciprocals and log(log(p)) (target value 0.26149...).

## Language Coverage
32 languages implement this task, spanning low-level and high-level ecosystems as well as several BASIC dialects. Representative implementations include C++, Rust, Go, Java, JavaScript, Python, Julia, Perl, Raku, and the symbolic systems Mathematica and Maxima.

## Connections
- [[NumberTheory]] — the constant arises from the distribution of primes
- [[PrimeNumbers]] — defined via the sum of reciprocals of primes
- [[EulerMascheroniConstant]] — the natural-number analogue M parallels
- [[MertensTheorems]] — the asymptotic law governing prime-reciprocal sums
- [[MathematicalConstants]] — M is a fundamental analytic constant

## Contradictions
- None — reference task page.
