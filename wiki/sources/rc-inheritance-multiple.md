---
title: "Inheritance/Multiple (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented, type-system]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Inheritance/Multiple
---

## Summary
This task asks the programmer to demonstrate multiple inheritance, where one class derives from several base classes at once. The concrete exercise is to define two classes (or interfaces) `Camera` and `MobilePhone`, then a `CameraPhone` class that is simultaneously both. No methods need to be implemented — the point is purely to show how each language expresses (or restricts) inheriting from more than one parent.

## Task Requirements
- Define two classes or interfaces named `Camera` and `MobilePhone`.
- Define a `CameraPhone` class that is both a `Camera` and a `MobilePhone`.
- No function bodies or behavior need to be implemented.

## Language Coverage
70 languages implement this task, spanning languages with true multiple inheritance, interface-only inheritance, and mixin-based workarounds. Representative examples include C++, Python, Common Lisp, Eiffel, Perl, Ruby, Scala, Java, C#, and Go — illustrating that some allow inheriting arbitrary classes while others restrict it to interfaces or traits.

## Connections
- [[MultipleInheritance]] — the core language feature being demonstrated.
- [[ObjectOrientedProgramming]] — the paradigm in which inheritance lives.
- [[Inheritance]] — the general subclassing relationship this extends.
- [[Mixins]] — the trait/mixin alternative many languages use instead.
- [[DiamondProblem]] — the ambiguity that arises when multiple parents share an ancestor.

## Contradictions
- None — reference task page.
