---
title: "One-time pad (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/One-time_pad
---

## Summary
Implement a one-time pad cipher for encrypting and decrypting letter-only messages. The pad is a file of truly random key material (ideally sourced from something like /dev/random); encryption and decryption are the same Vigenère-style operation, since combining plaintext with a random key as long as the message yields information-theoretically perfect secrecy when each key is used exactly once. The key insight is that true randomness and never reusing key material are what make the scheme unbreakable.

## Task Requirements
- Generate one-time pad data given a user-specified filename and length, using true random numbers.
- Encrypt and decrypt messages using key material read from the pad file (reusing Vigenère cipher logic; the two operations are essentially identical, like Rot-13).
- Optionally manage pad files: list, mark as used, and delete pads, tracking which pad serves which partner.
- Support a pad-file format with extension `.1tp`: lines starting with `#` are comment/metadata, lines starting with `-` are marked used, and whitespace within the pad data is ignored.

## Language Coverage
16 languages implement this task. Coverage spans systems and scripting languages alike, with representative solutions in C, Go, Haskell, Java, Julia, Kotlin, Python, Perl, Raku, and Tcl.

## Connections
- [[Cryptography]] — the task is a classic symmetric cipher exercise
- [[OneTimePad]] — the specific information-theoretically secure scheme implemented
- [[VigenereCipher]] — the underlying combining operation reused for encrypt/decrypt
- [[RandomNumberGeneration]] — true randomness from sources like /dev/random is essential
- [[Rot13]] — cited as an example of a self-inverse substitution operation

## Contradictions
- None — reference task page.
