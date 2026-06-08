---
title: "Damm algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksum, error-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Damm_algorithm
---

## Summary
The Damm algorithm is a check-digit (checksum) scheme that detects all single-digit errors and all adjacent transposition errors in a string of digits. Named after H. Michael Damm, it works by iterating over the input digits while looking up successive values in a precomputed 10x10 quasigroup table whose diagonal is all zeros; the final accumulated value is the check digit. The task is to verify a checksum that is stored as the last digit of an input number.

## Task Requirements
- Implement the Damm algorithm using its 10x10 weakly totally anti-symmetric quasigroup operation table.
- Process the input digit by digit, starting from an interim value of 0 and updating it via the table lookup `interim = table[interim][digit]`.
- Verify the checksum: a number is valid if and only if the final interim value is 0 after consuming all digits (including the stored check digit).

## Language Coverage
87 languages implement this task, reflecting very broad coverage across mainstream, functional, array, and assembly languages. Representative implementations include Python, C, C++, Java, JavaScript, Go, Rust, Haskell, Perl, Raku, APL, and 8080 Assembly.

## Connections
- [[ChecksumAlgorithms]] — Damm is one of several check-digit schemes
- [[ErrorDetection]] — detects single-digit and adjacent transposition errors
- [[Quasigroup]] — relies on a weakly totally anti-symmetric quasigroup table
- [[CheckDigit]] — the computed value appended to validate a number
- [[LuhnAlgorithm]] — a related but weaker check-digit alternative

## Contradictions
- None — reference task page.
