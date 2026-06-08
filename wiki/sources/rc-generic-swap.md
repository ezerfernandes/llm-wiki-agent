---
title: "Generic swap (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, generics, language-semantics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Generic_swap
---

## Summary
The task is to write a generic swap function or operator that exchanges the values of two variables (or any two assignable storage locations) regardless of their type. The key insight is that this exercise probes several deep language-semantics issues at once: how a language expresses genericity, whether it permits destructive mutation of variables, and how it provides indirection over storage locations. The two variables may be constrained to a mutually compatible type if the language's type system requires it.

## Task Requirements
- Implement a function or operator that swaps the values held in two variables/storage places.
- The swap must work generically, independent of the values' specific types.
- For statically typed languages, describe how the language provides genericity (e.g., parametric polymorphism, templates).
- It is permissible to constrain both variables to a mutually compatible type so each can hold the other's prior value without a type violation.
- The swap should destructively update the original storage locations (requiring indirection or reference/pointer semantics).

## Language Coverage
172 languages implement this task, spanning the full spectrum from low-level assembly to high-level functional and dynamic languages. Representative implementations include C, C++, Rust, Java, Python, Haskell, Common Lisp, Ada, Go, OCaml, and Forth, each highlighting its own approach to genericity and in-place mutation.

## Connections
- [[ParametricPolymorphism]] — how statically typed languages achieve type-independent swapping.
- [[Generics]] — the broad mechanism the task exercises.
- [[TupleAssignment]] — destructuring/parallel assignment (`a, b = b, a`) is the idiomatic swap in many languages.
- [[ReferenceSemantics]] — indirection over storage places needed for destructive in-place swaps.
- [[TypeSystem]] — type compatibility constraints that govern what may be exchanged.

## Contradictions
- None — reference task page.
