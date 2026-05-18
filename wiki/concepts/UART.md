---
title: "UART"
type: concept
tags: [embedded, bus, hardware-interface, serial, acronym]
sources: [rust-embedded-book-appendix-glossary, rust-embedded-book-intro-hardware, rust-embedded-book-intro-index]
last_updated: 2026-05-16
---

# UART — Universal Asynchronous Receiver-Transmitter

**UART** = *Universal Asynchronous Receiver-Transmitter*. The asynchronous-only subset of a [[USART]] — a [[Microcontroller|microcontroller]] peripheral that drives a serial line (typically start-bit + 8 data bits + optional parity + stop-bit at a configured baud rate) over **two wires** (TX + RX, plus ground) with **no shared clock**.

*[[TheEmbeddedRustBook]]*'s glossary lists UART as a standalone entry ([[rust-embedded-book-appendix-glossary]]) alongside the [[USART]] superset — both reference Wikipedia for the protocol details.

## UART vs USART

| Aspect | **UART** | **[[USART]]** |
|---|---|---|
| Synchronous mode | no | yes (separate clock line) |
| Asynchronous mode | yes | yes |
| Wires (data) | 2 (TX, RX) | 2–3 (TX, RX, optional CLK) |
| Typical use | debug logging, GPS, RS-232 / RS-485, USB-serial bridges | same + synchronous links to other clock-disciplined peripherals |

A USART peripheral can always be **configured to act as a UART** (clock disabled, asynchronous framing). Most MCU vendors expose USART blocks even when "UART" is what 99% of users will configure — the [[STM32F303VCT6]] on the [[STM32F3DISCOVERY]] is the canonical example ([[rust-embedded-book-intro-hardware]]).

## Position in the embedded book

The [[rust-embedded-book-intro-index|Introduction chapter]] lists serial / UART alongside [[I2C]] and [[SPI]] as a prerequisite "common interface" the embedded-experienced reader should already know — i.e. the book assumes UART literacy and does not teach the protocol itself.

## Connections

- [[USART]] — superset peripheral (synchronous + asynchronous modes); UART is the asynchronous-only subset.
- [[Microcontroller]] — UART / USART is a canonical integrated peripheral.
- [[STM32F303VCT6]] — exposes USART blocks on the [[STM32F3DISCOVERY]] that can be configured as UART.
- [[GPIO]] — UART TX/RX lines are pin-muxed onto GPIO pads.
- [[I2C]] — sibling serial-bus peripheral; multi-drop, addressed, synchronous (with clock line).
- [[SPI]] — sibling serial-bus peripheral; synchronous (with explicit clock line), point-to-point with chip-select.
- [[rust-embedded-book-appendix-glossary]] — source for this acronym entry.
- [[rust-embedded-book-intro-hardware]] — F3-Discovery hardware tour lists USART blocks.
- [[rust-embedded-book-intro-index]] — lists UART as an assumed-prerequisite interface.
- [[TheEmbeddedRustBook]] — parent book.
