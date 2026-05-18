---
title: "The Embedded Rust Book — Getting Started"
type: source
tags: [rust, embedded, book-chapter]
date: 2026-05-16
source_file: raw/book/src/start/index.md
last_updated: 2026-05-16
---

## Summary
Chapter intro (file 10/44) of *[[TheEmbeddedRustBook]]*: a six-line preface opening the **Getting Started** part of the book — the practical "write → build → flash → debug" loop that follows the now-closed intro chapter (files 1–9). Frames the chapter's pedagogical contract: **most examples are reproducible without hardware**, using [[QEMU]] as the [[ARMCortexM|Cortex-M]] emulator; only the Hardware sub-section requires the physical [[STM32F3DISCOVERY]] board flashed via [[OpenOCD]].

## Key Claims
- The Getting Started chapter walks the reader through the four-step embedded loop: **writing, building, flashing, debugging**.
- **Most examples in the chapter require no hardware** — [[QEMU]] (introduced as the "popular open-source hardware emulator") emulates the [[ARMCortexM|Cortex-M]] target for everything except the dedicated Hardware section.
- The Hardware section is the sole hardware-gated section; it uses [[OpenOCD]] to program an [[STM32F3DISCOVERY]] board — both already-established artifacts from the intro chapter ([[rust-embedded-book-intro-hardware]], [[rust-embedded-book-intro-verify]]).

## Key Quotes
> "You will be able to try most of the examples without any special hardware as we will show you the basics using QEMU, a popular open-source hardware emulator." — frames the QEMU-first pedagogy of the entire chapter

## Connections
- [[TheEmbeddedRustBook]] — file 10/44; opens Part 2 (*Getting Started*) after the intro chapter closed at file 9.
- [[rust-embedded-book-intro-verify]] — directly preceding file; the intro's closing smoke test (OpenOCD enumerates the ST-LINK) is the operational baseline this chapter assumes.
- [[QEMU]] — promoted from "one of the tools listed in [[rust-embedded-book-intro-tooling|tooling]]" to **the default execution substrate for the chapter's exercises**.
- [[OpenOCD]] — reserved for the Hardware sub-section only.
- [[STM32F3DISCOVERY]] — the reference board, already inventoried in [[rust-embedded-book-intro-hardware]].
- [[ARMCortexM]] — the architecture QEMU emulates and the F3 board hosts.

## Contradictions
None — strictly additive scoping page.
