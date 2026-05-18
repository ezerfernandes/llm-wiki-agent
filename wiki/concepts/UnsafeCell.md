---
title: "UnsafeCell"
type: concept
tags: [rust, language-feature, unsafe, concurrency]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# `UnsafeCell<T>`

The **bottom layer** of [[InteriorMutability|interior mutability]] in [[RustLanguage|Rust]]: *"`UnsafeCell` is the bottom layer of interior mutability in Rust: it allows you to obtain multiple mutable references to its value, but only with unsafe code"* ([[rust-embedded-book-concurrency-index]]).

Every safe interior-mutability container ([[CellRust|`Cell`]], [[RefCell]], `RwLock`, `Mutex`, atomics) is built on top of `UnsafeCell`. The compiler treats `&UnsafeCell<T>` specially — it's the **only** way a `&T` can legally be used to mutate `T` without invoking undefined behavior.

## Why it's not `Sync`

A type that contains `UnsafeCell<T>` is **not** [[Sync]] by default (auto-traits are negative on `UnsafeCell`). This is the load-bearing rule that forces embedded code to wrap an `UnsafeCell` in something the programmer guarantees is `Sync` (typically via `unsafe impl Sync`) before placing it in a `static`.

The chapter's `CSCounter` is a worked example:

```rust,ignore
use core::cell::UnsafeCell;

struct CSCounter(UnsafeCell<u32>);

impl CSCounter {
    pub fn reset(&self, _cs: &interrupt::CriticalSection) {
        unsafe { *self.0.get() = 0 };
    }
    pub fn increment(&self, _cs: &interrupt::CriticalSection) {
        unsafe { *self.0.get() += 1 };
    }
}

unsafe impl Sync for CSCounter {} // required to put it in a static
```

The `unsafe impl Sync` is **only sound on single-core**, since the [[CriticalSection]] token only excludes interrupts on the current core.

## Connections

- [[InteriorMutability]] — `UnsafeCell` is the bottom layer.
- [[CellRust|`Cell`]] / [[RefCell]] — the safe wrappers built on top.
- [[Sync]] — `UnsafeCell` is not `Sync`; everything else flows from that.
- [[Mutex]] — `cortex_m::interrupt::Mutex` internally wraps `UnsafeCell` and provides `Sync` via critical-section gating.
- [[CriticalSection]] — the typical evidence that an `unsafe impl Sync` over an `UnsafeCell` wrapper is sound.
- [[RustLanguage]] — `core::cell::UnsafeCell` is in the Rust core library.
