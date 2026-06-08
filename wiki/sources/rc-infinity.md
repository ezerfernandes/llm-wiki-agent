---
title: "Infinity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, floating-point, ieee-754]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Infinity
---

## Summary
This task asks the programmer to write a function that tests whether positive infinity is supported for floating-point numbers and returns it if so; otherwise it returns the largest representable positive floating-point value. The test step can be skipped in languages whose specification already mandates infinity (e.g. those requiring IEEE 754 numbers). The key insight is recognizing how a language exposes infinity, either as a built-in constant or as the overflow result of arithmetic.

## Task Requirements
- Write a function that tests if floating-point infinity is supported (omit this step where the language spec already demands IEEE numbers).
- If infinity is supported, return positive infinity.
- Otherwise, return the largest possible positive floating-point number.
- For languages with multiple floating-point types, use the type of the literal constant `1.5`.

## Language Coverage
122 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Ada, Fortran, OCaml, and Scala.

## Connections
- [[FloatingPoint]] — the numeric domain the task operates on
- [[IEEE754]] — the standard that defines representations of infinity
- [[NumericLimits]] — relating to returning the largest representable value
- [[SpecialValues]] — infinity and NaN as distinguished floating-point states

## Contradictions
- None — reference task page.
