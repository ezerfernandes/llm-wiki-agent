---
title: "Undefined values (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-semantics, variables, null]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Undefined_values
---

## Summary
This task asks the programmer to demonstrate, in languages that have an explicit notion of an "undefined" value, the mechanisms for detecting and manipulating whether a variable's value is undefined. The key insight is that "undefined" is a distinct, first-class state in many languages — separate from zero, empty string, or even a typed null — and idioms for testing it vary widely (e.g. JavaScript's `undefined` vs `null`, Perl's `undef` and `defined()`, Python's lack of a built-in undefined requiring sentinels or `NameError` handling).

## Task Requirements
- Identify the language's explicit concept of an undefined value (if one exists).
- Exercise the mechanisms for checking whether a variable's value is undefined.
- Exercise the mechanisms for setting or clearing a variable back to the undefined state.

## Language Coverage
74 languages implement this task, spanning low-level assembly, scripting languages, functional languages, and BASIC dialects. Representative implementations include JavaScript, Perl, Python, Ruby, Lua, Haskell, C, Go, Rust, and Tcl.

## Connections
- [[NullValue]] — the related but distinct concept of an explicit null
- [[VariableScope]] — undefined often arises from unbound or out-of-scope names
- [[TypeSystems]] — how languages model the absence of a value
- [[SentinelValue]] — a common workaround in languages lacking a true undefined

## Contradictions
- None — reference task page.
