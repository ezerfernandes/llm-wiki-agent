---
title: "Hailstone sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hailstone_sequence
---

## Summary
The task asks the programmer to generate the hailstone (Collatz) sequence for a positive integer: repeatedly halve even numbers and apply 3n+1 to odd numbers until reaching 1. The key insight is the Collatz conjecture — the unproven claim that this process always terminates at 1 regardless of the starting value. Sequence lengths vary wildly (the "hailstone" rises and falls), making the search for long sequences a simple but illustrative exercise.

## Task Requirements
- Create a routine to generate the hailstone sequence for a given number.
- Demonstrate that the sequence for 27 has 112 elements, beginning 27, 82, 41, 124 and ending 8, 4, 2, 1.
- Find the number below 100,000 with the longest hailstone sequence and report that length (without printing the full sequence).

## Language Coverage
184 languages implement this task, reflecting extremely broad coverage across mainstream, academic, and esoteric languages. Representative implementations include C, Python, Java, Haskell, Rust, Go, Lisp, APL, Prolog, and Brainf***.

## Connections
- [[CollatzConjecture]] — the open mathematical problem the sequence embodies
- [[NumberTheory]] — the domain of integer iteration the task explores
- [[Recursion]] — natural way to express the step-wise sequence generation
- [[IteratedFunctions]] — repeated application of a piecewise map until a fixed point

## Contradictions
- None — reference task page.
