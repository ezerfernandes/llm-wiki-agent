---
title: "Heap Section (C Program Memory)"
type: concept
tags: [c-language, memory, dynamic-allocation, address-space]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Heap Section

The **heap** is the region of a [[CLanguage|C]] program's [[ProcessMemory|address space]] reserved for [[DynamicMemoryAllocation|dynamically allocated]] storage. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "The *heap* portion of memory is the part of a program's address space associated with dynamic memory allocation."

[[dis-2-1-scope-memory|Ch 2.1]] *names* the heap and places it inside the four-region picture; the **mechanism** ([[Malloc|`malloc`]] / [[Calloc|`calloc`]] / [[Realloc|`realloc`]] / [[Free|`free`]]) is deferred to **Ch 2.4**. The wiki should therefore treat this page as a *placeholder* for the heap's existence and lifetime story — not a complete account of how to use it.

## Properties (preview)

- **Programmer-controlled lifetime** — neither pushed/popped by call/return ([[StackSection|stack]]) nor program-lifetime ([[DataSection|data]] / [[CodeSection|code]]). The programmer requests storage with [[Malloc|`malloc`]] and releases it with [[Free|`free`]].
- **Dynamic size** — unlike the [[StackSection|stack]] (whose growth follows call depth) and [[DataSection|data section]] (compile-time sized), the heap grows on demand from a few bytes to gigabytes.
- **Failure mode: [[MemoryLeak|leaks]]** — forgetting to [[Free|`free`]] heap allocations is a major class of C bugs; the heap holds onto the bytes until the program exits.
- **Failure mode: dangling pointers** — using a pointer *after* [[Free|`free`]]ing what it pointed to is undefined behavior, often security-relevant ([[UseAfterFree|use-after-free]]).

## Why it sits between the stack and data section

Ch 2.1 introduces the heap because [[GlobalVariable|globals]] (data section, program-lifetime) and [[LocalVariable|locals]] (stack, call-lifetime) cannot cover the case where a function needs to *return* a value that **outlives the call** without making it global. That is the heap's job: a function can [[Malloc|`malloc`]] storage, populate it, return the [[CMemoryAddress|address]] to its caller, and the storage survives even though the callee's [[StackFrame|frame]] is popped. This is the story Ch 2.4 will tell in full.

## Pedagogical placement

This is the third of the four [[ProcessMemory|program-memory]] regions Ch 2.1 introduces. It is **named** here in preparation for Ch 2.2's [[Pointer|pointers]] and Ch 2.4's [[DynamicMemoryAllocation|dynamic allocation]] — those two chapters are the *point* of having heap storage in the first place, since you need a [[Pointer|pointer]] to refer to a heap allocation and [[Malloc|`malloc`]] to create one.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[ProcessMemory]] / [[AddressSpace]] — the container.
- [[CodeSection]] / [[DataSection]] / [[StackSection]] — the other three regions.
- [[DynamicMemoryAllocation]] — the mechanism that populates the heap; deferred to Ch 2.4.
- [[CLanguage]] / [[DiveIntoSystems]].
