---
title: "Y combinator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lambda-calculus, recursion, functional-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Y_combinator
---

## Summary
This task asks the programmer to define the Y combinator — a stateless function that, applied to another stateless function, returns a recursive version of it. In pure functional programming and the lambda calculus, lambda expressions cannot refer to themselves or hold state, so ordinary self-referential recursion is impossible; the Y combinator solves this by being the simplest fixed-point combinator, enabling recursion to emerge from anonymous, stateless functions.

## Task Requirements
- Define the stateless Y combinator itself.
- Use it to compute factorials from a stateless function or lambda expression (no named self-reference).
- Use it to compute Fibonacci numbers in the same stateless manner.

## Language Coverage
109 languages implement this task, spanning functional, imperative, stack-based, and assembly languages — unusually broad given the abstract nature of the problem. Representative implementations include Haskell, Scheme, OCaml, Common Lisp, Clojure, JavaScript, Python, Racket, Java, Rust, and even Lambda Calculus and AArch64 Assembly.

## Connections
- [[LambdaCalculus]] — the formal system in which the Y combinator originates.
- [[FixedPointCombinator]] — the Y combinator is the canonical, simplest member of this class.
- [[Recursion]] — the combinator enables recursion without named self-reference.
- [[FunctionalProgramming]] — relies on first-class, stateless functions.
- [[HigherOrderFunctions]] — Y takes and returns functions.

## Contradictions
- None — reference task page.
