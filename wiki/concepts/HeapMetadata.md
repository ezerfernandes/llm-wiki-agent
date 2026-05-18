---
title: "Heap Metadata (Allocation Header)"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, allocator, implementation, security]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Heap Metadata (Allocation Header)

**Heap metadata** is the per-chunk bookkeeping the [[CLanguage|C]] heap manager stores alongside (typically *immediately preceding*) each user-visible allocation. It is what makes the [[Free|`free`]] function callable with only a pointer — the size and free/allocated status are read out of the header rather than passed by the caller.

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]: implicit in the framing that *"the implementation of `free` is able to determine how many bytes to release given just the address of the heap memory chunk."* The chapter doesn't dissect the header; this page collects what it implies.

## Typical contents (allocator-dependent)

- **Size of the chunk** — including the header itself, so [[Free|`free`]] can locate the next chunk in the heap.
- **Allocated / free flag** — usually packed into the low bits of the size field, since alignment makes them always zero.
- **Free-list pointers** (only when the chunk is free) — prev / next in the [[FreeList|free list]]. When the chunk is allocated, the same bytes are user data.
- **Footer / boundary tag** — some allocators (dlmalloc) duplicate the size at the chunk's end so coalescing on `free` can find the previous chunk's header.

## The layout

```
Allocated chunk:                       Free chunk:
+-----------+---------------+          +-----------+----+----+--------+
| size|flag | user payload  |          | size|flag |prev|next| unused |
+-----------+---------------+          +-----------+----+----+--------+
            ^                                      ^
            malloc returns here                    malloc returns here
                                                   if reused
```

The pointer [[Malloc|`malloc`]] returns is *past* the header — the user code sees `header_size` bytes before its pointer, even though it must not touch them. [[Free|`free`]] decrements its argument by `header_size` to find the header.

## Why this matters for security

A [[BufferOverflow|buffer overflow]] into the *next* chunk's header is the classic heap-corruption primitive. By rewriting the size field, the free/allocated flag, or the free-list prev/next pointers, an attacker turns a write-past-end bug into:

- A controlled heap-write primitive (via "unlink" — overwriting next/prev so a later coalescing `free` writes attacker bytes anywhere).
- A type-confusion primitive (via shrinking a free chunk's recorded size so the next `malloc` returns a pointer overlapping the next chunk).

Modern allocators have hardened against this — heap canaries, in-place pointer encryption (`protect_ptr` in glibc 2.32+), randomized fastbin / tcache pointers — but the basic geometry (metadata adjacent to user data) is the durable vulnerability surface.

## [[DoubleFree|Double-free]] and metadata corruption

Calling [[Free|`free`]] twice on the same chunk inserts a chunk that's already on the [[FreeList|free list]] into the list a second time. Depending on the allocator's variant of free-list integrity check, this either aborts the process (modern hardened path) or corrupts the list silently and enables fastbin / tcache-poisoning-style exploitation.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[FreeList]] — the data structure metadata threads through.
- [[Malloc]] / [[Free]] — the API that reads and writes the metadata.
- [[HeapSection]] — the region the metadata lives in.
- [[HeapFragmentation]] — internal fragmentation comes partly from metadata overhead.
- [[DoubleFree]] / [[UseAfterFree]] — failure modes that corrupt or read stale metadata.
- [[BufferOverflow]] — the classic primitive that exploits adjacent metadata.
- [[DynamicMemoryAllocation]] — the mechanism metadata implements.
- [[CLanguage]] / [[StandardLibrary]] / [[DiveIntoSystems]].
