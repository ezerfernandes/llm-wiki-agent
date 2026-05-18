---
title: "Cell (Rust)"
type: concept
tags: [rust, language-feature, concurrency]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# `Cell<T>` (Rust)

Middle layer of [[InteriorMutability|interior mutability]] in [[RustLanguage|Rust]] — a **safe** wrapper over [[UnsafeCell|`UnsafeCell<T>`]] that offers a deliberately restricted API: *"a `Cell` is like an `UnsafeCell` but it provides a safe interface: it only permits taking a copy of the current value or replacing it, not taking a reference, and since it is not [[Sync]], it cannot be shared between threads. These constraints mean it's safe to use, but we couldn't use it directly in a `static` variable as a `static` must be `Sync`"* ([[rust-embedded-book-concurrency-index]]).

**Key restriction**: `get()` returns `T` (by copy, requires `T: Copy`), not `&T`. `set(value)` overwrites. There is **no way to hold a reference into the cell**. This is what makes `Cell` safe with **zero runtime cost** — there are no aliasing rules to check at runtime.

## Embedded pattern: `Mutex<Cell<u32>>`

`Cell<u32>` alone cannot be a `static` (not [[Sync]]). Wrapped in a [[Mutex|`cortex_m::interrupt::Mutex`]], the combination **is** `Sync` (the [[Mutex]] is `Sync` for any `T: Send`, and `Cell<u32>` is `Send`) and is the chapter's recommended pattern for a simple shared counter:

```rust,ignore
use core::cell::Cell;
use cortex_m::interrupt::{self, Mutex};

static COUNTER: Mutex<Cell<u32>> = Mutex::new(Cell::new(0));

interrupt::free(|cs| COUNTER.borrow(cs).set(COUNTER.borrow(cs).get() + 1));
```

## When to prefer [[RefCell]] over `Cell`

`Cell` is **insufficient for non-`Copy`** shared state — peripherals, large structs, anything that owns resources. For those, the chapter promotes [[RefCell|`RefCell<T>`]], which gives out **references** at the cost of runtime borrow-counting.

## Connections

- [[InteriorMutability]] — the umbrella concept; `Cell` is the middle layer.
- [[UnsafeCell]] — what `Cell` wraps internally.
- [[RefCell]] — sibling layer; gives references rather than copies; runtime-checked.
- [[Mutex]] — the standard embedded composition: `Mutex<Cell<T>>` for simple shared state.
- [[Sync]] — `Cell` is not `Sync` by itself; embedding in a `Mutex` recovers `Sync`.
- [[Send]] — `Cell<T>` is `Send` when `T: Send`, which is enough for `Mutex<Cell<T>>: Sync`.
- [[RustLanguage]] — `core::cell::Cell` is in the Rust core library.
