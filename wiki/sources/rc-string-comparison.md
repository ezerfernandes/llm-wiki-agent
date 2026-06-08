---
title: "String comparison (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/String_comparison
---

## Summary
This task asks the programmer to demonstrate how a language compares two strings, both for equality and for lexical ordering. The key insight is that string comparison spans several distinct axes — exact equality vs. inequality, lexical before/after ordering, case sensitivity, and the treatment of numeric strings — and that languages differ in whether their comparison operators are generic/polymorphic (semantics bend to argument types) or coercive/allomorphic (arguments are forced to behave like strings).

## Task Requirements
- Compare two strings for exact equality.
- Compare two strings for inequality (inverse of exact equality).
- Determine whether one string is lexically ordered before another.
- Determine whether one string is lexically ordered after another.
- Show both case-sensitive and case-insensitive comparison.
- Show how the language handles numeric strings when not compared lexically.
- Demonstrate any other comparison kinds the language offers, e.g. generic/polymorphic vs. coercive/allomorphic comparison.

## Language Coverage
107 languages implement this task, reflecting its status as a fundamental, near-universal operation across the language landscape. Representative entries include C, C++, Java, Python, JavaScript, Go, Rust, Haskell, Raku, and Common Lisp, ranging from low-level assembly (ARM, RISC-V) to high-level functional and scripting languages.

## Connections
- [[StringProcessing]] — core domain of the task
- [[LexicographicOrder]] — the ordering relation used for before/after comparison
- [[CaseSensitivity]] — distinguishing case-sensitive from case-insensitive comparison
- [[TypeCoercion]] — coercive/allomorphic comparison forces arguments toward string type
- [[Polymorphism]] — generic comparison operators whose semantics depend on argument types

## Contradictions
- None — reference task page.
