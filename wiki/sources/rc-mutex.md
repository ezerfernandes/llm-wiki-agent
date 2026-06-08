---
title: "Mutex (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mutex
---

## Summary
A mutex (mutual exclusion) is a synchronization primitive used to protect a shared resource from concurrent access by multiple tasks. It behaves like a semaphore with k=1: a task seizes (acquires) the mutex, accesses the resource, then releases it. This is an encyclopedic/reference task that explains the concept and asks implementations to demonstrate the language's mutex facilities rather than solve a fixed algorithmic problem. The key insight is that mutexes are low-level and deadlock-prone — a deadlock can arise from just two tasks acquiring two mutexes in opposite order.

## Task Requirements
- Explain and demonstrate the language's mechanism for mutual exclusion (a mutex or equivalent synchronization object).
- Show seizing (acquiring) the mutex, accessing a protected shared resource, and releasing the mutex.
- Optionally cover variants such as reentrant mutexes, read/write mutexes, and global vs. local mutexes.
- Discuss deadlock risk and, where applicable, deadlock-prevention strategies.

## Language Coverage
43 sections appear on the page; three describe mutex variants (global/local, reentrant, read/write) and roughly 40 are language implementations, giving broad coverage across systems, functional, and scripting languages. Representative examples include Ada, C, C++, Rust, Go, Java, Python, Haskell, Erlang, OCaml, Ruby, and even 6502/8086 Assembly.

## Connections
- [[MutualExclusion]] — the property the primitive enforces
- [[Semaphore]] — generalization of a mutex (k > 1)
- [[Concurrency]] — the broader domain this task addresses
- [[Deadlock]] — the failure mode mutexes can introduce
- [[RaceCondition]] — the hazard mutexes are meant to prevent

## Contradictions
- None — reference task page.
