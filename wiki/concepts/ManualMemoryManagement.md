---
title: "Manual Memory Management"
type: concept
tags: [memory, systems-programming, allocation, resource-management]
sources: [zig-in-depth-overview]
last_updated: 2026-06-07
---

# Manual Memory Management

Manual memory management is a memory model in which the programmer is explicitly responsible for allocating and freeing memory, rather than relying on a garbage collector or other automatic reclamation. It is characteristic of systems languages such as C and [[Zig]], where predictable performance, low latency, and the ability to run without a runtime are required.

## In Zig

Per [[zig-in-depth-overview]], [[Zig]] adopts manual memory management as a deliberate design choice: programmers "must manage their own memory, and must handle memory allocation failure." Zig makes this tractable and verifiable through several features:

- **Explicit allocators** — no hidden allocations; allocation goes through an [[ZigAllocator|allocator]] parameter that can fail. See [[ZigAllocator]].
- **`defer` / `errdefer`** — scope-based cleanup that makes freeing resources local to their acquisition and easy to audit. See [[DeferStatement]].
- **Allocation failure as a value** — allocating functions return [[ErrorUnion|error unions]], so out-of-memory is handled like any other error.

This model is what lets Zig code run in freestanding/embedded environments, OS kernels, real-time software, and WebAssembly, and lets the standard library work without an OS or libc.

## Trade-offs

Manual management trades the safety net of automatic reclamation for control and predictability. The risks it must guard against — dangling pointers, leaks, double frees, buffer overflows — are mitigated in Zig by safety-checked build modes and tools like the leak-detecting `DebugAllocator`. See [[UndefinedBehavior]], [[DanglingPointer]], [[BufferOverflow]].

## Connections

- [[Zig]] — adopts manual memory management with safety tooling.
- [[ZigAllocator]] — explicit allocator passing is Zig's mechanism.
- [[DeferStatement]] — defer/errdefer make cleanup verifiable.
- [[DynamicMemoryAllocation]] — the heap allocation this model governs.
- [[MemoryAllocation]] — general background.
- [[DanglingPointer]] / [[BufferOverflow]] / [[UndefinedBehavior]] — failure modes it must avoid.
- [[zig-in-depth-overview]] — source linking this model to Zig's design.
