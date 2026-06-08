---
title: "Ethiopian multiplication (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, bitwise]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ethiopian_multiplication
---

## Summary
Ethiopian multiplication (also called Russian peasant multiplication) multiplies two integers using only addition, doubling, and halving. The two operands head two columns; the left is repeatedly halved (discarding remainders) until it reaches 1, while the right is repeatedly doubled. Summing the right-column values whose left-column counterpart is odd yields the product. The key insight is that it is binary multiplication in disguise: the odd left-column entries mark the set bits of the multiplier.

## Task Requirements
- Define three named functions: one to halve an integer, one to double an integer, and one to state whether an integer is even.
- Use these functions to build a function that performs Ethiopian multiplication.
- Worked example given: 17 × 34 = 578.

## Language Coverage
158 languages implement this task, an exceptionally broad spread from assembly to functional and esoteric languages. Representative implementations include C, Python, Haskell, Java, Rust, Common Lisp, Forth, Prolog, COBOL, and 8080 Assembly.

## Connections
- [[RussianPeasantMultiplication]] — alternate name for the same algorithm
- [[BinaryNumbers]] — odd left-column rows correspond to set bits of the multiplier
- [[BitwiseOperations]] — halving is a right shift, doubling a left shift, evenness a bit test
- [[Multiplication]] — the underlying arithmetic operation realized via addition only
- [[EgyptianDivision]] — related task using the inverse doubling/halving technique

## Contradictions
- None — reference task page.
