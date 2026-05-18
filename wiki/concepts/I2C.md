---
title: "I2C"
type: concept
tags: [embedded, bus, hardware-interface]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# I2C

**Inter-Integrated Circuit** — multi-drop, two-wire (SDA + SCL) synchronous serial bus, originally designed by Philips. Common for connecting [[Microcontroller|microcontrollers]] to sensors, EEPROMs, and other low-bandwidth peripherals. Addressed (7-bit or 10-bit), with one master initiating transfers to addressed slaves. Listed by [[TheEmbeddedRustBook]] as a prerequisite "common interface" the embedded-experienced reader should already know ([[rust-embedded-book-intro-index]]).

A concrete instance on the [[STM32F3DISCOVERY]]: the on-board [[LSM303DLHC]] (accelerometer + magnetometer) is read by the [[STM32F303VCT6]] over I2C ([[rust-embedded-book-intro-hardware]]).

## Connections

- [[EmbeddedSystems]] — I2C is a canonical peripheral interconnect in embedded designs.
- [[Microcontroller]] — MCUs ship dedicated I2C peripheral blocks.
- [[SPI]] — sibling bus, generally faster and lower-latency, four-wire.
- [[LSM303DLHC]] — F3 sensor chip read over I2C.
