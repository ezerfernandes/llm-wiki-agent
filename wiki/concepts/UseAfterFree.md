---
title: "Use-After-Free"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, bugs, security, undefined-behavior]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Use-After-Free

A **use-after-free** (UAF) is the failure mode where a [[Pointer|pointer]] is [[DereferenceOperator|dereferenced]] *after* the heap chunk it pointed to has been released via [[Free|`free`]]. The bytes are no longer the program's to read or write — the [[FreeList|heap manager]] may have already handed them out to a subsequent [[Malloc|`malloc`]] call, or zeroed them, or used them for its own bookkeeping ([[HeapMetadata|metadata]]).

UAF is **undefined behavior**: the program may appear to work (the bytes happen to still hold the old value), it may crash (the [[FreeList|free list]] reused the chunk and overwrote it), or it may execute attacker-controlled code (if the chunk has been reused for a structure with function pointers and the attacker shaped the input). It is one of the most exploited bug classes in [[CLanguage|C]] / C++ code in the wild.

## The mechanism

```c
int *p = malloc(sizeof(int));
*p = 42;
free(p);           // chunk returned to the free list
printf("%d\n", *p); // UAF — p is now a DANGLING POINTER
```

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]: *"After calling free, the freed memory should no longer be used by the program … if it gets accidentally used in the program, the program will crash on a `NULL`-pointer dereference rather than execute with bad memory contents (which could result in difficult-to-debug bad behavior)."* The *difficult-to-debug bad behavior* is UAF.

## The discipline

Per [[dis-2-4-dynamic-memory|Ch 2.4]]'s headline rule — set the pointer to [[NullPointer|`NULL`]] after [[Free|`free`]]ing:

```c
free(p);
p = NULL;        // now any accidental *p reliably segfaults
```

The trade-off: a UAF that would have silently read garbage (or attacker-controlled bytes) is converted into a [[SegmentationFault|segfault]] — a *visible* failure the developer can debug, rather than a *silent* one that surfaces hours later or never. This is why the corpus calls `NULL`-after-`free` the canonical defense.

The discipline is **not** sufficient when *multiple* pointers reference the same chunk — setting one to `NULL` doesn't disarm the others. That case requires ownership tracking (manual in [[CLanguage|C]], compiler-enforced in [[RustLanguage|Rust]], reference-counted in shared-ptr disciplines).

## Why UAF is a security bug

Once a freed chunk is reused for a different object — typically larger or differently-typed — a stale pointer dereferencing it sees the *new* object's bytes through the *old* type's lens. Classic exploitation pattern:

1. Allocate a victim object containing a function pointer.
2. Free it.
3. Trigger an allocator path that reuses the chunk for an attacker-controlled buffer.
4. The dangling pointer now reads attacker-controlled bytes as a function pointer.
5. Indirect call → arbitrary code execution.

This is why UAF lands routinely in browser CVEs and kernel CVEs.

## Distinction from neighbors

- A UAF *uses* a freed chunk; a [[MemoryLeak|leak]] *never frees* a still-reachable chunk.
- A UAF dereferences a [[DanglingPointer|dangling pointer]] — the dangling-pointer concept is the *state*, UAF is the *operation*.
- A [[DoubleFree|double-free]] frees the same chunk twice — also UB, but the corrupting operation is `free`, not deref.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Free]] / [[Malloc]] — the operations that bracket the UAF window.
- [[DanglingPointer]] — the pointer state that *enables* UAF.
- [[NullPointer]] — the discipline-anchor that converts UAF to [[SegmentationFault|segfault]].
- [[MemoryLeak]] / [[DoubleFree]] — adjacent failure modes.
- [[DynamicMemoryAllocation]] — the mechanism UAF inhabits.
- [[HeapSection]] / [[FreeList]] / [[HeapMetadata]] — the substrate UAF mis-reads.
- [[Pointer]] / [[DereferenceOperator]] — the [[dis-2-2-pointers|Ch 2.2]] machinery the UAF mis-uses.
- [[SegmentationFault]] — the *desired* outcome under the `NULL`-after-`free` discipline; the *undesired* alternative when discipline is missing.
- [[RustLanguage|Rust]]'s borrow checker — a language-level prevention of UAF.
- [[CLanguage]] / [[DiveIntoSystems]].
