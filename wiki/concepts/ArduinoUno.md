---
title: "Arduino Uno"
type: concept
tags: [embedded, mcu, dev-board, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Arduino Uno

Reference [[Arduino]] development board built around the [[ATmega328P]] [[AVR]] 8-bit microcontroller. Pedagogical default for the entire embedded chapters of [[embedded-controllers-fiore]] and the most common Arduino board in tutorials, hobby projects, and education.

## Headline specs (per [[embedded-controllers-fiore]] ch. 17)

- **MCU**: ATmega328P — 8-bit AVR, [[HarvardArchitecture|Harvard architecture]], [[RISC]], pipelined; 16 MHz clock; 32 general-purpose 8-bit registers.
- **Memory**: 32 k [[FlashMemory|Flash]] (program), 2 k [[SRAM]] (data), 1 k [[EEPROM]] (user settings).
- **I/O ports**: three GPIO ports — B (8 bits, PB0–PB7), C (7 bits, PC0–PC6), D (8 bits, PD0–PD7).
- **Pin mapping** (Uno designator → AVR port / bit):
  - A0–A5 → PORTC bits 0–5 (also ADC channels 0–5)
  - 0, 1 → PORTD bits 0, 1 (USART RX / TX)
  - 2–7 → PORTD bits 2–7 (3, 5, 6 are [[PulseWidthModulation|PWM]]-capable)
  - 8–13 → PORTB bits 0–5 (9, 10, 11 are PWM-capable; **13 has a hardwired on-board LED** and is reduced as a digital input)
- **ADC**: single 10-bit successive-approximation [[ADC]], multiplexed across A0–A5, ~15 kSPS, internal 1.1 V or external AREF reference. See [[analogRead]].
- **Timers**: three [[TimerCounter|timer/counters]] — TC0 (8-bit, used by `delay()`/`millis()`), TC1 (16-bit), TC2 (8-bit, the "safe" one to reprogram). Six [[PulseWidthModulation|PWM]] outputs (OC0A→pin 6, OC0B→pin 5, OC1A→pin 9, OC1B→pin 10, OC2A→pin 11, OC2B→pin 3).
- **Serial**: USART (also used by USB-to-serial bridge for IDE upload + Serial Monitor), SPI, TWI/I²C.
- **Interrupts**: multiple levels, internal + external; reset button on-board.
- **Power**: USB (≤ 500 mA enumerated, ≤ 100 mA un-enumerated), external wall-wart, or regulated 5 V input. Per-pin sink/source 40 mA; whole-chip 200 mA total — driving anything bigger than a small LED needs an external driver transistor.

## Connections

- [[ATmega328P]] — the MCU.
- [[Arduino]] — the platform family.
- [[Atmel]] — the chip designer.
- [[AVR]] — the architecture family.
- [[GPIO]] — the I/O paradigm; on Uno: DDRB/PORTB/PINB, DDRC/PORTC/PINC, DDRD/PORTD/PIND.
- [[embedded-controllers-fiore]] — the source.
