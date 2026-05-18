---
title: "SRAM"
type: concept
tags: [embedded, hardware, memory, volatile]
sources: [rust-embedded-book-intro-hardware, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# SRAM

**Static Random-Access Memory** — volatile, fast, single-cycle-access on-chip memory used by [[Microcontroller|MCUs]] for the runtime stack, heap (when present), `.data` / `.bss` sections, and DMA buffers. Loses contents on reset / power-off, in contrast to non-volatile [[FlashMemory|Flash]] which holds the firmware image. "Static" distinguishes it from DRAM (which requires periodic refresh); SRAM cells are larger and more expensive per bit, which is why MCU SRAM budgets are tiny relative to Flash.

The [[STM32F303VCT6]] on the [[STM32F3DISCOVERY]] ships with **48 KiB** of SRAM and 256 KiB of Flash ([[rust-embedded-book-intro-hardware]]). The 48 KiB ceiling is the hard limit on the firmware's runtime working set — stack, statics, and any heap if `alloc` is enabled. Embedded Rust's tendency to push the stack via large `Future` types (async state machines) and monomorphized generics is precisely why `#![no_std]` codebases lean on stack-allocated arenas and on type-state APIs that compile *into* zero-sized markers rather than runtime structures.

## On 8-bit AVR (per [[embedded-controllers-fiore]])

The [[ATmega328P]] has 2 KiB SRAM — ~24× smaller than the STM32F303VCT6 above. Same partition into data + stack-growing-down, but with no MMU and no isolation between the two — Fiore explicitly warns about *stack-data overrun*, where deep recursion or many `auto` locals push the stack into the data section and silently corrupt globals. SRAM also holds the [[MemoryMappedIO|memory-mapped]] peripheral registers (PORTx, DDRx, PINx, ADCH/ADCL, etc.) at the bottom of its address range, so the Arduino code `PORTB |= 0x01;` is literally a write to SRAM at address `0x25`.

## Connections

- [[Microcontroller]] — on-chip SRAM holds the runtime state on every MCU.
- [[STM32F303VCT6]] — 48 KiB SRAM on the [[STM32F3DISCOVERY]]'s application MCU.
- [[FlashMemory]] — sibling non-volatile tier; together they define the firmware's static + runtime budget.
- [[BareMetalProgramming]] — without an OS the firmware owns SRAM directly, partitioned by the linker script.
