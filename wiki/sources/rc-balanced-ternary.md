---
title: "Balanced ternary (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Balanced_ternary
---

## Summary
The task asks the programmer to implement balanced ternary, a base-3 numeral system whose digits take the values +1, 0, and −1 (written "+", "0", "−") rather than 0, 1, 2. The key insight is that this symmetric digit set lets a single representation express both positive and negative integers without a separate sign, since negation is simply flipping every "+" to "−" and vice versa.

## Task Requirements
- Support arbitrarily large integers, both positive and negative.
- Convert to and from text strings using the digits '+', '−', and '0'.
- Convert to and from the native integer type, signaling overflow if native integers cannot hold arbitrary length.
- Perform addition, negation, and multiplication directly on balanced ternary values without first converting to native integers.
- Keep the implementation reasonably efficient.
- Test case: build a from "+−0++0+", b from native integer −436, c from "+−++−"; print a, b, c in decimal, then compute a × (b − c) and print it in both ternary and decimal.

## Language Coverage
52 languages implement this task, spanning systems and functional languages as well as several BASIC and Lisp dialects. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Common Lisp, Racket, and Raku.

## Connections
- [[BalancedTernary]] — the numeral system the task is built around
- [[NumberBase]] — generalization to positional notation in arbitrary radices
- [[ArbitraryPrecisionArithmetic]] — required to support unbounded integer magnitudes
- [[RadixConversion]] — converting between base 3 and the native integer type
- [[ModularArithmetic]] — per-digit carry handling during addition and multiplication

## Contradictions
- None — reference task page.
