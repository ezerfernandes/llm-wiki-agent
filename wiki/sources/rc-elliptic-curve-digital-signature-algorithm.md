---
title: "Elliptic Curve Digital Signature Algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, number-theory, elliptic-curves]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm
---

## Summary
The task asks the programmer to implement a "toy" version of ECDSA over an elliptic curve E defined by y² = x³ + ax + b modulo a prime p, choosing parameters small enough to fit standard integer types. It requires building the elliptic-curve point group (addition, doubling, and the point at infinity), then layering key generation, signature computation, and verification on top. The key insight is that the scheme's security rests on the intractability of the elliptic curve discrete logarithm problem (ECDLP), and that group arithmetic over a finite field underlies the whole construction.

## Task Requirements
- Implement elliptic-curve point addition and doubling over ℤp, with the identity element 𝒪 (point at infinity).
- ECDSA key generation: pick curve E, base point G of large prime order r, random private key s, public key W = sG.
- Signature: given hash f = H(m), pick random u, compute V = uG, c ≡ xV mod r, d ≡ u⁻¹(f + s·c) mod r; signature is (c, d).
- Verification: compute h ≡ d⁻¹ mod r, h1 ≡ f·h, h2 ≡ c·h, then h1·G + h2·W = (x1, y1), accept iff c ≡ x1 mod r.
- No hash function or key export needed — use a sample hash value plus a way to tamper with it to demonstrate failure.
- Be lenient with a composite modulus (may illustrate elliptic-curve factorization) but strict where required: a point G not on E must always fail.

## Language Coverage
16 languages implement this task, a moderate-breadth set skewed toward systems and general-purpose languages comfortable with modular and big-integer arithmetic. Representative implementations include C, C++, C#, Go, Java, Python, Rust, Julia, Perl, Raku, Nim, and Zig.

## Connections
- [[EllipticCurveCryptography]] — the cryptosystem family this task instantiates.
- [[DigitalSignature]] — the primitive ECDSA realizes for message authentication.
- [[ModularArithmetic]] — point operations are computed over ℤp, requiring modular inverses.
- [[DiscreteLogarithmProblem]] — the ECDLP whose hardness underpins security.
- [[FiniteFieldGroup]] — the point group E(ℤp) structure that all operations live in.

## Contradictions
- None — reference task page.
