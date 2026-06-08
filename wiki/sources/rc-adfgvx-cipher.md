---
title: "ADFGVX cipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, ciphers, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/ADFGVX_cipher
---

## Summary
The task asks the programmer to implement the ADFGVX cipher, a WWI-era German field cipher that combines fractionation via a Polybius square with columnar transposition. Each plaintext character is first replaced by a pair of letters drawn from the set {A, D, F, G, V, X} using a 6x6 substitution square, and the resulting stream is then scrambled by a keyed columnar transposition. The key insight is that this two-stage design (substitution then transposition) makes the cipher far harder to break than either step alone.

## Task Requirements
- Implement encryption and decryption routines for the ADFGVX algorithm, given a Polybius square and a key.
- Treat "suitable" plaintext as ASCII uppercase letters and digits only.
- Build a 6x6 Polybius square from a random permutation of A-Z and 0-9, and display it.
- Select a random key word (7-12 letters, no repeated characters) from unixdict.txt and display it.
- Use a 9-letter key to encrypt the plaintext "ATTACKAT1200AM", then decrypt the cipher text, displaying both results.
- Handle a final short transposition row using either columnar-transposition convention.

## Language Coverage
29 languages implement this task, spanning systems and assembly languages, scripting languages, and array/functional languages. Representative entries include C++, C#, Rust, Go, Java, Python, Perl, Raku, Julia, Nim, and APL.

## Connections
- [[PolybiusSquare]] — the 6x6 substitution grid that fractionates each character into a letter pair
- [[ColumnarTransposition]] — the keyed reordering step applied after substitution
- [[SubstitutionCipher]] — the first stage of the two-phase scheme
- [[Cryptography]] — the broader field this WWI field cipher belongs to
- [[Fractionation]] — splitting each plaintext symbol across multiple cipher symbols

## Contradictions
- None — reference task page.
