---
title: "Harvard Architecture"
type: concept
tags: [computer-architecture, embedded, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Harvard Architecture

CPU architecture in which **program memory** (instructions) and **data memory** are physically separate, each accessed via its own bus, so the processor can fetch the next instruction while simultaneously reading or writing data. Named after the Harvard Mark I (see [[HarvardMarkI]]). Contrast: [[VonNeumannArchitecture|Von Neumann]], which shares one bus.

Per [[embedded-controllers-fiore]] ch. 2 / 16:

> "Having two separate memory buses will speed execution times."

The downside is that data and code can't freely move between regions — program-memory constants need special read instructions (on AVR, `pgm_read_word` / `pgm_read_byte`; the `PROGMEM` attribute marks data as living in Flash).

## Embedded implications

- **MCU program memory is usually [[FlashMemory|Flash]]** — non-volatile so the program survives power cycle; the boundary between "code" and "constant lookup tables in Flash" is enforced by Harvard separation.
- **Data memory is usually [[SRAM]]** — volatile, fast, holds variables and the [[Stack|stack]].
- **No conflict between instruction fetch and data load** — central to single-cycle execution on the [[AVR]].

## Examples

- [[AVR]] / [[ATmega328P]] — 8-bit Harvard with 32 k Flash (program) + 2 k SRAM (data) + 1 k [[EEPROM]] (settings).
- [[ARMCortexM]] — modified Harvard (separate I-bus / D-bus inside the core, but a unified address space externally).

## Connections

- [[VonNeumannArchitecture]] — the alternative single-bus model.
- [[HarvardMarkI]] — the namesake.
- [[FlashMemory]] / [[SRAM]] / [[EEPROM]] — the memory technologies typically used.
- [[ATmega328P]] / [[AVR]] / [[ARMCortexM]] — Harvard-architecture MCU families.
- [[embedded-controllers-fiore]] — the source.
