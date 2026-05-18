---
title: "Statically Typed"
type: concept
tags: [programming-languages, type-systems]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Statically Typed

A **statically typed** language assigns each variable, expression, and function signature a type that is fixed and checked **at compile time** — before the program runs. [[CLanguage|C]] (per [[dis-1-1-getting-started|DIS Ch 1.1]]) is the wiki's canonical example: every variable must be declared with an explicit [[CPrimitiveType|type]] before it can be used, and the compiler rejects programs that violate the type rules.

## Consequences in the C track

- **Predictable memory layout.** The compiler can compute byte widths and offsets at compile time — see [[SizeOf]].
- **Operator semantics depend on type.** `/` is [[IntegerDivision|integer division]] when both operands are integers, real division when at least one is floating point — and the compiler picks the semantics from the static types of the operands.
- **No runtime type errors of the Python-style `TypeError` flavor.** Type mismatches fail at compile time.

## Contrast with dynamic typing

[[Python]] is the chapter's foil: variables come into existence on first assignment and carry a *runtime* type tag; `x = 1` and then `x = "hello"` is fine; type errors surface only when an operation is actually attempted. The trade-off C makes — friction at write time in exchange for compile-time safety and zero runtime type overhead — is the same trade-off Rust makes (and that ML-family languages like Haskell push further with full inference).

## Connections

- [[CLanguage]] — the canonical example in the wiki.
- [[VariableDeclaration]] — the syntactic surface where typing happens.
- [[CPrimitiveType]] — the type vocabulary.
- [[CompilationProcess]] — when the checking runs.
- [[Python]] — the dynamic-typed contrast.
- [[dis-1-1-getting-started]] — introducing source.
