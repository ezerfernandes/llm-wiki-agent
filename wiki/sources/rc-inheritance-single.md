---
title: "Inheritance/Single (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented-programming, type-system]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Inheritance/Single
---

## Summary
This task asks the programmer to model single inheritance, where a derived type has exactly one parent. The concrete goal is to build a small class hierarchy that forms a tree: `Animal` at the root, `Dog` and `Cat` as its children, and `Lab` and `Collie` derived from `Dog`. The key insight is that with single inheritance the type relation forms a tree (a directed acyclic graph with one parent edge per node), as opposed to the more general graph permitted by multiple inheritance.

## Task Requirements
- Define a class hierarchy where each class inherits from exactly one superclass.
- Root class `Animal`; second level `Dog` and `Cat`; under `Dog` place `Lab` and `Collie`.
- Classes need no methods or behavior — only the inheritance (subclass) relationship must be expressed.
- Method overriding and behavioral polymorphism are explicitly out of scope (see the Polymorphism task).

## Language Coverage
102 languages implement this task, reflecting broad support across object-oriented and multi-paradigm languages. Representative implementations include Java, C++, C#, Python, Ruby, Smalltalk, Common Lisp, Eiffel, Go, Rust, Kotlin, and Haskell.

## Connections
- [[Inheritance]] — the core type-algebra operation this task demonstrates
- [[ObjectOrientedProgramming]] — the paradigm in which class hierarchies live
- [[LiskovSubstitutionPrinciple]] — substitutability of a derived type for its parents
- [[TypeSystem]] — single inheritance as a relation forming a tree of types
- [[Polymorphism]] — the companion task covering method overriding

## Contradictions
- None — reference task page.
