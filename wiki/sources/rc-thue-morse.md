---
title: "Thue-Morse (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Thue-Morse
---

## Summary
The task asks the programmer to generate the Thue-Morse sequence, a binary sequence (0, 1, 1, 0, 1, 0, 0, 1, ...) that is famously non-repeating in a structured way. The key insight is that each term equals the parity of the number of 1-bits in the index's binary representation, and the sequence can be built iteratively by repeatedly appending the bitwise complement of the string produced so far.

## Task Requirements
- Create/generate the Thue-Morse sequence.
- Display a prefix of the sequence (implementations typically print the first several terms or iterations).

## Language Coverage
100 languages implement this task, spanning low-level assembly, mainstream high-level languages, and esoteric/functional dialects. Representative examples include C, C++, Java, Python, Rust, Go, Haskell, Common Lisp, Perl, and APL.

## Connections
- [[ThueMorseSequence]] — the specific automatic sequence being generated
- [[BinaryNumbers]] — terms derive from the binary digit representation of indices
- [[ParityBit]] — each term is the parity (even/odd count) of set bits in the index
- [[StringConcatenation]] — the iterative construction appends a complemented copy each step
- [[Recursion]] — the sequence has a natural self-referential/recursive definition

## Contradictions
- None — reference task page.
