---
title: "Memory-Mapped I/O"
type: concept
tags: [embedded, hardware, mmio]
sources: [rust-embedded-book-intro-index, rust-embedded-book-peripherals-index, rust-embedded-book-peripherals-a-first-attempt]
last_updated: 2026-05-16
---

# Memory-Mapped I/O

Hardware-interface convention in which peripheral registers (GPIO, timers, ADCs, UART/SPI/I2C controllers, etc.) are exposed at fixed addresses in the CPU's address space, so peripheral access is just a load or store to a specific memory address. The dominant peripheral-access model on [[ARMCortexM|ARM Cortex-M]] [[Microcontroller|microcontrollers]] and most modern embedded targets. Listed by [[TheEmbeddedRustBook]] as a prerequisite concept for the embedded-experienced reader ([[rust-embedded-book-intro-index]]); the *Peripherals* chapter opener ([[rust-embedded-book-peripherals-index]]) formalizes it as the **language-agnostic** universal hardware-interface contract — "no matter what language is used, whether that language is Assembly, C, or Rust."

In Rust this is typically wrapped behind type-state peripheral access crates (`svd2rust`-generated PAC + HAL layers) so that reads / writes to MMIO are `volatile` and individual register bits are exposed as typed accessors — an idiomatic-Rust use of the type system to enforce hardware contracts at compile time.

## Address-space placement on Cortex-M

The [[rust-embedded-book-peripherals-index|Peripherals chapter opener]] makes the address-space mechanics concrete: 32-bit MCUs have a linear `0x0000_0000`–`0xFFFF_FFFF` space and no MMU, so peripheral register blocks are slotted between the [[FlashMemory|Flash ROM]] region (near `0x0000_0000`) and the [[SRAM]] region (near `0x2000_0000`). An address like `0x2000_1234` decodes by upper-bits chip-select (`0x2000` → RAM block active) and lower-bits offset (`0x1234` → byte within RAM); the same decode logic routes addresses in the peripheral range to the appropriate peripheral block.

## Connections

- [[Peripheral]] — the noun whose interface MMIO *is*.
- [[Microcontroller]] — MCUs expose peripherals via MMIO.
- [[BareMetalProgramming]] — firmware drives peripherals through MMIO directly, with no OS device driver layer.
- [[EmbeddedSystems]] — the canonical I/O model in the embedded domain.
- [[VolatileMemoryAccess]] — the required access semantics for MMIO (loads / stores must not be elided by the compiler); see [[rust-embedded-book-peripherals-a-first-attempt]] for the Rust expression via `core::ptr::read_volatile` / `write_volatile` and the [[VolatileRegisterCrate|`volatile_register`]] crate.
- [[RawPointer]] — Rust's `*mut T` / `*const T` is the access primitive that volatile reads/writes operate on; the canonical entry point is `addr as *mut RegisterBlock`.
- [[ReprC]] — required on every register-block struct so field order matches the hardware datasheet.
