---
title: "Binary strings (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Binary_strings
---

## Summary
This task asks the programmer to build a set of functions for handling binary-safe strings — strings made of arbitrary bytes, including embedded null bytes — in languages that lack built-in support for them. The key insight is that many languages assume text strings are NUL-terminated or Unicode, so working with raw byte sequences requires either a dedicated byte-buffer type or careful manual length tracking. Languages that already support binary strings should demonstrate an equivalent implementation of the requested operations.

## Task Requirements
- Provide string creation and destruction (including manual memory management where there is no garbage collection)
- Support string assignment
- Support string comparison
- Support string cloning and copying
- Check whether a string is empty
- Append a byte to a string
- Extract a substring from a string
- Replace every occurrence of a byte or substring with another string
- Join strings together

## Language Coverage
78 languages implement this task, spanning low-level assembly and systems languages where byte buffers must be managed by hand up through high-level languages with native binary-safe types. Representative implementations include C, Rust, Go, Java, Python, Haskell, Ada, Perl, Ruby, and 8086 Assembly.

## Connections
- [[StringProcessing]] — the task is a survey of core string operations
- [[ByteArray]] — binary strings are sequences of arbitrary bytes
- [[MemoryManagement]] — manual allocation and destruction are required in non-GC languages
- [[SubstringSearch]] — needed for the replace-every-occurrence operation
- [[NullTerminatedString]] — the C convention that binary strings must avoid

## Contradictions
- None — reference task page.
