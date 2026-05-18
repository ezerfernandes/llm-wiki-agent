---
title: "HAL Crate (Hardware Abstraction Layer)"
type: concept
tags: [embedded, rust, crate-stack, embedded-hal, portability]
sources: [rust-embedded-book-start-registers]
last_updated: 2026-05-16
---

# HAL Crate (Hardware Abstraction Layer)

**Layer 3** of the embedded-Rust four-layer crate stack. Sits on top of a [[PeripheralAccessCrate|PAC]] and offers a **user-friendly, portable API** by implementing the common traits defined in [[EmbeddedHalCrate|`embedded-hal`]] ([[rust-embedded-book-start-registers]]).

A HAL typically defines a `constrain()` method (single peripherals) or `split()` method (e.g. GPIO ports with multiple pins) that **consumes** the underlying raw PAC peripheral struct and returns a new object with a higher-level API. Example: `tm4c123x_hal` exposes `Serial::uart0(p.UART0, tx_pin, rx_pin, …, baud_rate, …, &clocks, &sc.power_control)`.

## Zero-cost compile-time enforcement

The HAL exploits Rust's type system to make hardware-misconfiguration bugs **statically impossible** ([[rust-embedded-book-start-registers]]):

- The `Serial::new` constructor takes a borrow on a `Clock` struct, which can only be produced by *configuring the PLLs and freezing the clock setup*. **It is impossible to construct a Serial port without first having configured the clock rates** — the baud-rate-divisor miscalculation bug is unrepresentable.
- GPIO pins use [[TypeStateProgramming|type-state]]: each pin mode (Input, Output, AlternateFunctionN) is a distinct type. Passing a pin in the wrong mode to a peripheral constructor is a **compile error**.

> "All with no run-time cost!" — the chapter's framing of the HAL contract ([[rust-embedded-book-start-registers]]).

## Stack position

- **Below**: [[PeripheralAccessCrate|PAC]] (chip-specific MMIO wrapper).
- **Above**: [[BoardCrate|board crate]] (dev-board-specific pre-configuration).

## Connections

- [[EmbeddedHalCrate]] — the trait crate every HAL crate implements (the portability contract).
- [[PeripheralAccessCrate]] — sits below.
- [[BoardCrate]] — sits above.
- [[TypeStateProgramming]] — the design pattern HAL crates use for GPIO pin modes.
- [[Portability]] — the goal: write peripheral-agnostic application code against `embedded-hal` traits. Formalized as the M·N → M+N collapse in [[rust-embedded-book-portability-index]].
- [[DriverCrate]] — the chip-agnostic peer crate kind that depends on `embedded-hal` traits the HAL crate implements.
- [[HardwareAbstractionLayer]] — the umbrella concept; a HAL crate is the per-chip realization of it in Rust.
