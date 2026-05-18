---
title: "Linker Script"
type: concept
tags: [embedded, linker, ld, gnu, memory-layout, elf]
sources: [rust-embedded-book-start-qemu]
last_updated: 2026-05-16
---

# Linker Script

**Text file consumed by the GNU `ld` / LLVM `lld` linker that declares the target's memory regions and how output ELF sections (`.text`, `.rodata`, `.data`, `.bss`, custom) map onto them.** On a hosted system the C library / loader supplies a default linker script and most developers never see one; in [[BareMetalProgramming|bare-metal]] / [[EmbeddedSystems|embedded]] development the linker script is **mandatory** — there is no loader to make the placement decisions at runtime.

## `memory.x` — the [[CortexMRTCrate|`cortex-m-rt`]] convention

*[[TheEmbeddedRustBook]]*'s [[rust-embedded-book-start-qemu|Chapter 11]] introduces the [[CortexMRTCrate|`cortex-m-rt`]] convention: the **user supplies a `memory.x` at the project root** declaring just the `MEMORY` block; `cortex-m-rt` ships the rest of the linker script (the `SECTIONS` block placing `.vector_table`, `.text`, `.rodata`, `.data`, `.bss` onto those regions).

The canonical `memory.x` for the [[LM3S6965]]:

```text
MEMORY
{
  FLASH : ORIGIN = 0x00000000, LENGTH = 256K
  RAM   : ORIGIN = 0x20000000, LENGTH = 64K
}
```

— two `MEMORY` regions, each with `ORIGIN` (the base address the [[ARMCortexM|Cortex-M]] sees) and `LENGTH`. Without `memory.x` "the build will fail to link the image."

## Optional overrides documented in the chapter

- **`_stack_start`** — pin the stack to a non-default location (default is `ORIGIN(RAM) + LENGTH(RAM)` — top of RAM, full-descending).
- **`_stext`** — push the start of the `.text` section past the [[VectorTable|vector table]] (e.g. `ORIGIN(FLASH) + 0x400`), useful for MCUs that store option bytes immediately after the vector table.
- **Extra `SECTIONS { … }` blocks via `INSERT AFTER .bss`** — for placing custom-attributed variables into custom RAM regions (e.g. a `RAM2` region accessed via `#[link_section = ".ram2bss"]`).

## Why bare-metal needs it

The linker script is the *only* place where the firmware author can encode:
- Where instructions live (Flash base address).
- Where data lives (SRAM base address).
- The boundary between read-only (Flash) and read-write (SRAM) regions.
- The position of the [[VectorTable|vector table]] (always at the Cortex-M reset address `0x0`).
- The stack origin.
- Custom on-chip memory regions (CCM RAM, backup RAM, instruction-cached vs uncached regions).

None of these can be inferred from Rust source alone — they are properties of the *target hardware*.

## Connections

- [[VectorTable]] — pinned to `ORIGIN(FLASH)` by the linker script.
- [[CortexMRTCrate]] — supplies the `SECTIONS` half of the script and consumes the user's `MEMORY` half.
- [[FlashMemory]] / [[SRAM]] — the two memory regions declared in every embedded linker script.
- [[BareMetalProgramming]] — the regime where linker scripts become mandatory.
- [[CrossCompilation]] — linker-script choice is part of the per-target build configuration.
- [[Bootloader]] — bootloaders use linker scripts to pin themselves at the reset vector and reserve regions for the application image.
- [[LM3S6965]] — the worked example MCU whose memory layout the chapter's `memory.x` encodes.
- [[TheEmbeddedRustBook]] — introduces `memory.x` as the first concrete linker script in [[rust-embedded-book-start-qemu]].
