---
title: "Polymorphism (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented, classes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Polymorphism
---

## Summary
This task asks the programmer to model two related shapes — `Point(x, y)` and `Circle(x, y, r)` — as classes and exercise the full machinery of object lifecycle and dispatch. The central idea is a polymorphic `print` operation that behaves differently depending on the actual object type, demonstrating how dynamic dispatch lets the same call site work across a class hierarchy.

## Task Requirements
- Define a `Point(x, y)` class and a `Circle(x, y, r)` class.
- Provide a polymorphic `print` function/method that dispatches on the concrete type.
- Supply accessors (getters) for the coordinates `x`, `y` and the radius `r`.
- Implement a copy constructor, an assignment operator/method, and a destructor.
- Provide every possible default constructor for the classes.

## Language Coverage
78 languages implement this task, spanning classic OOP languages, functional languages with object systems, and BASIC dialects — reflecting how differently each ecosystem handles construction, copying, and dispatch. Representative implementations include C++, Java, C#, Python, Ruby, Smalltalk, Common Lisp, Haskell, OCaml, Swift, and Go.

## Connections
- [[ObjectOrientedProgramming]] — the paradigm the task exercises
- [[Polymorphism]] — the type-dependent dispatch the task is named for
- [[DynamicDispatch]] — the mechanism resolving `print` at runtime
- [[Inheritance]] — relating `Circle` to `Point` in many implementations
- [[Encapsulation]] — motivating the accessor methods

## Contradictions
- None — reference task page.
