---
title: "Exponentiation operator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arithmetic, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Exponentiation_operator
---

## Summary
This task asks the programmer to re-implement integer exponentiation from scratch rather than relying on a language's built-in power function. Both an `int^int` variant and a `float^int` variant must be implemented, each exposed both as a procedure and as an operator (where the language supports defining operators). The key insight is exercising operator/procedure overloading so a single name dispatches correctly on the differing base types.

## Task Requirements
- Re-implement integer exponentiation (do not use the built-in operator) for both `int^int` and `float^int`.
- Provide each variant as a procedure.
- Provide each variant as an operator, if the language supports operator definition.
- If the language supports overloading, supply an overloaded form covering both the `int^int` and `float^int` variants.

## Language Coverage
105 languages implement this task, spanning systems languages, functional languages, scripting languages, and assembly. Representative implementations include C, C++, C#, Rust, Haskell, OCaml, Python, Ruby, Perl, Java, Scala, and Common Lisp.

## Connections
- [[Exponentiation]] — the core arithmetic operation being reimplemented
- [[OperatorOverloading]] — providing one operator for multiple base types
- [[ExponentiationBySquaring]] — efficient algorithm commonly used for integer powers
- [[NumericTypes]] — distinguishing `int` versus `float` base handling

## Contradictions
- None — reference task page.
