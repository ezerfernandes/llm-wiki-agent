---
title: "Driver Crate"
type: concept
tags: [embedded, rust, crate-stack, embedded-hal, driver]
sources: [rust-embedded-book-portability-index]
last_updated: 2026-05-16
---

# Driver Crate

A **driver crate** in the embedded-Rust ecosystem implements a set of custom functionality for an **internal or external hardware component** — sensor, display, actuator — connected to a peripheral that implements [[EmbeddedHalCrate|`embedded-hal`]] traits ([[rust-embedded-book-portability-index]]). Together with [[HALCrate|HAL implementations]], driver crates are the second multiplicand in the [[Portability|M·N → M+N collapse]] that the `embedded-hal` trait crate exists to deliver.

## Definition

> *"A driver implements a set of custom functionality for an internal or external component, connected to a peripheral implementing the embedded-hal traits. Typical examples for such drivers include various sensors (temperature, magnetometer, accelerometer, light), display devices (LED arrays, LCD displays) and actuators (motors, transmitters)."* ([[rust-embedded-book-portability-index]]).

## The trait-bound generic pattern

A driver is **initialized with a peripheral instance whose type is bounded by an [[EmbeddedHalCrate|`embedded-hal`]] trait**. The driver itself is therefore **chip-agnostic**: it depends on the *trait* (e.g. `embedded_hal::i2c::I2c`, `embedded_hal::spi::SpiBus`, `embedded_hal::digital::OutputPin`), not on a specific HAL crate.

> *"A driver has to be initialized with an instance of type that implements a certain trait of the embedded-hal which is ensured via trait bound and provides its own type instance with a custom set of methods allowing to interact with the driven device."* ([[rust-embedded-book-portability-index]]).

Concrete examples (forward references from the corpus): the [[LSM303DLHC]] accel/mag driver takes an [[I2C]] bus; the [[L3GD20]] gyro driver takes an [[SPI]] bus. Either driver compiles unchanged against **any** HAL whose I2C/SPI implementation satisfies the corresponding `embedded-hal` trait.

## Three component categories

Per the chapter:

- **Sensors** — temperature, magnetometer, accelerometer, light.
- **Displays** — LED arrays, LCD displays.
- **Actuators** — motors, transmitters.

## Stack position

Sits **alongside** the [[HALCrate|HAL]] layer in dependency terms, not on top of it. A driver depends on the [[EmbeddedHalCrate|`embedded-hal`]] *traits* (a leaf, no-hardware-dependency dependency) and is composed into an application together with a HAL crate. Portable across every chip whose HAL satisfies the relevant traits — the **zero-cost-to-port** layer of the architecture (vs. the chip-specific HAL implementation and the wiring-specific application).

## Connections

- [[EmbeddedHalCrate]] — the trait crate every driver crate depends on (the contract).
- [[HALCrate]] — the layer the driver crate is **composed with** (not stacked on top of) at the application level.
- [[Portability]] — the architectural goal driver crates are the N-side of the M·N → M+N collapse for.
- [[I2C]] / [[SPI]] / [[GPIO]] — the most common `embedded-hal` trait families driver crates depend on.
- [[LSM303DLHC]] / [[L3GD20]] — concrete examples in the corpus (accel/mag and gyro on the [[STM32F3DISCOVERY]]).
- [[rust-embedded-book-portability-index]] — the chapter that names this concept.
