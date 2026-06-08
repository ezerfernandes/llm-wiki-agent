---
title: "Repeat (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, higher-order-functions, control-flow]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Repeat
---

## Summary
The task asks the programmer to write a procedure that takes two arguments: another procedure and a positive integer N. It then invokes the passed-in procedure N times. The key insight is that this exercises first-class functions — passing a procedure as a value to another procedure — combined with a simple counted loop or recursion.

## Task Requirements
- Define a procedure that accepts two arguments: a procedure and a positive integer.
- Execute the passed-in procedure a number of times equal to the integer argument.

## Language Coverage
111 languages implement this task, spanning functional, imperative, assembly, and stack-based paradigms. Representative implementations include Python, Haskell, C, Java, JavaScript, Lisp, Rust, Ruby, Scheme, and Prolog.

## Connections
- [[HigherOrderFunctions]] — passing a procedure as an argument
- [[FirstClassFunctions]] — treating functions as values
- [[CallbackPattern]] — invoking a supplied routine
- [[Recursion]] — an alternative to iterative repetition
- [[ControlFlow]] — counted loop execution

## Contradictions
- None — reference task page.
