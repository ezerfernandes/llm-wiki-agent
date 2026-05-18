---
title: "Dynamic Memory Allocation (C)"
type: concept
tags: [c-language, memory, heap, dynamic-allocation]
sources: [dis-2-1-scope-memory, dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Dynamic Memory Allocation (C)

**Dynamic memory allocation** is the [[CLanguage|C]] mechanism for requesting [[ProcessMemory|memory]] at runtime — *"the part of a program's address space associated with"* the [[HeapSection|heap]], per [[dis-2-1-scope-memory|DIS Ch 2.1]]. The mechanism — [[Malloc|`malloc`]] / [[Free|`free`]] from `<stdlib.h>`, plus [[SizeOf|`sizeof`]] for byte-count arithmetic and [[Exit|`exit`]] for the failure path — is delivered in [[dis-2-4-dynamic-memory|Ch 2.4]] (with [[Calloc|`calloc`]] and [[Realloc|`realloc`]] left as standard-library siblings the corpus introduces later).

Per [[dis-2-4-dynamic-memory|Ch 2.4]]:

> "Dynamic memory allocation refers to allocating memory at run time and is performed through a set of specific C functions. Dynamic memory allocation allows a C program to request more memory as it's running, and a pointer variable stores the address of the dynamically allocated space."

## Why it exists

[[GlobalVariable|Global]] storage (data section, program-lifetime, fixed at compile time) and [[LocalVariable|local]] storage (stack, per-call, fixed at compile time) cannot cover three common cases:

1. **Size unknown at compile time.** Reading `N` from input, then allocating an `N`-element array — only the heap supports this.
2. **Lifetime outliving the callee.** A function that *builds* a data structure and returns a [[Pointer|pointer]] to it cannot use a [[LocalVariable|local]] (frame pops; pointer dangles) and cannot pollute the [[GlobalScope|global namespace]] for every such structure. Heap fits.
3. **Lifetime shorter than the program.** Long-running programs cannot afford program-lifetime storage for every transient data structure; the heap supports [[Free|free]]ing the bytes when done.

These are the three motivations [[dis-2-4-dynamic-memory|Ch 2.4]] spells out.

## The API ([[dis-2-4-dynamic-memory|Ch 2.4]] surface area)

| Function | What it does | Status |
|---|---|---|
| [[Malloc\|`malloc(n)`]] | Reserve `n` bytes on the heap; return a pointer to them (or [[NullPointer\|`NULL`]] on failure) | Delivered Ch 2.4 |
| [[Free\|`free(p)`]] | Release a heap allocation back to the heap | Delivered Ch 2.4 |
| [[Calloc\|`calloc(n, size)`]] | Like `malloc(n*size)` but zero-initialized | Named; deferred past Ch 2.4 |
| [[Realloc\|`realloc(p, n)`]] | Resize an existing allocation, possibly moving it | Named; deferred past Ch 2.4 |

Supporting operators / functions in the same chapter:

| Element | Role |
|---|---|
| [[SizeOf\|`sizeof(T)`]] | Computes the byte count to pass to [[Malloc\|`malloc`]] |
| [[SizeT\|`size_t`]] | The unsigned integer type carrying that byte count |
| [[Exit\|`exit(1)`]] | Canonical termination path on [[Malloc\|`malloc`]] returning [[NullPointer\|`NULL`]] |

## The two-line discipline ([[dis-2-4-dynamic-memory|Ch 2.4]] headline)

```c
// 1. Always test malloc's return for NULL
int *p = malloc(sizeof(int));
if (p == NULL) { exit(1); }
*p = 6;

// 2. After free, set the pointer to NULL
free(p);
p = NULL;
```

The pairing rule: **every successful [[Malloc|`malloc`]] must be matched by exactly one [[Free|`free`]]** — failure leaks the bytes ([[MemoryLeak|memory leak]]); [[DoubleFree|double-freeing]] or [[UseAfterFree|using after free]] is undefined behavior. The `p = NULL` after `free` defends against both — `free(NULL)` is defined as a no-op (defuses [[DoubleFree|double-free]]) and `*NULL` reliably [[SegmentationFault|segfaults]] (converts [[UseAfterFree|use-after-free]] to a visible failure).

## Dynamically allocated arrays

A single [[Malloc|`malloc`]] sized for `N` elements yields a [[DynamicallyAllocatedArray|dynamically allocated array]] whose use-site syntax is **identical** to a [[dis-1-5-arrays-strings|Ch 1.5]] [[CArray|static array]]:

```c
int *arr = malloc(sizeof(int) * 20);
arr[5] = 42;          // same syntax as static array
free(arr); arr = NULL;
```

The unification extends to function parameters — `void f(int *arr, int size)` accepts both static and heap arrays, completing the [[dis-2-3-pointers-functions|Ch 2.3]] [[PassByPointer|pass-by-pointer]] story.

## Implementation peek

The C runtime maintains a [[FreeList|free list]] of unused heap chunks. Each allocation carries a small [[HeapMetadata|header]] recording its size (which is why [[Free|`free`]] takes only the pointer). Repeated mixed [[Malloc|`malloc`]] / [[Free|`free`]] traffic produces [[HeapFragmentation|heap fragmentation]] — many small free chunks rather than a few large ones — which can make [[Malloc|`malloc`]] return [[NullPointer|`NULL`]] even when the total free byte count is large.

## Failure modes

| Bug | What goes wrong |
|---|---|
| [[MemoryLeak\|Memory leak]] | [[Malloc\|`malloc`]] without matching [[Free\|`free`]] |
| [[UseAfterFree\|Use-after-free]] | [[DereferenceOperator\|Deref]] a [[Pointer\|pointer]] after [[Free\|`free`]] |
| [[DoubleFree\|Double-free]] | [[Free\|`free`]] the same chunk twice |
| [[DanglingPointer\|Dangling pointer]] | Hold a [[Pointer\|pointer]] to released or out-of-scope storage |
| `NULL` deref | Skip the `malloc`-returned-`NULL` check |

## Pedagogical placement

[[dis-2-1-scope-memory|Ch 2.1]] *names* the heap and dynamic allocation, deferring the mechanism. [[dis-2-2-pointers|Ch 2.2]] introduces the [[Pointer|pointer]] machinery and explicitly forward-references dynamic allocation as the *second* of pointers' five use cases. [[dis-2-3-pointers-functions|Ch 2.3]] operationalizes [[PassByPointer|pass-by-pointer]] at the function boundary. [[dis-2-4-dynamic-memory|Ch 2.4]] is where all three lines converge — pointers + program-memory geography + pass-by-pointer all meet at [[Malloc|`malloc`]] / [[Free|`free`]].

## Connections

- [[dis-2-1-scope-memory]] — introducing source (names the concept; defers the mechanism).
- [[dis-2-4-dynamic-memory]] — the chapter that delivers the mechanism.
- [[dis-2-2-pointers]] — supplies the [[Pointer|pointer]] machinery.
- [[dis-2-3-pointers-functions]] — supplies the [[PassByPointer|pass-by-pointer]] mechanism heap arrays reuse.
- [[dis-1-5-arrays-strings]] — supplies the [[CArray|array]] / [[CString|string]] syntax heap allocations reuse.
- [[HeapSection]] — the memory region where dynamic allocations live.
- [[ProcessMemory]] / [[AddressSpace]] — the container.
- [[Pointer]] / [[PointerType]] / [[DereferenceOperator]] / [[NullPointer]] — the mechanism for *referring* to a heap allocation.
- [[Malloc]] / [[Free]] / [[Calloc]] / [[Realloc]] — the API.
- [[SizeOf]] / [[SizeT]] / [[Exit]] — the supporting elements.
- [[DynamicallyAllocatedArray]] — heap-allocated arrays + their unification with [[CArray|static arrays]].
- [[FreeList]] / [[HeapFragmentation]] / [[HeapMetadata]] — implementation peek.
- [[MemoryLeak]] / [[UseAfterFree]] / [[DoubleFree]] / [[DanglingPointer]] — failure modes.
- [[SegmentationFault]] — the visible crash mode of `NULL`-deref / use-after-free-with-`NULL`-discipline.
- [[GlobalVariable]] / [[LocalVariable]] — the *static-storage* alternatives the heap exists to extend beyond.
- [[CLanguage]] / [[DiveIntoSystems]].
