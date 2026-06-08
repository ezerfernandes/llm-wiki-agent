---
title: "Padovan sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Padovan_sequence
---

## Summary
The Padovan sequence is a Fibonacci-like integer sequence defined by the recurrence P(n) = P(n-2) + P(n-3) with initial values P(0) = P(1) = P(2) = 1, yielding 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, … The task asks the programmer to generate the sequence three independent ways and cross-check them: by the recurrence, by a closed-form floor formula using the plastic ratio, and by an L-system whose string lengths reproduce the sequence. The key insight is that the ratio of successive terms converges to the plastic ratio p ≈ 1.3247 (the real root of x³ − x − 1), the cubic analogue of the golden ratio.

## Task Requirements
- Compute successive Padovan members via the recurrence relation P(n) = P(n-2) + P(n-3).
- Compute successive members via the floor function: P(n) = floor(p^(n-1) / s + 0.5), where p is the plastic ratio and s ≈ 1.0453567932525329623.
- Show the first twenty terms of the sequence.
- Confirm the recurrence-based and floor-based functions agree for 64 terms.
- Generate successive strings with an L-system: axiom A, rules A→B, B→C, C→AB.
- Show the first 10 L-system strings.
- Confirm the lengths of the first 32 L-system strings equal the Padovan sequence.

## Language Coverage
41 languages implement this task, spanning systems languages, functional, scripting, array, and logic paradigms — including C, C++, Rust, Go, Java, Haskell, Clojure, Prolog, Python, Julia, J, and Wren.

## Connections
- [[PlasticRatio]] — limiting ratio of successive terms, the real root of x³ − x − 1
- [[GoldenRatio]] — Fibonacci analogue the task contrasts the plastic ratio against
- [[FibonacciSequence]] — the structurally parallel recurrence the task compares to
- [[LindenmayerSystem]] — string-rewriting grammar whose string lengths reproduce the sequence
- [[LinearRecurrence]] — the order-3 integer recurrence defining the sequence

## Contradictions
- None — reference task page.
