---
title: "Runtime evaluation/In an environment (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, interpreters]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Runtime_evaluation/In_an_environment
---

## Summary
The task asks the programmer to take a program written in the host language (supplied as a string or AST) that contains a free variable named `x`, evaluate it with `x` bound to one provided value, evaluate it again with `x` bound to a second value, then subtract the first result from the second and print it. The key insight is that the binding must be supplied by the evaluator's *environment* rather than by patching the source text, demonstrating that the language can treat variable environments as first-class, runtime-controllable data.

## Task Requirements
- Evaluate a program/expression with a free variable `x` bound to a provided value, then again with a different value, and print the difference of the two results.
- Must not involve string manipulation of the input source code.
- Must be plausibly extensible to a runtime-chosen set of bindings, not just `x`.
- Must not make `x` a global variable.
- Alternatively, note that these constraints are impossible in the language.

## Language Coverage
61 languages implement this task, spanning Lisp dialects with first-class environments, dynamic scripting languages, and JIT/eval-capable systems. Representative examples include Common Lisp, Scheme, Clojure, Racket, JavaScript, Python, Ruby, Perl, Tcl, Lua, J, and Mathematica.

## Connections
- [[Eval]] — the general runtime-evaluation mechanism this task specializes
- [[Metaprogramming]] — treating code as data to be executed at runtime
- [[LexicalScope]] — binding the free variable through a controlled environment rather than globals
- [[AbstractSyntaxTree]] — the AST input form some implementations evaluate
- [[Closure]] — capturing the variable binding without polluting global scope

## Contradictions
- None — reference task page.
