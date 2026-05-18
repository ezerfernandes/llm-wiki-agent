---
title: "Arduino (Platform)"
type: concept
tags: [embedded, mcu, open-source, dev-board, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Arduino

Open-source [[Microcontroller|MCU]] development platform — a family of boards built around primarily [[Atmel|Atmel]] [[AVR]] 8-bit MCUs (Uno / Mini / Nano / Mega) and a smaller line of [[ARMCortexM|ARM Cortex-M]]–based boards (Due, MKR series) — plus a cross-platform IDE, a C++-flavored "Wiring" library, a bootloader, and reference documentation at `arduino.cc/en/Reference`. Both hardware and software are open; schematics are public, and the runtime library source is the basis for the chapter-by-chapter "what's under the hood" tours in [[embedded-controllers-fiore]].

## Programming model

Per [[embedded-controllers-fiore]] ch. 18: the Arduino runtime ships a pre-written `main()` that calls two user-supplied entry points:

```c
void setup(void);  // run once at boot — initialize peripherals
void loop(void);   // run forever — the event loop
```

`setup()` typically calls `pinMode()` to set [[DataDirectionRegister|DDR]] bits, configures [[TimerCounter|timer/counters]] for [[PulseWidthModulation|PWM]] / [[Interrupt|interrupts]], and enables [[ADC|ADC]] subsystems. `loop()` polls inputs and drives outputs. If interrupts are used, [[InterruptServiceRoutine|ISRs]] register via the `ISR(VECTOR_vect)` macro outside both functions; the runtime calls `sei()` so the global interrupt-enable bit is already set.

## Wiring library — the convenient layer

The core functions Fiore dissects in chapters 21–29:

| Function | Maps to | Notes |
|---|---|---|
| `pinMode(pin, INPUT/OUTPUT/INPUT_PULLUP)` | DDRx bit + PORTx bit | Three-mode wrapper; INPUT_PULLUP enables the on-chip pull-up. |
| `digitalWrite(pin, HIGH/LOW)` | PORTx bit | Disables any associated PWM timer first. |
| `digitalRead(pin)` | PINx bit | Read goes through a [[SchmittTrigger]]. |
| `analogRead(pin)` | [[ADC|ADC]] subsystem (`ADMUX` + `ADCSRA`) | 10-bit, ~100 µs, returns 0–1023. |
| `analogReference(type)` | `REFS` bits of `ADMUX` | DEFAULT (5 V) / INTERNAL (1.1 V) / EXTERNAL (AREF). |
| `analogWrite(pin, val)` | OCnx + `TCCRnA/B` | [[PulseWidthModulation|PWM]] at ~490 Hz; six PWM pins (3/5/6/9/10/11). |
| `delay(ms)` / `delayMicroseconds(us)` | TC0 overflow + busy wait | Long `delay()` blocks `loop()` — preferred alternative is `millis()`. |
| `millis()` / `micros()` | TC0 + interrupt counter | Non-blocking elapsed time. |
| `map(x, fromLo, fromHi, toLo, toHi)` | Pure C | Integer rescale, useful with `analogRead` results. |

The library's design is **convenience over speed**. Fiore shows that `digitalWrite(8, HIGH)` decodes the Arduino pin number into a port + bit through a lookup table, disables any active PWM, saves/clears/restores SREG, and only then sets the bit — many times slower than the equivalent `PORTB |= 0x01;`.

## Connections

- [[ArduinoUno]] — the reference board.
- [[ATmega328P]] — the chip on the Uno.
- [[ArduinoCC]] — the organization.
- [[Microcontroller]] — what the platform programs.
- [[BareMetalProgramming]] — the regime; Arduino is bare-metal even though it feels less so than [[TheEmbeddedRustBook|Rust on Cortex-M]].
- [[embedded-controllers-fiore]] — the OER textbook that walks the library source.
