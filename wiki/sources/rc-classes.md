---
title: "Classes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented-programming, inheritance, polymorphism]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Classes
---

## Summary
This task asks the programmer to define a basic class in their language and demonstrate the core building blocks of object-oriented programming. The page frames a class formally as the transitive closure of types related by inheritance, rooted at a base type whose operations (methods) can be polymorphic. The key insight is that method dispatch — choosing a type-specific implementation based on a value's most specific type tag — distinguishes single-dispatch languages (one controlling argument, usually written `x.f()`) from multiple-dispatch ones.

## Task Requirements
- Create a basic class.
- Give the class at least one method.
- Give the class a constructor.
- Give the class an instance variable.
- Show how to instantiate (create an object of) the class.

## Language Coverage
129 languages implement this task, reflecting that classes are a near-universal feature spanning OO, functional, and even assembly languages. Representative entries include Java, C++, C#, Python, Ruby, Smalltalk, Common Lisp, Ada, OCaml, Rust, and Go.

## Connections
- [[ObjectOrientedProgramming]] — the paradigm this task exemplifies
- [[Inheritance]] — the relation that defines a class as a closure of types
- [[Polymorphism]] — methods and values that vary by specific type
- [[MethodDispatch]] — resolving the type-specific implementation via a value's type tag
- [[Encapsulation]] — bundling instance variables with their methods

## Contradictions
- None — reference task page.
