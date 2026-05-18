---
title: "Atmel Corporation"
type: entity
tags: [semiconductor, mcu, manufacturer]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Atmel

Semiconductor company that designed the **AVR** family of 8-bit RISC microcontrollers, including the [[ATmega328P]] used in the [[ArduinoUno|Arduino Uno]]. Founded 1984; acquired by Microchip Technology in 2016, so current ATmega part numbers are listed at microchip.com (e.g. microchip.com/wwwproducts/en/ATMEGA328P) but the architecture and naming conventions remain "Atmel AVR" in nearly all documentation and course material. The schematics, block diagrams, and register tables in [[embedded-controllers-fiore]] are derived from Atmel's October 2014 ATmega 328P datasheet.

The AVR family — and the ATmega series specifically — is the substrate of nearly every Arduino board with a "U"-class chip (Uno, Nano, Mini, Mega). Distinguishing features per [[embedded-controllers-fiore]]:

- **8-bit data bus**, [[HarvardArchitecture|Harvard architecture]] with simple pipelining.
- **[[RISC]]** instruction set — most instructions execute in one 16 MHz clock cycle.
- **32 general-purpose 8-bit registers** (large for an 8-bit MCU, small for a 32-bit one).
- Three special registers: [[ProgramCounter]] (PC), [[StackPointer]] (SP), [[StatusRegister]] (SREG) with bits `I T H S V N Z C`.
- Separate Flash (program, non-volatile), SRAM (data, volatile), and EEPROM (user settings, non-volatile, byte-programmable). See [[FlashMemory]], [[SRAM]], [[EEPROM]].
- All peripheral registers are [[MemoryMappedIO|memory-mapped]] into the SRAM address space.

## Connections

- [[ATmega328P]] — the specific 328P chip on the Uno.
- [[AVR]] — the broader microcontroller family.
- [[ArduinoUno]] / [[ArduinoCC]] — the dev board and organization that popularized the chip.
- [[embedded-controllers-fiore]] — the textbook that traces register-level operation back to Atmel's datasheet.
