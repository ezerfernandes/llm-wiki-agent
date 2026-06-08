---
title: "Zeckendorf arithmetic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, fibonacci]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zeckendorf_arithmetic
---

## Summary
The task asks the programmer to implement addition, subtraction, multiplication, and division directly on numbers expressed in Zeckendorf representation — the encoding of integers as sums of non-consecutive Fibonacci numbers — without ever converting to decimal. The key insight is that arithmetic must be done by manipulating the Zeckendorf digit strings themselves, propagating carries and borrows according to the Fibonacci recurrence and re-normalizing any forbidden adjacent ones (the substring `11` becomes `100`).

## Task Requirements
- Implement addition, subtraction, multiplication, and division on Zeckendorf-encoded values.
- Decimal numbers are explicitly discouraged ("total immersion" task); operate on the Zeckendorf strings.
- For addition, propagate carries left and right and rewrite occurrences of `11` (or `111`) into `100` to maintain canonical form.
- For subtraction, apply the borrow-1-right / carry-1-left rule, cascading borrows when a digit cannot lend.
- For multiplication, build a doubling/Fibonacci table (each row is the sum of the two previous rows) and add the selected rows.
- For division, repeatedly subtract the largest fitting table entry, yielding a quotient and remainder.
- Optionally provide increment, decrement, and comparison operators.

## Language Coverage
28 languages implement this task, a moderate breadth that includes both systems and functional languages. Representative implementations exist in C, C++, C#, D, Go, Haskell, Java, Julia, Python, Rust, Perl, Raku, and Wren.

## Connections
- [[ZeckendorfNumberRepresentation]] — the underlying encoding this task operates on.
- [[FibonacciSequence]] — the basis weights of each digit position.
- [[NumberTheory]] — the arithmetic and representation theory involved.
- [[PositionalNumberSystems]] — non-standard positional system with the no-adjacent-ones constraint.

## Contradictions
- None — reference task page.
