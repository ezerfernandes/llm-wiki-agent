---
title: "Constrained genericity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, type-system, generics, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Constrained_genericity
---

## Summary
This task demonstrates constrained genericity (also called bounded quantification): a parametrized type or function that can only be instantiated on types satisfying some condition, even if the condition isn't actually exercised inside the body. The programmer defines an "eatable" property as the ability to call an `eat` function, then writes a generic `FoodBox` container that may only hold eatable types — without ever calling `eat` itself. The key insight is that the constraint is purely a compile-time (or contract) restriction expressed through the language's type system, keeping the eatable specification as minimal and generic as the language allows.

## Task Requirements
- Define what makes a type "eatable" — namely that an `eat` function/method can be called on it.
- Write a generic container type `FoodBox` parametrized over an element type that can only be instantiated on eatable types.
- `FoodBox` must NOT use `eat` in any way; without the explicit constraint it would otherwise accept any type.
- Make the eatable specification as generic as possible, with minimal restrictions on eatable implementations.
- Explain whatever restrictions the language imposes on implementing eatable types.
- Show at least one concrete example of an eatable type.

## Language Coverage
44 languages implement this task, spanning statically typed OO and functional languages with rich type-constraint mechanisms (interfaces, traits, type classes, concepts, contracts) down to dynamic languages that emulate the constraint. Representative examples include Ada, C++, C#, Eiffel, Haskell, Java, OCaml, Rust, Scala, Swift, Go, and Python.

## Connections
- [[ParametricPolymorphism]] — constrained genericity is parametric polymorphism with added type bounds
- [[BoundedQuantification]] — the formal type-theory name for restricting type parameters
- [[TypeSystem]] — the constraint is enforced by the language's type checker
- [[Generics]] — `FoodBox` is a generic container parametrized over its element type
- [[Interface]] — the common mechanism (interfaces, traits, type classes, concepts) used to express the eatable requirement

## Contradictions
- None — reference task page.
