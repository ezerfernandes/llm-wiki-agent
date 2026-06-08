---
title: "IBAN (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksum, string-processing, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/IBAN
---

## Summary
The task asks the programmer to validate an International Bank Account Number (IBAN), an internationally standardized identifier for cross-border bank accounts designed to reduce transcription errors. An IBAN packs a two-letter ISO 3166-1 country code, two check digits, and a country-specific Basic Bank Account Number (BBAN) into up to 34 alphanumeric characters. The key insight is that validation reduces to a checksum: move the first four characters to the end, replace each letter with two digits (A=10 … Z=35), then verify the resulting large integer is congruent to 1 modulo 97.

## Task Requirements
- Validate the fictitious IBAN `GB82 WEST 1234 5698 7654 32`.
- Strip spaces and confirm the IBAN consists of up to 34 alphanumeric characters.
- Apply the mod-97 check digit algorithm (rearrange, letter-to-digit substitution, integer mod 97 == 1) as described on the linked Wikipedia page.
- Ideally also check that the length matches the country's expected IBAN length.

## Language Coverage
80 languages implement this task, giving very broad coverage spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, Ruby, and REXX.

## Connections
- [[Checksum]] — IBAN validation is fundamentally a checksum integrity check.
- [[ModularArithmetic]] — the validity test is the mod-97 congruence (value mod 97 == 1).
- [[StringProcessing]] — requires rearranging characters and substituting letters for digit pairs.
- [[BigInteger]] — the substituted IBAN forms a number too large for native integer types in most languages.
- [[ISO3166]] — the leading two-letter country code follows the ISO 3166-1 alpha-2 standard.

## Contradictions
- None — reference task page.
