---
title: "Kolakoski sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sequences, self-reference, run-length-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kolakoski_sequence
---

## Summary
The task asks the programmer to generate the Kolakoski sequence — an infinite self-describing sequence of natural numbers whose own run-length counts reproduce the sequence itself. The key insight is the self-referential construction: an index `k` walks through the growing sequence `s`, and `s[k]` dictates how many times the most recently appended symbol should repeat, while symbols are drawn cyclically from a seed list such as `(1, 2)`.

## Task Requirements
- Implement a cycling routine that, given an ordered list like `(1, 2)`, returns successive items in a repeating cycle.
- Implement a generator that builds at least N members of the Kolakoski sequence from a seed list using the cycle routine and the self-referential algorithm.
- Implement a verifier that computes a sequence's run-length encoding and checks whether the sequence starts with its own RLE (ignoring the final RLE element due to sampling/truncation).
- Show the first 20 members for seeds `(1, 2)` and `(2, 1)`, and the first 30 members for `(1, 3, 1, 2)` and `(1, 3, 2, 1)`, checking each against its RLE.

## Language Coverage
32 languages implement this task, spanning systems languages, functional languages, scripting languages, and array/math languages. Representative implementations include C, C++, C#, Rust, Go, Haskell, Java, JavaScript, Python, Julia, Perl, Raku, J, and Wren.

## Connections
- [[SelfReferentialSequence]] — the sequence is defined by its own run-length structure
- [[RunLengthEncoding]] — RLE is both the defining property and the verification mechanism
- [[KolakoskiSequence]] — the specific integer sequence (OEIS A000002) named after William Kolakoski
- [[SequenceGeneration]] — incremental construction of an infinite sequence to a requested length

## Contradictions
- None — reference task page.
