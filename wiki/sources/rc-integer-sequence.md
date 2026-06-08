---
title: "Integer sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numeric-limits, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Integer_sequence
---

## Summary
This task asks the programmer to write a program that prints all integers starting from 1 and counting upward indefinitely (1, 2, 3, 4, ...) given enough time. The core teaching point is how a language represents integers and where its limits lie: a fixed-width type (e.g. 32-bit unsigned, capped at 4,294,967,295) will eventually overflow, while languages with built-in or library-provided bignums can count without bound. Where relevant, implementations are encouraged to show both a native-limit version and an arbitrary-precision version.

## Task Requirements
- Display all integers from 1 upward in increasing sequence (1, 2, 3, 4, ...).
- Continue until reaching the implementation's limit (or forever if unbounded).
- If the language has both fixed-width and arbitrary-precision integers, ideally provide an example of each.
- Describe the nature of the integer-size limitation, or note its absence.

## Language Coverage
197 languages implement this task, spanning nearly every paradigm and era — from assembly and esoteric languages to modern functional and scripting languages. Representative examples include C, Java, Python, Haskell, Rust, Go, Ruby, Perl, Common Lisp, and 8080 Assembly.

## Connections
- [[ArbitraryPrecisionArithmetic]] — how unbounded counting is achieved beyond native word size
- [[IntegerOverflow]] — what happens when fixed-width counters exceed their maximum
- [[FixedWidthIntegers]] — machine integer representations and their bounds
- [[InfiniteLoop]] — the unbounded counting loop at the task's core

## Contradictions
- None — reference task page.
