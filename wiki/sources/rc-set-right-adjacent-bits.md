---
title: "Set right-adjacent bits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bit-manipulation, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Set_right-adjacent_bits
---

## Summary
Given a fixed-width sequence of `e` bits (1 ≤ e ≤ 10000) and an integer `n`, the task is to set the `n` bits immediately to the right of every set bit, while preserving the original width `e`. The key insight is that the operation is a kind of rightward "smearing" or dilation of each 1-bit by `n` positions, with newly created bits not themselves triggering further propagation; an efficient implementation processes the original bits rather than iterating the smeared result.

## Task Requirements
- Implement a routine that sets the `n` bits to the right of any set bit in `b`, only where those positions exist within the width `e`.
- The routine must scale over the full given range of input widths `e`.
- Demonstrate the results for the provided example inputs (nibble cases with n=2, and the 66-bit input with n = 0, 1, 2, 3).
- Print output aligned so the binary input and output can be compared by eye.

## Language Coverage
27 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C++, Rust, Go, Nim, Java, Python, Perl, Raku, Julia, F#, J, and Wren.

## Connections
- [[BitManipulation]] — the operation works directly on individual bit positions.
- [[BitwiseOperations]] — shift-and-OR techniques implement the rightward propagation.
- [[Dilation]] — setting adjacent bits is a 1D morphological dilation of the set bits.
- [[StringProcessing]] — many solutions treat the bit field as a character string of '0'/'1'.

## Contradictions
- None — reference task page.
