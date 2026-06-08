---
title: "Verhoeff algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, checksum, error-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Verhoeff_algorithm
---

## Summary
The task asks the programmer to implement the Verhoeff algorithm, a decimal check-digit scheme devised by Jacobus Verhoeff in 1969. Its key insight is to base the checksum on the algebra of the dihedral group of order 10 (the symmetries of a pentagon) combined with a digit-permutation table, which lets it catch all single-digit errors and all transpositions of adjacent digits — error classes that simpler weighted-sum checksums miss.

## Task Requirements
- Write routines to generate a Verhoeff check digit for a non-negative integer of any length and to validate a number with its appended check digit (a combined routine is acceptable).
- Optionally generate the three required tables (multiplication, permutation, inverse) from the description rather than hard-coding them.
- Support an option to display the digit-by-digit calculation as shown in the Wikipedia worked example.
- Compute and validate check digits for 236, 12345, and 123456789012, then attempt validation when the check digit is forced to 9 in each case (expecting failures).
- Show digit-by-digit detail for the first two integers but not the third.

## Language Coverage
27 languages implement this task, spanning systems, scripting, functional, and array languages. Representative entries include C, C++, Rust, Zig, Go, Java, JavaScript, Python, Perl, Raku, Julia, J, and Fortran.

## Connections
- [[DihedralGroup]] — the checksum arithmetic is performed in D5, the dihedral group of order 10.
- [[CheckDigit]] — Verhoeff is a check-digit scheme appended to a number for error detection.
- [[ErrorDetection]] — it detects all single-digit and adjacent-transposition errors.
- [[DammAlgorithm]] — a related, simpler check-digit method using a quasigroup, listed as the related task.
- [[GroupTheory]] — the algorithm's correctness rests on non-commutative group structure.

## Contradictions
- None — reference task page.
