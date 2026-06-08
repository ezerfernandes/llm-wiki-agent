---
title: "Define a primitive data type (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, type-system, bounds-checking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Define_a_primitive_data_type
---

## Summary
This task asks the programmer to define a custom type that behaves like an integer but is constrained to the range 1 through 10 inclusive. The implementation must include all necessary bounds checking, or explain how the language's compiler or interpreter generates those checks automatically. It highlights how differently languages handle bounded subtypes: some (like Ada or Pascal) support range-constrained subtypes natively, while others require wrapping a value in a class or struct with explicit validation.

## Task Requirements
- Define a type that behaves like an integer.
- Enforce a lowest valid value of 1 and a highest valid value of 10.
- Include all bounds checking needed, or explain how the compiler/interpreter provides it.

## Language Coverage
65 languages implement this task, spanning statically typed languages with native range subtypes and dynamically typed languages that emulate the constraint at runtime. Representative implementations include Ada, ALGOL 68, C++, Haskell, Java, Python, Rust, Go, OCaml, Pascal, and Tcl.

## Connections
- [[TypeSystem]] — the task is categorized under type systems and explores constrained types.
- [[BoundsChecking]] — central to enforcing the 1–10 valid range.
- [[SubrangeType]] — languages like Ada and Pascal model this directly as a subrange.
- [[DataAbstraction]] — wrapping a primitive in a validating type encapsulates invariants.

## Contradictions
- None — reference task page.
