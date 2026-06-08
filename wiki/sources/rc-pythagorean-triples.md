---
title: "Pythagorean triples (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pythagorean_triples
---

## Summary
A Pythagorean triple is three positive integers (a, b, c) with a < b < c satisfying a² + b² = c²; a triple is "primitive" when a and b are co-prime (gcd(a, b) = 1). The task is to count how many such triples have a perimeter (a + b + c) no greater than 100, and how many of those are primitive. The key insight is that naive triple-loop enumeration does not scale, so the extra credit (perimeters up to 100,000,000) requires generating primitives via a proper method such as the Euclid/Berggren tree of triples, then scaling each primitive by integer multiples.

## Task Requirements
- Count all Pythagorean triples with perimeter ≤ 100.
- Among those, count how many are primitive (a and b co-prime).
- Extra credit: handle very large maximum perimeters (1,000,000; 10,000,000; 100,000,000) using an efficient algorithm rather than brute force.

## Language Coverage
88 languages implement this task, spanning systems languages, functional languages, scripting languages, and assembly. Representative implementations include C, C++, Rust, Go, Haskell, Python, Java, Perl, Raku, Common Lisp, Prolog, and 360 Assembly.

## Connections
- [[PythagoreanTheorem]] — the defining relation a² + b² = c².
- [[NumberTheory]] — triples and their primitive classification are a number-theory problem.
- [[GreatestCommonDivisor]] — primitivity is decided by gcd(a, b) = 1.
- [[CoprimeIntegers]] — primitive triples require co-prime legs.
- [[EuclidsFormula]] — generates primitive triples and enables the efficient large-perimeter solution.

## Contradictions
- None — reference task page.
