---
title: "Priority queue (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, heap]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Priority_queue
---

## Summary
The task asks the programmer to implement a priority queue: a queue-like structure where each element is inserted with an associated numeric priority and elements are removed highest-priority-first rather than in insertion order. It must support at least insertion and top-item removal (dequeue). The key insight is that an efficient implementation typically uses a binary heap, giving O(log n) insertion and extraction.

## Task Requirements
- Implement a priority queue supporting at least two operations: insertion of an element with a numeric priority, and removal/return of the element with the current top priority.
- Optionally support peeking (inspect the top element) and merging two queues.
- Test by inserting several elements with random priorities, then dequeuing sequentially so they emerge sorted by priority.
- A sample dataset of five priority/task pairs (e.g., 3 "Clear drains", 1 "Solve RC tasks") is provided.
- Aim for efficiency, ideally O(log n) insertion and extraction; implementation-specific limits (priority range, capacity) are allowed if justified.

## Language Coverage
88 languages implement this task, spanning systems languages, scripting languages, functional languages, and even assembly. Representative implementations include C, C++, C#, Java, Python, Go, Rust, Haskell, OCaml, Common Lisp, Ruby, and AArch64 Assembly.

## Connections
- [[BinaryHeap]] — the canonical data structure backing an efficient priority queue
- [[Heapsort]] — sorting via repeated heap extraction, closely related to the dequeue test
- [[Queue]] — the FIFO structure this generalizes by adding priority ordering
- [[AbstractDataType]] — the priority queue is defined by its operations rather than its representation
- [[BigONotation]] — the O(log n) efficiency target for insertion and extraction

## Contradictions
- None — reference task page.
