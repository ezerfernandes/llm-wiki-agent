---
title: "String prepend (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/String_prepend
---

## Summary
This Rosetta Code task asks the programmer to take a string variable holding any text value and prepend a string literal to the front of it. The key insight is to highlight whether a language offers an idiomatic in-place prepend that avoids referencing the variable twice (e.g. a dedicated prepend operator or method) versus the common `var = literal + var` reassignment pattern. After the operation the variable's content is printed to illustrate the result.

## Task Requirements
- Create a string variable equal to any text value.
- Prepend the string variable with another string literal.
- If the language supports idiomatic ways to do this without referring to the variable twice in one expression, include those solutions.
- Display the variable's content to show the result.

## Language Coverage
123 languages implement this task, reflecting very broad coverage across paradigms — from low-level assembly to high-level scripting and functional languages. Representative examples include C, C++, Python, Java, JavaScript, Rust, Haskell, Perl, Ruby, and AArch64 Assembly.

## Connections
- [[StringManipulation]] — the core operation category this task belongs to.
- [[StringConcatenation]] — prepending is concatenation with operand order reversed.
- [[MutableVsImmutableStrings]] — whether in-place prepend is possible depends on string mutability.

## Contradictions
- None — reference task page.
