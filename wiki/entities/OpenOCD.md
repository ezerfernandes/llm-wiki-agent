---
title: "OpenOCD"
type: entity
tags: [debug-server, on-chip-debugging, embedded, tooling, open-source]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# OpenOCD (Open On-Chip Debugger)

Open-source software bridging a host PC's debugger ([[GDB]]) to a target [[Microcontroller|MCU]] through a [[JTAG]] / [[SWD]] hardware probe. Provides a [[GDB|GDB]]-compatible *remote* debugging server, plus flashing, halting, and register-access primitives. The de-facto open-source standard for embedded [[OnChipDebugging|on-chip debugging]] before [[ProbeRs|Probe-rs]] arrived.

In *[[TheEmbeddedRustBook]]* the listed minimum is ≥ 0.8 (tested 0.9.0 and 0.10.0) ([[rust-embedded-book-intro-tooling]]). The book's framing: widely supported, extensive docs, large community — but can require complex configuration for custom embedded setups. The Rust-native alternative [[ProbeRs|Probe-rs]] is offered as a simpler-config option.

## Connections

- [[GDB]] — the debugger front-end OpenOCD typically bridges to.
- [[ProbeRs]] — Rust-native alternative server.
- [[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]] — hardware probes OpenOCD drives.
- [[JTAG]] / [[SWD]] — transport protocols.
- [[OnChipDebugging]] — the umbrella concept.
- [[TheEmbeddedRustBook]] — listed in the toolchain inventory ([[rust-embedded-book-intro-tooling]]).
