---
title: "RSA code (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/RSA_code
---

## Summary
The task asks the programmer to implement the RSA public-key cipher from scratch — without calling a crypto library — to encrypt and decrypt short text messages. Given a key triple (n, e, d), a message is first encoded as numbers, then ciphertext is computed as C ≡ P^e mod n and recovered via P ≡ C^d mod n. The key insight is that RSA's security rests on the difficulty of factoring the modulus n into its two secret primes p and q, so a real demonstration requires big-integer arithmetic.

## Task Requirements
- Encrypt and decrypt a short message using RSA with a demonstration key.
- Implement RSA directly; do not call a cryptographic library.
- Encode/decode the message with any reversible scheme (ASCII or a=1..z=26 both acceptable).
- Either support blocking (splitting plaintext so each block is < n) or error out if blocking would be needed.
- Use a non-trivial key requiring large-integer support to show real-key viability (the page supplies a sample n, e=65537, d); library big-int code may be referenced but not reproduced.
- Messages may be hard-coded; show plaintext, intermediate numeric results, ciphertext, and the decrypted output.

## Language Coverage
41 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include Python, C, C#, Go, Rust, Haskell, Common Lisp, Java, Perl, Raku, Ruby, and Wren.

## Connections
- [[RSA]] — the public-key cryptosystem this task implements
- [[ModularExponentiation]] — the core operation C ≡ P^e mod n
- [[PublicKeyCryptography]] — the asymmetric encryption paradigm RSA exemplifies
- [[IntegerFactorization]] — the hard problem underpinning RSA's security
- [[ModularMultiplicativeInverse]] — how the private exponent d is derived from e

## Contradictions
- None — reference task page.
