---
title: "Unprimeable numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Unprimeable_numbers
---

## Summary
An unprimeable number is a composite number that stays composite no matter which single decimal digit you change (to any other digit). The task is to generate these numbers, recognizing that all one- and two-digit numbers can always be made prime by a single-digit change, so unprimeable numbers begin at three digits. The key insight is that testing a candidate requires checking every number reachable by altering exactly one digit position and confirming none of them is prime.

## Task Requirements
- Show the first 35 unprimeable numbers on one line, preferably with a title.
- Show the 600th unprimeable number.
- Optional: show the lowest unprimeable number ending in each decimal digit (0 through 9).
- Optional: format numbers with commas where appropriate.
- Treat leading zeros as removable (e.g. changing 189 to 089 means testing 89).
- Show all output on the task page.

## Language Coverage
42 languages implement this task, spanning systems languages, scripting languages, functional languages, and array/stack languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wren.

## Connections
- [[PrimeNumbers]] — the core notion being negated; each digit variant is primality-tested.
- [[CompositeNumbers]] — unprimeable numbers are a subset of composites.
- [[PrimalityTest]] — the inner check applied to every single-digit variation.
- [[NumberTheory]] — the task is a number-theoretic classification (OEIS A118118).
- [[DigitManipulation]] — generating all single-digit-change variants of a number.

## Contradictions
- None — reference task page.
