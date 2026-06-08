---
title: "Null object (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-semantics, type-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Null_object
---

## Summary
This task asks the programmer to demonstrate how their language represents the "null" (or "nil") object — the computer-science concept of an undefined or unbound value — and how to test whether an object is equivalent to it. The key insight is that null handling varies widely across languages: some expose an explicit null literal, some lack one entirely, and some distinguish null from genuinely undefined values while others conflate the two.

## Task Requirements
- Show how to access null in the language.
- Check whether an object is equivalent to the null object.
- Note that the task concerns "null"-like values, not whether a variable is defined (though the two may be related in some languages).

## Language Coverage
138 languages implement this task, reflecting how universal yet inconsistent null/nil semantics are across the programming landscape. Representative implementations include Python (None), Java, C#, JavaScript (null vs undefined), Common Lisp (nil), Haskell, Ruby, Go, Rust, and Smalltalk.

## Connections
- [[NullPointer]] — the runtime hazard this concept is associated with
- [[TypeSystem]] — how languages model the absence of a value
- [[OptionType]] — a safer alternative to nullable references
- [[EqualityComparison]] — testing an object against the null object

## Contradictions
- None — reference task page.
