---
title: "Free List (Heap Manager)"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, allocator, implementation]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Free List (Heap Manager)

The **free list** is the [[CLanguage|C]] runtime's bookkeeping data structure for tracking unused chunks of [[HeapSection|heap]] memory available for allocation. It is the substrate over which [[Malloc|`malloc`]] and [[Free|`free`]] operate:

- [[Malloc|`malloc(n)`]] walks the free list looking for a free chunk of at least `n` bytes (plus [[HeapMetadata|header overhead]]); splits it if larger; removes the allocated portion from the list; returns its [[CMemoryAddress|user-visible address]].
- [[Free|`free(p)`]] adds the chunk back to the free list (possibly coalescing with adjacent free neighbors).

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]] the chapter's brief implementation peek: the heap manager keeps *"a list of unused chunks of heap memory available for allocation."*

## Why "list" is a simplification

The classic textbook image is a singly-linked list of free chunks threaded through the heap. Real-world allocators are more elaborate:

- **[[glibc|glibc]]'s ptmalloc** — multiple size-segregated bins (fastbins, tcache, smallbins, largebins, unsorted bin), each with its own list.
- **jemalloc / mimalloc** — size-class arenas with thread-local caches and radix trees over heap regions.
- **`dlmalloc`** — Doug Lea's original — boundary-tag chunks with size in both header and footer for coalescing.

In all cases the conceptual role is the same: track which bytes are free, find one fast on `malloc`, return one fast on `free`.

## [[HeapFragmentation|Fragmentation]]

Repeated mixed `malloc` / `free` traffic produces [[HeapFragmentation|heap fragmentation]] — many small free chunks scattered across the heap, with allocated chunks between them. The free list may total enough bytes to satisfy a `malloc(N)` request — but if no *contiguous* free chunk is N bytes, `malloc` returns [[NullPointer|`NULL`]] anyway. This is why long-running programs whose allocation patterns are irregular sometimes appear to leak even when they don't — the bytes are free, just not in a usable shape.

## [[HeapMetadata|Metadata]] coupling

The free list is intertwined with per-chunk [[HeapMetadata|metadata]]: every chunk (free or allocated) carries a header recording its size and (for free chunks) its prev/next pointers in the list. This is why:

- [[Free|`free`]] can release a chunk given only its pointer (size is in the header).
- A buffer overflow into the next chunk's header corrupts the free list (classic "unlink" exploit).
- [[DoubleFree|Double-free]] corrupts the list directly by inserting a chunk that's already on it.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Malloc]] / [[Free]] — the operations that read and write the free list.
- [[HeapMetadata]] — the per-chunk headers the free list threads through.
- [[HeapFragmentation]] — the failure mode the free list exhibits over time.
- [[HeapSection]] — the memory region the free list describes.
- [[DynamicMemoryAllocation]] — the user-facing mechanism the free list implements.
- [[DoubleFree]] / [[UseAfterFree]] — the failure modes that corrupt the list.
- [[CLanguage]] / [[StandardLibrary]] / [[DiveIntoSystems]].
