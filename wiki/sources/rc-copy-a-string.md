---
title: "Copy a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Copy_a_string
---

## Summary
This task asks the programmer to copy a string and, where the distinction is meaningful in the language, to differentiate between duplicating the actual contents of a string versus merely creating an additional reference (alias) to an existing string. The key insight is that the meaning of "copy" depends heavily on whether strings are mutable values or reference/pointer types in a given language, exposing how each language models memory, aliasing, and value semantics.

## Task Requirements
- Copy a string.
- Where relevant, distinguish between copying the contents of a string and making an additional reference to an existing string.

## Language Coverage
213 languages implement this task, an unusually broad set reflecting that string handling is fundamental across nearly every paradigm — from low-level assembly to high-level dynamic languages. Representative implementations include C, C++, Rust, Java, Python, Haskell, JavaScript, Common Lisp, Ada, and several assembly variants (x86, 6502, ARM).

## Connections
- [[StringProcessing]] — the core domain of the task
- [[ReferenceSemantics]] — distinguishing aliases from independent copies
- [[ValueSemantics]] — copying contents rather than sharing a reference
- [[ImmutableStrings]] — in languages with immutable strings, "copy" often collapses to a reference
- [[MemoryManagement]] — how copies are allocated and shared

## Contradictions
- None — reference task page.
