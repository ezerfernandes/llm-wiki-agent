---
title: "Next highest int from digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Next_highest_int_from_digits
---

## Summary
Given a zero or positive integer, generate the next largest integer that uses exactly the same digits (with the same multiplicity). The core insight is that this is the classic "next permutation" problem applied to the decimal digits: scan right-to-left for the first digit smaller than one to its right, swap it with the smallest larger digit on the right, then sort the suffix ascending. If no larger arrangement exists, return zero.

## Task Requirements
- For each input number, return the smallest integer larger than it formed by reordering its base-ten digits.
- Use every given digit with its original multiplicity; do not left-pad with zeroes.
- Return zero when no next-highest arrangement exists (digits already in descending order).
- Compute results for the inputs: 0, 9, 12, 21, 12453, 738440, 45072010, 95322020.
- Optional stretch goal: handle the 22-digit number 9589776899767587796600.

## Language Coverage
40 languages implement this task, spanning systems and scripting families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, JavaScript, Julia, Perl, and Raku.

## Connections
- [[NextPermutation]] — the underlying lexicographic-ordering algorithm
- [[Permutations]] — the brute-force Algorithm 1 enumerates and sorts all digit permutations
- [[Combinatorics]] — ordering arrangements of a multiset of digits
- [[StringProcessing]] — treating the number as a sequence of digit characters

## Contradictions
- None — reference task page.
