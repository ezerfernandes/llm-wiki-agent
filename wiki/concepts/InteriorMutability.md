---
title: "Interior Mutability"
type: concept
tags: [rust, language-feature, concurrency]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# Interior Mutability

The [[RustLanguage|Rust]] pattern of **mutating a value through a shared (`&T`) reference**, bypassing the borrow checker's usual *one mutable XOR many shared* exclusion. Realized through a stack of standard-library types that **trade compile-time guarantees for runtime checks** at successively higher safety levels.

## Three layers ([[rust-embedded-book-concurrency-index]])

| Layer | Safety | What it offers | `Sync`? |
|---|---|---|---|
| [[UnsafeCell|`UnsafeCell<T>`]] | `unsafe` | Bottom layer. *"Allows you to obtain multiple mutable references to its value, but only with unsafe code."* | No |
| [[CellRust|`Cell<T>`]] | safe | *"Only permits taking a copy of the current value or replacing it, not taking a reference"* — copy-in / copy-out only. | No |
| [[RefCell|`RefCell<T>`]] | safe | Gives out **references** (`&T` / `&mut T`) with **runtime borrow-counting**. More overhead than `Cell`. | No |

**None of the three are `Sync` by themselves**. Embedded code makes them sharable across `main` ↔ [[Interrupt|interrupt]] by wrapping them in a [[Mutex|critical-section-gated `Mutex`]] (which **does** implement [[Sync]] for any `T: Send`).

## Why interior mutability is central in embedded

[[rust-embedded-book-concurrency-index]] frames the use case sharply: *"Unlike non-embedded Rust, we will not usually have the luxury of creating heap allocations and passing references to that data into a newly-created thread. Instead, our interrupt handlers might be called at any time and must know how to access whatever shared memory we are using. At the lowest level, this means we must have **statically allocated** mutable memory."*

Without interior mutability, that means `static mut COUNTER: u32 = 0;` — which is *always* `unsafe` to read or write. **With** interior mutability, it becomes `static COUNTER: Mutex<Cell<u32>> = …;` — a *safe* `static` whose contents can be mutated through `&` references, gated by a [[CriticalSection|critical section]].

## Connections

- [[UnsafeCell]] — bottom layer; the primitive everything else is built on.
- [[CellRust|`Cell`]] — middle layer; copy-in / copy-out only; cheap.
- [[RefCell]] — top layer; reference-granting; runtime borrow-counting.
- [[Mutex]] — the embedded composition step that recovers [[Sync]].
- [[Sync]] — the property interior-mutability containers usually *lack* by themselves.
- [[Send]] — `Mutex<T>: Sync` for any `T: Send` (interior-mutability containers like `Cell<u32>` and `RefCell<T>` are `Send`).
- [[Interrupt]] — the "other thread" that motivates `Sync`-recovery in embedded.
- [[RustLanguage]] — interior mutability is a Rust-specific design pattern.
