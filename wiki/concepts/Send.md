---
title: "Send (Rust trait)"
type: concept
tags: [rust, concurrency, trait, embedded]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# `Send` (Rust trait)

Marker trait in [[RustLanguage|Rust]] indicating a type *"can safely be moved to another thread"* ([[rust-embedded-book-concurrency-index]]). Auto-derived by the compiler for most types; explicit `unsafe impl Send for T {}` is needed only when a type contains raw pointers or other non-`Send` interior that is nevertheless safe to move across threads.

**Embedded interpretation** (per [[TheEmbeddedRustBook]]'s *Concurrency* chapter): *"in an embedded context, we consider interrupts to be executing in a separate thread to the application code"* — so any type that is moved from `main` into a static accessible from an [[Interrupt|interrupt handler]] (via [[Mutex|`Mutex`]] + interior-mutability) must be `Send`.

**Relationship to [[Sync]]**: `T: Sync` ⇔ `&T: Send`. The two together carve the *thread-safety lattice* of Rust. The `cortex_m::interrupt::Mutex<T>` implements [[Sync]] for any `T: Send` — i.e. you can share a `Send` value across the `main` / interrupt boundary by routing it through a critical-section-gated container.

## Connections

- [[Sync]] — sibling marker trait; *shared across threads* rather than *moved between them*.
- [[Mutex]] — `cortex_m::interrupt::Mutex<T>: Sync` requires `T: Send`.
- [[Interrupt]] — the "other thread" in embedded contexts.
- [[RustLanguage]] — the language-level traits this concept lives in.
- [[InteriorMutability]] — interior-mutability containers ([[CellRust|`Cell`]], [[RefCell]]) have specific `Send` / `Sync` properties that matter for static placement.
