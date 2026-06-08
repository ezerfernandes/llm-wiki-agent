---
title: "Sudan function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, number-theory, memoization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sudan_function
---

## Summary
The Sudan function is a classic recursive function defined over the non-negative integers, notable for being the first published example of a recursive function that is total but not primitive recursive. The task is to implement F(n, x, y) following its three-case recursive definition. Its rapid, nested-recursion growth (like the related Ackermann function) makes memoization a practical implementation concern.

## Task Requirements
- Implement a function that returns the value of the Sudan function F(x, y) (commonly indexed as F_n(x, y)).
- Honor the recursive definition: F_0(x, y) = x + y; F_{n+1}(x, 0) = x for n >= 0; and F_{n+1}(x, y+1) = F_n(F_{n+1}(x, y), F_{n+1}(x, y) + y + 1) for n >= 0.

## Language Coverage
60 languages implement this task, spanning low-level assembly and systems languages through functional and array languages. Representative entries include 8080 Assembly, C, C++, Rust, Go, Java, Haskell, OCaml, Python, J, APL, and Wren.

## Connections
- [[Recursion]] — defined by nested self-reference
- [[AckermannFunction]] — better-known sibling, also total but not primitive recursive
- [[PrimitiveRecursiveFunction]] — the class this function provably escapes
- [[Memoization]] — used to tame the function's explosive recursive growth
- [[ComputabilityTheory]] — context for total computable vs. primitive recursive functions

## Contradictions
- None — reference task page.
