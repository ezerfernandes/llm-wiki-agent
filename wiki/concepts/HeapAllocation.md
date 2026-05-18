---
title: "Heap Allocation (Dynamic Memory)"
type: concept
tags: [rust, embedded, memory, no-std]
sources: [rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Heap Allocation (Dynamic Memory)

**Dynamic memory allocation** — runtime growth/shrinkage of memory regions via an allocator (`malloc`/`free`, or in [[RustLanguage|Rust]] `Box::new` / `Vec::push` / `String::from`). Lives on the **heap**, distinct from the fixed-size stack and `.data` / `.bss` regions in [[SRAM]].

## Why it's the marquee thing `no_std` removes

[[RustCoreLibrary|libcore]] *deliberately omits a memory allocator*, because dynamic memory is **not always desirable in an embedded environment** — fragmentation, unbounded worst-case latency, unpredictable footprint, and out-of-memory failure modes all conflict with the determinism, real-time, and tight-RAM budgets typical of [[Microcontroller|MCU]] firmware ([[rust-embedded-book-intro-no-std]]). Consequently, under [[NoStd|`#![no_std]`]] the heap is **off by default** — no `Box`, no `Vec`, no `String`, no `BTreeMap`, no `HashMap`.

## Opt-in recipe (the embedded Rust pattern)

The chapter lays out the canonical opt-in path:

1. Add the `alloc` crate dependency. This brings `Box`, `Vec`, `String`, etc. **APIs** back, but not their implementation — `alloc` requires a global allocator.
2. Supply a **global allocator** suitable for the target. The chapter's reference is [`alloc-cortex-m`](https://github.com/rust-embedded/alloc-cortex-m) for [[ARMCortexM|Cortex-M]] targets.
3. For richer containers — `BTreeMap`, etc. — add the `collections` crate plus a configured default allocator.
4. `HashMap` / `HashSet` remain **unavailable even with an allocator** because [[RustCoreLibrary|`core`]] lacks a secure random-number generator that hash-DoS resistance requires.

## Connections

- [[NoStd]] — the attribute that removes the heap by default.
- [[RustCoreLibrary]] — the library that omits the allocator.
- [[RustStandardLibrary]] — supplies a default allocator on hosted targets.
- [[BareMetalProgramming]] / [[EmbeddedSystems]] / [[Microcontroller]] — the contexts where heap-off-by-default is a feature, not a bug.
- [[SRAM]] — the on-chip memory the heap (when enabled) shares with stack / `.data` / `.bss` on an MCU; 48 KiB total on the [[STM32F303VCT6]] ([[rust-embedded-book-intro-hardware]]) — a hard ceiling on heap usage.
- [[TheEmbeddedRustBook]] — every later chapter codes against this constraint.
