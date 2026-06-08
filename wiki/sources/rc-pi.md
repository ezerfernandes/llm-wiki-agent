---
title: "Pi (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pi
---

## Summary
This task asks the programmer to write a program that continually calculates and outputs the successive decimal digits of pi, starting with 3.14159265..., running indefinitely until the user aborts it. The key insight is that this requires a digit-streaming (spigot) algorithm rather than a fixed-precision formula, since digits must be emitted one at a time without committing to a final precision in advance.

## Task Requirements
- Continually calculate and output the next decimal digit of pi.
- Run forever until aborted by the user, emitting each digit in succession.
- Produce a decimal sequence beginning 3.14159265...
- The task is specifically about *calculating* pi, not using a built-in pi constant.

## Language Coverage
89 languages implement this task, spanning low-level assembly, mainstream languages, and many BASIC and Lisp dialects. Representative implementations include C, C++, Python, Haskell, Java, Go, Rust, Perl, Raku, and REXX.

## Connections
- [[SpigotAlgorithm]] — the streaming technique for emitting pi digits one at a time
- [[ArbitraryPrecisionArithmetic]] — needed since standard floats cannot hold unbounded digits
- [[Pi]] — the mathematical constant being computed
- [[ArithmeticGeometricMean]] — a related convergent method for computing pi
- [[ContinuedFractions]] — underpins several unbounded spigot formulations

## Contradictions
- None — reference task page.
