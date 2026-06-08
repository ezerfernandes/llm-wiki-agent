---
title: "Equal prime and composite sums (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Equal_prime_and_composite_sums
---

## Summary
The task defines two cumulative sequences: prime partial sums (P_n = sum of the first n primes: 2, 5, 10, 17, 28, ...) and composite partial sums (C_m = sum of the first m composites: 4, 10, 18, 27, 37, ...). The goal is to find numbers that appear in both sequences — values that are simultaneously the sum of the first n primes and the sum of the first m composites. The key insight is that this is a merge/intersection problem over two monotonically increasing integer sequences (e.g., 10 = P_3 = C_2).

## Task Requirements
- Generate the running sum of the first n primes (OEIS A007504).
- Generate the running sum of the first m composites (OEIS A053767).
- Find values common to both sequences (OEIS A294174), reporting the indices n and m and the shared value.
- Display at least the first 6 such common terms.

## Language Coverage
32 languages implement this task, spanning systems languages, scripting languages, functional languages, and array/stack languages. Representative implementations include Ada, ALGOL 68, C++, Go, Java, Python, Perl, Raku, Julia, J, Lua, and Wren.

## Connections
- [[PrimeNumbers]] — the prime sequence drives one partial-sum series.
- [[CompositeNumbers]] — the composite sequence drives the other partial-sum series.
- [[PrefixSums]] — both sequences are cumulative running sums.
- [[SequenceIntersection]] — the core task is finding common terms via a two-pointer merge.
- [[OEIS]] — references sequences A007504, A053767, and A294174.

## Contradictions
- None — reference task page.
