---
title: "Main step of GOST 28147-89 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, feistel-network, block-cipher]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Main_step_of_GOST_28147-89
---

## Summary
GOST 28147-89 is a Soviet/Russian standard symmetric block cipher built on a Feistel network. The task asks the programmer to implement only its innermost building block — the "main step" — a function that takes a 64-bit text block plus one 32-bit subkey, applies modular addition, a 4-bit S-box substitution table, and a cyclic bit rotation, and returns the transformed block. The full cipher repeats this step 32 or 16 times across its encryption cycles.

## Task Requirements
- Implement the main step (single round function) of the GOST 28147-89 algorithm.
- Operate on a 64-bit block of text split into two 32-bit halves.
- Use one of the eight 32-bit key elements from the encryption key.
- Apply the substitution table: an 8x16 matrix of 4-bit values (S-boxes).
- Return the encrypted/transformed 64-bit block.

## Language Coverage
28 languages implement this task, a moderate spread spanning systems, scripting, and assembly languages. Representative implementations include C, C++, C#, Java, Go, Rust, Python, Perl, Raku, Julia, and X86 Assembly.

## Connections
- [[FeistelNetwork]] — the cipher structure the main step is a round of
- [[BlockCipher]] — GOST 28147-89 is a 64-bit symmetric block cipher
- [[SubstitutionBox]] — the 8x16 4-bit S-box table used in the step
- [[BitwiseOperations]] — modular addition and cyclic left rotation drive the round
- [[SymmetricKeyCryptography]] — the broader category this algorithm belongs to

## Contradictions
- None — reference task page.
