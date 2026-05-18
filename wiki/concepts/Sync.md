---
title: "Sync (Rust trait)"
type: concept
tags: [rust, concurrency, trait, embedded]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# `Sync` (Rust trait)

Marker trait in [[RustLanguage|Rust]] indicating a type *"can be safely shared between multiple threads"* ([[rust-embedded-book-concurrency-index]]). Formally: `T: Sync` ⇔ `&T: Send` ([[Send]]).

**`static` requires `Sync`**: *"`static` variables *must* be `Sync`, since they can be accessed by multiple threads"* ([[rust-embedded-book-concurrency-index]]). This is the load-bearing rule for embedded shared state — any data accessible from both `main` and an [[Interrupt|interrupt handler]] lives in a `static` and must therefore implement `Sync`.

**Embedded interpretation**: interrupts and `main` are treated as separate threads; data crossing that boundary must be `Sync`. [[CellRust|`Cell`]] and [[RefCell]] are **not** `Sync` (they're single-thread interior-mutability), which is why they cannot be used in a `static` directly — they must be wrapped in a [[Mutex|`Mutex`]] that re-implements `Sync` (only safely accessible inside a [[CriticalSection|critical section]]).

**`unsafe impl Sync`** is the manual escape hatch when a type's `Sync`-ness is *load-bearing on programmer-supplied invariants* — e.g. `CSCounter` in the *Concurrency* chapter wraps an [[UnsafeCell|`UnsafeCell`]] (auto-not-`Sync`) and provides safe access only through methods that require a `CriticalSection` token: *"to tell the compiler we have taken care that the `CSCounter` is in fact safe to share between threads, we implement the `Sync` trait explicitly. As with the previous use of critical sections, this is only safe on single-core platforms."*

## Connections

- [[Send]] — sibling marker trait; `T: Sync` ⇔ `&T: Send`.
- [[Mutex]] — `cortex_m::interrupt::Mutex<T>: Sync` for any `T: Send`; *"it can do this safely because it only gives access to its contents during a critical section."*
- [[CriticalSection]] — the runtime mechanism that *makes* `cortex_m::interrupt::Mutex<T>` `Sync`-safe.
- [[UnsafeCell]] — the canonical non-`Sync` type; wrapping it in a critical-section-gated container is how you recover `Sync`.
- [[InteriorMutability]] — `Sync`-ness is the axis along which `Cell` / `RefCell` / `Mutex<Cell>` / `Mutex<RefCell>` partition.
- [[Interrupt]] — the "other thread" in embedded.
- [[ARMCortexM]] — `unsafe impl Sync` for critical-section-gated types is single-core-only; multi-core (SMP) needs stronger primitives ([[Atomic]]).
- [[RustLanguage]] — the language-level trait.
