---
title: "Binary digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, radix-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Binary_digits
---

## Summary
This task asks the programmer to convert a given non-negative integer into its binary (base-2) representation and display it. For example, 5 produces "101", 50 produces "110010", and 9000 produces "10001100101000". The key insight is that this is a radix conversion from base 10 to base 2, achievable via built-in radix/formatting functions or a hand-written routine using repeated division by 2 and remainders.

## Task Requirements
- Generate and display the binary digit sequence for a given non-negative integer.
- Demonstrate with the values 5, 50, and 9000.
- May use built-in radix functions if available, or a user-defined function.
- Output only the binary digits followed by a newline.
- No extra whitespace, radix prefixes, or sign markers.
- No leading zeros in the output.

## Language Coverage
217 languages implement this task, making it one of the most broadly covered "basic learning" tasks on Rosetta Code. Representative implementations include C, Python, Java, JavaScript, Haskell, Rust, Go, Common Lisp, Forth, and assembly variants such as 8086 Assembly.

## Connections
- [[NumberBaseConversion]] — converting an integer from base 10 to base 2
- [[PositionalNotation]] — binary as a radix-2 positional numeral system
- [[BitwiseOperations]] — implementations often shift and mask bits
- [[IntegerToString]] — formatting a numeric value as its digit string

## Contradictions
- None — reference task page.
