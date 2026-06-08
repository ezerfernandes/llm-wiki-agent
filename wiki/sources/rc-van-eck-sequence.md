---
title: "Van Eck sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, self-referential-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Van_Eck_sequence
---

## Summary
The task asks the programmer to generate the Van Eck sequence (OEIS A181391), a self-referential integer sequence that starts at zero. Each term is determined by the previous one: if the previous term has never appeared before, the next term is 0; otherwise it is the number of steps back to its most recent prior occurrence. The key insight is that an efficient implementation tracks the last-seen index of every value (e.g. in a hash map) so each gap lookup is constant time.

## Task Requirements
- Create a function/procedure to generate the Van Eck sequence.
- The first term is zero.
- For each subsequent term: if the last term is new to the sequence, the next term is 0; otherwise it is how far back that last term previously occurred.
- Display the first ten terms of the sequence.
- Display terms 991 through 1000 of the sequence.

## Language Coverage
86 languages implement this task, spanning assembly, systems, scripting, functional, and array-oriented styles. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, APL, and AWK.

## Connections
- [[IntegerSequence]] — Van Eck is a self-referential integer sequence
- [[HashMap]] — efficient last-occurrence tracking uses a key-to-index map
- [[OEIS]] — catalogued as sequence A181391
- [[SelfReferentialSequence]] — each term depends on the history of prior terms

## Contradictions
- None — reference task page.
