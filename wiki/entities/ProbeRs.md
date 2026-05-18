---
title: "Probe-rs"
type: entity
tags: [rust, debug-server, embedded, tooling, open-source]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# Probe-rs

Modern, Rust-native software for talking to debug probes in embedded systems. Pitched in *[[TheEmbeddedRustBook]]* as the Rust ecosystem's answer to [[OpenOCD]]: simpler configuration, supports a wide range of probes and targets, integrates directly with Rust tooling, and ships its own Visual Studio Code extension (the [[ProbeRsVSCodeExtension]]) — *"reducing the configuration burden often found in other debugging solutions"* ([[rust-embedded-book-intro-tooling]]).

Operationally fills the same slot as [[OpenOCD]] in the debug stack: server-side translator between a host-side debugger (GDB or its own VS Code extension) and a hardware probe ([[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]]) over [[JTAG]] / [[SWD]].

## Connections

- [[RustLanguage]] — written in Rust; first-class in the embedded-Rust ecosystem.
- [[OpenOCD]] — the older alternative Probe-rs is positioned against.
- [[ProbeRsVSCodeExtension]] — VS Code debugger UI on top of Probe-rs.
- [[RustyProbe]] — open-source USB probe designed specifically for Probe-rs.
- [[STLink]] / [[JLink]] / [[MCULink]] — other probes Probe-rs supports.
- [[OnChipDebugging]] — the operating regime.
- [[TheEmbeddedRustBook]] — listed in the toolchain inventory ([[rust-embedded-book-intro-tooling]]).
