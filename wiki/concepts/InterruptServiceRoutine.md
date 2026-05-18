---
title: "Interrupt Service Routine (ISR)"
type: concept
tags: [embedded, interrupt, mcu, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Interrupt Service Routine

Short function that the CPU executes in response to an [[Interrupt|interrupt]] — an asynchronous event (pin state change, timer overflow, ADC conversion complete, serial byte received) that should pre-empt the main program. The CPU saves enough state to return later, jumps to the ISR's address via a [[VectorTable|vector table]] indirection, runs the ISR, then resumes the interrupted code.

The C-level counterpart of Rust's `#[interrupt]` attribute (see [[InterruptAttribute]]).

## On the ATmega 328P (per [[embedded-controllers-fiore]] ch. 29)

26 predefined vectors — names in `iom328p.h`:

```c
INT0_vect           // External Interrupt Request 0
INT1_vect           // External Interrupt Request 1
PCINT0_vect / 1 / 2 // Pin-Change Interrupts
WDT_vect            // Watchdog Time-out
TIMER2_COMPA_vect
TIMER2_COMPB_vect
TIMER2_OVF_vect
TIMER1_CAPT_vect
TIMER1_COMPA_vect / COMPB_vect / OVF_vect
TIMER0_COMPA_vect / COMPB_vect / OVF_vect
SPI_STC_vect
USART_RX_vect / UDRE_vect / TX_vect
ADC_vect
EE_READY_vect
ANALOG_COMP_vect
TWI_vect
SPM_READY_vect
```

User code installs a handler by writing:

```c
ISR(TIMER2_OVF_vect) {
    // … short body …
}
```

The `ISR(...)` macro expands into a function with the right name, calling convention, and `__attribute__((signal))` so the AVR-GCC emits register-save / `RETI` boilerplate, and the build system wires the vector-table entry at link time. **No function prototype needed; no manual vector-table edits.**

## Enable mechanics (two layers)

1. **Per-source enable**: the appropriate bit in the appropriate mask register — `EIMSK` for external pin interrupts, `TIMSKn` for timer-n interrupts, `ADCSRA.ADIE` for ADC, etc.
2. **Global enable**: the `I` bit in [[StatusRegister|SREG]] — set with `sei()`, cleared with `cli()`. The Arduino runtime calls `sei()` for you.

For an external pin (e.g. `INT0` on Uno pin 2 / PORTD.2), additionally choose the edge via `EICRA` (`ISC01:ISC00` = `00` low-level, `01` any change, `10` falling edge, `11` rising edge).

## Rules of engagement

- **Keep ISRs short.** Long ISRs delay other interrupts and starve the main loop. Defer heavy work to the loop by setting a flag (`volatile uint8_t event_pending`).
- **`SREG` is *not* auto-saved on entry** — the AVR-GCC `ISR` macro saves it for you, but if you write the ISR manually in C or assembly you must do it yourself.
- **Variables shared with main code must be `volatile`** — otherwise the optimizer caches them in registers and misses ISR-side updates.
- **Atomic access for multi-byte shared variables** — use `cli()` / `sei()` brackets or `ATOMIC_BLOCK` to read a 16-bit counter without an interrupt mid-read.
- **`loop()` can be empty** when all work happens in ISRs — and often is in Fiore's examples.

## Connections

- [[Interrupt]] — the asynchronous event itself.
- [[InterruptAttribute]] — the Rust counterpart.
- [[VectorTable]] — the indirection table.
- [[StatusRegister]] — the global enable bit.
- [[TimerCounter]] / [[ADC]] / [[ExternalInterrupt]] — common interrupt sources.
- [[embedded-controllers-fiore]] — the source.
