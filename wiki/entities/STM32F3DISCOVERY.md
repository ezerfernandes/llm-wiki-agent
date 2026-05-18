---
title: "STM32F3DISCOVERY"
type: entity
tags: [microcontroller, dev-board, arm-cortex-m, hardware]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# STM32F3DISCOVERY

Low-cost development board from [[STMicroelectronics]] based on the STM32F3 series ([[ARMCortexM|ARM Cortex-M4]] core with FPU). Used as the reference hardware for **every example** in [[TheEmbeddedRustBook]]. The book notes that basic Cortex-M functionality is the same across vendors, but peripherals and implementation details differ — sometimes even between MCU families from the same vendor — so a fixed dev board makes the examples reproducible ([[rust-embedded-book-intro-index]]).

## Hardware details ([[rust-embedded-book-intro-hardware]])

- **Application MCU**: [[STM32F303VCT6]] — single-core [[ARMCortexM|Cortex-M4F]] (with FPU), 72 MHz max, **256 KiB [[FlashMemory|Flash]] + 48 KiB [[SRAM]]**. Integrated [[GPIO]] / timers / [[I2C]] / [[SPI]] / [[USART]] peripherals; pin headers expose GPIO + alt-functions along both edges of the board.
- **Sensors (9-axis [[IMU]])**: [[Accelerometer]] + [[Magnetometer]] on the [[LSM303DLHC]] chip ([[I2C]]); [[Gyroscope]] on the [[L3GD20]] chip ([[SPI]]).
- **User feedback**: 8 user LEDs arranged in a compass-rose pattern (N / NE / E / SE / S / SW / W / NW) — the visual basis for the canonical *digital-compass* tutorial.
- **On-board debugger**: a second MCU, an [[STM32F103]], implements an on-board [[STLink|ST-LINK]] programmer/debugger wired to the host PC over the "USB ST-LINK" Mini-USB port. The "USB USER" port goes directly to the [[STM32F303VCT6]] application MCU. New users routinely confuse the two.
- **Electrical contract**: pins are nominal **3.3 V** — exceeding the absolute-maximum ratings (datasheet §6.2) damages the part.

## Connections

- [[TheEmbeddedRustBook]] — uses this board for all worked examples.
- [[STMicroelectronics]] — manufacturer.
- [[ARMCortexM]] — the core profile (M4) underneath the board.
- [[Microcontroller]] — class of device.
- [[STM32F303VCT6]] / [[STM32F103]] — the two MCUs on the board (application + on-board debugger).
- [[LSM303DLHC]] / [[L3GD20]] — the two sensor chips composing the 9-axis [[IMU]].
- [[STLink]] — the debug protocol the on-board F103 implements.
