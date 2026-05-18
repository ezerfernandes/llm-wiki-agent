---
title: "embedded-hal"
type: entity
tags: [rust, embedded, crate, traits, portability, hal]
sources: [rust-embedded-book-start-registers, rust-embedded-book-portability-index]
last_updated: 2026-05-16
---

# embedded-hal

`crates.io/crates/embedded-hal` — the **portability trait crate** that defines the common abstractions every [[HALCrate|HAL crate]] in the embedded-Rust ecosystem implements ([[rust-embedded-book-start-registers]], [[rust-embedded-book-portability-index]]). Maintained by the [[RustEmbeddedWorkingGroup]].

Defines hardware-agnostic traits — `digital::OutputPin`, `serial::Read` / `serial::Write`, `i2c::I2c`, `spi::SpiBus`, `delay::DelayNs`, etc. — so that driver crates and application code can be written **once** against the traits and compile against any chip whose HAL implements them. The *Portability* chapter ([[rust-embedded-book-portability-index]]) defines `embedded-hal` as *"a set of traits which define implementation contracts between HAL implementations, drivers and applications (or firmwares)"* and pins the architectural payoff as the **[[Portability|M·N → M+N collapse]]**: with M HAL implementations and N driver crates, the trait split collapses ecosystem complexity from M·N to M+N.

Named trait families per [[rust-embedded-book-portability-index]]: GPIO (input + output pins), serial, [[I2C]], [[SPI]], timers/countdowns, ADC.

## Connections

- [[HALCrate]] — every HAL crate implements `embedded-hal` traits; this is the contract.
- [[DriverCrate]] — driver crates depend on `embedded-hal` traits, not on a specific HAL implementation — the chip-agnostic side of the M·N → M+N collapse.
- [[Portability]] — the cross-chip-write-once goal `embedded-hal` exists to deliver — formalized in [[rust-embedded-book-portability-index]].
- [[HardwareAbstractionLayer]] — `embedded-hal` is the embedded-Rust ecosystem's trait-based realization of the HAL umbrella concept.
- [[RustEmbeddedWorkingGroup]] — maintains `embedded-hal`.
- [[PeripheralAccessCrate]] — the layer beneath HAL crates that the HAL wraps.
