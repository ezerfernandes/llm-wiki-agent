---
title: "QEMU"
type: entity
tags: [emulator, virtualization, arm, embedded, tooling]
sources: [rust-embedded-book-intro-tooling]
last_updated: 2026-05-16
---

# QEMU

Open-source machine emulator and virtualizer. *[[TheEmbeddedRustBook]]* uses the **`qemu-system-arm`** variant — full-system emulation of ARM machines, distinct from QEMU's user-mode emulation — to run embedded Rust programs *on the host* without target hardware. Tested version listed in the book: 3.0.0 ([[rust-embedded-book-intro-tooling]]).

This is the no-hardware escape hatch the book offers: *"Thanks to this you can follow some parts of this book even if you don't have any hardware with you!"* — readers without an [[STM32F3DISCOVERY|F3 board]] can still execute many examples.

## Connections

- [[ARMCortexM]] — the ISA family QEMU emulates for embedded examples.
- [[STM32F3DISCOVERY]] — physical alternative QEMU substitutes for.
- [[TheEmbeddedRustBook]] — uses `qemu-system-arm` as the host-side runner ([[rust-embedded-book-intro-tooling]]).
- [[BareMetalProgramming]] — what's being emulated.
