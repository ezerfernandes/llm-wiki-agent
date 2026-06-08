---
title: "Pernicious numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, bit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pernicious_numbers
---

## Summary
A pernicious number is a positive integer whose population count — the number of 1-bits in its binary representation — is itself a prime number. The task asks the programmer to identify such numbers. The key insight is combining a popcount (Hamming weight) computation with a primality test on that small count.

## Task Requirements
- Display the first 25 pernicious numbers in decimal.
- Display all pernicious numbers between 888,888,877 and 888,888,888 inclusive.
- Print each list of integers on a single line (a title is optional).

## Language Coverage
89 languages implement this task, a broad cross-section spanning systems, scripting, functional, and esoteric languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, REXX, and Befunge.

## Connections
- [[PopulationCount]] — the count of set bits that drives the definition
- [[PrimeNumber]] — the popcount must be prime for the number to qualify
- [[BitManipulation]] — computing the Hamming weight of an integer
- [[PrimalityTest]] — checking whether the small bit-count is prime
- [[BinaryRepresentation]] — the binary form whose ones are counted

## Contradictions
- None — reference task page.
