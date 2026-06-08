---
title: "Active object (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, object-oriented, numerical-integration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Active_object
---

## Summary
The task asks the programmer to implement an "active object" — an object whose state depends on a clock and is updated by an encapsulated background task, while still exposing ordinary methods to the outside world. Because the internal task and external method calls run concurrently, the implementation must use a synchronization mechanism to prevent state corruption. The concrete instance to build is an active integrator that continuously integrates a time-varying input function.

## Task Requirements
- Implement an active integrator object exposing two methods: `Input` (set the input, a function of time) and `Output` (query the current integrated value).
- The object integrates its input over elapsed time using the trapezoidal rule: `S → S + (K(t1) + K(t0)) * (t1 - t0) / 2`.
- Initially the input function `K` is the constant 0 and the state `S` is 0.
- Test sequence: set input to `sin(2π f t)` with frequency `f = 0.5 Hz`, wait 2s, set input to constant 0, wait 0.5s.
- Verify the output is approximately 0 (the sine's 2s period integrates to ~0); accuracy depends on OS scheduler time-slicing and clock precision.

## Language Coverage
49 languages implement this task, spanning systems languages, functional languages, and scripting languages, reflecting how each handles concurrency primitives. Representative implementations include Ada, C, C++, C#, Go, Haskell, Erlang, Java, Python, Rust, Tcl, and Common Lisp.

## Connections
- [[Concurrency]] — the core challenge: a background task and external callers share mutable state.
- [[ObjectOrientedProgramming]] — the active object is an OOP design pattern.
- [[Synchronization]] — locks/mutexes/message-passing prevent state corruption.
- [[TrapezoidalRule]] — the numerical integration method used to accumulate output.
- [[NumericalIntegration]] — integrating a time-varying signal over elapsed time.

## Contradictions
- None — reference task page.
