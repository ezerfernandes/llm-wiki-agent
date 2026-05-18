---
title: "defmt"
type: entity
tags: [rust, embedded, crate, logging, ferrous-systems, knurling]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# defmt

**Deferred-formatting logging framework for embedded Rust**, developed by [[FerrousSystems|Ferrous Systems]] / [[Knurling]] (`https://defmt.ferrous-systems.com/`). Designed for the tight Flash / cycle budgets of [[ARMCortexM|Cortex-M]] firmware: the framework keeps format strings in a separate interned table linked into the firmware's `.defmt` section, transmits **only the format-string index + argument bytes** at runtime, and reconstructs the human-readable log on the **host** side via a decoder that reads the same ELF.

The result: orders-of-magnitude smaller code size and runtime overhead than `hprintln!` ([[CortexMSemihostingCrate|`cortex-m-semihosting`]]) and faster than `log` + `println!` over a UART.

## Transport layers

`defmt` is transport-agnostic — the runtime sink is supplied by a separate crate. The two referenced in *[[TheEmbeddedRustBook]]*'s [[rust-embedded-book-start-qemu|QEMU chapter]]:

- **`defmt-rtt`** — RTT (Real-Time Transfer) over an [[OnChipDebugging|on-chip-debug]] probe. Default in the template's `hello` example. Requires a real debug session.
- **`defmt-semihosting`** — routes through [[ARMSemihosting|ARM semihosting]]. The chapter swaps to this one ("`cargo remove defmt-rtt` / `cargo add defmt-semihosting`") because semihosting "Just Works" under [[QEMU]] without a debug session.

## Decoding on the host

The chapter notes: *"In our case, since we use `defmt`, the host will not be able to decode the output. Instead, we will need a tool by Ferrous Systems named [`qemu-run`]"* — a helper at `github.com/knurling-rs/defmt/tree/main/qemu-run/` that wraps `qemu-system-arm` and consumes the binary's `.defmt` section to print decoded log lines.

The book's footnote: *"`defmt` is a third-party dependency (i.e. non-core) widely used in the Embedded Rust ecosystem."*

## Connections

- [[FerrousSystems]] — vendor.
- [[Knurling]] — the project group within Ferrous Systems that publishes `defmt`.
- [[QemuRun]] — `defmt`-aware QEMU runner.
- [[CortexMSemihostingCrate]] — the pre-`defmt` semihosting-based logger; `defmt` is the modern replacement.
- [[ARMSemihosting]] — one of `defmt`'s transports (via `defmt-semihosting`).
- [[OnChipDebugging]] — the other transport (RTT via `defmt-rtt`).
- [[TheEmbeddedRustBook]] — uses `defmt` in the `hello` example QEMU-debugged in [[rust-embedded-book-start-qemu]].
