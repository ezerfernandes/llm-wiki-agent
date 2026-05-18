---
title: "The Embedded Rust Book — Appendix A: Glossary"
type: source
tags: [rust, embedded, book-chapter, glossary]
date: 2026-05-16
source_file: raw/book/src/appendix/glossary.md
last_updated: 2026-05-16
---

## Summary

File **44/44** of *[[TheEmbeddedRustBook]]* — **Appendix A: Glossary** and the **closing file of the corpus**. Compact one-paragraph-per-term reference defining the embedded-vendor abbreviations the preceding 43 chapters use freely: **[[BSP]]** (Board Support Crate), **[[FPU]]** (Floating-Point Unit), **[[HALCrate|HAL]]** (Hardware Abstraction Layer), **[[I2C]]** (Inter-IC), **[[PeripheralAccessCrate|PAC]]** (Peripheral Access Crate), **[[SPI]]** (Serial Peripheral Interface), **[[SVDFile|SVD]]** (System View Description XML), **[[UART]]** (Universal Asynchronous Receiver-Transmitter), and **[[USART]]** (Universal Synchronous/Asynchronous Receiver-Transmitter). Each entry is two-to-four sentences plus pointers (`registers.md`, [`svd2rust`](https://github.com/rust-embedded/svd2rust/), Wikipedia, ARM CMSIS docs, a YouTube overview). Pure cross-walk — no new concepts, no code, no claims beyond definitions.

## Key Claims

- **[[BSP]]** (Board Support Crate) provides a high-level interface configured for a specific board; usually depends on a [[HALCrate|HAL]] crate. Cross-referenced to `start/registers.md` ([[rust-embedded-book-start-registers]]) for the deeper crate-stack treatment.
- **[[FPU]]** (Floating-Point Unit) is "a 'math processor' running only operations on floating-point numbers" — the one-sentence definition is the entire entry. Implicitly references the `thumbv7em-none-eabihf` target's `hf` suffix from [[rust-embedded-book-start-hardware]].
- **[[HALCrate|HAL]]** (Hardware Abstraction Layer) provides developer-friendly access to MCU peripherals, usually implemented on top of a [[PeripheralAccessCrate|PAC]]; may implement traits from the [[EmbeddedHalCrate|`embedded-hal`]] crate. Cross-referenced to `start/registers.md`.
- **[[I2C]]** (sometimes `I²C` or Inter-IC) is "a protocol meant for hardware communication within a single integrated circuit." Pointer to Wikipedia.
- **[[PeripheralAccessCrate|PAC]]** (Peripheral Access Crate) provides access to a microcontroller's peripherals; **"one of the lower level crates"**, usually generated from an [[SVDFile|SVD]] via [[Svd2Rust|`svd2rust`]]. A [[HALCrate|HAL]] usually depends on a PAC.
- **[[SPI]]** (Serial Peripheral Interface). Pointer to Wikipedia — no further text.
- **[[SVDFile|SVD]]** (System View Description) is "an XML file format used to describe the programmers view of a microcontroller device." Pointer to ARM CMSIS documentation.
- **[[UART]]** (Universal Asynchronous Receiver-Transmitter). Pointer to Wikipedia — single-line definition.
- **[[USART]]** (Universal Synchronous and Asynchronous Receiver-Transmitter). Pointer to Wikipedia — single-line definition.

## Key Quotes

> "A Board Support Crate provides a high level interface configured for a specific board. It usually depends on a HAL crate." — opening sentence of the BSP entry; the canonical one-line definition the rest of the book assumes.

> "A Peripheral Access Crate provides access to a microcontroller's peripherals. It is one of the lower level crates and is usually generated directly from the provided SVD, often using svd2rust. The Hardware Abstraction Layer would usually depend on this crate." — the entry that ties the PAC / HAL / SVD / svd2rust four-way relationship into one sentence.

## Connections

- [[TheEmbeddedRustBook]] — closes the book; sources frontmatter updated **in-place** to add this 44th and final file.
- [[BSP]] — **new concept page**. The book uses "BSP" as a short-form abbreviation and "Board Support Crate" / "Board Crate" as the long form. The wiki already has [[BoardCrate]] from [[rust-embedded-book-start-registers]]; the new [[BSP]] page is the **acronym disambiguator** that redirects to [[BoardCrate]] and surfaces the glossary's explicit BSP-as-acronym usage.
- [[FPU]] — **new concept page**. The book defines this in one sentence here, but the term recurs in [[rust-embedded-book-start-hardware]] (the `thumbv7em-none-eabihf` target triple's `hf` suffix on the [[STM32F303VCT6|Cortex-M4F]]) and [[ARMCortexM]] (the M4F has an FPU, the M0/M0+/M3 do not).
- [[UART]] — **new concept page**. The wiki already has [[USART]] which defines UART as "the asynchronous-only subset of USART"; the new [[UART]] page is the explicit standalone entry the glossary requires, cross-linking to [[USART]] for the synchronous-capable superset.
- [[HALCrate]] — reused; glossary definition matches the existing page exactly.
- [[PeripheralAccessCrate]] — reused; glossary's "lower level crates" + "generated from SVD via svd2rust" + "HAL depends on this" matches the existing page's crate-stack framing.
- [[I2C]] — reused; existing page covers the Inter-IC framing.
- [[SPI]] — reused; existing page covers the synchronous-serial framing.
- [[SVDFile]] — reused; existing page covers the XML-description framing.
- [[USART]] — reused; existing page already incorporates "asynchronous-only subset = UART" framing.
- [[BoardCrate]] — reused; the BSP abbreviation's long-form referent.
- [[rust-embedded-book-start-registers]] — back-reference; the glossary's BSP / HAL / PAC entries all point readers here for the deeper crate-stack treatment.
- [[Svd2Rust]] — back-reference; the PAC entry names svd2rust as the canonical PAC generator.
- [[EmbeddedHalCrate]] — back-reference; the HAL entry names `embedded-hal` as the trait crate HAL implementations target.

## Contradictions

None. The glossary is a pure definitional cross-walk and is consistent with every prior page that defines or uses these terms (in particular [[rust-embedded-book-start-registers]] for BSP / HAL / PAC, [[USART]] for UART, [[ARMCortexM]] for FPU).

## Corpus closure

This file is the **44th and final file** of the *Embedded Rust* corpus. The corpus is now **complete**: 44/44 chapters ingested between 2026-05-16 (file 1, [[rust-embedded-book-intro-index]]) and 2026-05-16 (this file). See [[TheEmbeddedRustBook]] for the full file index and the overview's *Embedded Rust corpus* paragraph for the synthesis.
