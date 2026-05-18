---
title: "tm4c123x"
type: entity
tags: [rust, embedded, crate, pac, tiva-c, texas-instruments]
sources: [rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# tm4c123x

`crates.io/crates/tm4c123x` — the [[PeripheralAccessCrate|Peripheral Access Crate]] for the **Texas Instruments Tiva-C TM4C123 series** of [[ARMCortexM|Cortex-M4]] microcontrollers (80 MHz / 256 KiB Flash). Auto-generated from TI's SVD by [[Svd2Rust|`svd2rust`]] ([[rust-embedded-book-start-registers]]).

The book's **worked PAC example** — used throughout the [[rust-embedded-book-start-registers|Registers chapter]] to demonstrate the `read()` / `write()` / `modify()` closure idiom:

```rust
let p = tm4c123x::Peripherals::take().unwrap();
let pwm = p.PWM0;
pwm.ctl.write(|w| w.globalsync0().clear_bit());
pwm._2_ctl.write(|w| w.enable().set_bit().mode().set_bit());
pwm._2_load.write(|w| unsafe { w.load().bits(263) });
```

The companion HAL crate is `tm4c123x-hal` (one layer up in the stack, implementing the [[EmbeddedHalCrate|`embedded-hal`]] traits).

## Connections

- [[PeripheralAccessCrate]] — `tm4c123x` is the chapter's worked example.
- [[Svd2Rust]] — the generator that produced it.
- [[HALCrate]] — `tm4c123x-hal` is the partner HAL crate.
