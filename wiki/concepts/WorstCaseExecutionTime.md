---
title: "Worst Case Execution Time (WCET)"
type: concept
tags: [embedded, real-time, performance, rust]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# Worst Case Execution Time (WCET)

**Worst Case Execution Time (WCET)** is the upper bound on how long a piece of code can take to execute, over all possible inputs and runtime states. In **hard real-time** systems — where missing a deadline is a system failure, not a degradation — WCET is the load-bearing performance metric, far more relevant than average-case latency.

The *Collections* chapter of [[TheEmbeddedRustBook]] introduces WCET as one of the four trade-off axes between [[AllocCrate|`alloc`]] and [[HeaplessCrate|`heapless`]] collections ([[rust-embedded-book-collections-index]]):

> "If you are building time sensitive applications or hard real time applications then you care, maybe a lot, about the worst case execution time of the different parts of your program."

## Why heap collections complicate WCET

`alloc::Vec::push` *can* reallocate, and *"the WCET of operations that may grow the collection will also include the time it takes to reallocate the collection, which itself depends on the *runtime* capacity of the collection."* ([[rust-embedded-book-collections-index]]) — making the WCET of a `push` a function of (a) the [[GlobalAllocator|allocator]]'s worst-case behavior (which may include searches across fragmented free lists) and (b) the *runtime* capacity at the moment of growth (which can be arbitrarily large). Neither is tractable to bound statically.

## Why [[HeaplessCrate|`heapless`]] makes WCET tractable

*"`heapless::Vec.push` executes in constant time."* ([[rust-embedded-book-collections-index]]) — and the same holds for every other capacity-changing operation, because [[FixedCapacityCollection|fixed-capacity collections]] never reallocate. The WCET is the time of a single bounds check + store + length update — a small, fixed number of cycles, independent of capacity or runtime state.

## Connections

- [[FixedCapacityCollection]] / [[HeaplessCrate]] — the design pattern / crate that delivers tractable WCET.
- [[AllocCrate]] — the alternative whose WCET is unbounded by realloc behavior.
- [[MemoryFragmentation]] — the substrate condition that amplifies allocator WCET.
- [[RTIC]] — the higher-level embedded-Rust framework that markets *"extremely low time and memory overhead"* and *"no deadlocks"* — both WCET-relevant ([[rust-embedded-book-concurrency-index]]).
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
