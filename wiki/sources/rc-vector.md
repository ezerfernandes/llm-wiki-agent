---
title: "Vector (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Vector
---

## Summary
This task asks the programmer to implement a Vector class (or set of functions) modeling a physical vector. The key insight is exposing the four basic vector operations through natural operator syntax along with a readable "pretty print" representation, encouraging idiomatic use of operator overloading where the language supports it.

## Task Requirements
- Implement a Vector type that models a physical vector.
- Allow initialization in any reasonable way (e.g. start/end points and direction, or angular coefficient and length/magnitude).
- Implement four operations: Vector + Vector (addition), Vector - Vector (subtraction), Vector * scalar (scalar multiplication), and Vector / scalar (scalar division).
- Provide a pretty-print function for display.

## Language Coverage
76 languages implement this task, spanning systems languages, functional languages, and dynamic scripting languages. Representative implementations include C, C++, C#, Rust, Go, Java, Haskell, Python, Ruby, Perl, Julia, and Wren.

## Connections
- [[LinearAlgebra]] — vectors are the foundational objects of the field
- [[OperatorOverloading]] — the natural way to expose +, -, *, / on a custom type
- [[DotProduct]] — a related vector operation linked from the task
- [[VectorSpace]] — the algebraic structure these operations satisfy

## Contradictions
- None — reference task page.
