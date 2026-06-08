---
title: "Reflection/List methods (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reflection, object-oriented, metaprogramming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Reflection/List_methods
---

## Summary
This task asks the programmer to retrieve the methods of an object using reflection, returning them as names, as values (callable references), or both. The key insight is that languages with dynamic dispatch may expose methods only through a class's public introspection API, so listing them requires querying the runtime's metadata facilities rather than parsing source code.

## Task Requirements
- Obtain the methods of an object via reflection.
- Present those methods as their names, their values (callable handles), or both.
- For languages offering dynamic methods, inspect them only when the class's public API provides a way to enumerate them.

## Language Coverage
36 languages implement this task, spanning managed/VM languages with rich introspection (Java, C#, Kotlin, Scala), dynamic scripting languages (Python, Ruby, Perl, JavaScript, PHP, Lua), and others such as Go, Julia, Nim, Clojure, Raku, and Tcl. Several low-level and minimalist languages (C, C++, Rust, and various assemblies) are explicitly omitted for lacking reflection.

## Connections
- [[Reflection]] — the core runtime introspection capability the task exercises.
- [[Metaprogramming]] — listing methods at runtime is a metaprogramming operation.
- [[ObjectOrientedProgramming]] — methods belong to objects/classes, the unit being inspected.
- [[DynamicDispatch]] — dynamic/unknown methods are reachable only through public listing APIs.

## Contradictions
- None — reference task page.
