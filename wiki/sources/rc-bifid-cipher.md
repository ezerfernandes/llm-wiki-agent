---
title: "Bifid cipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bifid_cipher
---

## Summary
Implement encryption and decryption for the Bifid cipher, a polygraphic substitution cipher invented by Félix Delastelle around 1901. It combines a 5x5 Polybius square with transposition and fractionation: each letter is mapped to row/column coordinates, the coordinates are written vertically then read off horizontally, and the regrouped pairs are looked back up in the square. The key insight is fractionation — splitting and recombining coordinates spreads each plaintext letter's information across the ciphertext.

## Task Requirements
- Write routines to encrypt and decrypt a message using the Bifid cipher.
- Since a 5x5 square has only 25 cells for 26 letters, merge two letters into one cell (commonly I and J).
- Verify round-trip (encrypt then decrypt) on: the worked "ATTACKATDAWN" example; the Wikipedia article's message and square; and the first example using the Wikipedia square, showing the square choice is arbitrary as long as it is consistent.
- Encrypt and decrypt "The invasion will start on the first of January" with any square, uppercasing and ignoring spaces.
- Bonus: suggest a modification so that all 26 letters can be uniquely encrypted.

## Language Coverage
41 languages implement this task, spanning assembly, systems, scripting, and functional styles. Representative implementations include C++, C#, Java, Python, Rust, Go, Haskell, Perl, Raku, Julia, and several assembly variants (AArch64, ARM).

## Connections
- [[SubstitutionCipher]] — Bifid is a polygraphic substitution cipher.
- [[PolybiusSquare]] — the 5x5 grid mapping letters to coordinate pairs.
- [[Cryptography]] — classical encryption technique.
- [[PlayfairCipher]] — related Polybius-square-based cipher (named related task).
- [[Transposition]] — the fractionation/regrouping step that diffuses letters.

## Contradictions
- None — reference task page.
