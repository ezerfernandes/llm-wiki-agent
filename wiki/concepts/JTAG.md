---
title: "JTAG"
type: concept
tags: [embedded, debug-protocol, hardware-interface]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# JTAG

Standardized hardware debug-and-test wireline interface (IEEE 1149.1) used to program, debug, and boundary-scan [[Microcontroller|microcontrollers]] and other integrated circuits. The classic 4-/5-wire bus (TCK, TMS, TDI, TDO, optional TRST) over which a host-side debugger reads / writes target registers and memory.

In *[[TheEmbeddedRustBook]]*'s [[OnChipDebugging|on-chip-debugging]] stack, JTAG is one of the two hardware transports — alongside [[SWD]] — that probes ([[STLink|ST-Link]] / [[JLink|J-Link]] / [[MCULink|MCU-Link]] / [[RustyProbe|Rusty-probe]]) speak to the target, and that probe-servers ([[OpenOCD]] / [[ProbeRs|Probe-rs]]) drive ([[rust-embedded-book-intro-tooling]]).

## Connections

- [[SWD]] — the 2-wire ARM-Cortex-M alternative.
- [[OnChipDebugging]] — the umbrella regime JTAG transports.
- [[OpenOCD]] / [[ProbeRs]] — probe-servers that drive JTAG.
- [[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]] / [[TRACE32]] — probes / debuggers that speak JTAG.
- [[ARMCortexM]] — supports JTAG (and SWD).
