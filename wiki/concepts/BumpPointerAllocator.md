---
title: "Bump-Pointer Allocator"
type: concept
tags: [rust, embedded, memory, no-std, allocator]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# Bump-Pointer Allocator

A **bump-pointer allocator** (a.k.a. *linear allocator*) is the simplest possible [[GlobalAllocator|global allocator]] design: maintain a single `head` pointer into a contiguous memory region, and on each `alloc(layout)` request, round `head` up to the requested alignment, claim `layout.size()` bytes starting there, and bump `head` past them. There is **no `free`** — `dealloc` is a no-op. Used as the illustrative `#[global_allocator]` in the *Collections* chapter of [[TheEmbeddedRustBook]] ([[rust-embedded-book-collections-index]]).

## The chapter's worked implementation

```rust
unsafe impl GlobalAlloc for BumpPointerAlloc {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        interrupt::free(|_| {                       // single-core interrupt safety
            let head = self.head.get();             // *mut usize via UnsafeCell
            let size = layout.size();
            let align = layout.align();
            let align_mask = !(align - 1);
            let start = (*head + align - 1) & align_mask;
            if start + size > self.end {
                ptr::null_mut()                     // OOM signal
            } else {
                *head = start + size;
                start as *mut u8
            }
        })
    }
    unsafe fn dealloc(&self, _: *mut u8, _: Layout) { /* never deallocates */ }
}

#[global_allocator]
static HEAP: BumpPointerAlloc = BumpPointerAlloc {
    head: UnsafeCell::new(0x2000_0100),
    end: 0x2000_0200,
};
```

Key design notes ([[rust-embedded-book-collections-index]]):

- **`UnsafeCell<usize>` for `head`** — gives [[InteriorMutability|interior mutability]] over the `&self` of `GlobalAlloc::alloc`. `unsafe impl Sync` is required to put the allocator in a `static`.
- **`cortex_m::interrupt::free` for serialization** — the [[CriticalSection|critical-section]] primitive from [[CortexMCrate|`cortex-m`]] makes the allocator interrupt-safe on **single-core only**. The same primitive used pervasively in [[rust-embedded-book-concurrency-index]].
- **Null pointer = OOM** when `start + size > self.end`.
- **Fixed RAM window** `[0x2000_0100, 0x2000_0200]` — the user must guarantee no other part of the program uses this region.

## Properties

- **O(1)** allocation, **trivially const-time WCET** (no fragmentation logic).
- **Smallest code size** of any allocator design.
- **Never reclaims memory** — total program-lifetime allocation is capped by the region size.

## When it's appropriate

- *Educational demos* — the chapter's stated reason.
- Programs with predictable, monotonic allocation patterns (e.g. arena allocation per frame / per request) where the entire arena is reset wholesale rather than per-object.
- The chapter is explicit it is **not** for production: *"we *strongly* suggest you use a battle tested allocator from crates.io in your program instead of this allocator."*

## Connections

- [[GlobalAllocator]] / [[GlobalAlloc]] — the abstract role this concretizes.
- [[AllocCrate]] — the consumer of the allocator's services.
- [[OutOfMemory]] — signaled via null `*mut u8`.
- [[CriticalSection]] / [[CortexMCrate]] — the single-core interrupt-safety primitive.
- [[UnsafeCell]] / [[InteriorMutability]] — the mechanism that lets `&self` mutate `head`.
- [[AllocCortexMCrate]] — the production-grade Cortex-M alternative the chapter recommends instead.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
