---
title: "Microcontroller"
type: concept
tags: [embedded, hardware, mcu]
sources: [rust-embedded-book-intro-index, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Microcontroller

Single-chip integrated circuit combining a CPU core, on-chip memory (Flash + SRAM), and a fixed set of peripherals (GPIO, timers, ADCs, I2C/SPI/UART controllers, etc.) — designed to run dedicated firmware in an [[EmbeddedSystems|embedded system]], typically in a [[BareMetalProgramming|bare-metal]] (no-OS) configuration. The compute substrate [[TheEmbeddedRustBook]] focuses on; its examples use the [[STM32F3DISCOVERY]] dev board built around an [[ARMCortexM|ARM Cortex-M4]] MCU ([[rust-embedded-book-intro-index]]).

The book notes that **peripherals and implementation details differ between vendors and even between MCU families from the same vendor**, so portable embedded code requires either vendor-specific HAL crates or trait-based abstractions — a recurring theme in the Rust embedded ecosystem.

## The 8-bit AVR end of the spectrum

[[embedded-controllers-fiore]] ch. 16 establishes the same concept at a much smaller scale: the [[ATmega328P]] on the [[ArduinoUno|Arduino Uno]] is an 8-bit [[AVR]] [[HarvardArchitecture|Harvard]] [[RISC]] MCU with 32 k Flash, 2 k SRAM, 1 k EEPROM, three I/O ports (B / C / D), six 10-bit [[ADC]] channels, three [[TimerCounter|timer/counters]], USART/SPI/I²C, and 26 interrupt vectors — all running at 16 MHz with most instructions completing in one clock tick. Every peripheral is [[MemoryMappedIO|memory-mapped]] into the same address space as SRAM, so peripheral access in C looks exactly like a normal variable write: `PORTB |= 0x01;`.

## Connections

- [[EmbeddedSystems]] — the parent domain.
- [[ARMCortexM]] — the most common 32-bit MCU core family today and the one standardized by [[TheEmbeddedRustBook]].
- [[STM32F3DISCOVERY]] — the specific Cortex-M4 MCU dev board the book uses.
- [[MemoryMappedIO]] — how peripherals are accessed from firmware.
