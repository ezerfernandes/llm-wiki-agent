---
title: "Vigenère cipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Vigenère_cipher
---

## Summary
The task is to implement the Vigenère cipher, a classic polyalphabetic substitution cipher, supporting both encryption and decryption. Each plaintext letter is shifted by the corresponding key letter (the key repeated to match the message length), which is equivalent to a Caesar cipher whose shift varies per position. The key insight is that decryption simply reverses the per-letter shift using modular arithmetic over the 26-letter alphabet.

## Task Requirements
- Implement both encryption and decryption.
- Handle keys and text of unequal length (the key repeats/cycles to cover the message).
- Capitalize all letters and discard non-alphabetic characters before processing.
- If non-alphabetic characters are handled differently than discarding, document the behavior.

## Language Coverage
86 languages implement this task, reflecting broad coverage across systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Rust, Go, Python, Java, Haskell, Common Lisp, Perl, and ARM Assembly.

## Connections
- [[VigenereCipher]] — the polyalphabetic substitution cipher being implemented
- [[CaesarCipher]] — Vigenère generalizes Caesar with a per-position varying shift
- [[ModularArithmetic]] — letter shifts are computed modulo 26
- [[Cryptography]] — classical encryption technique
- [[SubstitutionCipher]] — the broader family this cipher belongs to

## Contradictions
- None — reference task page.
