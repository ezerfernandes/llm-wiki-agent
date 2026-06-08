---
title: "Metered concurrency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Metered_concurrency
---

## Summary
The task asks the programmer to implement a counting semaphore that coordinates a set of concurrent units. The key insight is demonstrating how a passive synchronization primitive (the semaphore) can throttle and coordinate multiple active concurrent units, limiting how many may run at once.

## Task Requirements
- Create a counting semaphore supporting three operations: `acquire`, `release`, and `count`.
- Each active concurrent unit must attempt to `acquire` the semaphore before doing its work.
- Upon acquiring, the unit should report that it has acquired the semaphore.
- After acquiring, the unit should sleep for 2 seconds and then `release` the semaphore.

## Language Coverage
42 languages implement this task, spanning systems languages, functional languages, and scripting languages with varied concurrency models. Representative implementations include Ada, C, C++, C#, Go, Haskell, Java, Erlang, Python, Ruby, Rust, and Tcl.

## Connections
- [[CountingSemaphore]] — the central synchronization primitive being built
- [[Concurrency]] — the domain the task exercises
- [[ThreadSynchronization]] — coordinating shared access across active units
- [[MutualExclusion]] — related limiting of concurrent access to resources

## Contradictions
- None — reference task page.
