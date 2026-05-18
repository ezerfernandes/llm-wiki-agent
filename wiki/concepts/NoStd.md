---
title: "`no_std`"
type: concept
tags: [rust, embedded, no-std, language-feature]
sources: [rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# `no_std`

`#![no_std]` is a **crate-level attribute** in [[RustLanguage|Rust]] that tells the compiler **not** to link the [[RustStandardLibrary|standard library]] (`std`) and instead link only the platform-agnostic [[RustCoreLibrary|core library]] (`core`). It is the one-line language switch that puts a Rust crate into *bare-metal* mode, and the gate through which every example in [[TheEmbeddedRustBook]] enters embedded territory ([[rust-embedded-book-intro-no-std]]).

## What `no_std` actually removes

`std` is *not* just a thicker API over `core` — it is also (a) the OS-abstraction layer (file system / network / threads / memory mgmt) and (b) a **runtime** ([[RustRuntime]]) that runs *before* `main()` to set up stack-overflow protection, process command-line arguments, and spawn the main thread. `#![no_std]` removes both.

The chapter's summary table (the load-bearing artifact of this concept):

| Feature                                                   | `no_std` | `std` |
|-----------------------------------------------------------|:--------:|:-----:|
| [[HeapAllocation\|heap]] (dynamic memory)                 |   \*     |   ✓   |
| collections (`Vec`, `BTreeMap`, …)                        |  \*\*    |   ✓   |
| stack overflow protection                                 |    ✘     |   ✓   |
| runs init code before main                                |    ✘     |   ✓   |
| `libstd` available                                        |    ✘     |   ✓   |
| `libcore` available                                       |    ✓     |   ✓   |
| writing firmware, kernel, or [[Bootloader\|bootloader]]   |    ✓     |   ✘   |

\* via the opt-in `alloc` crate + a user-supplied global allocator (e.g. [`alloc-cortex-m`](https://github.com/rust-embedded/alloc-cortex-m)).
\*\* via the `collections` crate + a configured global default allocator; `HashMap` / `HashSet` remain unavailable even then because `core` has no secure RNG.

## Why it exists

`#![no_std]` is the precondition for using Rust as a **stage-0 systems language**: the chapter spells out that *"no_std and libcore code can be used for any kind of bootstrapping (stage 0) code like bootloaders, firmware or kernels"* ([[rust-embedded-book-intro-no-std]]). The flip side — `std` cannot write any of those, because it presumes its own runtime is already running.

Stabilized by [RFC-1184](https://github.com/rust-lang/rfcs/blob/master/text/1184-stabilize-no_std.md).

## Connections

- [[RustCoreLibrary]] — what `no_std` crates link against instead of [[RustStandardLibrary|std]].
- [[RustStandardLibrary]] — the library `no_std` opts out of.
- [[RustRuntime]] — the pre-main initialization that `no_std` removes; the non-obvious cost of opting out.
- [[BareMetalProgramming]] — the execution model `no_std` enables in [[RustLanguage|Rust]].
- [[EmbeddedSystems]] / [[Microcontroller]] — typical targets where `no_std` is required.
- [[HeapAllocation]] — the most prominent default-off feature; recovered via `alloc` + a global allocator.
- [[Bootloader]] — canonical stage-0 use case for `no_std`.
- [[TheEmbeddedRustBook]] — every code chapter assumes `#![no_std]`.
