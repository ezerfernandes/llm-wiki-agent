---
title: "Bitwise operations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bit-manipulation, discrete-math]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitwise_operations
---

## Summary
This task asks the programmer to implement the full set of bitwise primitives on integers: the logical operators AND, OR, XOR on two integers and NOT on the first integer, plus several bit-shifting operations. The key distinction the task draws out is between shifts (which discard bits that fall off the end) and rotates (which wrap those bits around), and between logical and arithmetic right shifts, which differ in how they treat the sign bit. If a language lacks any of these operations natively, that gap is to be noted in the implementation.

## Task Requirements
- Perform bitwise AND, OR, and XOR on two integers.
- Perform a bitwise NOT (complement) on the first integer.
- Perform a left shift and a right shift on the first integer.
- Perform a right arithmetic shift (sign-preserving) on the first integer.
- Perform a left rotate and a right rotate on the first integer.
- Use the second integer as the shift/rotate amount for all shift and rotate operations.
- Note any operation not available in the language.

## Language Coverage
162 languages implement this task, an extremely broad cross-section spanning low-level assembly, systems, scripting, and functional languages — reflecting how fundamental bit manipulation is. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, x86 Assembly, and Forth.

## Connections
- [[BitManipulation]] — the core domain of the task.
- [[BitwiseOperators]] — AND, OR, XOR, and NOT are the logical primitives exercised.
- [[BitShifting]] — logical vs. arithmetic shifts and their handling of the sign bit.
- [[CircularShift]] — left and right rotates that wrap bits around the word boundary.
- [[TwosComplement]] — underlies arithmetic right shift and complement (NOT) behavior on signed integers.

## Contradictions
- None — reference task page.
