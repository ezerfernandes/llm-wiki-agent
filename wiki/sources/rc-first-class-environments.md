---
title: "First class environments (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-semantics, closures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/First_class_environments
---

## Summary
This task explores whether a language treats environments (sets of variable bindings) as first-class values that can be created at runtime, passed as parameters, returned from subroutines, and assigned to variables. Unlike a closure, which bundles code with an environment, a first-class environment is "a closure without code" — a standalone binding store inside which arbitrary statements can be executed. The key insight is that the same statement run against different environments yields different results, demonstrated by stepping twelve independent Hailstone computations.

## Task Requirements
- Build a dozen environments, each holding two variable bindings: a current Hailstone-sequence value and a step count (initialized to zero).
- Initialize the twelve Hailstone values to 1 through 12.
- Write a single piece of code that runs repeatedly inside each environment.
- On each run, compute the next Hailstone step (unless the value is already 1) and increment the count, then print the current value in tabular form.
- Stop processing once all values have dropped to 1, then print the total step count for each environment.

## Language Coverage
34 languages implement this task, spanning Lisp-family languages with native first-class environments alongside imperative and functional languages that simulate them via maps, objects, or closures. Representative implementations include C, C++, Clojure, Haskell, Python, Racket, Ruby, Perl, Julia, J, and Tcl.

## Connections
- [[Closure]] — the task contrasts first-class environments with closures (code plus environment)
- [[HailstoneSequence]] — the concrete computation run inside each environment
- [[FirstClassObject]] — the broader notion of values constructible, passable, and assignable at runtime
- [[VariableBinding]] — environments are sets of name-to-value bindings
- [[LexicalScope]] — environments formalize the scope rules a statement executes under

## Contradictions
- None — reference task page.
