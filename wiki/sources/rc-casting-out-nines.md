---
title: "Casting out nines (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic, checksums]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Casting_out_nines
---

## Summary
A three-part task built around "casting out nines," the classic digit-sum technique for computing a number's least positive residue modulo 9. The key insight is that this checksum is invariant under operations that only rearrange digits, so it can cheaply filter candidates: any Kaprekar number k satisfies co9(k) == co9(k^2), and the test generalizes from base 9 to any base by reducing modulo (Base - 1).

## Task Requirements
- Part 1: Implement a procedure co9(x) returning the casting-out-nines checksum (least positive residue mod 9), ideally via repeated digit-summing rather than a built-in modulo operator.
- Part 2: Use the checksum to generate/filter a range of numbers where co9(k) == co9(k^2); show this subset is a small fraction of the range yet contains every Kaprekar number in it.
- Part 3: Generalize to arbitrary bases, filtering on k % (Base-1) == (k^2) % (Base-1), and demonstrate the same small-subset / Kaprekar-coverage property.

## Language Coverage
58 languages implement this task, spanning systems, scripting, functional, and assembly families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, J, Raku, Fortran, and 360 Assembly.

## Connections
- [[ModularArithmetic]] — the checksum is reduction modulo 9 (or Base-1)
- [[DigitalRoot]] — repeated digit-summing yields the same residue
- [[KaprekarNumbers]] — the co9(k) == co9(k^2) filter captures all Kaprekar numbers in a range
- [[NumberTheory]] — divisibility and residue properties underpin the method
- [[Checksums]] — casting out nines is a historical error-detection checksum

## Contradictions
- None — reference task page.
