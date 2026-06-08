---
title: "Sealed classes and methods (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented-programming, inheritance]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sealed_classes_and_methods
---

## Summary
A sealed (or final) class is one that cannot be inherited from, and a sealed method is one that cannot be overridden in subclasses. Authors seal classes or methods when subclassing would be undesirable, and compilers can exploit the guarantee to perform optimizations such as devirtualizing method calls. The task asks each language to describe its support for this restriction, or how to simulate it when no native support exists.

## Task Requirements
- For object-oriented languages, explain what support exists for sealed/final classes and/or methods.
- If there is no native support, describe what can be done to simulate the behavior.
- Illustrate the answer with an example where possible.
- For non-OO languages (or those lacking inheritance), simply say so, omit the task, or describe equivalent structures and restrictions.

## Language Coverage
13 languages implement this task, spanning compiled OO languages with first-class support (Java's `final`, C++'s `final`, V) and languages that must simulate sealing through idioms or private constructors (C, Go, Julia, Python, Raku). Representative entries include C, C++, Go, Java, Julia, Nim, Python, Raku, and Wren.

## Connections
- [[ObjectOrientedProgramming]] — the paradigm whose inheritance feature this task restricts
- [[Inheritance]] — sealing is a deliberate prohibition on subclassing
- [[MethodOverriding]] — sealed methods cannot be overridden by subclasses
- [[Encapsulation]] — sealing constrains how a class may be extended or reused

## Contradictions
- None — reference task page.
