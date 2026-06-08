---
title: "Playfair cipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Playfair_cipher
---

## Summary
The task is to implement the Playfair cipher, a manual symmetric encryption technique that encrypts pairs of letters (digraphs) using a 5x5 key square built from a keyword. Because the square holds only 25 cells, two letters must share one slot, so the implementation must let the user choose between merging J with I or omitting Q. The key insight is that encryption operates on letter pairs positioned on the grid, with different rules depending on whether the pair shares a row, a column, or forms a rectangle.

## Task Requirements
- Implement both encryption and decryption with the Playfair cipher.
- Let the user choose either J = I or "no Q" to reduce the 26-letter alphabet to 25 cells.
- Output encrypted and decrypted messages as capitalized digraphs separated by spaces.
- Handle the standard digraph preparation (e.g., padding rules) so plaintext maps cleanly onto letter pairs.

## Language Coverage
36 languages implement this task, spanning systems, scripting, functional, and array languages — representative examples include C, C++, Rust, Go, Java, Python, Haskell, J, Perl, and Ruby.

## Connections
- [[PlayfairCipher]] — the named cipher this task implements
- [[Cryptography]] — the broader field of secure message encoding
- [[SubstitutionCipher]] — Playfair is a digraph substitution cipher
- [[StringProcessing]] — letter-pair preparation and grid lookups

## Contradictions
- None — reference task page.
