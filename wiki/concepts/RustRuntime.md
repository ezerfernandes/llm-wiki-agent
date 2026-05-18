---
title: "Rust Runtime (Pre-`main` Initialization)"
type: concept
tags: [rust, runtime, embedded, no-std]
sources: [rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Rust Runtime (Pre-`main` Initialization)

The **runtime** is the code that executes *before* a Rust program's `main()` function is invoked, plus the support machinery alongside it. In a [[HostedEnvironment|hosted environment]], the runtime ships **inside [[RustStandardLibrary|`libstd`]]** — meaning it is automatically present in any normal Rust binary. Under [[NoStd|`#![no_std]`]] (link only [[RustCoreLibrary|`core`]]) **the runtime is absent** ([[rust-embedded-book-intro-no-std]]).

## What the `libstd` runtime does

The chapter's enumeration of pre-`main` responsibilities:

- **Stack-overflow protection** — install guard pages / probes so a runaway recursion is caught instead of corrupting adjacent memory silently.
- **Command-line-argument processing** — parse `argc`/`argv` (or the OS-equivalent) into the `std::env::args()` iterator before `main` runs.
- **Spawning the main thread** — set up TLS, the panic infrastructure, and the runtime's notion of "the main thread" before `main()` enters.

Together this is the *"runs init code before main"* row of the `no_std` / `std` feature table ([[rust-embedded-book-intro-no-std]]).

## Why losing it on `no_std` matters

This is the non-obvious cost of `#![no_std]` — beyond the missing API surface. Embedded Rust crates that mimic the runtime's behavior (e.g. `cortex-m-rt` for the Cortex-M reset handler, `.bss` zeroing, `.data` copy from Flash to SRAM, optional FPU init, then calling `main`) are doing exactly this work, just at the bare-metal layer and under explicit programmer control rather than as a `libstd`-internal black box.

## Connections

- [[NoStd]] — the attribute whose effect this concept describes.
- [[RustStandardLibrary]] — the library that ships this runtime.
- [[RustCoreLibrary]] — the library that does **not** ship this runtime.
- [[BareMetalProgramming]] — the regime where this layer must be supplied (typically by a runtime crate like `cortex-m-rt`) rather than inherited from the language.
- [[Bootloader]] — pre-`main` init at the firmware level is conceptually adjacent: it is the code that runs before *any* application code.
- [[ARMCortexM]] / [[STM32F303VCT6]] — the architecture/MCU class where the absence of a `libstd` runtime is most visible; reset-handler-driven init replaces it.
- [[TheEmbeddedRustBook]] — every code chapter from chapter 3 onward operates under this missing-runtime constraint.
