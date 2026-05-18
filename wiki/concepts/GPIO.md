---
title: "GPIO"
type: concept
tags: [embedded, hardware, peripheral, mcu]
sources: [rust-embedded-book-intro-hardware, rust-embedded-book-design-patterns-hal-gpio, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# GPIO

**General-Purpose Input / Output** — the most basic [[Microcontroller|MCU]] peripheral: a bank of digital pins that firmware can individually configure as input or output, read as a logic level (0 / 1), or drive high / low. On [[ARMCortexM|Cortex-M]] MCUs, GPIO banks are exposed via [[MemoryMappedIO|memory-mapped]] registers (mode, output-data, input-data, pull-up/pull-down, alternate-function-mux, etc.). The [[STM32F3DISCOVERY]] exposes the [[STM32F303VCT6]]'s GPIO pins through two header rows along the board's edges ([[rust-embedded-book-intro-hardware]]).

In Rust, GPIO is canonically the *first* peripheral a learner touches ("blinky" — toggle an LED) and is also the textbook example of type-state HAL design: each pin has compile-time-tracked mode (`Input<Floating>`, `Output<PushPull>`, `Alternate<AF7>`, …) so misuse is a type error rather than a silent runtime fault.

## On 8-bit AVR (per [[embedded-controllers-fiore]])

The [[ATmega328P]] uses a three-register-per-port pattern that's common on 8-bit MCUs:

- **[[DataDirectionRegister|DDRx]]** — direction (1 = output, 0 = input).
- **[[PortRegister|PORTx]]** — output-data latch (also engages internal [[PullUpResistor|pull-up]] when bit is in input mode).
- **[[PinRegister|PINx]]** — read the physical pin level (after a [[SchmittTrigger]]).

Mnemonic: **"o" in PORT = output, "in" in PIN = input.**

Same physical block (DDR flip-flop + PORT flip-flop + tri-state buffer + pull-up MOSFET + Schmitt trigger) sits under both the AVR's raw register interface and the Cortex-M's `PinTypeState` API — the Rust type-state machinery encodes the DDR / PORT state into the type, while the AVR C convention encodes it into a register that the programmer must read/write correctly.

## Connections

- [[Microcontroller]] — GPIO is the universal MCU peripheral.
- [[MemoryMappedIO]] — how GPIO registers are accessed from firmware.
- [[STM32F303VCT6]] — the MCU whose GPIO pins are exposed on the [[STM32F3DISCOVERY]] headers.
- [[I2C]] / [[SPI]] / [[USART]] — GPIO pins are typically multiplexed into these alternate-function peripherals via the pin-mux.
- [[PinTypeState]] / [[ErasedPin]] — the canonical [[HALCrate|HAL]]-design patterns (`C-PIN-STATE` / `C-ERASED-PIN`) for pin APIs, per [[rust-embedded-book-design-patterns-hal-gpio]]. Pin typestate makes mode-misuse a compile error; type erasure trades compile-time-pin-distinctness for heterogeneous-collection-ability.
