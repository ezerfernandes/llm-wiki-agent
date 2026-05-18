---
title: "Out Of Memory (OOM)"
type: concept
tags: [rust, embedded, memory, no-std, allocator, error-handling]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# Out Of Memory (OOM)

**Out Of Memory (OOM)** is the failure condition where a [[GlobalAllocator|global allocator]] cannot satisfy an allocation request — there is no contiguous, properly-aligned region of the requested size available. In embedded Rust, OOM is the marquee implicit failure mode of [[AllocCrate|`alloc`]]-based code, and the central reason [[HeaplessCrate|`heapless`]] exists as an alternative ([[rust-embedded-book-collections-index]]).

## Two surfaces

1. **The allocator's signal.** A [[GlobalAlloc|`GlobalAlloc`]]-implementing allocator returns a **null `*mut u8`** from its `alloc(layout)` method to indicate OOM. The chapter's bump-pointer allocator does this when `start + size > self.end` ([[rust-embedded-book-collections-index]]).
2. **The user's handler.** When `alloc` (or one of its collections like `Vec::push`) observes a null return, it dispatches to the program's `#[alloc_error_handler]` (unstable `alloc_error_handler` feature) — a `fn(Layout) -> !` that the user *must* supply. The chapter's stub calls `cortex_m::asm::bkpt()` then `loop {}`, so a debugger catches the failure.

## Why it is *implicit and non-local* in `alloc`

*"all `alloc::Vec.push` invocations can potentially generate an OOM condition"* ([[rust-embedded-book-collections-index]]) — every growth site is an OOM site, even apparently-tiny ones. Worse, the *cause* of the failure may be far from the *observed* site: a leak or [[MemoryFragmentation|fragmentation]] elsewhere can exhaust the allocator, and the next innocent `vec.reserve(1)` is what tips it over. The chapter notes *"memory leaks are possible in safe Rust."* `try_reserve` exists as a proactive check but must be called explicitly.

## Why [[HeaplessCrate|`heapless`]] makes it impossible

With **no global allocator**, there is no shared resource to exhaust. Capacity-exhaustion failures (`push` returning `Err`) are **local** — they reflect *this specific collection's* fixed capacity, not the program's aggregate memory pressure. *"If you exclusively use `heapless` collections and you don't use a memory allocator for anything else then an OOM condition is impossible."* ([[rust-embedded-book-collections-index]]).

## Connections

- [[GlobalAllocator]] / [[GlobalAlloc]] — null-pointer return is the allocator's OOM signal.
- [[AllocCrate]] — the crate where OOM is an implicit, non-local failure at every growth site.
- [[HeaplessCrate]] — the alternative that makes OOM impossible (local capacity failures only).
- [[MemoryFragmentation]] — the failure-amplifier that makes OOM's observed location diverge from its cause.
- [[BumpPointerAllocator]] — the chapter's illustrative allocator, which signals OOM via `ptr::null_mut()`.
- [[HeapAllocation]] — the substrate where OOM can occur.
- [[NoStd]] — the regime that forces the user to declare an `#[alloc_error_handler]` explicitly.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
