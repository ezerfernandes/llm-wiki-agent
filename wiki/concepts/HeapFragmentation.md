---
title: "Heap Fragmentation"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, allocator]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Heap Fragmentation

**Heap fragmentation** is the state where the [[HeapSection|heap]]'s free memory is scattered into many small non-contiguous chunks rather than a few large ones, even when the total free byte count is large. It is an emergent property of mixed [[Malloc|`malloc`]] / [[Free|`free`]] traffic over time and the headline reason a long-running program can hit [[Malloc|`malloc`]] returning [[NullPointer|`NULL`]] *without* being out of memory in any meaningful sense.

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]] — the chapter's brief implementation peek — the [[FreeList|free list]] holds *"chunks of free heap space interspersed with chunks of allocated heap space."* That *interspersing* is the fragmentation.

## Two kinds

- **External fragmentation** — total free bytes ≥ request size, but no single contiguous chunk is large enough. The headline kind; what fragmentation usually means.
- **Internal fragmentation** — bytes allocated to a request beyond what the user asked for (due to size-class rounding, header overhead, alignment padding). Smaller and per-allocation rather than emergent.

## How it arises

The canonical pattern: a long-running program allocates many small short-lived chunks interleaved with fewer large long-lived chunks. The short-lived chunks come and go, but the long-lived ones pin specific regions of the heap. Over time the free space becomes ragged — every long-lived chunk is a divider in what used to be a contiguous run.

```
Initial heap:   [................................] 32 free bytes
After traffic:  [LL.LL.LL.LL.LL.LL.LL.LL.LL.LL.LL] — 11 free bytes, max chunk 1
malloc(2)? FAILS — 11 free bytes total, no contiguous run of 2.
```

## Defense

- **Size-class arenas.** Modern allocators (jemalloc, mimalloc, ptmalloc tcache) segregate by size, so small-allocation churn doesn't fragment the regions large allocations live in.
- **Coalescing on [[Free|`free`]].** Merge a freed chunk with adjacent free neighbors to keep the [[FreeList|free list]] entries large.
- **Arena reuse.** Allocate similarly-typed objects from the same arena.
- **Lifetime grouping.** When possible, allocate same-lifetime objects together (pool allocators).
- **Avoid the heap when you can.** Embedded systems often forbid heap use entirely — see [[HeapAllocation]] for the [[RustLanguage|Rust]] embedded story.

## Why [[BareMetalProgramming|embedded]] worries about this most

A long-running [[Microcontroller|MCU]] firmware cannot tolerate fragmentation-induced OOM — there's no OS to restart it, often no log to debug it. This is why the [[NoStd|`#![no_std]`]] embedded [[RustLanguage|Rust]] world makes the heap *opt-in* (see [[HeapAllocation]]) and why many embedded codebases use only static / stack allocation: the worst case is bounded at compile time.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[FreeList]] — the data structure whose distribution becomes fragmented.
- [[Malloc]] / [[Free]] — the operations whose traffic produces fragmentation.
- [[HeapSection]] — the region that fragments.
- [[NullPointer]] — the [[Malloc|`malloc`]] return value when fragmentation prevents satisfying a request.
- [[HeapMetadata]] — the per-chunk overhead contributing to internal fragmentation.
- [[DynamicMemoryAllocation]] — the mechanism this failure mode inhabits.
- [[HeapAllocation]] — the embedded perspective.
- [[CLanguage]] / [[DiveIntoSystems]].
