---
title: "Caesar cipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Caesar_cipher
---

## Summary
The task asks the programmer to implement a Caesar cipher with both encoding and decoding, given an integer key from 1 to 25. Each letter is shifted by the key positions through the alphabet (A–Z), wrapping from Z back to A. The key insight is that decoding is just encoding with the complementary shift (26 − key), and that this mono-alphabetic substitution offers essentially no security since all 25 keys can be brute-forced or guessed via frequency analysis.

## Task Requirements
- Implement both encoding and decoding routines.
- Accept an integer key in the range 1 to 25.
- Rotate letters of the alphabet (A to Z), wrapping Z around to A.
- Example: key 2 encrypts "HI" to "JK"; key 20 encrypts "HI" to "BC".
- Note the relationships: it equals a Vigenère cipher with a length-1 key, and Rot-13 is the special case of key 13.

## Language Coverage
176 languages implement this task, an extremely broad spread covering systems languages, scripting languages, assembly, and esoteric languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Ruby, Perl, and several assembly variants (x86, ARM, AArch64).

## Connections
- [[CaesarCipher]] — the named encryption technique being implemented
- [[SubstitutionCipher]] — the broader cipher family this belongs to
- [[Rot13]] — the special case of a Caesar cipher with key 13
- [[VigenereCipher]] — equivalent when its key has length 1
- [[ModularArithmetic]] — the wrap-around shift is computed modulo 26

## Contradictions
- None — reference task page.
