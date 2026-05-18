---
title: "Analog-to-Digital Converter (ADC)"
type: concept
tags: [embedded, peripheral, analog, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# ADC

**Analog-to-Digital Converter** — a peripheral that samples a continuously variable input voltage and produces an integer-valued representation. The mechanism for embedded firmware to read sensors (temperature, light, force, microphone, potentiometer) into a digital domain it can compute on. Almost every [[Microcontroller|MCU]] has one or more ADC channels; the [[ATmega328P]] used in the [[ArduinoUno|Arduino Uno]] has a single 10-bit successive-approximation ADC multiplexed across 6 channels.

## ATmega 328P specifics (per [[embedded-controllers-fiore]] ch. 25–26)

| Property | Value |
|---|---|
| Resolution | 10 bits → 1024 levels |
| Channels | 6 on Uno (8 on Mini/Nano, 16 on Mega) |
| Max rate | ~15 kSPS (1 conversion ≈ 13 ADC clocks + 25 for init) |
| Reference | Internal 1.1 V, AVCC, or external AREF pin |
| Resolution @ 5 V | ~4.9 mV per LSB |
| Source impedance | Optimized for ≤ 10 kΩ |
| Polarity | Unipolar — positive only; bipolar signals need DC-shifting |
| Accuracy | ±0.5 LSB integral nonlinearity, ±2 LSB absolute |

The peripheral has its own input multiplexer that also gives access to an internal **temperature sensor** (channel 1000) and the **1.1 V bandgap** (channel 1110) for self-calibration.

## Programming registers

- **`ADCSRA`** — control / status A:
  - `ADEN` enable
  - `ADSC` start conversion (auto-cleared when complete)
  - `ADATE` auto-trigger enable
  - `ADIF` interrupt flag
  - `ADIE` interrupt enable
  - `ADPS2:0` prescaler bits (must yield 50–200 kHz ADC clock)
- **`ADCSRB`** — control / status B (auto-trigger source `ADTS2:0`, analog-comparator mux `ACME`).
- **`ADMUX`** — multiplexer + reference + justification:
  - `REFS1:0` — 00=AREF, 01=AVCC, 10=reserved, 11=internal 1.1 V
  - `ADLAR` — left-justify if set (high 8 bits in ADCH, low 2 in ADCL)
  - `MUX3:0` — channel select
- **`ADCH:ADCL`** — 16-bit result. **Must read `ADCL` first** — that read locks both registers so the hardware doesn't overwrite mid-read; reading `ADCH` then unlocks.

## Single-conversion code (from `wiring_analog.c`)

```c
int analogRead(uint8_t pin) {
    if (pin >= 14) pin -= 14;  // channel or pin numbers
    ADMUX = (analog_reference << 6) | (pin & 0x07);
    sbi(ADCSRA, ADSC);                       // start
    while (bit_is_set(ADCSRA, ADSC));        // busy-wait
    uint8_t low = ADCL;
    uint8_t high = ADCH;
    return (high << 8) | low;
}
```

## Sensor-mapping recipe

To use a sensor whose output spans only part of the 0–5 V range, [[embedded-controllers-fiore]] ch. 26 recommends an external op-amp signal-conditioning stage to scale onto 0–5 V, then a simple integer affine map in software:

```c
// av = analogRead() result, dv = displayed value
dv = (short)(32 + 180L * (long)(av - 205) / 409);  // 32–212 °F mapping
```

The `long` cast inside avoids overflow during multiply; doing integer divide *last* preserves precision.

## Connections

- [[ATmega328P]] — the host MCU.
- [[analogRead]] — the Arduino wrapper.
- [[PulseWidthModulation]] — the inverse direction (digital-→-analog via duty cycle).
- [[InterruptServiceRoutine]] — the `ADC_vect` interrupt for free-running / async modes.
- [[embedded-controllers-fiore]] — the source.
