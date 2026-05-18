---
title: "Memory Fragmentation"
type: concept
tags: [rust, embedded, memory, allocator]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# Memory Fragmentation

**Memory fragmentation** is the runtime accumulation of unusable gaps in a heap allocator's address space: enough total free memory exists to satisfy a request, but no contiguous, properly-aligned region of the required size is available. The *Collections* chapter of [[TheEmbeddedRustBook]] names fragmentation as a key reason heap-based memory accounting in embedded systems is hard to reason about ([[rust-embedded-book-collections-index]]).

## Why it matters in embedded

- **Apparent memory usage > actual usage.** *"The allocator may have to deal with memory fragmentation which can increase the *apparent* memory usage."* ([[rust-embedded-book-collections-index]])
- **[[OutOfMemory|OOM]] becomes non-local in time and space.** A fragmented allocator can fail a small allocation (`vec.reserve(1)`) even when total free bytes are abundant — and the *cause* of fragmentation (some earlier alloc/free pattern, possibly in unrelated code or a leaked collection) is divorced from the *observed* failure site.
- **[[WorstCaseExecutionTime|WCET]] is unbounded.** Allocator behavior on a fragmented heap can include expensive searches or compaction.
- **`shrink_to_fit` is allocator-discretionary** — *"ultimately, it's up to the allocator to decide whether to actually shrink the memory allocation or not"* — so even careful programs can't deterministically reclaim fragmented space.

## The structural answer: avoid the substrate

[[FixedCapacityCollection|Fixed-capacity collections]] ([[HeaplessCrate|`heapless`]]) eliminate fragmentation by eliminating the allocator. Each collection's memory is statically known; the linker (for `static`s) or stack-sizing tools (for stack allocations) can detect overcommit at build time rather than runtime.

## Connections

- [[OutOfMemory]] — the failure mode fragmentation amplifies / accelerates.
- [[AllocCrate]] / [[GlobalAllocator]] — the substrate where fragmentation can occur.
- [[FixedCapacityCollection]] / [[HeaplessCrate]] — the alternative that sidesteps fragmentation entirely.
- [[HeapAllocation]] — the underlying mechanism.
- [[WorstCaseExecutionTime]] — the timing axis fragmentation undermines.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
