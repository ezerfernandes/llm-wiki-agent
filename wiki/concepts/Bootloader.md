---
title: "Bootloader"
type: concept
tags: [embedded, systems-programming, firmware, boot]
sources: [rust-embedded-book-intro-no-std]
last_updated: 2026-05-16
---

# Bootloader

**Bootloader** — the program that runs *first* on power-up / reset, before any application code. Its job is typically (a) minimal hardware init (clocks, memory controller), (b) optionally selecting between firmware images / upgrading firmware, and (c) jumping to the application entry point. On [[Microcontroller|microcontrollers]], the bootloader often lives in a reserved region of [[FlashMemory|Flash]] (vendor ROM, or a programmable region) and hands control to the application image after init.

## Why `no_std` is required for bootloader code

[[rust-embedded-book-intro-no-std]] is explicit that *"no_std and libcore code can be used for any kind of bootstrapping (stage 0) code like bootloaders, firmware or kernels."* The reverse — `std`-using code *cannot* be a bootloader — follows from the fact that [[RustStandardLibrary|`std`]] presumes an underlying OS *and* ships its own [[RustRuntime|pre-`main` runtime]]: a bootloader has neither of those above it, by definition. Linking against [[RustCoreLibrary|`core`]] only ([[NoStd|`#![no_std]`]]) is the floor that makes [[RustLanguage|Rust]] usable for this layer.

## Connections

- [[NoStd]] — the language switch that makes bootloader code possible in Rust.
- [[RustCoreLibrary]] — the only standard library a bootloader can rely on.
- [[RustStandardLibrary]] — *not* usable for a bootloader (no OS underneath).
- [[BareMetalProgramming]] — the regime bootloaders live in.
- [[FlashMemory]] — where bootloader code typically resides on an MCU.
- [[Microcontroller]] / [[EmbeddedSystems]] — the typical context.
- [[RustRuntime]] — bootloader code runs *before* any runtime exists; conceptually the level *below* a runtime.
