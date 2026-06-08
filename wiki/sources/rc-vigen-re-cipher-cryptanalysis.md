---
title: "Vigenère cipher/Cryptanalysis (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, frequency-analysis]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Vigenère_cipher/Cryptanalysis
---

## Summary
Given a block of text encrypted with a Vigenère cipher, recover both the key and the plaintext using only the ciphertext. The standard approach first estimates the key length (e.g. via index of coincidence or Kasiski examination), then treats each key-length column as a separate Caesar shift and solves it with English letter-frequency analysis. The task supplies a long sample ciphertext, since these statistical methods only become reliable with enough text.

## Task Requirements
- Take only the ciphertext as input; it is all uppercase, has no punctuation, but may contain whitespace.
- Assume the plaintext is English.
- Find and output the recovered key.
- Use that key to decrypt and output the original plaintext (preserving whitespace is optional).
- The algorithm need not be perfect but should succeed on sufficiently long ciphertext.

## Language Coverage
31 languages implement this task, spanning systems languages, scripting languages, functional languages, and even hand-written assembly. Representative solutions include C, C++, Rust, Go, Zig, Python, Perl, Raku, Haskell, OCaml, Java, and ARM/AArch64 Assembly.

## Connections
- [[VigenereCipher]] — the polyalphabetic cipher being broken
- [[FrequencyAnalysis]] — solving each column as a Caesar shift via letter frequencies
- [[IndexOfCoincidence]] — statistical measure used to estimate key length
- [[KasiskiExamination]] — detecting repeated segments to deduce key length
- [[Cryptanalysis]] — the broader discipline of breaking ciphers

## Contradictions
- None — reference task page.
