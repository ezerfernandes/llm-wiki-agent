---
title: "Queue/Definition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Queue/Definition
---

## Summary
The task asks the programmer to implement a FIFO (first-in, first-out) queue from scratch rather than using a built-in container. Elements are added at one end and removed from the other in insertion order. The core insight is that a queue exposes only enqueue/dequeue at opposite ends, which can be backed by a linked list, a pair of stacks, or a circular buffer.

## Task Requirements
- Implement a FIFO queue where elements are pushed on one side and popped from the other in insertion order.
- Provide a `push` (enqueue) operation that adds an element.
- Provide a `pop` (dequeue) operation that removes and returns the first element.
- Provide an `empty` operation that returns a truth value when the queue holds no elements.
- Handle the error of popping from an empty queue (behavior is language/platform dependent).

## Language Coverage
115 languages implement this task, spanning systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Java, Python, Haskell, OCaml, Rust, Go, Lisp, Erlang, and AArch64 Assembly.

## Connections
- [[Queue]] — the abstract data type being defined
- [[FIFO]] — the ordering discipline the queue enforces
- [[LinkedList]] — common backing structure for an efficient queue
- [[DataStructures]] — the broader category this task belongs to
- [[AbstractDataType]] — queue specified by its operations rather than representation

## Contradictions
- None — reference task page.
