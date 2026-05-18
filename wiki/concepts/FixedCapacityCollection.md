---
title: "Fixed-Capacity Collection"
type: concept
tags: [rust, embedded, collections, no-std, real-time]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# Fixed-Capacity Collection

A **fixed-capacity collection** is a data structure whose maximum size is determined at *compile time* (encoded in its type) and **never reallocates** at runtime. Insertion failures arising from capacity exhaustion surface as **explicit `Result`s** rather than via the allocator. The canonical Rust realization in the embedded corpus is [[HeaplessCrate|`heapless`]] (`Vec<_, U8>`, capacity encoded via [[Typenum|`typenum`]] in v0.4.x) ([[rust-embedded-book-collections-index]]).

## Defining properties

- **Capacity in the type signature.** `Vec<_, U8>` and `Vec<_, U64>` are *different types*. Generic functions can be bounded over the capacity.
- **No reallocation.** Memory is allocated once — typically on the stack (where `heapless::Vec::new()` lives by default), or in a `static`, or behind a `Box`.
- **Explicit, local failure.** Every method that could exceed capacity returns `Result` (`push`, `extend_from_slice`, …). The caller decides per-site whether to `?`, `unwrap`, or recover.
- **Constant-time inserts.** No reallocation tail — `heapless::Vec::push` executes *"in constant time"* ([[rust-embedded-book-collections-index]]) — the [[WorstCaseExecutionTime|WCET]] win.

## Why embedded favors them

- **OOM becomes impossible** if no global allocator is configured ([[OutOfMemory]]).
- **Static memory analysis works.** Stack-resident fixed-capacity collections are visible to `-Z emit-stack-sizes` / `stack-sizes` tooling; static-resident ones are sized by the linker, which can fail the link rather than the running program.
- **No [[MemoryFragmentation|fragmentation]].**
- **WCET is bounded.** No realloc tail; cycle-counting is tractable.

## Trade-offs

- Capacity must be picked per instance — no `shrink_to_fit`, so the **load factor** (`size / capacity`) is typically lower than what relocatable collections can achieve.
- The explicit-`Result` API is more verbose than the implicitly-fallible `alloc` API.
- One instance's capacity-exhaustion is unrecoverable for *that* instance without re-architecting the data flow (vs. heap collections, which can grow opportunistically).

## Connections

- [[HeaplessCrate]] — the canonical Rust implementation in the embedded corpus.
- [[Typenum]] — the type-level-numerics mechanism that encodes capacity.
- [[AllocCrate]] — the heap-backed alternative; opposite trade-off curve.
- [[OutOfMemory]] — the failure mode fixed-capacity collections make impossible / local.
- [[WorstCaseExecutionTime]] — the timing-determinism justification.
- [[MemoryFragmentation]] — the substrate failure mode fixed-capacity collections sidestep.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
