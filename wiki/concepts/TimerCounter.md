---
title: "Timer / Counter"
type: concept
tags: [embedded, peripheral, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Timer / Counter

Hardware block in nearly every [[Microcontroller|MCU]] that increments a counter on every clock tick (or external pulse). Used to generate time delays, count external events, produce [[PulseWidthModulation|PWM]] waveforms, drive periodic [[InterruptServiceRoutine|interrupts]], time-stamp inputs, and synthesize software clocks like `millis()`. Independent of the CPU — runs in parallel and signals via [[Interrupt|interrupts]] when its count overflows or matches a compare value.

## ATmega 328P specifics (per [[embedded-controllers-fiore]] ch. 28)

Three blocks:

| Block | Width | Notes |
|---|---|---|
| TC0 | 8-bit | Used by Arduino runtime for `delay()` / `millis()` — risky to reprogram |
| TC1 | 16-bit | Also used by runtime — extended capabilities |
| TC2 | 8-bit | The "safe" one to reprogram by hand |

Each timer has:

- **`TCNTn`** — current count register (8 or 16 bits).
- **`OCRnA` / `OCRnB`** — output compare registers; trigger compare-match events when `TCNTn` equals their value.
- **`TCCRnA` / `TCCRnB`** — control registers.
- **`TIMSKn`** — interrupt mask register (`TOIEn` for overflow, `OCIEnA` / `OCIEnB` for compare-match).
- **`TIFRn`** — interrupt flag register.

### Waveform Generation Mode (WGM bits, spread across TCCRnA / TCCRnB)

| WGM | Mode |
|---|---|
| 000 | Normal — free-running count to 255 / 65535 then wrap |
| 001 | Phase Correct PWM, TOP = 0xFF |
| 010 | [[ClearTimerOnCompare\|CTC]] — reset on compare match with OCRnA |
| 011 | Fast PWM, TOP = 0xFF |
| 101 | Phase Correct PWM, TOP = OCRnA |
| 111 | Fast PWM, TOP = OCRnA |

### Prescaler (CS bits in TCCRnB)

| CS | Divide by |
|---|---|
| 000 | Stopped |
| 001 | 1 (no prescale) |
| 010 | 8 |
| 011 | 32 (TC2 only) |
| 100 | 64 |
| 101 | 128 (TC2 only) |
| 110 | 256 |
| 111 | 1024 |

At 16 MHz with the 1024× prescaler, an 8-bit timer overflows ~16 kHz / 256 ≈ 60 Hz — handy for "blink the LED" or accumulating slow events through a global counter incremented in the overflow ISR.

### Compare Output Mode (COM bits)

The COM bits decide what happens to the OCnx pin on a compare match: disconnected, toggle, clear, or set. The associated [[DataDirectionRegister|DDR]] bit must still be set to output, or no signal reaches the physical pin.

## Connections

- [[PulseWidthModulation]] — the most common timer use.
- [[ClearTimerOnCompare]] — fixed-frequency square-wave mode.
- [[InterruptServiceRoutine]] — overflow / compare-match interrupts.
- [[ATmega328P]] / [[ArduinoUno]] — the platform.
- [[embedded-controllers-fiore]] — the source.
