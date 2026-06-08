---
title: "Short-circuit evaluation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, boolean-logic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Short-circuit_evaluation
---

## Summary
This task demonstrates short-circuit evaluation of boolean expressions, where a language stops evaluating an `and`/`or` expression as soon as the overall result is determined. The programmer writes two functions `a` and `b` that each print their name when called and return their boolean argument, then evaluates `a and b` and `a or b` so that the expensive `b` is invoked only when its value can still affect the outcome.

## Task Requirements
- Define two functions `a` and `b` that take and return the same boolean value, and print their own name whenever they are called.
- Compute `x = a(i) and b(j)` such that `b` is called only when `a` returns true.
- Compute `y = a(i) or b(j)` such that `b` is called only when `a` returns false.
- In languages lacking short-circuit operators, emulate the behavior with nested `if` statements.

## Language Coverage
114 languages implement this task, spanning a very broad range of paradigms. Representative implementations include C, C++, C#, Java, Python, Haskell, Lisp, Perl, Ruby, Rust, and Go, alongside shells and assembly variants.

## Connections
- [[ShortCircuitEvaluation]] — the core technique being demonstrated.
- [[BooleanLogic]] — conjunction and disjunction semantics underpin the optimization.
- [[ControlFlow]] — evaluation order is a control-flow concern, often emulated with conditional branches.
- [[LazyEvaluation]] — related notion of deferring computation until a result is needed.

## Contradictions
- None — reference task page.
