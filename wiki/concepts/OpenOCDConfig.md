---
title: "OpenOCD Configuration (`openocd.cfg`)"
type: concept
tags: [openocd, embedded, debugging, configuration]
sources: [rust-embedded-book-start-hardware]
last_updated: 2026-05-16
---

# OpenOCD Configuration (`openocd.cfg`)

A small Tcl-syntax file consumed by [[OpenOCD]] at startup that declares **two paired things**: which hardware **interface** (debug probe) is attached, and which **target** (MCU family) sits on the other end of it. [[OpenOCD]] picks the file up automatically when invoked from the directory containing it (or via `-f openocd.cfg`); the [[CortexMQuickstartTemplate|`cortex-m-quickstart`]] template ships a working one at project root.

## The two-cfg pairing

```tcl
# interface: which hardware probe is plugged in
source [find interface/stlink.cfg]
# target: which MCU is on the other end
source [find target/stm32f3x.cfg]
```

The `find` Tcl command resolves the file against OpenOCD's bundled cfg directory tree (`/usr/share/openocd/scripts/` on Linux; the same `interface/` + `target/` hierarchy on every platform). OpenOCD ships hundreds of interface cfgs (one per probe variant) and hundreds of target cfgs (one per MCU family) — the pairing is what configures a session.

## Interface cfgs for the [[STM32F3DISCOVERY]]

The F3 board ships two hardware revisions, each requiring a different interface cfg:

- **Revision C (newer)** — `interface/stlink.cfg`
- **Revisions A and B (older)** — `interface/stlink-v2.cfg`

The user determines which revision they have during the [[rust-embedded-book-intro-verify|verify]] step, then uncomments the matching `source` line.

## Target cfg

`target/stm32f3x.cfg` covers the entire STM32F3 family (including the [[STM32F303VCT6]] on the F3 board). One cfg per MCU **family**, not per part number — pin-compatible variants share a cfg.

## Connections

- [[OpenOCD]] — the consumer of `openocd.cfg`.
- [[STLink]] — the [[STM32F3DISCOVERY]]'s built-in probe; the interface cfg names its protocol variant.
- [[STM32F303VCT6]] — the MCU the F3's target cfg drives.
- [[STM32F3DISCOVERY]] — the reference board.
- [[CortexMQuickstartTemplate]] — ships the F3-specific `openocd.cfg` example.
- [[rust-embedded-book-start-hardware]] — chapter where the pairing pattern is introduced.
- [[rust-embedded-book-intro-verify]] — earlier chapter where the user runs `openocd -f interface/stlink.cfg -f target/stm32f3x.cfg` directly (via `-f` flags) before learning the config-file form.
- [[GDB]] — connects to OpenOCD on TCP 3333 once OpenOCD's config has brought up the probe.
