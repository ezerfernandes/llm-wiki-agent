---
title: "SVD File (CMSIS-SVD)"
type: concept
tags: [embedded, arm, cmsis, register-description, xml]
sources: [rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# SVD File (CMSIS-SVD)

**System View Description** — an ARM CMSIS-SVD XML format published by chip vendors that fully describes a specific microcontroller's [[MemoryMappedIO|memory-mapped]] register map: every peripheral block, every register, every sub-field, with addresses, access modes, reset values, and (when documented) enumerated valid values. The machine-readable form of the chip's *Technical Reference Manual* register section.

The **canonical input to [[Svd2Rust|`svd2rust`]]**, which consumes the SVD and emits a fully typed Rust [[PeripheralAccessCrate|PAC]] crate with `R` / `W` accessor structs per register and typed sub-field accessors per bit-field ([[rust-embedded-book-start-registers]]).

## Why the closure API needs SVD

The `read()` / `write()` / `modify()` closure idiom is entirely shape-derived from the SVD ([[rust-embedded-book-start-registers]]):

- Each register's sub-field accessor name and bit width come from the SVD.
- Each register's `R` and `W` struct types come from the SVD.
- The default values restored by `write(|w| …)` for unset fields are read from the SVD's reset-value declarations.
- **Where the SVD declares a 32-bit field but does not enumerate the valid values**, the generated `bits()` setter is marked `unsafe` — encoding the SVD's incompleteness directly in Rust's safety system.

## Connections

- [[Svd2Rust]] — the generator that consumes SVD.
- [[PeripheralAccessCrate]] — the output.
- [[MemoryMappedIO]] — the underlying hardware model the SVD describes.
- [[ARMCortexM]] — the SVD format originated in ARM's CMSIS effort for Cortex-M MCUs.
