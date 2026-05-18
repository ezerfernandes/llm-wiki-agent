---
title: "Pulse Width Modulation (PWM)"
type: concept
tags: [embedded, peripheral, analog, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Pulse Width Modulation

Technique for synthesizing a controllable *average* voltage (or current, or power) from a fixed-amplitude digital pin by rapidly toggling it between HIGH and LOW with a controlled **duty cycle** — the fraction of each period spent HIGH. Used wherever an [[Microcontroller|MCU]] needs analog-like output but the chip has no [[DAC|DAC]]: LED dimming, motor speed, resistive heater control, servo position, audio synthesis (with low-pass reconstruction).

The intuition Fiore offers (ch. 27): *area under the curve*. A 5 V pulse that's high 50 % of the time averages 2.5 V. If the pulse rate is fast enough relative to the load's response time, the load sees the average — an LED's brightness or a motor's torque tracks the duty cycle directly. For loads with sharper time response (audio, RF), you add a low-pass filter to extract the smoothed signal.

## On the ATmega 328P / Arduino Uno (per [[embedded-controllers-fiore]] ch. 27–28)

- **6 PWM-capable pins**: 3, 5, 6, 9, 10, 11 (marked with `~` on the Uno silkscreen). Mapped to the six OCnx outputs of the three [[TimerCounter|timer/counters]]:
  - OC0A → pin 6, OC0B → pin 5 (TC0)
  - OC1A → pin 9, OC1B → pin 10 (TC1)
  - OC2A → pin 11, OC2B → pin 3 (TC2)
- **`analogWrite(pin, val)`** API. `val` is `0..255`, **not** `0..100`, because the 8-bit hardware counters naturally count to 255.
- **~490 Hz** default frequency.
- **Two modes** available per timer in `TCCRnA`:
  - **Fast PWM** — single-slope counter from BOTTOM (0) up to TOP, then wraps. OCnx flips at the OCRnA/B compare-match.
  - **Phase-Correct PWM** — dual-slope counter (0→TOP→0); slower (half the frequency) but with no phase shift as the duty cycle changes. Preferred for motor control.
- On the [[Arduino]] Due (Atmel SAM3X8E, [[ARMCortexM|ARM Cortex-M3]]), `analogWrite()` on pins DAC0 / DAC1 produces *real* analog from the two internal 12-bit DACs — PWM only on the other pins.

## Setting up PWM by hand

`analogWrite()` works on 6 pre-configured pins. To generate PWM on an arbitrary pin (e.g., for "hand-wrought" PWM on Uno pin 8 / PORTB.0), Fiore ch. 29 uses a [[TimerCounter|timer]] overflow [[InterruptServiceRoutine|ISR]]:

```c
ISR(TIMER2_OVF_vect) {
    if (PORTB & ARBPINMASK)
        TCNT2 = OVF_COUNT_START;       // high half
    else
        TCNT2 = 255 - OVF_COUNT_START; // low half
    PORTB ^= ARBPINMASK;               // toggle
}
```

Asymmetric overflow restarts produce the duty cycle; the ISR runs at every wrap.

## Connections

- [[TimerCounter]] — the hardware that generates PWM.
- [[DAC]] — the alternative for true analog output.
- [[ADC]] — the inverse direction.
- [[ATmega328P]] / [[ArduinoUno]] — the platform.
- [[embedded-controllers-fiore]] — the source.
