---
title: "TRACE32"
type: entity
tags: [debugger, commercial, embedded, tooling, arm, riscv]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# TRACE32

Professional debugging and tracing solution from [[Lauterbach]]. Supports a wide range of processor architectures including [[ARMCortexM|ARM]] and RISC-V; connects to targets via [[JTAG]], [[SWD]], and various trace interfaces. Features include multicore debugging, complex breakpoints, and real-time trace analysis.

Works with standard ELF/DWARF debug information, so Rust binaries built with conventional toolchains debug under TRACE32 without custom support ([[rust-embedded-book-intro-tooling]]).

## Connections

- [[Lauterbach]] — vendor.
- [[ARMCortexM]] — one of the supported core families.
- [[JTAG]] / [[SWD]] — supported transports.
- [[OnChipDebugging]] — the operating regime.
- [[GDB]] / [[ProbeRsVSCodeExtension]] — alternative debugger front-ends in the embedded-Rust ecosystem.
- [[TheEmbeddedRustBook]] — listed in the debugger survey ([[rust-embedded-book-intro-tooling]]).
