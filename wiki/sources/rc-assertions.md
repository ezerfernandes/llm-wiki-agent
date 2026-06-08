---
title: "Assertions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, error-handling, debugging]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Assertions
---

## Summary
This Rosetta Code task asks the programmer to demonstrate an assertion: a runtime check that halts execution (or raises an error) when a condition is violated. The concrete demonstration is to assert that an integer variable equals 42. The key insight is that assertions express invariants the programmer believes must hold; depending on the language they either throw an exception or trigger a break point when the assumption fails.

## Task Requirements
- Show an assertion in your language.
- The assertion must verify that an integer variable is equal to 42.
- Convey how the language reacts when the assertion fails (exception, abort, or break point).

## Language Coverage
129 languages implement this task, reflecting how nearly every language offers some built-in or idiomatic assertion mechanism. Representative implementations include C, C++, Java, Python, Rust, Go, Ruby, Perl, Haskell, and Ada.

## Connections
- [[DefensiveProgramming]] — assertions encode invariants to catch unexpected states early.
- [[ExceptionHandling]] — many languages implement a failed assertion by throwing an exception.
- [[DesignByContract]] — preconditions, postconditions, and invariants are assertion-based contracts (notably in Eiffel).
- [[Debugging]] — assertions serve as in-code checks that surface bugs during development.

## Contradictions
- None — reference task page.
