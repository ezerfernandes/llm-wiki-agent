---
title: "Mutual recursion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mutual_recursion
---

## Summary
Two functions are mutually recursive when the first calls the second and the second in turn calls the first. The task asks the programmer to demonstrate this by implementing the Hofstadter Female and Male sequences, where F and M are each defined in terms of the other. The key challenge is that languages requiring functions to be declared before use must support forward declaration or some equivalent to define a pair of co-dependent functions.

## Task Requirements
- Write two mutually recursive functions, F (Female) and M (Male).
- Base cases: F(0) = 1 and M(0) = 0.
- For n > 0: F(n) = n - M(F(n-1)) and M(n) = n - F(M(n-1)).
- Each function must call the other, not itself directly.
- If a language cannot express a solution with genuinely mutually recursive functions, state that fact rather than substituting another approach.

## Language Coverage
157 languages implement this task, spanning functional, imperative, assembly, and esoteric paradigms — making it a broad survey of how each language handles forward references and co-dependent definitions. Representative implementations include Haskell, OCaml, Scheme, Common Lisp, Prolog, C, C++, Java, Python, Rust, and ALGOL 68.

## Connections
- [[MutualRecursion]] — the defining technique demonstrated by the task
- [[Recursion]] — the broader programming and mathematical concept
- [[HofstadterSequence]] — the integer sequences (Female and Male) used as the example
- [[ForwardDeclaration]] — required in many languages to define co-dependent functions

## Contradictions
- None — reference task page.
