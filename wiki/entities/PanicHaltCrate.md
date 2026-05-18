---
title: "panic-halt"
type: entity
tags: [rust, embedded, crate, panic-handler, no-std]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# panic-halt

**Minimal Rust crate providing a `#[panic_handler]` that halts the CPU in an infinite loop** — one of the simplest implementations of the panic ABI mandated by [[NoStd|`#![no_std]`]] crates. Used in *[[TheEmbeddedRustBook]]*'s canonical first code example ([[rust-embedded-book-start-qemu]]):

```rust
use panic_halt as _;
```

The `as _` import pattern is idiomatic: the crate is linked purely for its side-effect of registering the panic handler — no name binding is needed in user code. Without *some* `#[panic_handler]` provider, a `no_std` binary fails to link.

`panic-halt`'s behavior is intentionally trivial: on panic, enter `loop {}`, freezing the MCU. Production embedded programs typically choose richer alternatives (`panic-rtt-target`, `panic-semihosting`, `panic-probe` with `defmt`, `panic-persist` for post-mortem capture) but `panic-halt` is the book's pedagogical default — *"This crate provides a `panic_handler` that defines the panicking behavior of the program. We will cover this in more detail in the Panicking chapter of the book."*

## Connections

- [[NoStd]] — the regime that demands an explicit panic handler.
- [[CortexMRTCrate]] — paired with `panic-halt` in every chapter-11 example.
- [[CortexMQuickstartTemplate]] — the template wires `panic-halt` into `Cargo.toml` by default.
- [[TheEmbeddedRustBook]] — `panic-halt` is the book's default panic provider before [[rust-embedded-book-start-qemu|Chapter 11]]'s deferred *Panicking* chapter.
