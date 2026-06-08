---
title: "Arduino"
type: entity
tags: [open-source, hardware, mcu, dev-board]
sources: [embedded-controllers-fiore, mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Arduino

Open-source hardware-and-software organization (arduino.cc) that designs, documents, and distributes a family of microcontroller development boards together with a cross-platform IDE, a C++-flavored Wiring library, and an extensive set of tutorials and reference documentation at `arduino.cc/en/Reference`. Both **hardware and software are open** — schematics, board layouts, and library source code are public. The Arduino [[ArduinoUno|Uno]] is the canonical hobbyist / pedagogical MCU dev board and the platform [[embedded-controllers-fiore]] uses throughout chapters 15–29.

Per [[embedded-controllers-fiore]]:

- The IDE runs on Windows, macOS, and Linux; command-line builds are possible.
- The Arduino runtime supplies a pre-written `main()` that calls user-defined `setup()` and `loop()` — embedded code is structured as those two entry points, not as classical `main`.
- The Wiring library wraps the [[AVR|AVR]] [[MemoryMappedIO|memory-mapped]] registers behind functions like `pinMode`, `digitalWrite`, `digitalRead`, `analogRead`, `analogWrite`, `delay`, `millis`. Fiore demonstrates that this wrapping is convenient but not free, and shows how to bypass it with direct register writes when speed or interrupt-safety matters.
- Inline assembly and direct register manipulation are explicitly permitted.

## Board family (selected, per [[embedded-controllers-fiore]])

- **Uno** — [[ATmega328P]] (8-bit AVR, 16 MHz, 32 k Flash / 2 k SRAM / 1 k EEPROM). The default reference board.
- **Mini / Nano** — same 328P-class chip, smaller form factor; the Nano has 8 ADC channels vs the Uno's 6.
- **Mega** — ATmega2560 (still 8-bit AVR); 16 analog channels; more I/O.
- **Due** — Atmel SAM3X8E, an **[[ARMCortexM|ARM Cortex-M3]]** part with two true 12-bit DACs. The only one of these where `analogWrite` produces an actual analog signal rather than [[PulseWidthModulation|PWM]].

## Connections

- [[ArduinoUno]] — the specific Uno reference board.
- [[ATmega328P]] / [[AVR]] / [[Atmel]] — the chip family Arduino is built on.
- [[TinyML]] / [[mlsysbook-ch02-ml-systems]] — mlsysbook Ch 2 cites the Arduino Nano 33 BLE Sense (256 KB RAM, 1 MB flash, 20–40 mW) as a representative TinyML developer kit.
- [[Microcontroller]] — the substrate Arduino boards are built around.
- [[embedded-controllers-fiore]] — the OER textbook teaching Arduino at the register level.
