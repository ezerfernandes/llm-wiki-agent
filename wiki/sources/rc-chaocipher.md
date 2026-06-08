---
title: "Chaocipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Chaocipher
---

## Summary
The Chaocipher is a hand cipher invented by J.F. Byrne in 1918 whose algorithm stayed secret until his family disclosed it in 2010. The task asks the programmer to implement the cipher, which uses two 26-character alphabets (a left "ciphertext" wheel and a right "plaintext" wheel) that are dynamically permuted after every encrypted character, making it a self-modifying substitution cipher. The key insight is that the alphabets are not static: each step locates the character, reads off its counterpart, then rotates and shuffles both wheels so the substitution table continuously evolves.

## Task Requirements
- Implement the Chaocipher encryption (and typically decryption) algorithm in the chosen language.
- Model the two interacting alphabets and apply the prescribed permutation/rotation of each wheel after every character.
- Verify the implementation by encrypting the plaintext `WELLDONEISBETTERTHANWELLSAID`, the example used in M. Rubin's 2010 paper.

## Language Coverage
54 languages implement this task, showing broad coverage across systems, scripting, and functional languages. Representative examples include C, C++, C#, Rust, Go, Java, Python, Haskell, Perl, Ruby, JavaScript, and Wren.

## Connections
- [[Cryptography]] — the task is a classic encryption algorithm.
- [[SubstitutionCipher]] — Chaocipher is a dynamic substitution cipher.
- [[StringProcessing]] — implementation centers on rotating and rearranging character sequences.
- [[Permutation]] — each step permutes the two alphabet wheels.

## Contradictions
- None — reference task page.
