---
title: "Primes - allocate descendants to their ancestors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Primes_-_allocate_descendants_to_their_ancestors
---

## Summary
Define a number's "parent" as the sum of its prime factors (with multiplicity): e.g. 46 = 2*23 has parent 25, since 2+23 = 25. Repeatedly applying this yields a chain of ancestors up to a prime (which has no parent), and conversely a number's descendants are all numbers whose parent is that number. The task asks, for each ancestor from 1 to 99, to report its level (ancestor count), its ancestors, and the count and list of its direct descendants, plus a grand total of descendants. The key insight is that a naive scan up to 3^33 is intractable, so an efficient algorithm must generate descendants from prime-factor partitions rather than test every integer.

## Task Requirements
- For each ancestor in the range 1 to 99, report: the LEVEL (total count of its own ancestors), the list of ANCESTORS, the count of DESCENDANTS, and all direct descendants.
- The parent of a number is the sum of its prime factors counted with multiplicity; primes have no parent.
- Only consider prime factors below 100.
- Print a grand total of descendants at the end (546,986).
- Complete in a reasonable time-frame, avoiding a brute-force scan of all numbers up to 3^33.

## Language Coverage
27 languages implement this task. Coverage is broad, spanning systems languages, functional languages, and scripting, including C, C++, Go, Java, Haskell, Julia, Python, Perl, Raku, REXX, and Wren.

## Connections
- [[PrimeFactorization]] — parents are derived by summing prime factors
- [[NumberTheory]] — the entire task is rooted in integer factor structure
- [[IntegerPartition]] — descendants correspond to prime-factor partitions summing to the target
- [[DynamicProgramming]] — efficient solutions cache or generate descendant sets to avoid brute force

## Contradictions
- None — reference task page.
