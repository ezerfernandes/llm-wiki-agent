---
title: "Rust Core Library (`libcore`)"
type: concept
tags: [rust, embedded, no-std, standard-library]
sources: [rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Rust Core Library (`libcore`)

The **platform-agnostic subset of the [[RustStandardLibrary|Rust standard library]]**, exposed at [`doc.rust-lang.org/core`](https://doc.rust-lang.org/core/). `core` makes **no assumptions about the system the program will run on** — it does not require an OS, allocator, threads, file system, or any other host facilities ([[rust-embedded-book-intro-no-std]]). When a crate declares [[NoStd|`#![no_std]`]], it links against `core` instead of `std`.

## What `core` provides

- Language primitives — `f32` / `f64`, `&str` and string utilities, slices, iterators, `Option` / `Result`, traits like `Copy`, `Clone`, `Iterator`, `Drop`.
- APIs that expose **processor features** — atomic operations (`core::sync::atomic`) and SIMD intrinsics.
- All the trait / type machinery that powers Rust's compile-time abstractions.

## What `core` deliberately excludes

- **No memory allocator** — and therefore no `Box`, `Vec`, `String`, `BTreeMap`, `HashMap`. The chapter calls out that the allocator is omitted because dynamic memory is *not always desirable in an embedded environment*. Crates needing heap data structures opt back in via the `alloc` / `collections` crates plus a user-supplied global allocator (e.g. [`alloc-cortex-m`](https://github.com/rust-embedded/alloc-cortex-m)).
- **No platform integration** — no file system, no networking, no threads, no environment variables, no command-line arguments.
- **No pre-main [[RustRuntime|runtime]]** — `core` does not bring stack-overflow protection or `main`-thread spawning; that lives in `std`.

## Why it matters

Because `core` makes zero platform assumptions, `no_std` + `core` is what makes Rust usable for *stage-0 / bootstrapping* code — [[Bootloader|bootloaders]], firmware, kernels — i.e. code that runs **before** anything else exists on the machine ([[rust-embedded-book-intro-no-std]]).

## Connections

- [[NoStd]] — the language switch that selects `core` over `std`.
- [[RustStandardLibrary]] — the superset; `core` is *"a platform-agnostic subset of the std crate."*
- [[RustLanguage]] — `core` ships with every Rust toolchain.
- [[HeapAllocation]] — not provided by `core` by default; the central missing capability.
- [[BareMetalProgramming]] / [[EmbeddedSystems]] / [[Microcontroller]] — the contexts where `core`-only Rust runs.
- [[TheEmbeddedRustBook]] — every code chapter assumes `core`-only by default.
