---
title: "Increasing gaps between consecutive Niven numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Increasing_gaps_between_consecutive_Niven_numbers
---

## Summary
A Niven (Harshad) number is a positive integer evenly divisible by the sum of its base-ten digits. This task asks the programmer to scan the sequence of Niven numbers, compute the gap between each Niven number and the previous one, and report every time a new record-largest gap appears. The key insight is that record gaps are rare and grow slowly, so the program must efficiently iterate up to the ten-millionth Niven number to surface them.

## Task Requirements
- Compute the gap (difference) between each Niven number and the previous Niven number.
- Whenever a gap exceeds all previous gaps, report a new record: the index (occurrence) of the gap (first gap is 1).
- For each record gap, show the index of the Niven number that starts the gap (1 is the 1st Niven number; 100 is the 33rd).
- Show the actual Niven number that starts the gap.
- Optionally format numbers with comma separators.
- Show all increasing (record) gaps up to the 10,000,000th Niven number.
- Optionally extend further if feasible; display all output on the page.

## Language Coverage
38 languages implement this task, spanning systems and scripting languages alongside math-oriented and assembly entries. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and x86-64 Assembly.

## Connections
- [[NivenNumbers]] — the core sequence being analyzed (also called Harshad numbers)
- [[DigitSum]] — the divisibility test depends on summing base-ten digits
- [[Divisibility]] — Niven numbers are defined by even divisibility by their digit sum
- [[IntegerSequences]] — relates to OEIS-style enumeration and record-gap analysis

## Contradictions
- None — reference task page.
