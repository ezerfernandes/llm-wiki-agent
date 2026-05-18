---
title: "Peripheral"
type: concept
tags: [embedded, hardware, peripherals, mmio]
sources: [rust-embedded-book-peripherals-index]
last_updated: 2026-05-16
---

# Peripheral

A **silicon block on a [[Microcontroller|microcontroller]] dedicated to interacting with the world outside the CPU** — directly (sensors, motor controllers, displays, keyboards) or indirectly (serial buses, timers, DMA controllers). Collectively distinct from the CPU core, on-chip RAM, and on-chip Flash. Useful because firmware can **offload processing to dedicated hardware**, freeing the CPU to do other work or sleep for power savings — the embedded analogue of offloading graphics to a GPU on a desktop ([[rust-embedded-book-peripherals-index]]).

## Hardware API, not software API

Unlike a GPU (Vulkan / Metal / OpenGL) or an OS-mediated device, an MCU peripheral exposes a **hardware interface mapped to a chunk of memory** — the [[MemoryMappedIO|memory-mapped I/O]] model. Operation is "write the right data to the correct address": e.g. sending a 32-bit word over a serial port = writing it to that port's data register; configuring an [[SPI]] frequency = writing a magic value (`0x8000_0000` → 8 Mbps, `0x0200_0000` → 125 Kbps on the nRF52832) to the SPI frequency register. The interface is **language-agnostic** — "no matter what language is used, whether that language is Assembly, C, or Rust" ([[rust-embedded-book-peripherals-index]]).

## Address-space placement

[[ARMCortexM|Cortex-M]] MCUs have a linear 32-bit physical address space (`0x0000_0000`–`0xFFFF_FFFF`) and **no MMU**, so peripheral registers are simply slotted between the [[FlashMemory|Flash ROM region]] (near `0x0000_0000`) and the [[SRAM|SRAM region]] (near `0x2000_0000`). Upper address bits select which peripheral block (chip-select), lower bits select which register within that block ([[rust-embedded-book-peripherals-index]]).

## Examples in this wiki

- [[GPIO]] — general-purpose digital I/O pins.
- [[USART]] — universal asynchronous serial.
- [[I2C]] — two-wire bus.
- [[SPI]] — four-wire synchronous bus (worked example for the chapter's frequency-register figure).
- [[SysTick]] — Cortex-M architectural timer peripheral.
- [[NVIC]] — Cortex-M architectural interrupt-controller peripheral.

## Rust-specific access layers

Idiomatic Rust wraps raw [[MemoryMappedIO|MMIO]] in a four-layer crate stack so peripheral access becomes typed, single-ownership, and zero-cost ([[rust-embedded-book-start-registers]]):

- [[MicroArchitectureCrate]] — core-level (e.g. [[CortexMCrate|`cortex-m`]] for architectural peripherals like [[SysTick]] / [[NVIC]]).
- [[PeripheralAccessCrate|PAC]] — chip-specific, auto-generated from the [[SVDFile|SVD]] by [[Svd2Rust|`svd2rust`]].
- [[HALCrate|HAL]] — ergonomic portable API via [[EmbeddedHalCrate|`embedded-hal`]] traits.
- [[BoardCrate]] — dev-board-specific pre-configuration.

## Connections

- [[Microcontroller]] — the host substrate; the chapter contrasts an MCU's collection of peripherals with the desktop CPU + discrete-cards model.
- [[MemoryMappedIO]] — the hardware-interface convention through which all peripherals are accessed.
- [[BareMetalProgramming]] — the regime in which firmware drives peripherals directly with no OS device-driver layer.
- [[ARMCortexM]] — the architecture whose memory-map convention places peripherals between Flash and SRAM.
- [[EmbeddedSystems]] — the broader domain.
- [[Interrupt]] — peripherals are also the source of most device-specific IRQs (see [[rust-embedded-book-start-interrupts]]).
