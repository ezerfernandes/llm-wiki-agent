---
title: "Minimum multiple of m where digital sum equals m (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Minimum_multiple_of_m_where_digital_sum_equals_m
---

## Summary
For each index n, find the smallest positive integer multiplier m such that the sum of the decimal digits of n×m equals n. The task asks to generate the first 40 elements of this sequence (with a stretch goal of 30 more). The key insight is a simple brute-force search: for a given n, try multipliers m = 1, 2, 3, ... until the digit sum of the product n·m first equals n; the sequence corresponds to OEIS A131382.

## Task Requirements
- Generate sequence a(n): the minimum integer multiple m such that the digit sum of n×m equals n.
- Find and report the first 40 elements of the sequence.
- Stretch goal: find the next 30 elements (elements 41–70).

## Language Coverage
50 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Go, Rust-adjacent Jakt, Java, Python, Haskell, Raku, APL, J, and REXX.

## Connections
- [[DigitSum]] — the core operation: summing decimal digits of a product.
- [[NumberTheory]] — the sequence is an integer-sequence / number-theory problem.
- [[BruteForceSearch]] — the natural solution iterates multipliers until the condition holds.
- [[OEIS]] — registered as sequence A131382.

## Contradictions
- None — reference task page.
