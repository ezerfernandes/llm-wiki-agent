---
title: "Visitor pattern (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, design-patterns, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Visitor_pattern
---

## Summary
This task asks the programmer to demonstrate the Visitor design pattern, a way of separating an algorithm from the object structure it operates on so new operations can be added without modifying the structures. The key insight is double dispatch: an element exposes an `accept` method that calls back into the matching `visit` method on a visitor, letting behavior live in the visitor rather than the element classes. The task suggests translating one of the Wikipedia examples (C#, Smalltalk, Go, Java, Common Lisp, or Python).

## Task Requirements
- Implement the Visitor pattern by translating one or more of the Wikipedia examples into your language.
- If your language already has an example, translate a different Wikipedia example instead.
- Define visitor classes with a `visit` method per element type, and element classes with an `accept` method that dispatches to the visitor.
- Composite elements should iterate over children, calling each child's `accept`.
- If the language lacks OO support, emulate the pattern's intent and reproduce the same output as a Wikipedia example.

## Language Coverage
15 languages implement this task, spanning OO-native languages and more procedural ones that emulate the pattern. Representative implementations include Ada, C++, Java, Python, Rust, JavaScript, Julia, Nim, Raku, and Wren.

## Connections
- [[VisitorPattern]] — the Gang of Four design pattern this task implements
- [[DesignPatterns]] — the broader catalog of reusable OO solutions
- [[DoubleDispatch]] — the dispatch mechanism that makes the pattern work
- [[OpenClosedPrinciple]] — the SOLID principle the pattern follows
- [[ObjectOrientedProgramming]] — the paradigm the task targets

## Contradictions
- None — reference task page.
