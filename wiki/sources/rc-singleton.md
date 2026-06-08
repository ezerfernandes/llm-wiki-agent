---
title: "Singleton (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, design-pattern, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Singleton
---

## Summary
The task is to implement a Global Singleton: a class for which only a single instance is ever permitted to exist within a running program. Any use of the class's non-static members operates on that one shared instance. The key insight is controlling instantiation so that repeated requests for the object always return the same instance, often via a private constructor plus a static accessor, with attention to thread-safe lazy initialization.

## Task Requirements
- Define a class that can have at most one instance during the program's lifetime.
- Route operations on non-static members through that single shared instance.
- Provide a controlled means of obtaining the instance (e.g., a static accessor) rather than free instantiation.

## Language Coverage
62 languages implement this task, spanning object-oriented, functional, and multi-paradigm ecosystems. Representative implementations include Java, C++, C#, Python, Ruby, Swift, Kotlin, Go, Scala, and Common Lisp, illustrating how each language enforces single-instance semantics differently.

## Connections
- [[SingletonPattern]] — the canonical design pattern this task realizes
- [[DesignPatterns]] — Singleton is one of the classic Gang of Four creational patterns
- [[ObjectOrientedProgramming]] — task is framed around class instantiation control
- [[LazyInitialization]] — common technique for deferring single-instance creation
- [[ThreadSafety]] — concurrency concern when guarding the unique instance

## Contradictions
- None — reference task page.
