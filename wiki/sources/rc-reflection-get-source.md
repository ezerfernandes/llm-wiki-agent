---
title: "Reflection/Get source (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reflection, metaprogramming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Reflection/Get_source
---

## Summary
This task asks the programmer to use a language's reflection facilities to recover, at runtime, the source code (or the file path and line number) where a programming object — such as a module, class, function, or method — is defined. The key insight is that introspection must expose not just an object's value or type but also its provenance, which many languages preserve only when source or debug metadata is available.

## Task Requirements
- Given a programming object (module, class, function, or method), obtain its defining source code, or alternatively the file path and line number where it is defined.

## Language Coverage
26 languages implement this task, spanning dynamic scripting languages with rich introspection, JVM languages, and a few systems and assembly languages. Representative implementations include Python, Ruby, Perl, Raku, JavaScript, Java, C#, Go, Julia, and Tcl. Notably, C, C++, and Rust are explicitly omitted as lacking the required reflection.

## Connections
- [[Reflection]] — runtime inspection of program structure that this task exercises
- [[Metaprogramming]] — programs examining and manipulating their own definitions
- [[Introspection]] — querying an object's type, name, and defining location
- [[DebugMetadata]] — symbol/line information that makes source retrieval possible

## Contradictions
- None — reference task page.
