---
title: "On-Chip Debugging"
type: concept
tags: [embedded, debugging, toolchain]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# On-Chip Debugging

Live inspection and control of a running [[Microcontroller|microcontroller]] from a host PC via a dedicated hardware *debug probe*, using a wireline transport protocol like [[JTAG]] or [[SWD]]. *[[TheEmbeddedRustBook]]* operationalizes the embedded-Rust on-chip-debugging stack in three software layers + hardware ([[rust-embedded-book-intro-tooling]]):

1. **Debug-probe driver / server** — [[ProbeRs|Probe-rs]] or [[OpenOCD]] — translates between USB and the probe's protocol, exposes a GDB Remote Serial Protocol (or similar) endpoint to the higher-level debugger.
2. **Debugger** — [[GDB]] / [[ProbeRsVSCodeExtension]] / [[TRACE32]] — the user-facing tool driving breakpoints, watchpoints, stepping, register reads, memory inspection.
3. **Hardware probe** — [[STLink|ST-Link]] / [[JLink|J-Link]] / [[MCULink|MCU-Link]] / [[RustyProbe|Rusty-probe]] — bridges USB ↔ [[JTAG]] / [[SWD]] on the target.

The book's canonical capability list for an embedded debugger:

- Interact with the [[MemoryMappedIO|memory-mapped registers]].
- Set breakpoints / watchpoints.
- Read and write memory.
- Detect when the MCU has been halted for a debug event.
- Continue MCU execution after a debug event has been encountered.
- Erase and write to the microcontroller's [[FlashMemory|FLASH]].

This is the operational contract every layer of the on-chip-debugging stack collaborates to provide.

## Connections

- [[GDB]] / [[ProbeRs]] / [[OpenOCD]] / [[ProbeRsVSCodeExtension]] / [[TRACE32]] — software layers.
- [[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]] — hardware probes.
- [[JTAG]] / [[SWD]] — wireline protocols.
- [[FlashMemory]] / [[SRAM]] / [[MemoryMappedIO]] — what the debugger inspects on the target.
- [[STM32F3DISCOVERY]] — reference target with on-board [[STLink]].
- [[TheEmbeddedRustBook]] — chapter 4 names the layered stack ([[rust-embedded-book-intro-tooling]]).
