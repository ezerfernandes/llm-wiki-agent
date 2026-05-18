---
title: "AVR (Microcontroller Family)"
type: concept
tags: [embedded, mcu, atmel, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# AVR

Family of 8-bit [[RISC]] microcontrollers designed by [[Atmel]] (now part of Microchip), distinguished by [[HarvardArchitecture|Harvard]] architecture, pipelined single-cycle instruction execution, and a generous 32-entry 8-bit general-purpose register file feeding the [[ALU]]. The substrate of nearly every classic [[Arduino]] board: Uno / Mini / Nano use the [[ATmega328P]]; Mega uses the ATmega2560; older 168 / 8 boards are slightly smaller variants of the same architecture.

Per [[embedded-controllers-fiore]] ch. 16, the AVR core sits in the same category as ARM at the RISC end of the [[CISC]]/RISC divide; AVR is used "in everything from simple embedded applications to cell phones to supercomputers" via the related ARM line, while AVR itself is the workhorse 8-bit MCU in cost-sensitive embedded design.

## Distinctive properties

- **8-bit data bus** between the ALU, registers, and memory.
- **Harvard architecture** — separate Flash (program) and SRAM (data) memory spaces. Implies that program-memory data (e.g. lookup tables in PROGMEM) requires special access functions (`pgm_read_word`, `pgm_read_byte`) rather than normal pointer dereferences.
- **Pipelined**: while one instruction executes, the next is being fetched.
- **Most instructions in 1 clock cycle**.
- **32 GPRs** (large for an 8-bit MCU; small compared to ARM's 16 32-bit ARM-mode registers).
- **Specialized I/O modules** — timer/counters, ADC, USART, SPI, TWI, watchdog — all [[MemoryMappedIO|memory-mapped]].

## Members (selected)

- ATmega48A — 4 k Flash / 256 B EEPROM / 512 B SRAM (small footprint).
- ATmega168 — older Arduino chip.
- [[ATmega328P]] — 32 k Flash / 2 k SRAM / 1 k EEPROM. The Uno.
- ATmega2560 — Mega. More pins, more memory.
- ATxmega256A3B — high-end xmega line, 256 k Flash.

## Connections

- [[ATmega328P]] — the specific 328P.
- [[Atmel]] — the designer.
- [[Arduino]] / [[ArduinoUno]] — the platform that popularized AVR.
- [[Microcontroller]] — the broader category.
- [[ARMCortexM]] — the modern 32-bit alternative; co-exists in the Arduino line on the Due / MKR boards.
- [[embedded-controllers-fiore]] — the source.
