---
title: "Euclidean rhythm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, music, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Euclidean_rhythm
---

## Summary
Implement the Euclidean rhythm generator proposed by Godfried Toussaint (2004), which distributes m onset beats as evenly as possible across n total time slots. Given integers (m, n), the program outputs a binary string of m ones and (n-m) zeros. The key insight is that the same recursive grouping process used in the Euclidean algorithm for the GCD produces these maximally even rhythmic patterns found across many world music traditions.

## Task Requirements
- Take two integers m and n as input (m ones, n-m zeros).
- Begin with m groups each holding a "1" and (n-m) groups each holding a "0".
- Repeatedly append/substitute trailing groups onto the leading groups, splitting into two forms when needed, mirroring the Euclidean GCD process.
- Terminate once the groups reduce to a single form (or a remainder group of one element), then output the concatenated binary string (e.g. (5, 13) yields 1001010010100).

## Language Coverage
40 languages implement this task, giving broad coverage across functional, imperative, and array-oriented styles. Representative examples include C++, C#, Java, Python, JavaScript, Go, Rust, Julia, Raku, Common Lisp, and the array language Uiua.

## Connections
- [[EuclideanAlgorithm]] — the recursive grouping mirrors the GCD subtraction/division steps.
- [[GreatestCommonDivisor]] — the divisor structure determines the rhythmic distribution.
- [[BresenhamLineAlgorithm]] — closely related to evenly distributing discrete points (the Bjorklund/Euclidean string).
- [[RecursionTechnique]] — the algorithm is naturally expressed as repeated recursive splitting.

## Contradictions
- None — reference task page.
