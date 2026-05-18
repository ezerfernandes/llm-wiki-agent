---
title: "bare-metal"
type: entity
tags: [rust, embedded, crate, concurrency]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# bare-metal

`bare-metal` is a [[RustLanguage|Rust]] crate ([crates.io/crates/bare-metal](https://crates.io/crates/bare-metal)) maintained by the [[RustEmbeddedWorkingGroup|Rust Embedded Working Group]] that provides **architecture-agnostic primitives for bare-metal concurrency** — most notably the **`CriticalSection`** token type that [[CortexMCrate|`cortex-m`]] (and other arch-specific micro-architecture crates) re-export and use as the proof-of-being-inside-a-critical-section token.

## Why it shows up in the Concurrency chapter

[[rust-embedded-book-concurrency-index|The *Concurrency* chapter]] does not name `bare-metal` directly, but every `cortex_m::interrupt::CriticalSection` and `cortex_m::interrupt::Mutex` reference in the chapter is **structurally** a `bare-metal::CriticalSection` / `bare-metal::Mutex` re-exported through the arch-specific surface. The split exists so that the same `CriticalSection` *token* (and `Mutex<T>` wrapper) can be produced and consumed by **multiple architectures** — Cortex-M (`cortex-m`), RISC-V (`riscv`), etc. — without each arch crate redefining its own incompatible token.

## Connections

- [[CortexMCrate|`cortex-m`]] — re-exports `bare-metal::CriticalSection` and `bare-metal::Mutex` as `cortex_m::interrupt::CriticalSection` / `cortex_m::interrupt::Mutex`.
- [[CriticalSection]] — the cross-platform concept this crate provides the token type for.
- [[Mutex]] — `bare-metal::Mutex<T>` is the cross-platform critical-section-gated mutex.
- [[RustEmbeddedWorkingGroup]] — maintainer.
- [[ARMCortexM]] — one architecture that uses this crate via `cortex-m`.
- [[TheEmbeddedRustBook]] — the *Concurrency* chapter is the corpus's first chapter where this crate's primitives become load-bearing.
