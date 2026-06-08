---
title: "Man or boy test (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, closures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Man_or_boy_test
---

## Summary
The task asks the programmer to reproduce Donald Knuth's ALGOL 60 "man or boy" routine in another language. The routine sets up a deliberately convoluted mutually-recursive structure between a function A and an inner function B, where B updates a non-local variable k captured from the activation record where it was defined. The key insight is that this tests whether a language correctly handles recursion together with non-local references (the Funarg Problem); a correct implementation yields -67 for k=10.

## Task Requirements
- Imitate Knuth's ALGOL 60 example as faithfully as the target language allows.
- Correctly support passing routines (closures/procedures) as arguments that retain access to and can mutate variables from their originating call environment.
- For input k=10, the computed result must be -67 to confirm correct activation-record handling.
- Optionally demonstrate how to adjust stack/heap or recursion-depth limits, since the test stresses memory rather than CPU.

## Language Coverage
89 languages implement this task, spanning functional, imperative, object-oriented, and stack-based paradigms; representatives include the original ALGOL 60, plus C, C++, Java, Python, Haskell, OCaml, Scheme, Lisp, Rust, and Smalltalk.

## Connections
- [[Recursion]] — relies on mutual recursion between A and B
- [[Closures]] — B must capture and mutate its defining environment
- [[FunargProblem]] — the precise behavior the test diagnoses
- [[ActivationRecord]] — correctness hinges on heap-allocated call frames
- [[ALGOL60]] — the language and example the test originates from

## Contradictions
- None — reference task page.
