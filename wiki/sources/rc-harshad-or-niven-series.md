---
title: "Harshad or Niven series (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Harshad_or_Niven_series
---

## Summary
The task asks the programmer to generate the Harshad (or Niven) numbers: positive integers that are evenly divisible by the sum of their own digits — for example, 42 qualifies because 4+2=6 divides 42. The key insight is a simple predicate combining digit-sum extraction with a divisibility test, then iterating over integers in increasing order.

## Task Requirements
- Create a function/method/procedure that generates successive members of the Harshad sequence (numbers ≥ 1 divisible by their digit sum).
- List the first 20 members of the sequence.
- List the first Harshad number greater than 1000.
- Show the output.

## Language Coverage
133 languages implement this task, reflecting very broad coverage across paradigms and eras — from low-level assembly to modern functional and scripting languages. Representative implementations include C, Python, Haskell, Java, Rust, Go, Common Lisp, APL, Fortran, and REXX.

## Connections
- [[NumberTheory]] — Harshad numbers are a number-theoretic sequence (OEIS A005349)
- [[DigitSum]] — the defining test relies on summing a number's decimal digits
- [[Divisibility]] — membership requires the digit sum to divide the number without remainder
- [[SequenceGeneration]] — the task centers on iterating integers and filtering by a predicate

## Contradictions
- None — reference task page.
