---
title: "Straddling checkerboard (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Straddling_checkerboard
---

## Summary
The task asks the programmer to implement encryption and decryption using the straddling checkerboard, a classic fractionation cipher that converts letters into decimal digits. A 28-character alphabet (A–Z plus a full stop and an escape character) is laid out in a grid whose first row has two blank columns; letters in that row map to a single digit while all other letters map to a two-digit code. The key insight is that the chosen blank positions make the variable-length codes self-delimiting, so the digit stream can be unambiguously decoded.

## Task Requirements
- Implement both an encrypt and a decrypt function for the straddling checkerboard method.
- Use a 28-character alphabet: A–Z, a full stop, and an escape character.
- Accept two distinct numbers specifying the blank (gap) positions in the first row.
- Produce output as a series of decimal digits.
- Encode literal numbers by emitting the escape character before each digit, then the digit itself unencrypted; reverse this on decryption.

## Language Coverage
40 languages implement this task, spanning systems, scripting, and functional styles. Representative examples include C, C++, C#, Go, Java, Python, Haskell, Julia, Perl, Raku, Ruby, and REXX.

## Connections
- [[StraddlingCheckerboard]] — the cipher this task implements
- [[Cryptography]] — the domain of the technique
- [[SubstitutionCipher]] — the broader class of letter-to-symbol ciphers
- [[Fractionation]] — variable-length digit encoding that makes codes self-delimiting

## Contradictions
- None — reference task page.
