---
title: "Memory Leak"
type: concept
tags: [c-language, dynamic-allocation, heap, memory, bugs, undefined-behavior]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Memory Leak

A **memory leak** is the failure mode where heap memory allocated via [[Malloc|`malloc`]] (or [[Calloc|`calloc`]] / [[Realloc|`realloc`]]) is never released via [[Free|`free`]] before the program ends or the last [[Pointer|pointer]] to it is lost. The bytes remain allocated for the program's lifetime, gradually shrinking the available [[HeapSection|heap]] and — in long-running programs — eventually causing [[Malloc|`malloc`]] to return [[NullPointer|`NULL`]] from out-of-memory.

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]'s framing: *"when a program no longer needs the heap memory it dynamically allocated with `malloc`, it should explicitly deallocate the memory by calling the `free` function."* Skipping the explicit `free` is the leak.

## The two flavors

1. **Forgot to call [[Free|`free`]] at all.** The simplest case: a function [[Malloc|`malloc`]]s, uses the memory, and returns without freeing. If the pointer was on the [[StackSection|stack]] and is now gone, the heap chunk is permanently unreachable.
2. **Lost the [[Pointer|pointer]] before [[Free|`free`]]ing.** Overwriting the only pointer to a chunk with a new [[Malloc|`malloc`]] result, or letting it go out of scope, makes the chunk unreachable — the program has no way left to name the bytes for [[Free|`free`]].

## Why it matters

- **Long-running programs degrade.** A server that leaks 100 bytes per request and serves 10⁹ requests has leaked ~100 GB. The leak isn't visible at request granularity — it shows up as a process that keeps growing until the OS kills it (OOM).
- **Short-lived programs are *partially* exempt.** When the program exits, the OS reclaims the process's entire address space — leaks don't *persist* across runs. But that's a property of the OS, not of the program; it doesn't make leaks defensible in correct code.
- **Embedded / `no_std` is worse.** On [[BareMetalProgramming|bare-metal]] systems without an OS to reclaim, the firmware lifetime *is* the leak's lifetime — see [[HeapAllocation|the embedded heap story]].

## Defense

- **Pair every [[Malloc|`malloc`]] with exactly one [[Free|`free`]].** The corpus's headline discipline.
- **Match allocation lifetime to the obvious owner.** If a function allocates a structure and returns it, the caller frees it; if a function only reads, it does not free. Document the contract.
- **Tools** — [[Valgrind|Valgrind]]'s `memcheck`, AddressSanitizer's `-fsanitize=leak`, and language-level alternatives ([[RustLanguage|Rust]] ownership, C++ RAII / `unique_ptr`) all aim at the same bug.

## Distinction from neighbors

- A leak is **not** a [[UseAfterFree|use-after-free]] — the pointer either still references valid memory (you just never freed) or has been dropped (you can't free).
- A leak is **not** a [[DoubleFree|double-free]] — one `free` (or none) too few, not one too many.
- A leak is **not** a [[DanglingPointer|dangling pointer]] — the memory is still allocated; you just have no way to find it.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Malloc]] / [[Free]] — the API whose imbalance creates the leak.
- [[DynamicMemoryAllocation]] — the mechanism leaks live inside.
- [[HeapSection]] — the region that accumulates leaked bytes.
- [[UseAfterFree]] / [[DoubleFree]] / [[DanglingPointer]] — the adjacent failure modes.
- [[NullPointer]] — the eventual [[Malloc|`malloc`]] return value once enough leaks accumulate.
- [[Pointer]] — the mechanism whose loss makes a leak unrecoverable.
- [[HeapAllocation]] — the embedded-Rust angle on the same hazard.
- [[CLanguage]] / [[DiveIntoSystems]].
