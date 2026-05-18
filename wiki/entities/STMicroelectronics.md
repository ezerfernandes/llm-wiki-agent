---
title: "STMicroelectronics"
type: entity
tags: [semiconductor, microcontroller, vendor]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# STMicroelectronics

Franco-Italian semiconductor manufacturer. Producer of the **STM32** family of [[ARMCortexM|ARM Cortex-M]]-based 32-bit [[Microcontroller|microcontrollers]] and associated *Discovery* / *Nucleo* development boards. [[TheEmbeddedRustBook]] standardizes its examples on the [[STM32F3DISCOVERY]] dev board ([[rust-embedded-book-intro-index]]).

## Connections

- [[STM32F3DISCOVERY]] — the reference dev board used in [[TheEmbeddedRustBook]].
- [[ARMCortexM]] — the ISA family STM32 MCUs are built on.
- [[STM32F303VCT6]] — the application MCU on the [[STM32F3DISCOVERY]].
- [[STM32F103]] — Cortex-M3 MCU family; on the F3 board it serves as the on-board [[STLink|ST-LINK]] debugger.
- [[LSM303DLHC]] / [[L3GD20]] — STMicro MEMS sensor chips on the F3 board.
- [[STLink]] — STMicro's in-circuit programmer/debugger protocol and product family.
