---
title: "The Embedded Rust Book — Hardware"
type: source
tags: [rust, embedded, book-chapter, hardware]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/hardware.md
---

# The Embedded Rust Book — Hardware

## Summary

Chapter 2 (file 2/44) of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — a hardware tour of the [[STM32F3DISCOVERY|STM32F3DISCOVERY ("F3")]] dev board that every example in the book targets. Enumerates the on-board MCU ([[STM32F303VCT6]], a [[ARMCortexM|Cortex-M4F]] at up to 72 MHz with 256 KiB [[FlashMemory|Flash]] / 48 KiB [[SRAM]]), the integrated sensors ([[Accelerometer]] + [[Magnetometer]] on the [[LSM303DLHC]] chip, [[Gyroscope]] on the [[L3GD20]] chip), 8 user LEDs in a compass pattern, and a second MCU ([[STM32F103]]) acting as an on-board [[STLink|ST-LINK]] programmer/debugger over the USB ST-LINK port. The chapter also warns that the [[STM32F303VCT6]] is a **3.3 V** part — applying external signals above the absolute-maximum rating will damage it.

## Key Claims

- **Main MCU**: [[STM32F303VCT6]] — single-core [[ARMCortexM|ARM Cortex-M4F]] with hardware single-precision FPU, max clock 72 MHz, **256 KiB Flash + 48 KiB SRAM**, with integrated peripherals: timers, [[I2C]], [[SPI]], [[USART]], [[GPIO]]. The "F" in Cortex-M4F denotes the FPU variant.
- **Pinout**: the board exposes the MCU's [[GPIO]] and other pin types through two header rows on the sides of the board; a Mini-USB on the "USB USER" port is wired to the main MCU.
- **Sensors**: an [[Accelerometer]] *and* [[Magnetometer]] are integrated on a single [[LSM303DLHC]] chip from [[STMicroelectronics]]; a [[Gyroscope]] on a separate [[L3GD20]] chip. Combined this gives the board a 9-axis [[IMU|inertial motion unit]] (3 axes each for accel/mag/gyro). Both chips are read over [[I2C]] (LSM303DLHC) and [[SPI]] (L3GD20) — the canonical sensor-bus pair the prior chapter listed as prerequisite knowledge.
- **User-visible feedback**: 8 user LEDs physically arranged in a compass-rose pattern (N / NE / E / SE / S / SW / W / NW). Combined with the magnetometer these enable the "digital compass" worked example used in the [[DiscoveryBook|Discovery Book]] companion.
- **Debug probe is on-board**: a second MCU — an [[STM32F103]] — sits on the board and acts as a built-in [[STLink|ST-LINK]] programmer / debugger. It is connected to the host via the Mini-USB labeled "USB ST-LINK" (distinct from "USB USER"). This is *why* the board needs no external debug probe and can be programmed directly from a host PC over USB — a major usability advantage for a learning board.
- **Two distinct USB ports** — "USB USER" goes to the application MCU ([[STM32F303VCT6]]); "USB ST-LINK" goes to the debugger MCU ([[STM32F103]]). New users routinely confuse them.
- **Electrical safety constraint**: nominal pin voltage is **3.3 V** (not 5 V) on the [[STM32F303VCT6]]. Exceeding the absolute-maximum ratings (consult §6.2 of the datasheet) damages the part. This is the first explicit hardware-safety contract in the book.

## Key Quotes

> "A single-core ARM Cortex-M4F processor with hardware support for single-precision floating point operations and a maximum clock frequency of 72 MHz." — defines the compute envelope every example in the book runs against.

> "A word of caution: be careful if you want to apply external signals to the board. The microcontroller STM32F303VCT6 pins take a nominal voltage of 3.3 volts." — first hardware-safety contract; sets the level-shifting requirement for any 5 V interfacing.

> "A second microcontroller: a STM32F103. This microcontroller is actually part of an on-board programmer / debugger and is connected to the Mini-USB port named 'USB ST-LINK'." — explains the dual-MCU architecture that makes the board self-programmable.

## Connections

- [[TheEmbeddedRustBook]] — chapter 2 of the book; this is the hardware basis for every later code example.
- [[STM32F3DISCOVERY]] — the board being described in detail.
- [[STMicroelectronics]] — manufacturer of the board, both MCUs, and the LSM303DLHC sensor; also the [[STLink]] debug protocol.
- [[STM32F303VCT6]] — the application MCU; new entity from this ingest.
- [[STM32F103]] — the on-board debugger MCU; new entity from this ingest.
- [[ARMCortexM]] — the core profile (M4F variant); pre-existing.
- [[Microcontroller]] — the device class; pre-existing.
- [[GPIO]], [[USART]], [[I2C]], [[SPI]] — the four canonical MCU peripheral classes the chapter calls out. [[I2C]] / [[SPI]] pre-existed; [[GPIO]] / [[USART]] are new from this ingest.
- [[FlashMemory]], [[SRAM]] — the two on-MCU memory tiers (256 KiB / 48 KiB); new from this ingest. Define the firmware's code-vs-runtime budget.
- [[Accelerometer]], [[Magnetometer]], [[Gyroscope]] — the three sensor classes the board ships; new from this ingest.
- [[LSM303DLHC]], [[L3GD20]] — the specific sensor chips; new from this ingest.
- [[STLink]] — the [[STMicroelectronics]] debug-probe protocol; new from this ingest.

## Contradictions

- None. The chapter is a hardware datasheet excerpt — purely additive to [[rust-embedded-book-intro-index]].

## Notes for the Embedded Rust corpus

- **File 2 of 44.** First substantively technical chapter. Establishes the *physical* contract every later chapter codes against (clock, memory budget, peripheral mix, sensor set, 3.3 V signaling).
- The 9-axis IMU + 8-LED compass arrangement is engineered for the *digital-compass* tutorial in the companion [[DiscoveryBook|Discovery Book]] — a forward pointer worth tracking when later chapters or the Discovery Book are ingested.
- Minor erratum in the chapter prose: "1 KiB = 10**24** bytes" — should be **1024** (Markdown's `**` consumed the digit). Worth flagging upstream if reporting bugs to the rust-embedded book repo.
