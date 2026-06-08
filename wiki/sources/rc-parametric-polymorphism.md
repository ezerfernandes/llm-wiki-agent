---
title: "Parametric polymorphism (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, type-systems, generics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parametric_polymorphism
---

## Summary
Parametric polymorphism lets a programmer define types or functions that are generic over other types, using type variables in place of concrete types and substituting real types when needed. The task asks for a small example of a type declaration parametric over another type, plus a snippet (with its type signature) that uses it. The key insight is that one generic definition works uniformly across all element types without code duplication; this feature applies only to statically-typed languages.

## Task Requirements
- Declare a type that is parametric over another type (uses one or more type variables).
- A canonical example is a container such as a binary tree generic in its element type.
- Provide a short piece of code, together with its type signature, that operates on the generic type.
- A suggested example is a `map`-style function that traverses the tree and applies an operation to every element.

## Language Coverage
49 languages implement this task, spanning ML-family and functional languages with full type inference as well as mainstream generics-based and object-oriented languages. Representative implementations include Haskell, OCaml, Standard ML, F#, Rust, Scala, Swift, Java, C#, C++, and Go.

## Connections
- [[GenericProgramming]] — the broad discipline this task exemplifies
- [[TypeSystem]] — parametric polymorphism is a static type-system feature
- [[TypeInference]] — ML-family languages infer the generic signatures automatically
- [[BinaryTree]] — the suggested generic container example
- [[HigherOrderFunctions]] — the map function passed over the tree elements

## Contradictions
- None — reference task page.
