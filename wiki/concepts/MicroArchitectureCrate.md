---
title: "Micro-architecture Crate"
type: concept
tags: [embedded, rust, crate-stack, cortex-m]
sources: [rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# Micro-architecture Crate

**Layer 1** of the embedded-Rust four-layer crate stack. A crate that wraps routines and peripherals **common to every [[Microcontroller|microcontroller]] using a particular processor core** — not to a specific chip part-number. Canonical example: the [[CortexMCrate|`cortex-m`]] crate, which exposes `enable_interrupts()` / `disable_interrupts()` and the [[SysTick]] peripheral for every [[ARMCortexM|Cortex-M]] MCU regardless of vendor ([[rust-embedded-book-start-registers]]).

Sits **below** the [[PeripheralAccessCrate|PAC]] in the layered crate stack ([[MicroArchitectureCrate|micro-arch]] → [[PeripheralAccessCrate|PAC]] → [[HALCrate|HAL]] → [[BoardCrate|board]]). Distinguished from the PAC by core-vs-part scope: a micro-arch crate is reusable across every Cortex-M chip; a PAC is specific to one vendor's part number.

## Connections

- [[CortexMCrate]] — the canonical example; the entry layer of the chapter's first code sample ([[rust-embedded-book-start-registers]]).
- [[PeripheralAccessCrate]] — sits above; chip-specific.
- [[HALCrate]] — sits above the PAC; portable.
- [[BoardCrate]] — sits at the top; dev-board-specific.
- [[ARMCortexM]] — the processor-core family the canonical micro-arch crate targets.
- [[SysTick]] — the core-standardized peripheral exposed by every Cortex-M micro-arch crate.
