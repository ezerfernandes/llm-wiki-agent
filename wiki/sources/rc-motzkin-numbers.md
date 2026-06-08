---
title: "Motzkin numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, integer-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Motzkin_numbers
---

## Summary
The task asks the programmer to compute Motzkin numbers, where M[n] counts the distinct ways of drawing non-intersecting chords between n points on a circle (chords need not touch every point), with M[0] = 1 by convention. The key insight is that these numbers grow quickly, so they are best computed with a recurrence relation rather than by enumerating chord drawings, and the task also requires testing each value for primality.

## Task Requirements
- Compute and display the first 42 Motzkin numbers (or as many as fit if the language lacks 64-bit integers).
- Indicate which of the displayed numbers are prime.
- Use the convention M[0] = 1; the sequence corresponds to OEIS A001006.

## Language Coverage
44 languages implement this task, spanning systems, functional, scripting, array, and BASIC-family languages. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Julia, Perl, Raku, and J.

## Connections
- [[MotzkinNumber]] — the combinatorial sequence this task computes
- [[RecurrenceRelation]] — the standard way to generate successive terms efficiently
- [[Combinatorics]] — counting non-intersecting chord configurations
- [[PrimalityTest]] — required to flag which Motzkin numbers are prime
- [[IntegerSequence]] — the task maps directly to an OEIS catalog entry

## Contradictions
- None — reference task page.
