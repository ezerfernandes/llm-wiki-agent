---
title: "BSP (Board Support Crate)"
type: concept
tags: [embedded, rust, crate-stack, board-support, acronym]
sources: [rust-embedded-book-appendix-glossary, rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# BSP — Board Support Crate

**BSP** = *Board Support Crate* (or, in the wider embedded world, *Board Support Package*). The acronym the glossary appendix of *[[TheEmbeddedRustBook]]* registers as a first-class entry ([[rust-embedded-book-appendix-glossary]]).

A BSP provides a **high-level interface configured for a specific board** and usually depends on a [[HALCrate|HAL]] crate. It is the **fourth and topmost layer** of the embedded-Rust crate stack — see [[BoardCrate]] for the full treatment (compass-rose LEDs on the [[STM32F3DISCOVERY]], the `stm32f3-discovery` canonical example, why the book recommends BSPs for newcomers, etc.).

## BSP vs Board Crate

In Rust embedded usage the two terms are synonymous: the *crate* (Rust packaging unit) **is** the *package* (vendor's collection of board-specific configurations + helper drivers). The book uses **"Board Crate"** in prose ([[rust-embedded-book-start-registers]]) and **"BSP" / "Board Support Crate"** in the glossary appendix — same artifact, different name register.

## Crate-stack position

```
Application
  ↑
[[BoardCrate|Board Crate / BSP]]   ← this page
  ↑
[[HALCrate|HAL crate]]
  ↑
[[PeripheralAccessCrate|PAC]]
  ↑
[[MicroArchitectureCrate|Micro-architecture crate]] (e.g. cortex-m)
```

## Connections

- [[BoardCrate]] — the canonical concept page (this acronym redirects there for the long treatment).
- [[HALCrate]] — the layer immediately below; a BSP composes HAL constructors with board-specific pin / clock / peripheral choices baked in.
- [[PeripheralAccessCrate]] — two layers below.
- [[STM32F3DISCOVERY]] — the board the book standardizes on; `stm32f3-discovery` is the canonical BSP example.
- [[rust-embedded-book-appendix-glossary]] — the source for this acronym entry.
- [[rust-embedded-book-start-registers]] — the source for the crate-stack chapter that defines the BSP layer.
- [[TheEmbeddedRustBook]] — parent book.
