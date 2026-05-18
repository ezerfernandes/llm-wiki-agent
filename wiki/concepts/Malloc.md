---
title: "malloc (C)"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, stdlib]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# `malloc` (C)

**`malloc`** is the [[CLanguage|C]] standard-library function that requests a contiguous run of bytes on the [[HeapSection|heap]] at runtime. Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]:

> "To call `malloc`, a program passes in the total number of bytes of contiguous heap memory to allocate."

Declared in `<stdlib.h>`:

```c
void *malloc(size_t size);
```

- **Parameter** — `size`: number of bytes to allocate (a [[SizeT|`size_t`]]). Idiomatically computed with the [[SizeOf|`sizeof`]] operator: `malloc(sizeof(int))` for one `int`, `malloc(sizeof(int) * N)` for an `N`-element `int` array.
- **Return** — a [[Pointer|pointer]] (`void *`) to the [[CMemoryAddress|base address]] of the allocated region, or [[NullPointer|`NULL`]] on failure. In modern [[CLanguage|C]] the `void *` assigns to any [[PointerType|pointer type]] without an explicit cast (older code shows `p = (int *) malloc(...)`).
- **Lifetime** — programmer-controlled. The bytes belong to the program until released with [[Free|`free`]] or the program exits. Unlike [[StackSection|stack]] locals, they survive past the [[StackFrame|call frame]] that created them; unlike [[GlobalVariable|globals]], they aren't bound to a name at compile time.
- **Contents** — *uninitialized*. The bytes hold whatever the heap manager left there. For zero-filled storage use [[Calloc|`calloc`]] (named in [[DynamicMemoryAllocation|the API preview]] but **deferred** past Ch 2.4).

## The two-line safety rule

Per [[dis-2-4-dynamic-memory|Ch 2.4]]:

> "Be sure to always test the return value of `malloc` for `NULL`. Dereferencing a `NULL` pointer will cause your program to crash!"

The canonical pattern:

```c
int *p = malloc(sizeof(int));
if (p == NULL) {
    printf("Bad malloc\n");
    exit(1);
}
*p = 6;        // safe — p is known non-NULL here
```

`malloc` returns [[NullPointer|`NULL`]] when the heap can't satisfy the request — usually exhausted memory or a request too large for the largest free chunk after [[HeapFragmentation|fragmentation]]. Skipping the check is the corpus's headline [[CLanguage|C]] safety bug — a [[NullPointer|`NULL`]] [[DereferenceOperator|dereference]] reliably [[SegmentationFault|segfaults]] (Ch 2.2's failure mode).

## Pairing with [[Free|`free`]]

Per [[dis-2-4-dynamic-memory|Ch 2.4]]: **every successful `malloc` must be matched by exactly one [[Free|`free`]]**. Failure leaks the bytes ([[MemoryLeak|memory leak]]) — they stay allocated until the program exits, accruing in long-running programs. Double-freeing a chunk ([[DoubleFree|double-free]]) corrupts the heap. [[Free|`free`]]ing a [[Pointer|pointer]] that didn't come from `malloc` is undefined behavior.

## Implementation peek: the [[FreeList|free list]] and [[HeapMetadata|metadata]]

`malloc` walks a [[FreeList|free list]] of unused heap chunks, finds one big enough, splits it, and returns the user-visible portion. Each allocation has a small [[HeapMetadata|header]] preceding it recording the chunk's size — which is why [[Free|`free`]] takes only the pointer and not the size. Repeated mixed `malloc` / `free` produces [[HeapFragmentation|heap fragmentation]] — many small free chunks rather than a few large ones — which can make a `malloc(N)` call fail even when the total free bytes ≥ N.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Free]] — the matching deallocator.
- [[Calloc]] / [[Realloc]] — the API siblings (deferred past Ch 2.4).
- [[SizeOf]] — the byte-count operator paired with `malloc`.
- [[SizeT]] — the parameter type.
- [[NullPointer]] — the failure return value.
- [[Exit]] — the canonical OOM exit.
- [[DynamicMemoryAllocation]] — the headline mechanism `malloc` operationalizes.
- [[HeapSection]] / [[ProcessMemory]] — the memory region `malloc` allocates from.
- [[Pointer]] / [[PointerType]] / [[DereferenceOperator]] — the [[dis-2-2-pointers|Ch 2.2]] machinery callers use on `malloc`'s return.
- [[FreeList]] / [[HeapFragmentation]] / [[HeapMetadata]] — implementation-side concepts.
- [[MemoryLeak]] / [[UseAfterFree]] / [[DoubleFree]] / [[DanglingPointer]] — failure modes.
- [[SegmentationFault]] — the crash mode of [[NullPointer|`NULL`]]-`malloc`-deref.
- [[CLanguage]] / [[StandardLibrary]] / [[DiveIntoSystems]].
