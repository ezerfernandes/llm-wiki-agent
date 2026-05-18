---
title: "Double-Free"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, bugs, security, undefined-behavior]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Double-Free

A **double-free** is the failure mode where the same heap chunk is passed to [[Free|`free`]] twice without an intervening [[Malloc|`malloc`]] re-allocating it. The first `free` returns the chunk to the [[FreeList|free list]]; the second corrupts the free list — typically by inserting a chunk that's already there, or by manipulating the [[HeapMetadata|header]] that's now controlled by allocator bookkeeping rather than user data.

Double-free is **undefined behavior**. Modern allocators ([[glibc|glibc]]'s ptmalloc, jemalloc, mimalloc) include double-free *detection* for common cases (immediate re-free of the same chunk), aborting the process with a diagnostic. But the protection is not complete — a `free`-`malloc`-`free` sequence on the same pointer (where the intervening `malloc` happened to *not* return that chunk) is still a double-free and may not be detected.

## The mechanism

```c
int *p = malloc(sizeof(int));
free(p);
free(p);    // DOUBLE FREE — heap corruption
```

The defense is the same as for [[UseAfterFree|use-after-free]] — set the pointer to [[NullPointer|`NULL`]] after the first `free`:

```c
free(p);
p = NULL;
free(p);    // free(NULL) is a defined no-op — SAFE
```

[[CLanguage|C]] explicitly guarantees `free(NULL)` is a no-op, so the discipline doubles as double-free protection for free.

## Why double-free is a security bug

A corrupted [[FreeList|free list]] is exploitable. The classic technique (*"unlink"* / *"tcache poisoning"* / *"fastbin attack"*, depending on era and allocator) is:

1. Allocate two chunks A and B.
2. Free A, then free B, then free A *again*.
3. The free list now contains A in two positions.
4. Three subsequent allocations return A → B → A — the attacker has obtained *two* live pointers to the same chunk through different program paths.
5. Writing through one and reading through the other produces a type-confused object the attacker controls.

This is why allocator hardening (`tcache_perthread_struct` integrity checks, randomized fastbin pointers via `protect_ptr` since glibc 2.32) is a continuous arms race.

## Defense

- **Set the pointer to [[NullPointer|`NULL`]] after [[Free|`free`]]** — the [[dis-2-4-dynamic-memory|DIS Ch 2.4]] discipline. `free(NULL)` is defined as a no-op, so a second `free(p)` after `p = NULL` is harmless.
- **Single-ownership conventions** — exactly one named owner per allocation, freed exactly once. C++ `unique_ptr`, [[RustLanguage|Rust]] `Box` / move semantics, manual `XXX_destroy()` functions in C libraries.
- **Tools** — [[Valgrind|Valgrind]] / AddressSanitizer detect most double-frees deterministically.

## Distinction from neighbors

- [[MemoryLeak|Leak]] — one `free` too *few*. Double-free — one `free` too *many*.
- [[UseAfterFree|UAF]] — dereferencing a freed chunk. Double-free — *re-freeing* a freed chunk. Both stem from a [[DanglingPointer|dangling pointer]] but the *operation* differs.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Free]] / [[Malloc]] — the API double-free abuses.
- [[NullPointer]] — the discipline-anchor: `free(NULL)` is the defined no-op that defuses repeat `free` calls.
- [[DanglingPointer]] — the pointer state that *enables* double-free.
- [[UseAfterFree]] / [[MemoryLeak]] — adjacent failure modes.
- [[FreeList]] / [[HeapMetadata]] — the substrate double-free corrupts.
- [[DynamicMemoryAllocation]] / [[HeapSection]] — the context.
- [[Pointer]] — the [[dis-2-2-pointers|Ch 2.2]] machinery underneath.
- [[CLanguage]] / [[DiveIntoSystems]].
