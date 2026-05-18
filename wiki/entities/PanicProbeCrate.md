---
title: "panic-probe"
type: entity
tags: [rust, embedded, crate, panic-handler, defmt, probe-rs, knurling, no-std]
sources: [rust-embedded-book-start-panicking]
last_updated: 2026-05-16
---

# panic-probe

**[[Knurling]] / [[FerrousSystems]] panic-handler crate** that prints the panic message over [[Defmt|`defmt`]] (via RTT) and then triggers a hard fault to break the debugger — the modern Rust-embedded panic handler paired with the [[ProbeRs|`probe-rs`]] / `cargo embed` / `cargo flash` toolchain.

```rust
use panic_probe as _;
```

## Why it exists

The four panic-handler crates explicitly surveyed by [[rust-embedded-book-start-panicking|chapter 15 of *The Embedded Rust Book*]] ([[PanicAbortCrate|`panic-abort`]] / [[PanicHaltCrate|`panic-halt`]] / [[PanicItmCrate|`panic-itm`]] / [[PanicSemihostingCrate|`panic-semihosting`]]) all predate the `defmt` / `probe-rs` ecosystem. The chapter points readers at *"the [`panic-handler`] keyword on crates.io"* for the broader catalog — `panic-probe` is the dominant entry in that catalog for modern embedded-Rust projects scaffolded from [[Knurling]]'s `app-template`.

`panic-probe` differs from its book-listed siblings in three ways:

1. **`defmt`-native formatting.** The panic message is encoded with the deferred-formatting protocol [[Defmt]] uses for all other logging, so panic output lands in the same `defmt-rtt` stream as ordinary `defmt::info!` / `defmt::error!` calls — no separate decoding path.
2. **RTT transport, no SWO pin required.** Unlike [[PanicItmCrate|`panic-itm`]], `panic-probe` does not need a working SWO trace line; RTT works on any Cortex-M with a debug probe.
3. **Hard-fault trap, not infinite loop.** After logging, `panic-probe` triggers a hardware breakpoint so an attached debugger sees a clean fault context — strictly more useful than [[PanicHaltCrate|`panic-halt`]]'s `loop {}` for post-mortem inspection.

## Connections

- [[PanicHandlerAttribute]] — the attribute the crate implements.
- [[PanicInfo]] — the struct the crate hands to `defmt` for encoding.
- [[Defmt]] — the formatting / wire-protocol layer `panic-probe` sits on top of.
- [[Knurling]] / [[FerrousSystems]] — the project that maintains both `defmt` and `panic-probe`.
- [[ProbeRs]] — the host-side decoder that consumes RTT and renders the panic message.
- [[PanicHaltCrate]] / [[PanicAbortCrate]] / [[PanicItmCrate]] / [[PanicSemihostingCrate]] — the book-listed siblings; `panic-probe` is the modern alternative pointed at by the chapter's "see also the `panic-handler` crates.io keyword" note.
- [[NoStd]] — the regime that requires an explicit panic handler.
- [[TheEmbeddedRustBook]] — mentioned obliquely in [[rust-embedded-book-start-panicking]] via the crates.io keyword pointer.
