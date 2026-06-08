---
title: "Detect division by zero (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, error-handling, arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Detect_division_by_zero
---

## Summary
This task asks the programmer to write a function that detects a divide-by-zero error without inspecting the denominator beforehand. The key insight is that instead of guarding with an `if denominator == 0` check, the solution must attempt the division and catch the resulting error condition (exception, signal, or special floating-point value) reactively rather than proactively.

## Task Requirements
- Implement a function that performs a division.
- Detect when a divide-by-zero error occurs.
- Do this without first checking whether the denominator equals zero.

## Language Coverage
138 languages implement this task, reflecting very broad coverage typical of a "Simple" category exercise. Representative implementations include C, C++, Java, Python, Ruby, Haskell, Rust, Go, JavaScript, Perl, and Common Lisp, spanning approaches from exception handling to signal trapping and IEEE 754 infinity/NaN inspection.

## Connections
- [[ExceptionHandling]] — the common technique of wrapping the division in try/catch to detect the failure
- [[FloatingPointArithmetic]] — IEEE 754 systems may yield infinity or NaN instead of raising an error
- [[ErrorHandling]] — broader category of reacting to runtime failures rather than guarding against them
- [[Integer division]] — integer divide-by-zero typically traps or raises, unlike floating-point

## Contradictions
- None — reference task page.
