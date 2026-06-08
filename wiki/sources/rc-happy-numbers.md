---
title: "Happy numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Happy_numbers
---

## Summary
A happy number is a positive integer for which repeatedly replacing the number with the sum of the squares of its digits eventually reaches 1; numbers that instead fall into a cycle never containing 1 are unhappy. The task asks the programmer to find and print the first 8 happy numbers (1, 7, 10, 13, 19, 23, 28, 31). The key insight is detecting termination: either you reach 1 (happy) or you enter a repeating cycle, so cycle detection or a visited-set is needed to avoid an infinite loop.

## Task Requirements
- Implement the happy-number process: replace a number by the sum of the squares of its decimal digits, repeating until it reaches 1 or loops.
- Classify numbers as happy (process ends in 1) or unhappy (process loops without reaching 1).
- Find and print the first 8 happy numbers.
- Display the program's output on the page.

## Language Coverage
149 languages implement this task, reflecting very broad coverage across paradigms — from low-level assembly to high-level scripting and functional languages. Representative examples include C, C++, Java, Python, Haskell, Rust, Go, Ruby, Lisp, and APL.

## Connections
- [[NumberTheory]] — the task is a classic recreational number-theory problem.
- [[DigitManipulation]] — relies on extracting decimal digits and squaring them.
- [[CycleDetection]] — termination requires detecting endless cycles that never reach 1.
- [[Iteration]] — the core process is an iterated transformation of integers.

## Contradictions
- None — reference task page.
