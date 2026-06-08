---
title: "Lah numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Lah_numbers
---

## Summary
Lah numbers (sometimes called Stirling numbers of the third kind) are coefficients that express rising factorials in terms of falling factorials. The unsigned Lah number L(n, k) counts the ways a set of n elements can be partitioned into k non-empty linearly ordered subsets. The task is to implement a routine for unsigned Lah numbers using the closed-form L(n, k) = n!(n-1)! / (k!(k-1)!) / (n-k)!, which avoids the recurrence by direct factorial computation.

## Task Requirements
- Write a routine to compute unsigned Lah numbers L(n, k).
- Generate and display a table or triangle of L(n, k) up to L(12, 12); showing the n=0/k=0 row/column and the zero entries (k > n) is optional.
- If the language supports big integers, find and show the maximum value of L(n, k) for n == 100.
- Honor the base identities: L(n, n) = 1, L(n, 1) = n!, and L(n, 0) = L(0, k) = 0 for n, k > 0.

## Language Coverage
55 languages implement this task, spanning systems languages, scripting languages, functional languages, and array/math-oriented languages — including C, C++, Java, Go, Python, Haskell, Julia, Raku, J, and Wren. Big-integer support is needed for the n == 100 maximum.

## Connections
- [[CombinatorialNumbers]] — Lah numbers are a family of combinatorial coefficients.
- [[StirlingNumbers]] — closely related to and derivable from Stirling numbers of the first and second kinds.
- [[Factorial]] — the closed form is built entirely from factorials.
- [[BigInteger]] — required to represent the large L(100, k) values.
- [[SetPartition]] — unsigned Lah numbers count partitions into ordered subsets.

## Contradictions
- None — reference task page.
