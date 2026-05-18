---
title: "alloc (crate)"
type: entity
tags: [rust, embedded, crate, no-std, allocator]
sources: [rust-embedded-book-collections-index, rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# `alloc` (crate)

The **`alloc`** crate ships with the standard Rust distribution and provides the heap-backed collection types — `Box`, `Vec`, `String`, `BTreeMap`, etc. — that [[RustStandardLibrary|`std`]] re-exports. Under [[NoStd|`#![no_std]`]], `alloc` is the **opt-in path back to dynamic collections**: `extern crate alloc; use alloc::vec::Vec;` (unstable `#![feature(alloc)]` in the chapter's snippet; stable on modern toolchains) — no `Cargo.toml` entry required ([[rust-embedded-book-collections-index]]).

## Activation contract

Two declarations the user must supply ([[rust-embedded-book-collections-index]]):

1. A [[GlobalAllocator|`#[global_allocator]`]] `static` implementing the [[GlobalAlloc|`GlobalAlloc`]] trait — defines how `alloc` gets memory. The chapter implements a [[BumpPointerAllocator|bump-pointer allocator]] for illustration but strongly recommends a battle-tested crates.io implementation in production. The forward-referenced canonical Cortex-M choice is `alloc-cortex-m` ([[rust-embedded-book-intro-no-std]]).
2. An [[AllocErrorHandlerAttribute|`#[alloc_error_handler]`]] `fn(Layout) -> !` — defines what to do on [[OutOfMemory|OOM]] (unstable `alloc_error_handler` feature).

## Connections

- [[HeaplessCrate]] — the **alternative** crate; fixed-capacity stack-allocated collections, no allocator required, constant-time push, OOM impossible.
- [[GlobalAllocator]] / [[GlobalAlloc]] — the trait `alloc` plugs into.
- [[OutOfMemory]] — the failure mode `alloc` exposes implicitly at every growth site.
- [[HeapAllocation]] — the underlying mechanism.
- [[NoStd]] — the regime that makes `alloc` *opt-in* rather than implicit.
- [[RustStandardLibrary]] — re-exports the same collection types over its own default allocator.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
