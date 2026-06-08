---
title: "Loops/With multiple ranges (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/With_multiple_ranges
---

## Summary
This task asks the programmer to replicate a PL/I `do` loop that iterates over several comma-separated ranges in sequence, each with its own start, end, and (optional) step expression. The loop variable runs through every range in the order given, and the program accumulates a running sum of absolute values plus a bounded product to verify correct incrementing. The key insight is that most languages lack PL/I's native multi-range `do`, so the construct must be emulated by chaining individual stepped loops.

## Task Requirements
- Translate the given PL/I multiple-range `do` loop as faithfully as possible, emphasizing the loop construct.
- Visit the seven ranges in the exact order shown, honoring each range's `to` bound and `by` step (defaulting to a step of 1 when omitted); all bound/step expressions are evaluated up front.
- Maintain `sum` (sum of absolute values of the index) and `prod` (product of nonzero index values, only multiplied while `abs(prod) < 2**27`) for verification.
- Add thousands separators (commas) to the two displayed numbers if feasible, and show all output.

## Language Coverage
74 languages implement this task, spanning systems languages, scripting languages, functional languages, and many BASIC dialects. Representative examples include C, C++, C#, Java, Python, Haskell, Julia, Perl, Raku, Go, REXX, and several assembly variants (AArch64, ARM, RISC-V).

## Connections
- [[ControlFlow]] — multiple ranges are a control-flow looping construct
- [[Iteration]] — the task is fundamentally about iterating over sequences of values
- [[ArithmeticProgression]] — each range is a stepped arithmetic sequence
- [[PLI]] — the reference snippet uses PL/I's native multi-range `do`

## Contradictions
- None — reference task page.
