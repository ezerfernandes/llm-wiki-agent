---
title: "The Embedded Rust Book — Peripherals"
type: source
tags: [rust, embedded, book-chapter, peripherals]
date: 2026-05-16
source_file: raw/book/src/peripherals/index.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Peripherals

## Summary

File 18/44 of *[[TheEmbeddedRustBook]]* — the **chapter opener** for the *Peripherals* part of the book, immediately after the *Getting Started* chapter closed at file 17 ([[rust-embedded-book-start-interrupts]]). Compact conceptual intro (three sub-sections, no code) that defines [[Peripheral|peripherals]] as the silicon blocks on a [[Microcontroller|microcontroller]] that interact with the outside world (sensors, motor controllers, displays, keyboards), explains why the embedded address space is **linear and real** (no [[Microcontroller|MMU]] on typical MCUs — software uses physical addresses directly), and frames the [[MemoryMappedIO|memory-mapped peripheral]] model as the universal hardware-interface convention "no matter what language is used, whether that language is Assembly, C, or Rust." Backstops the chapter's later mechanical sub-sections (singletons, ownership, RAII) with the underlying address-space mental model. Re-uses the [[Microcontroller|nRF52832]] memory map and the [[SPI|SPI frequency configuration register]] from the Nordic datasheet as anchor diagrams.

## Key Claims

- **Peripherals are silicon blocks on the MCU for outside-world interaction** — sensors, motor controllers, displays, keyboards — collectively distinct from the CPU, RAM, and Flash. Useful because they let firmware **offload processing** to dedicated hardware (analogous to a desktop GPU), freeing the CPU to do other work or sleep for power savings.
- **The 1970s/1980s home-computer analogy**: processor + RAM + ROM + I/O controller, joined by a parallel **address-and-data bus**. Same architecture, just packed onto a single piece of silicon in a modern MCU.
- **Microcontrollers do not have an MMU** (unlike desktops): no virtual memory, no inter-process memory protection. Software uses **real physical addresses** directly. Writing to an arbitrary address like `0x4000_0000` or `0x0000_0000` "may also be a completely valid action."
- **32-bit MCUs have a linear address space `0x0000_0000`–`0xFFFF_FFFF`** but only use a few hundred KiB of actual memory. The vast remaining space is **populated by memory-mapped peripheral registers**, slotted between the Flash ROM region (typically near `0x0000_0000`) and the SRAM region (typically near `0x2000_0000` on [[ARMCortexM|Cortex-M]]).
- **Address-decode mechanics** (worked example): with 64 KiB of RAM at `0x2000_0000`, an address like `0x2000_1234` decodes as upper bits (`0x2000`) → activate RAM chip-select, lower bits (`0x1234`) → offset within RAM. The same decoding logic routes addresses in the peripheral range to the appropriate peripheral block.
- **Memory-mapped peripherals are operated by writing data to specific addresses** — e.g. sending a 32-bit word over a serial port = writing the word to that port's data register address; configuration registers work identically (`0x8000_0000` to the SPI frequency register → 8 Mbps; `0x0200_0000` → 125 Kbps).
- **The hardware-interface contract is language-agnostic**: "This interface is how interactions with the hardware are made, no matter what language is used, whether that language is Assembly, C, or Rust." Peripherals expose a **hardware API**, not a software API like Vulkan / Metal / OpenGL.
- **Visual anchor**: the chapter references the [[Microcontroller|Nordic nRF52832]] memory map image and the nRF52832 SPI frequency register bit-layout image (both from the Nordic datasheet) as the concrete artifacts the abstract description is grounded in.

## Key Quotes

> "These components are collectively known as Peripherals." — defining sentence for the chapter's headline noun.

> "Microcontrollers do not typically have an MMU, and instead only use real physical addresses in software." — the structural difference from desktop programming that motivates the entire chapter.

> "Rather than ignore all remaining space between these two regions, Microcontroller designers instead mapped the interface for peripherals in certain memory locations." — the design-decision quote that ties the address-space layout to the memory-mapped peripheral model.

> "This interface is how interactions with the hardware are made, no matter what language is used, whether that language is Assembly, C, or Rust." — the universality claim that frames the chapter's later Rust-specific sub-sections (singletons, ownership, RAII) as **idioms on top of a language-agnostic hardware contract**, not Rust-only inventions.

## Connections

- [[TheEmbeddedRustBook]] — file 18/44; **opens the Peripherals chapter** after *Getting Started* closed at file 17 ([[rust-embedded-book-start-interrupts]]).
- [[rust-embedded-book-start-interrupts]] — directly preceding file; closed the *Getting Started* chapter. This chapter shifts the level of abstraction from runtime/handler plumbing back down to the **address-space model** the runtime is built on top of.
- [[rust-embedded-book-start-registers]] — earlier *Getting Started* chapter that already walked the [[PeripheralAccessCrate|PAC]] / [[HALCrate|HAL]] crate stack over memory-mapped registers; this chapter intro is the **conceptual ground floor** that mechanical chapter implicitly assumed.
- [[Peripheral]] — the central concept this file defines.
- [[MemoryMappedIO]] — the hardware-interface convention the chapter explains (peripheral registers exposed at fixed addresses in the CPU's address space).
- [[Microcontroller]] — the compute substrate; the chapter contrasts its lack of MMU and linear physical address space against the desktop-MMU/virtual-memory model.
- [[BareMetalProgramming]] — the regime in which "writing to an arbitrary address may be a completely valid action."
- [[ARMCortexM]] — the Cortex-M memory-map convention (Flash ROM near `0x0000_0000`, SRAM near `0x2000_0000`) is the concrete instance the chapter walks.
- [[FlashMemory]] — the on-chip Flash ROM region the chapter places near `0x0000_0000`.
- [[SRAM]] — the on-chip SRAM region the chapter places at `0x2000_0000`.
- [[GPIO]] / [[USART]] / [[I2C]] / [[SPI]] — examples of peripherals whose configuration the chapter uses to illustrate the memory-mapped register model (SPI frequency register is the worked example).
- [[Interrupt]] — peripherals are also the source of most device-specific [[Interrupt|IRQs]] (already covered at [[rust-embedded-book-start-interrupts]]); not explicitly mentioned here but forms the bridge from this chapter's address-space view back to the prior chapter's controller view.

## Contradictions

None with existing wiki content. Strictly additive — formalizes the **address-space mental model** that prior chapters ([[rust-embedded-book-start-qemu]] with its `memory.x` linker script, [[rust-embedded-book-start-hardware]] with the `0x0800_0000` Flash + `0x2000_0000` SRAM map for the [[STM32F303VCT6]], [[rust-embedded-book-start-registers]] with its [[PeripheralAccessCrate|PAC]] register accessors) used operationally without ever stating in plain prose. The MMU-absence note slightly refines [[Microcontroller]]'s "single-chip combining CPU + memory + peripherals" framing by adding the **flat physical address space, no protection** corollary.
