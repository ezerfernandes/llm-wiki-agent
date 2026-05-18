---
title: "STM32F303VCT6"
type: entity
tags: [microcontroller, mcu, arm-cortex-m, stm32, hardware]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# STM32F303VCT6

The application [[Microcontroller|microcontroller]] on the [[STM32F3DISCOVERY]] dev board, manufactured by [[STMicroelectronics]]. Single-core [[ARMCortexM|ARM Cortex-M4F]] (the "F" denotes the hardware single-precision FPU), max clock 72 MHz, **256 KiB [[FlashMemory|Flash]] + 48 KiB [[SRAM]]**, with integrated [[GPIO]] / timers / [[I2C]] / [[SPI]] / [[USART]] peripherals. Nominal pin voltage is **3.3 V** — the [[TheEmbeddedRustBook|book]] explicitly warns that exceeding the absolute-maximum ratings (datasheet §6.2) damages the part ([[rust-embedded-book-intro-hardware]]).

This is the MCU every code example in *[[TheEmbeddedRustBook]]* actually runs on, accessed from the host PC via the on-board [[STM32F103]] [[STLink|ST-LINK]] debugger over the "USB ST-LINK" port, while the "USB USER" port is wired directly to this part.

## Connections

- [[STM32F3DISCOVERY]] — the dev board this MCU sits on.
- [[STMicroelectronics]] — manufacturer.
- [[ARMCortexM]] — Cortex-M4F core profile.
- [[Microcontroller]] — device class.
- [[STM32F103]] — sibling Cortex-M3 MCU on the same board acting as its [[STLink|ST-LINK]] debug probe.
- [[FlashMemory]] / [[SRAM]] — 256 KiB / 48 KiB on-chip memory.
