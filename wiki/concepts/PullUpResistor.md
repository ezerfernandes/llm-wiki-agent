---
title: "Pull-Up Resistor"
type: concept
tags: [embedded, gpio, electronics, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Pull-Up Resistor

Resistor connecting a digital input pin to the positive supply rail (typically through a few tens of kΩ) so that **when no active driver pulls the pin low, the input reads as logic HIGH**. The default-state hardware that makes "a switch between the pin and ground" a usable input — when the switch is open, the resistor pulls the pin to V_CC; when the switch closes, the pin is dragged to GND.

[[Microcontroller|MCUs]] usually provide *internal* pull-ups so external resistors aren't needed.

## On the AVR (per [[embedded-controllers-fiore]] ch. 20 / 21)

The internal pull-up on each [[GPIO]] pin of the [[ATmega328P]] is a MOSFET-switched ~20 kΩ resistor, enabled by writing **DDR=0 (input mode) AND PORT=1**. The control gate that activates the MOSFET is fed by AND(¬DDR, PORT) — clever reuse of the otherwise-unused PORT bit in input mode.

```c
// Arduino library way:
pinMode(2, INPUT_PULLUP);

// Direct register way:
DDRD &= ~(1 << PD2);   // input mode
PORTD |=  (1 << PD2);  // engage pull-up
```

Reading back without a pull-up *or* an active external driver gives **floating input** — the pin's level is determined by stray capacitance and the [[SchmittTrigger]] threshold, producing random / noisy reads. Most input designs need either a pull-up or pull-down resistor.

## Pin-13 caveat

Arduino digital pin 13 has an on-board LED with series resistor soldered to it. Engaging the 20 kΩ pull-up on this pin via `INPUT_PULLUP` produces a voltage divider with the LED's series resistor, yielding only ~1.7 V — below the logic-HIGH threshold, so pin 13 in `INPUT_PULLUP` always reads LOW. If you must use pin 13 as a digital input, supply an external pull-**down** resistor instead.

## Connections

- [[GPIO]] / [[DataDirectionRegister]] / [[PortRegister]] — the registers that configure pull-ups.
- [[SchmittTrigger]] — the next stage that reads the resulting voltage.
- [[ATmega328P]] / [[ArduinoUno]] — the platform.
- [[embedded-controllers-fiore]] — the source.
