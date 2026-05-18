---
title: "Global Allocator"
type: concept
tags: [rust, embedded, memory, no-std, allocator]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# Global Allocator

A **global allocator** is the single, program-wide source of dynamic memory for every [[HeapAllocation|heap]] allocation a Rust program makes via [[AllocCrate|`alloc`]] (`Box`, `Vec`, `String`, `BTreeMap`, …) or [[RustStandardLibrary|`std`]] collections. In Rust, the global allocator is selected via the `#[global_allocator]` attribute on a `static` value whose type implements the [[GlobalAlloc|`GlobalAlloc`]] trait ([[rust-embedded-book-collections-index]]).

## The contract

```rust
#[global_allocator]
static HEAP: MyAllocator = MyAllocator { /* … */ };
```

The chosen type must implement [[GlobalAlloc|`GlobalAlloc`]] — the two-method `unsafe trait` (`alloc(&self, Layout) -> *mut u8` returning null on [[OutOfMemory|OOM]], and `dealloc(&self, *mut u8, Layout)`).

On [[HostedEnvironment|hosted]] targets, `std` installs a system-malloc-backed allocator by default. Under [[NoStd|`#![no_std]`]] there is **no default** — the user must provide one before any `alloc` collection can be constructed ([[rust-embedded-book-collections-index]]).

## Embedded choices

The chapter implements a **[[BumpPointerAllocator|bump-pointer allocator]]** for pedagogical completeness — minimal, single-core, monotonically increases a `head` pointer, and **never frees** — and strongly cautions against shipping it (*"we *strongly* suggest you use a battle tested allocator from crates.io"*). The canonical [[ARMCortexM|Cortex-M]] production choice forward-referenced from [[rust-embedded-book-intro-no-std]] is **`alloc-cortex-m`** ([[AllocCortexMCrate|`alloc-cortex-m`]]).

## Interrupt safety

A global allocator is shared mutable state by definition, so on single-core embedded targets it must serialize allocation calls against interrupt handlers — the chapter's bump allocator does this by wrapping every `alloc` call in `cortex_m::interrupt::free` ([[CriticalSection|critical section]] from [[CortexMCrate|`cortex-m`]]). Multi-core targets need atomic-instruction-based allocators ([[Atomic|atomics]] / lock-free designs) since [[CriticalSection|critical sections]] don't provide cross-core exclusivity ([[rust-embedded-book-concurrency-index]]).

## Connections

- [[GlobalAlloc]] — the trait the global allocator implements.
- [[AllocCrate]] — the crate that depends on a global allocator being installed.
- [[OutOfMemory]] — the failure mode (signaled by `alloc` returning null; then dispatched to `#[alloc_error_handler]`).
- [[HeapAllocation]] — what global allocators serve.
- [[NoStd]] — the regime that makes the choice user-explicit.
- [[BumpPointerAllocator]] — the chapter's illustrative implementation.
- [[CriticalSection]] / [[CortexMCrate]] — the single-core interrupt-safety primitive used by the chapter's allocator.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
