---
title: "USART"
type: concept
tags: [embedded, bus, hardware-interface, serial]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# USART

**Universal Synchronous / Asynchronous Receiver-Transmitter** — an MCU peripheral that drives a serial line (typically asynchronous, framed as start-bit + 8 data bits + optional parity + stop-bit at a configured baud rate). The asynchronous-only subset is what most people call **UART**. On a [[Microcontroller|MCU]], a USART peripheral lets firmware send and receive bytes over two wires (TX + RX), commonly used for debug logging, GPS receivers, RS-232 / RS-485 industrial links, and host-PC consoles over a USB-to-serial bridge.

The [[STM32F303VCT6]] on the [[STM32F3DISCOVERY]] integrates USART blocks ([[rust-embedded-book-intro-hardware]]), and the previous chapter listed serial / UART alongside [[I2C]] and [[SPI]] as a prerequisite "common interface" the embedded-experienced reader should already know ([[rust-embedded-book-intro-index]]).

## Connections

- [[Microcontroller]] — USART is a canonical integrated peripheral.
- [[STM32F303VCT6]] — exposes USART blocks on the [[STM32F3DISCOVERY]].
- [[GPIO]] — USART TX/RX lines are pin-muxed onto GPIO pads.
- [[I2C]] / [[SPI]] — sibling serial-bus peripherals; SPI is *synchronous* with separate clock, USART can do either, I2C is multi-drop addressed.
