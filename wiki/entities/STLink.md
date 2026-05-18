---
title: "ST-LINK"
type: entity
tags: [debug-probe, programmer, stm32, hardware, embedded]
sources: [rust-embedded-book-intro-hardware, rust-embedded-book-intro-tooling, rust-embedded-book-intro-install-linux]
last_updated: 2026-05-16
---

# ST-LINK

[[STMicroelectronics]]'s in-circuit programmer / debugger protocol and product family for STM32 (and STM8) [[Microcontroller|microcontrollers]]. Provides JTAG / SWD access to the target MCU over USB from a host PC, used to flash firmware and drive a debugger (GDB / probe-rs / OpenOCD).

On the [[STM32F3DISCOVERY]] board, an **on-board ST-LINK** is implemented by a dedicated [[STM32F103]] MCU wired to the "USB ST-LINK" Mini-USB port, so the board can be programmed and debugged directly over USB without an external debug probe ([[rust-embedded-book-intro-hardware]]). This integrated-debugger pattern is shared across the wider STMicroelectronics *Discovery* and *Nucleo* dev-board families and is one of the major reasons these boards are favored for embedded learning materials such as [[TheEmbeddedRustBook]].

## Connections

- [[STMicroelectronics]] — vendor / protocol owner.
- [[STM32F3DISCOVERY]] — board with on-board ST-LINK.
- [[STM32F103]] — the MCU that implements the on-board ST-LINK on the F3 board.
- [[STM32F303VCT6]] — the application MCU the on-board ST-LINK programs and debugs.
- [[JLink]] / [[MCULink]] / [[RustyProbe]] — alternative probes in the same slot in the embedded-Rust [[OnChipDebugging|on-chip-debugging]] stack ([[rust-embedded-book-intro-tooling]]).
- [[OpenOCD]] / [[ProbeRs]] — debug-server software the ST-LINK probe is driven by.
- [[GDB]] / [[ProbeRsVSCodeExtension]] — front-end debuggers that reach the target *through* ST-LINK + an OpenOCD / Probe-rs server.
- [[JTAG]] / [[SWD]] — wireline transports ST-LINK speaks to the target over.
- [[OnChipDebugging]] — the umbrella regime ST-LINK participates in.
- [[UdevRules]] — the Linux mechanism that grants non-root user access to the ST-LINK USB device on the [[STM32F3DISCOVERY]] ([[rust-embedded-book-intro-install-linux]]).
