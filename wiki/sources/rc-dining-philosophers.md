---
title: "Dining philosophers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, synchronization, deadlock]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dining_philosophers
---

## Summary
A classic concurrency exercise based on a problem posed by Edsger Dijkstra. Five philosophers sit around a round table alternating between thinking and eating spaghetti; each needs the two forks adjacent to their seat to eat, but only five forks exist. The task illustrates the non-composability of low-level synchronization primitives like semaphores: a naive implementation can deadlock when every philosopher grabs one fork and waits forever for the other. The point is to implement and explain at least one deadlock-free solution.

## Task Requirements
- Model five philosophers (Aristotle, Kant, Spinoza, Marx, Russell) who alternate thinking and eating.
- Represent five shared forks, each between two adjacent seats; eating requires acquiring both neighboring forks.
- A philosopher who cannot grab both forks waits; eating and thinking each take a random amount of time.
- Implement at least one solution that prevents deadlock, and explain how the deadlock is prevented.

## Language Coverage
55 languages implement this task, spanning systems languages, functional languages, and high-level scripting languages — reflecting how universal concurrency primitives are. Representative implementations include C, C++, Rust, Go, Java, C#, Python, Haskell, Erlang, Clojure, Ada, and Tcl.

## Connections
- [[Concurrency]] — the core domain the task exercises
- [[Deadlock]] — the central failure mode the solution must prevent
- [[Semaphore]] — the synchronization primitive whose non-composability is highlighted
- [[ResourceHierarchySolution]] — ordering fork acquisition is a common deadlock-avoidance strategy
- [[MutualExclusion]] — forks are shared resources requiring exclusive access

## Contradictions
- None — reference task page.
