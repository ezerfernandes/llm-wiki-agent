---
title: "J-Link"
type: entity
tags: [debug-probe, programmer, embedded, hardware, commercial]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# J-Link

Hardware debug probe family from [[Segger|SEGGER Microcontroller]]. Supports a wide range of CPU cores beyond ARM (including RISC-V); communicates via [[JTAG]], [[SWD]], and fine-pitch JTAG interfaces. Known for high performance and reliability; advanced features include unlimited breakpoints in flash memory; compatible with many development environments ([[rust-embedded-book-intro-tooling]]).

## Connections

- [[Segger]] — vendor.
- [[ARMCortexM]] / RISC-V — supported core families.
- [[JTAG]] / [[SWD]] — supported transports.
- [[GDB]] / [[OpenOCD]] / [[ProbeRs]] — software stacks J-Link integrates with.
- [[STLink]] / [[MCULink]] / [[RustyProbe]] — alternative probes in the same slot.
- [[OnChipDebugging]] — the operating regime.
- [[TheEmbeddedRustBook]] — listed in the probe survey.
