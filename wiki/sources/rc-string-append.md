---
title: "String append (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/String_append
---

## Summary
This task asks the programmer to demonstrate appending a string literal to an existing string variable in the most idiomatic way the language allows. The key distinction it highlights is in-place append (modifying a variable without naming it twice, e.g. via an append operator) versus plain concatenation that requires re-referencing the variable. After appending, the program shows the variable's contents.

## Task Requirements
- Create a string variable equal to any text value.
- Append another string literal to that variable in the most idiomatic way, avoiding a double reference to the variable if the language supports it.
- Display the contents of the variable after the append operation.

## Language Coverage
140 languages implement this task, spanning compiled, scripting, functional, and assembly languages, reflecting how universal string handling is. Representative examples include C, C++, Java, Python, JavaScript, Rust, Go, Haskell, Ruby, and Perl.

## Connections
- [[StringManipulation]] — the task is a basic data operation on strings.
- [[StringConcatenation]] — append is a specialized, in-place form of concatenation.
- [[MutabilityVsImmutability]] — idiomatic in-place append depends on whether the language's strings are mutable.
- [[AugmentedAssignment]] — many languages express the append via a compound operator like `+=` or `.=`.

## Contradictions
- None — reference task page.
