---
title: "Board Crate"
type: concept
tags: [embedded, rust, crate-stack, board-support]
sources: [rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# Board Crate

**Layer 4** (the top) of the embedded-Rust four-layer crate stack. Goes one step further than a [[HALCrate|HAL crate]] by **pre-configuring** various peripherals and GPIO pins for a specific developer kit or board ([[rust-embedded-book-start-registers]]).

Canonical example: `stm32f3-discovery` for the [[STM32F3DISCOVERY]] board — provides ready-made APIs to blink the eight compass-rose LEDs, drive the on-board [[LSM303DLHC|compass]] / [[L3GD20|gyro]], and (via the F3-Discovery's USB stack) talk to a host. Functionality varies a lot between board crates.

## Pedagogical positioning

The chapter explicitly recommends board crates as the **best starting point for new embedded-Rust developers**: they abstract HW details that can overwhelm beginners and make standard tasks (blink an LED) trivial. *[[TheEmbeddedRustBook]] itself does not use board crates* — it stays hardware-agnostic — but it points readers at the *Discovery* book and the `stm32f3-discovery` crate for a board-crate-first introduction.

## Stack position

- **Below**: [[HALCrate|HAL crate]] (board crates depend on a HAL crate for the chip's peripheral implementations).
- Above: application code.

## Connections

- [[HALCrate]] — sits below; the board crate composes HAL constructors with board-specific pin / clock choices baked in.
- [[STM32F3DISCOVERY]] — the canonical board the book references.
- [[PeripheralAccessCrate]] — two layers below.
- [[MicroArchitectureCrate]] — three layers below.
