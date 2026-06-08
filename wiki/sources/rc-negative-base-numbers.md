---
title: "Negative base numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, radix-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Negative_base_numbers
---

## Summary
This task asks the programmer to encode integers using a negative radix (negative base) positional numeral system, which can represent both positive and negative values without a separate minus sign. The key insight is that during repeated division by a negative base, the remainder must be normalized to stay non-negative (adjusting the quotient accordingly), so that each digit is a valid digit of the system.

## Task Requirements
- Encode decimal 10 as negabinary (base -2), expecting `11110`.
- Encode decimal 146 as negaternary (base -3), expecting `21102`.
- Encode decimal 15 as negadecimal (base -10), expecting `195`.
- For each case, convert the encoded value back to decimal to verify the round trip.
- Extra credit: encode an integer in base -62 (or higher) so the result spells the name of the language being used, with correct capitalization.

## Language Coverage
40 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C, C++, C#, Java, Rust, Go, Haskell, F#, Python, Perl, Raku, Ruby, J, and REXX.

## Connections
- [[PositionalNotation]] — negative bases are a positional numeral system variant
- [[RadixConversion]] — encoding/decoding is base conversion with a negative radix
- [[ModularArithmetic]] — remainder normalization keeps each digit non-negative
- [[NumberTheory]] — properties of representations in non-standard bases

## Contradictions
- None — reference task page.
