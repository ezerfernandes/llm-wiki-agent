---
title: "Embedded Systems"
type: concept
tags: [embedded, systems-programming, hardware]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-no-std, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Embedded Systems

Computing systems designed to run as a dedicated component inside a larger device, typically with constrained memory, compute, and power, and often interacting with the physical world via sensors / actuators. The domain ranges across orders of magnitude: from 8-bit MCUs with a few KB of RAM/ROM (e.g. ST72325xx) up to Linux-class SoCs like a Raspberry Pi 3B+ (4-core Cortex-A53 @ 1.4 GHz, 1 GB RAM) — *"Different restrictions/limitations will apply when writing code depending on what kind of target and use case you have"* ([[rust-embedded-book-intro-no-std]]). [[TheEmbeddedRustBook]] targets the small / bare-metal end of the spectrum and uses [[ARMCortexM|ARM Cortex-M]] as its standardized substrate ([[rust-embedded-book-intro-index]]).

[[rust-embedded-book-intro-no-std]] partitions the domain into two execution regimes:
- **[[HostedEnvironment|Hosted]]** — an OS underneath providing POSIX-class primitives; standard library fully usable. Linux-class SoCs.
- **[[BareMetalProgramming|Bare-metal]]** — no OS, no pre-loaded code; standard library not loadable. Small MCU firmware. The regime the book focuses on; requires [[NoStd|`#![no_std]`]] in [[RustLanguage|Rust]].

Distinguishing technical concerns relative to desktop programming, per [[rust-embedded-book-intro-index]]'s prerequisites list:
- [[CrossCompilation]] — building binaries on a host for a different target ISA.
- [[MemoryMappedIO]] — peripherals appear as memory addresses, not OS-mediated calls.
- [[Interrupt|Interrupts]] — asynchronous control flow driven by external events.
- Wire-level interfaces — [[I2C]], [[SPI]], serial / UART.

## Two complementary corpora in this wiki

| Corpus | Language | Target | Pedagogy |
|---|---|---|---|
| [[TheEmbeddedRustBook]] | [[RustLanguage\|Rust]] (`#![no_std]`) | [[ARMCortexM\|ARM Cortex-M]] (32-bit, STM32F303VCT6 / 256 k Flash / 48 k SRAM) | Type-state, [[ZeroCostAbstraction\|zero-cost abstractions]], static safety via the type system |
| [[embedded-controllers-fiore]] | [[CLanguage\|C]] (with [[Arduino]] library) | [[AVR\|Atmel AVR]] (8-bit, [[ATmega328P]] / 32 k Flash / 2 k SRAM) | Read the library source, then bypass it with direct register pokes; safety comes from understanding the hardware, not from the type system |

The two are deliberate opposites in the embedded-language tradeoff space and together cover the bulk of the practical embedded-MCU domain. Neither is wrong; they reflect different audiences (production engineers vs first-time embedded undergraduates) and different priorities (correctness-by-construction vs hardware-intuition-first).

## Connections

- [[Microcontroller]] — the canonical compute substrate for small embedded systems.
- [[BareMetalProgramming]] / [[HostedEnvironment]] — the two execution regimes.
- [[NoStd]] — required for bare-metal Rust on this domain.
- [[HeapAllocation]] — off by default in bare-metal embedded; opt-in via `alloc` + global allocator.
- [[RustLanguage]] — Rust offers safety + abstraction in this domain without giving up bare-metal control.
