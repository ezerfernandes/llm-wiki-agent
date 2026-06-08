---
title: "Substitution cipher (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Substitution_cipher
---

## Summary
This task asks the programmer to implement a classic substitution cipher: encrypt a source file by replacing every upper- and lower-case alphabetic character with a predetermined substitute character (another letter or symbol), writing the result to an output file. The same fixed mapping is then inverted to decrypt the output back into the original text. The key insight is that the cipher is just a fixed, reversible one-to-one character mapping (a permutation of the alphabet), so decryption simply applies the inverse lookup table.

## Task Requirements
- Read an input/source file.
- Encrypt it by mapping each upper/lower case alphabet character to another predetermined letter or symbol, saving to an encrypted output file.
- Decrypt that encrypted file back into the original text using the inverse mapping.

## Language Coverage
59 languages implement this task, spanning systems languages, scripting languages, and several assembly variants. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Ruby, and ARM Assembly.

## Connections
- [[SubstitutionCipher]] — the cryptographic scheme this task implements
- [[CaesarCipher]] — a special case of substitution where the mapping is a fixed alphabetic shift
- [[Rot13]] — a self-inverse substitution cipher rotating letters by 13 positions
- [[StringManipulation]] — character-by-character transformation over file contents
- [[Cryptography]] — the broader field of encryption and decryption techniques

## Contradictions
- None — reference task page.
