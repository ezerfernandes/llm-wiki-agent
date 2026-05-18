---
title: "alloc-cortex-m (crate)"
type: entity
tags: [rust, embedded, crate, no-std, allocator, cortex-m]
sources: [rust-embedded-book-intro-no-std, rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# `alloc-cortex-m` (crate)

The **`alloc-cortex-m`** crate is the canonical production-grade [[GlobalAllocator|global allocator]] for [[ARMCortexM|Cortex-M]] firmware in Rust, maintained by the [[RustEmbeddedWorkingGroup]] at <https://github.com/rust-embedded/alloc-cortex-m>. Named in [[rust-embedded-book-intro-no-std]] as *the* go-to allocator for the opt-in heap recipe, and forward-referenced from [[rust-embedded-book-collections-index]]'s repeated *"use a battle tested allocator from crates.io"* caveat against its illustrative [[BumpPointerAllocator|bump-pointer allocator]].

## Role

Provides a `CortexMHeap` type implementing [[GlobalAlloc|`GlobalAlloc`]] (wrapping a `linked_list_allocator` under the hood) suitable for `#[global_allocator] static ALLOCATOR: CortexMHeap = CortexMHeap::empty();` followed by an `ALLOCATOR.init(start, size)` call inside `#[entry] fn main()` once the heap region's start and size are known.

## Connections

- [[GlobalAllocator]] / [[GlobalAlloc]] — the role / trait this crate implements.
- [[AllocCrate]] — the crate that depends on a global allocator being installed.
- [[BumpPointerAllocator]] — the chapter's illustrative alternative that this crate is recommended over.
- [[ARMCortexM]] — the architecture this crate targets.
- [[RustEmbeddedWorkingGroup]] — the maintainer.
- [[TheEmbeddedRustBook]] — files 3/44 and 29/44 ([[rust-embedded-book-intro-no-std]], [[rust-embedded-book-collections-index]]).
