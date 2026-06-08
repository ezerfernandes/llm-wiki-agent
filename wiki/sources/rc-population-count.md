---
title: "Population count (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bit-manipulation, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Population_count
---

## Summary
The task asks for a function that returns the population count (Hamming weight) of a non-negative integer — the number of 1 bits in its binary representation. The key insight is that this single primitive also classifies integers as "evil" (even population count) or "odious" (odd population count), and many platforms expose it as a hardware instruction (e.g. POPCNT) or a built-in like `bin(n).count('1')`.

## Task Requirements
- Write a function/routine returning the population count of a non-negative integer.
- All generated lists are zero-indexed (start at 0).
- Display the pop count of the first thirty powers of 3 (3^0 through 3^29).
- Display the first thirty evil numbers (even pop count).
- Display the first thirty odious numbers (odd pop count).
- Print each list on one line, each set clearly identified.

## Language Coverage
101 languages implement this task, spanning low-level assembly, mainstream high-level languages, functional languages, and array/stack languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, APL, J, Forth, and 8080 Assembly.

## Connections
- [[HammingWeight]] — the population count is exactly the Hamming weight of the binary representation
- [[BitManipulation]] — implemented via bit shifts, masking, or hardware POPCNT
- [[BinaryNumberSystem]] — counts set bits in the base-2 form of an integer
- [[EvilAndOdiousNumbers]] — even vs. odd pop counts define these OEIS sequences (A001969, A000069)
- [[NumberTheory]] — relates to integer sequences catalogued in OEIS (A000120)

## Contradictions
- None — reference task page.
