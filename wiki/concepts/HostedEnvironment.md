---
title: "Hosted Environment"
type: concept
tags: [embedded, systems-programming, os]
sources: [rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Hosted Environment

One of the two embedded-programming execution regimes [[TheEmbeddedRustBook]] introduces in chapter 3 — the regime *closer to a normal PC*. The hardware exposes a **system interface** (e.g. POSIX) that provides primitives for file system / networking / memory management / threads. Standard libraries depend on these primitives; programs feel like they are running on *"a special-purpose PC environment,"* possibly with sysroot constraints, RAM/ROM ceilings, or special hardware ([[rust-embedded-book-intro-no-std]]).

Typical hosted targets sit on the *Linux-class* end of the spectrum the chapter sketches — e.g. a Raspberry Pi 3B+ (Cortex-A53 @ 1.4 GHz, 1 GB RAM running Linux) — where the [[RustStandardLibrary|Rust standard library]] is fully usable, including its [[RustRuntime|pre-`main` runtime]] and [[HeapAllocation|heap]].

## Contrast: bare metal

The complementary regime is [[BareMetalProgramming|bare-metal]] — *"no code has been loaded before your program"*, no OS, no `libstd`. The split is mutually exclusive and is the central organizing distinction of [[rust-embedded-book-intro-no-std]]. [[TheEmbeddedRustBook]] targets the bare-metal side; the hosted side is named primarily to define what the book is **not** about.

## Connections

- [[BareMetalProgramming]] — the opposite regime; [[NoStd|`#![no_std]`]] required there.
- [[RustStandardLibrary]] — fully available in hosted environments; the runtime + OS abstractions both make sense here.
- [[RustRuntime]] — runs by default on hosted Rust binaries.
- [[EmbeddedSystems]] — broader domain; the hosted/bare-metal split partitions it.
- [[TheEmbeddedRustBook]] — names this concept only to scope it *out* of the book's coverage.
