---
title: "Anonymous recursion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anonymous_recursion
---

## Summary
The task explores how to recurse without inventing a named helper function. A recursive routine frequently needs an inner helper to carry out the actual recursion — to validate arguments once, avoid namespace pollution, or pass different parameters — and naming that helper is awkward. The key insight is that many languages let you recurse in place via a label, a local gosub, a self-referencing keyword, or the Y combinator, so the recursion stays anonymous.

## Task Requirements
- Demonstrate anonymous recursion if the language supports it.
- Implement a recursive Fibonacci function as the concrete example.
- Check for a negative argument once, before entering the actual recursion (so the validation is not repeated on every recursive call).

## Language Coverage
121 languages implement this task, a very broad spread covering functional, imperative, stack-based, and assembly styles. Representative entries include Haskell, Scheme, OCaml, Common Lisp, Python, JavaScript, C, Rust, Java, Forth, Prolog, and x86 Assembly.

## Connections
- [[Recursion]] — the core mechanism the task demonstrates
- [[YCombinator]] — fixed-point combinator enabling recursion without a name
- [[FibonacciSequence]] — the example function being implemented
- [[FixedPointCombinator]] — the theoretical basis for self-application
- [[HigherOrderFunctions]] — used to pass a function to itself

## Contradictions
- None — reference task page.
