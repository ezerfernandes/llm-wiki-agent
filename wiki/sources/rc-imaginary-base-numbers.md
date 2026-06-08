---
title: "Imaginary base numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, complex-numbers, radix-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Imaginary_base_numbers
---

## Summary
The task implements an imaginary-base positional numeral system, where the radix is an imaginary number rather than a real integer. The canonical case is the quater-imaginary base (radix 2i), proposed by Donald Knuth in 1955, which can represent every complex number with integer real and imaginary parts using only digits 0–3, without a separate sign or imaginary marker. The key insight is that successive powers of 2i cycle between real and imaginary axes (1, 2i, −4, −8i, 16, ...), so a single digit string encodes both components of a complex number.

## Task Requirements
- Write functions to convert base-10 numbers to an imaginary base and back again.
- At minimum support quater-imaginary (base 2i).
- For extra credit, support positive or negative bases from 2i through 6i (or higher).
- As a stretch goal, support converting non-integer complex numbers (e.g. 227.65625+10.859375i), producing a fractional part after a radix point.

## Language Coverage
22 languages implement this task, a moderate spread reflecting that complex-number arithmetic and custom radix logic are needed. Representative implementations include C, C++, C#, Go, Haskell, Java, Julia, Kotlin, Python, Perl, Raku, and Wren.

## Connections
- [[ComplexNumbers]] — the values being encoded have real and imaginary parts
- [[PositionalNumeralSystem]] — generalizes place-value notation to an imaginary radix
- [[RadixConversion]] — core algorithm converting between base 10 and base 2i
- [[QuaterImaginaryBase]] — the specific base-2i system named in the task
- [[DonaldKnuth]] — proposed the quater-imaginary system in 1955

## Contradictions
- None — reference task page.
