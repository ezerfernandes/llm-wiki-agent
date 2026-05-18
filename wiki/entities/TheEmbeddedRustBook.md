---
title: "The Embedded Rust Book"
type: entity
tags: [rust, embedded, book]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-hardware, rust-embedded-book-intro-no-std, rust-embedded-book-intro-tooling, rust-embedded-book-c-tips-index, rust-embedded-book-interoperability-index, rust-embedded-book-interoperability-c-with-rust, rust-embedded-book-interoperability-rust-with-c, rust-embedded-book-unsorted-index, rust-embedded-book-unsorted-speed-vs-size, rust-embedded-book-unsorted-math, rust-embedded-book-appendix-glossary]
last_updated: 2026-05-16
---

# The Embedded Rust Book

Introductory book on using the [[RustLanguage|Rust]] programming language for **"[[BareMetalProgramming|bare-metal]]" [[EmbeddedSystems|embedded systems]]** such as [[Microcontroller|microcontrollers]]. Maintained by the [[RustEmbeddedWorkingGroup|Rust Embedded Working Group]]'s **resources team** in `github.com/rust-embedded/book`. Standardizes all examples on the [[ARMCortexM|ARM Cortex-M]] architecture via the [[STM32F3DISCOVERY]] dev board. Three stated goals: get developers onto embedded Rust (env setup), share current best practices, and serve as a cookbook (e.g. mixing C and Rust). Assumes either Rust desktop fluency *or* C/C++/Ada embedded background. Dual MIT / Apache 2.0 (code) + CC-BY-SA 4.0 (prose) license. Volunteer Japanese and Chinese translations.

**Corpus status:** **complete in the wiki — all 44/44 files ingested** between 2026-05-16 (file 1, [[rust-embedded-book-intro-index]]) and 2026-05-16 (file 44, [[rust-embedded-book-appendix-glossary]]).

## Connections

- [[rust-embedded-book-intro-index]] — Introduction chapter (file 1/44) sets scope, prerequisites, and conventions.
- [[rust-embedded-book-intro-hardware]] — Chapter 2 (file 2/44) — hardware tour of the [[STM32F3DISCOVERY]] (MCU, sensors, on-board ST-LINK debugger, 3.3 V signaling).
- [[rust-embedded-book-intro-no-std]] — Chapter 3 (file 3/44) — the `#![no_std]` execution-regime split ([[HostedEnvironment|hosted]] vs [[BareMetalProgramming|bare-metal]]), [[RustCoreLibrary|`libcore`]] vs [[RustStandardLibrary|`libstd`]], and the [[RustRuntime|pre-`main` runtime]] / [[HeapAllocation|heap]] consequences that every later chapter assumes.
- [[rust-embedded-book-intro-tooling]] — Chapter 4 (file 4/44) — the toolchain inventory: [[Cargo]] / [[Rustc]] / [[Rustup]] / [[CargoBinutils]] / [[CargoGenerate]] / [[QEMU]] on the build side; [[GDB]] / [[OpenOCD]] / [[ProbeRs]] / [[TRACE32]] driving [[STLink|ST-Link]] / [[JLink]] / [[MCULink]] / [[RustyProbe]] over [[JTAG]] / [[SWD]] on the debug side.
- [[rust-embedded-book-appendix-glossary]] — **Appendix A: Glossary (file 44/44, closing file of the corpus)** — pure cross-walk into the vendor-acronym alphabet ([[BSP]], [[FPU]], [[HALCrate|HAL]], [[I2C]], [[PeripheralAccessCrate|PAC]], [[SPI]], [[SVDFile|SVD]], [[UART]], [[USART]]); introduces only 3 new concept pages ([[BSP]], [[FPU]], [[UART]]) — every other glossary acronym already had a wiki page from prior chapters.
- [[RustEmbeddedWorkingGroup]] — governing body.
- [[STMicroelectronics]] — vendor of the standardized [[STM32F3DISCOVERY]] reference hardware.
- [[ARMCortexM]] — the ISA / core profile used in every example.
