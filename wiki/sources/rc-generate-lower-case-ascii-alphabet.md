---
title: "Generate lower case ASCII alphabet (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, ascii]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Generate_lower_case_ASCII_alphabet
---

## Summary
The task asks the programmer to produce a sequence (array, list, lazy sequence, or indexable string) of all 26 lowercase ASCII letters from `a` to `z`. Where a standard library already exposes such a sequence, the solution should show how to access it, but must also demonstrate how to generate one programmatically. The key insight is that hand-typing the alphabet is error-prone — the task even highlights a Tcl example that silently omits `l`, which is hard to catch in code review.

## Task Requirements
- Generate all lowercase ASCII characters from `a` through `z`.
- The result may be an array, list, lazy sequence, or indexable string.
- If a standard library constant exists (e.g. Python's `string.ascii_lowercase`), show how to access it.
- Regardless of any library shortcut, also show how to generate an equivalent sequence.
- Use reliable, strongly-typed coding suitable for a large program; avoid enumerating the letters manually.

## Language Coverage
163 languages implement this task, spanning everything from low-level assembly to high-level scripting and functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Lisp, and 8086 Assembly.

## Connections
- [[AsciiEncoding]] — the task relies on the contiguous numeric ordering of lowercase letters in the ASCII table.
- [[CharacterRange]] — generating `a`..`z` is a canonical character-range construction.
- [[StringManipulation]] — the parent category for this task.
- [[OffByOneError]] — manual enumeration risks omission bugs, the cautionary point the task makes.

## Contradictions
- None — reference task page.
