---
title: "Abstract type (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented-programming, type-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abstract_type
---

## Summary
This task asks the programmer to show how an abstract type — a type with no direct instances — can be declared in a given language. Abstract types serve as partial implementations meant to be derived from, and languages typically forbid instantiating them directly, forcing instantiation through a concrete descendant. The key distinction the task draws is between fully unimplemented abstract types (interfaces) and partially implemented ones, which some languages treat differently and others (e.g. with multiple inheritance) treat the same.

## Task Requirements
- Show how an abstract type can be declared in the language.
- If the language distinguishes between interfaces (no implementation) and partially implemented abstract types, illustrate both.

## Language Coverage
102 languages implement this task, reflecting how widely the abstract-type concept spans paradigms — from statically typed OO languages to functional and dynamic ones. Representative entries include Ada, C++, C#, Java, Python, Haskell, OCaml, Rust, Scala, Go, and Common Lisp.

## Connections
- [[ObjectOrientedProgramming]] — abstract types are a core OO mechanism for shared partial implementations
- [[Interface]] — an abstract type with no implementation at all
- [[Inheritance]] — concrete subclasses derive from and complete abstract types
- [[TypeSystem]] — abstract types and phantom types relate to static type checking and inference
- [[InformationHiding]] — abstract datatypes hide implementation behind a specification

## Contradictions
- None — reference task page.
