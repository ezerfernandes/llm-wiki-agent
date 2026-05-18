---
title: "free (C)"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, stdlib]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# `free` (C)

**`free`** is the [[CLanguage|C]] standard-library function that releases a heap allocation previously returned by [[Malloc|`malloc`]] (or [[Calloc|`calloc`]] / [[Realloc|`realloc`]]). Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]:

> "When a program no longer needs the heap memory it dynamically allocated with `malloc`, it should explicitly deallocate the memory by calling the `free` function."

Declared in `<stdlib.h>`:

```c
void free(void *ptr);
```

- **Parameter** — `ptr`: the [[Pointer|pointer]] previously returned from a successful [[Malloc|`malloc`]]. Any [[PointerType|pointer type]] is accepted (`void *` converts implicitly).
- **Return** — none. `free` cannot fail in the [[Malloc|`malloc`]] sense — but [[Free|free]]ing a [[Pointer|pointer]] that didn't come from `malloc`, or [[DoubleFree|free-ing the same chunk twice]], is undefined behavior and typically corrupts the heap manager's internal state.
- **Effect** — the chunk is returned to the [[FreeList|free list]]; a subsequent [[Malloc|`malloc`]] may reuse the same bytes. The chunk's [[HeapMetadata|header]] is what `free` consults to know the chunk's size — which is why the call takes only the pointer, not the size.

## Why `free` exists

Without `free`, every [[Malloc|`malloc`]] permanently consumes heap bytes for the program's remaining lifetime ([[MemoryLeak|memory leak]]). Long-running programs that leak slowly — servers, daemons, simulations — eventually exhaust the heap and `malloc` starts returning [[NullPointer|`NULL`]]. `free` is the discipline that keeps the heap recyclable.

## The `NULL`-after-`free` discipline

Per [[dis-2-4-dynamic-memory|Ch 2.4]] the chapter's load-bearing safety rule:

> "After calling free, the freed memory should no longer be used by the program … it's good programming practice to set the pointer to `NULL` after freeing it."

The canonical idiom:

```c
free(p);
p = NULL;
```

Once `p` is [[NullPointer|`NULL`]], any accidental [[DereferenceOperator|deref]] reliably [[SegmentationFault|segfaults]] (Ch 2.2's failure mode) instead of silently reading or corrupting whatever the heap manager has since handed out at the same address ([[UseAfterFree|use-after-free]] / [[DanglingPointer|dangling pointer]]). Without this discipline, the [[Pointer|pointer]] holds an address that *was* valid — and the bug surfaces only intermittently, when something else has reused that chunk.

## Failure modes `free` is involved in

- **[[MemoryLeak|Memory leak]]** — `malloc` without matching `free`. The bytes are never reclaimed.
- **[[DoubleFree|Double free]]** — calling `free(p)` twice on the same pointer. Corrupts the [[FreeList|free list]], typically crashes or enables exploitation.
- **[[UseAfterFree|Use-after-free]] / [[DanglingPointer|dangling pointer]]** — dereferencing a pointer after `free`. Undefined behavior; the `NULL`-after-`free` discipline above is the standard defense.
- **Freeing a non-`malloc`'d pointer** — `free(&local_var)` or `free` of a pointer into the middle of a chunk. Undefined behavior; typically corrupts the heap.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Malloc]] — the producer this consumer pairs with.
- [[NullPointer]] — the post-`free` value pointers should hold.
- [[DynamicMemoryAllocation]] — the headline mechanism `free` completes.
- [[HeapSection]] / [[ProcessMemory]] — the memory region `free` returns bytes to.
- [[FreeList]] / [[HeapMetadata]] / [[HeapFragmentation]] — the implementation surface `free` operates on.
- [[MemoryLeak]] / [[UseAfterFree]] / [[DoubleFree]] / [[DanglingPointer]] — failure modes around `free`.
- [[SegmentationFault]] — the crash mode `NULL`-after-`free` *enables* (as the safer alternative to silent UAF).
- [[Pointer]] / [[DereferenceOperator]] / [[CMemoryAddress]] — the [[dis-2-2-pointers|Ch 2.2]] machinery underneath.
- [[CLanguage]] / [[StandardLibrary]] / [[DiveIntoSystems]].
