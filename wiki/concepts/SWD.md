---
title: "SWD (Serial Wire Debug)"
type: concept
tags: [embedded, debug-protocol, hardware-interface, arm]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# SWD (Serial Wire Debug)

ARM's two-wire (SWDIO + SWCLK) alternative to [[JTAG]] for debugging [[ARMCortexM|ARM Cortex-M]] and related ARM cores. Same operational capability surface (program / debug / halt / step / inspect) but uses two pins instead of four, freeing GPIO on pin-constrained MCUs.

In *[[TheEmbeddedRustBook]]*'s [[OnChipDebugging|on-chip-debugging]] stack, SWD is the dominant transport between hardware probes ([[STLink|ST-Link]] / [[JLink|J-Link]] / [[MCULink|MCU-Link]] / [[RustyProbe|Rusty-probe]]) and the target MCU ([[rust-embedded-book-intro-tooling]]). The on-board [[STLink|ST-LINK]] on the [[STM32F3DISCOVERY]] reaches the application [[STM32F303VCT6]] over SWD.

## Connections

- [[JTAG]] — the older 4-wire alternative.
- [[OnChipDebugging]] — the umbrella regime SWD transports.
- [[ARMCortexM]] — the ISA SWD was designed for.
- [[STLink]] / [[JLink]] / [[MCULink]] / [[RustyProbe]] / [[TRACE32]] — probes / debuggers that speak SWD.
- [[OpenOCD]] / [[ProbeRs]] — probe-servers that drive SWD.
- [[STM32F3DISCOVERY]] — uses SWD for the on-board probe ↔ application-MCU link.
