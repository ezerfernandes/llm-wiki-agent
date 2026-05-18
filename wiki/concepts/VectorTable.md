---
title: "Vector Table (Interrupt Vector Table)"
type: concept
tags: [arm, embedded, cortex-m, interrupts, reset, elf]
sources: [rust-embedded-book-start-qemu, rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# Vector Table

**Table of function pointers at a fixed CPU-defined address that the [[ARMCortexM|Cortex-M]] core consults on reset and on every exception / [[Interrupt|interrupt]].** Entry 0 is the initial stack pointer; entry 1 is the **reset handler** (where the CPU jumps after power-on); subsequent entries are the exception handlers (NMI, HardFault, MemManage, BusFault, UsageFault, SVCall, PendSV, SysTick) and the device-specific external interrupts (IRQ0…IRQn from the [[Microcontroller|MCU]]'s NVIC).

## Position in a Cortex-M binary

On Cortex-M the vector table sits at **address `0x0`** by default — the very base of [[FlashMemory|Flash]]. In an ELF linked by [[CortexMRTCrate|`cortex-m-rt`]], it shows up as a non-standard ELF section named **`.vector_table`** — the chapter explicitly flags it ([[rust-embedded-book-start-qemu]]):

> "`.vector_table` is a *non*-standard section that we use to store the vector (interrupt) table"

Its observed size in the chapter's `cargo size` output: **1024 bytes** at address `0x0`, with the user's `.text` starting immediately after at `0x400`.

## Why 1 KiB

256 entries × 4 bytes each = 1024 bytes. Cortex-M reserves the first 16 entries for architectural exceptions; the remaining ~240 are device-specific external interrupts mapped by the MCU's NVIC. The `cortex-m-rt` runtime emits stubs (mostly `DefaultHandler_`) for every slot so the table is always full and ready to dispatch.

## Relationship with the linker script

The vector table's *placement* is fixed by the [[LinkerScript|linker script]] — `cortex-m-rt`'s embedded linker fragment puts `.vector_table` at the start of the `FLASH` region defined in the user's `memory.x`. The optional `_stext` symbol lets the user push the application `.text` further into Flash, leaving a gap right after the vector table for vendor configuration words (some MCUs store option bytes / boot config there).

## Connections

- [[Interrupt]] — the dispatch mechanism the vector table backs.
- [[ExceptionAttribute]] — `#[exception]` writes user functions into the vector-table slots that would otherwise hold [[DefaultHandler]] stubs ([[rust-embedded-book-start-exceptions]]).
- [[HardFault]] / [[DefaultHandler]] — specific named slots in the architectural-exception region of the table.
- [[CortexMRTCrate]] — generates and populates `.vector_table` for the user.
- [[LinkerScript]] — pins the vector table's address to the start of [[FlashMemory|Flash]].
- [[ARMCortexM]] — defines the table's layout and the reset / exception model.
- [[FlashMemory]] — where the vector table lives at `0x0` on Cortex-M.
- [[Bootloader]] — bootloaders are essentially custom code occupying the vector-table position before handing off to the application.
- [[TheEmbeddedRustBook]] — exposes `.vector_table` directly via `cargo size` in [[rust-embedded-book-start-qemu]].
