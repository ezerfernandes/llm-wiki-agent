---
title: "SPI"
type: concept
tags: [embedded, bus, hardware-interface]
sources: [rust-embedded-book-intro-index, rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# SPI

**Serial Peripheral Interface** — full-duplex, four-wire (MOSI / MISO / SCK / CS) synchronous serial bus. Higher bandwidth and lower latency than [[I2C]] at the cost of more pins per slave (one chip-select line per slave). Common for connecting [[Microcontroller|microcontrollers]] to flash chips, displays, and higher-bandwidth sensors. Listed by [[TheEmbeddedRustBook]] as a prerequisite "common interface" for the embedded-experienced reader ([[rust-embedded-book-intro-index]]).

A concrete instance on the [[STM32F3DISCOVERY]]: the on-board [[L3GD20]] gyroscope is read by the [[STM32F303VCT6]] over SPI ([[rust-embedded-book-intro-hardware]]).

## Connections

- [[EmbeddedSystems]] — SPI is a canonical embedded peripheral bus.
- [[Microcontroller]] — MCUs ship dedicated SPI controller blocks.
- [[I2C]] — sibling bus, slower but multi-drop with only two wires.
- [[L3GD20]] — F3 gyroscope chip read over SPI.
