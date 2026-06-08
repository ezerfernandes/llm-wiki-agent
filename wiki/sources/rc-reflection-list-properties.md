---
title: "Reflection/List properties (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reflection, metaprogramming, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Reflection/List_properties
---

## Summary
This task asks the programmer to use reflection to enumerate the properties of an object — retrieving them as names, values, or both. The key insight is that a language's reflection facilities (or its dynamic-property introspection API) must expose enough metadata at runtime to walk an object's attributes. Some languages support dynamic properties that can only be inspected when the class's public API explicitly offers a way to list them.

## Task Requirements
- Obtain the properties of an object using reflection.
- Expose those properties as names, as values, or as both.
- Where the language supports dynamic properties, inspect them only if the class's public API provides a listing mechanism.

## Language Coverage
39 languages implement this task, spanning statically-typed reflection-heavy platforms and dynamically-typed scripting languages. Representative implementations include C#, Java, Python, JavaScript, Ruby, Go, Kotlin, Perl, Raku, and Smalltalk. Notably, C, C++, and Rust are explicitly omitted as lacking the requisite runtime reflection.

## Connections
- [[Reflection]] — the core runtime introspection capability the task exercises
- [[Metaprogramming]] — listing properties is a form of treating program structure as data
- [[Introspection]] — examining an object's own structure and members at runtime
- [[ObjectOrientedProgramming]] — properties belong to objects/classes, the task's domain

## Contradictions
- None — reference task page.
