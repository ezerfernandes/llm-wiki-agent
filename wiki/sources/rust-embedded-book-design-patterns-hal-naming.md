---
title: "The Embedded Rust Book — HAL Naming"
type: source
tags: [rust, embedded, book-chapter, hal, naming-conventions]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/design-patterns/hal/naming.md
sources: [rust-embedded-book-design-patterns-hal-naming]
---

## Summary

File 33/44 of *[[TheEmbeddedRustBook]]* — the first leaf-section of the *HAL Design Patterns* sub-chapter ([[rust-embedded-book-design-patterns-hal-index]]) and the **Naming** group of the [[rust-embedded-book-design-patterns-hal-checklist|HAL Checklist]]. Single named pattern: **`C-CRATE-NAME`** — *the crate is named appropriately*. Three rules: (1) HAL crates should be named after **the chip or family of chips** they support; (2) the name **must end with `-hal`** to distinguish from [[PeripheralAccessCrate|register access (PAC)]] crates; (3) **dashes, not underscores** (`stm32f4xx-hal`, not `stm32f4xx_hal`). Cite-able in code review as *"this violates C-CRATE-NAME."*

## Key Claims

- **Naming reflects scope**: HAL crates are named after the chip or family of chips they aim to support (e.g. `stm32f4xx-hal` covers the STM32F4 family, not a single chip).
- **`-hal` suffix is mandatory**: distinguishes [[HALCrate|HAL crates]] from the underlying [[PeripheralAccessCrate|PAC crates]] (e.g. `stm32f4` is the PAC, `stm32f4xx-hal` is the HAL).
- **Dashes, not underscores** in the crate name (Cargo allows both; this pattern picks one).

## Key Quotes

> "HAL crates should be named after the chip or family of chips they aim to support. Their name should end with `-hal` to distinguish them from register access crates. The name should not contain underscores (use dashes instead)." — the entire normative content of `C-CRATE-NAME`.

## Connections

- [[TheEmbeddedRustBook]] — file 33/44.
- [[rust-embedded-book-design-patterns-hal-index]] — parent sub-chapter (file 31/44).
- [[rust-embedded-book-design-patterns-hal-checklist]] — top-level checklist that lists `C-CRATE-NAME` under the **Naming** group (file 32/44).
- [[HALCrate]] — the crate kind this pattern names.
- [[PeripheralAccessCrate]] — the layer the `-hal` suffix distinguishes against.

## Contradictions

- None. Consistent with the [[HALCrate|HAL]] / [[PeripheralAccessCrate|PAC]] stack established in [[rust-embedded-book-start-registers]] and the checklist in [[rust-embedded-book-design-patterns-hal-checklist]].
