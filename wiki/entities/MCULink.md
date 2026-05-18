---
title: "MCU-Link"
type: entity
tags: [debug-probe, programmer, embedded, hardware]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# MCU-Link

Debug-and-programming probe from [[NXP|NXP Semiconductors]]. Supports a variety of [[ARMCortexM|ARM Cortex]] microcontrollers; interfaces with development tools like MCUXpresso IDE. Notable for being versatile and affordable — accessible to hobbyists, educators, and professional developers alike ([[rust-embedded-book-intro-tooling]]).

## Connections

- [[NXP]] — vendor.
- [[ARMCortexM]] — supported core family.
- [[JTAG]] / [[SWD]] — supported transports.
- [[OpenOCD]] / [[ProbeRs]] — software stacks MCU-Link integrates with.
- [[STLink]] / [[JLink]] / [[RustyProbe]] — alternative probes in the same slot.
- [[OnChipDebugging]] — the operating regime.
- [[TheEmbeddedRustBook]] — listed in the probe survey.
