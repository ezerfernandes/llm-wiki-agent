---
title: "Flash Memory"
type: concept
tags: [embedded, hardware, memory, nonvolatile]
sources: [rust-embedded-book-intro-hardware, rust-embedded-book-unsorted-speed-vs-size, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Flash Memory

Non-volatile, electrically-erasable, block-rewritable solid-state memory. On a [[Microcontroller|microcontroller]] the on-chip Flash typically stores the **firmware image** (code + read-only data + vector table) that survives power cycles, in contrast to volatile [[SRAM]] which holds the runtime stack / heap / mutable data and loses its contents on reset.

The [[STM32F303VCT6]] on the [[STM32F3DISCOVERY]] ships with **256 KiB** of on-chip Flash and 48 KiB of SRAM ([[rust-embedded-book-intro-hardware]]) — this 256 KiB is the hard ceiling on every code example in [[TheEmbeddedRustBook]] and is the budget that linker scripts allocate the text + rodata sections into. Compile-time-aggressive abstractions (zero-cost generics, monomorphization, `#[inline]`) push Rust's typical firmware size against this ceiling much sooner than equivalent C — hence the importance of `cargo size`, `--release`, and `opt-level = "z"` in the embedded-Rust toolchain. The canonical reference for the `opt-level` dial is [[OptLevel]] ([[rust-embedded-book-unsorted-speed-vs-size]]), which also operationalizes [[Cargo]]'s `profile-overrides` recipe — `[profile.dev.package."*"] opt-level = "z"` for size-optimized dependencies + debugger-friendly top crate — and notes that *"debuginfo is zero cost in the sense that it won't occupy space in Flash / ROM"* so `[profile.release] debug = true` is a free win on bare metal.

## At the smaller end: the 8-bit AVR

[[embedded-controllers-fiore]] ch. 16 covers the same memory hierarchy on a much smaller MCU — the [[ATmega328P]] has **32 KiB Flash**, ~1/8 the Cortex-M4 figure above. Under [[HarvardArchitecture|Harvard architecture]] the program-memory bus is physically separate from the data-memory bus, which is why constants placed in Flash with the `PROGMEM` attribute need special access functions (`pgm_read_word`, `pgm_read_byte`) rather than ordinary pointer dereferences. The Arduino runtime uses this for the per-port lookup tables `port_to_mode_PGM` / `port_to_output_PGM` that `digitalPinToPort()` consults — the table lives in Flash so it doesn't burn precious SRAM.

## Connections

- [[Microcontroller]] — on-chip Flash holds the firmware image on every MCU.
- [[STM32F303VCT6]] — 256 KiB Flash on the [[STM32F3DISCOVERY]]'s application MCU.
- [[SRAM]] — sibling volatile memory tier; together they define the firmware's static + runtime budget.
- [[BareMetalProgramming]] — without an OS, the firmware image in Flash *is* the entire executable.
- [[OptLevel]] — the `rustc -C opt-level=<N>` dial whose `"s"` / `"z"` values are the canonical tools for fitting Rust firmware into the Flash budget.
- [[rust-embedded-book-unsorted-speed-vs-size]] — the operational chapter on `opt-level`, `profile-overrides`, and `inline-threshold` tuning.
