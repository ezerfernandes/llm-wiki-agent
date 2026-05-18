---
title: "Single-Board Computer"
type: concept
tags: [systems, hardware, sbc]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# Single-Board Computer (SBC)

A **single-board computer (SBC)** is a complete [[ComputerSystem|computer system]] built on a single printed circuit board — [[CPU]] (typically a [[SystemOnAChip|SoC]]), [[RAM]], storage interfaces, I/O, networking, and power management all on one board.

[[DiveIntoSystems]] Ch 0 cites SBCs as a key data point in the miniaturization story: the [[RaspberryPi]] is the canonical example of a credit-card-sized board running a general-purpose [[OperatingSystem|OS]] on a [[MulticoreProcessor|multicore SoC]] — fully a computer system by the book's definition.

## Distinguishing from microcontrollers

The line between an SBC and a microcontroller board is the presence of an OS and a full memory hierarchy. The [[RaspberryPi]] runs Linux; an [[STM32F3DISCOVERY]] runs `no_std` firmware. By [[dis-0-introduction]]'s definition, the former is a computer system and the latter is not.

## Connections

- [[RaspberryPi]] — canonical example.
- [[SystemOnAChip]] — the chip the SBC is built around.
- [[ComputerSystem]] — what an SBC + OS amounts to.
- [[Microcontroller]] — the non-OS counterpart.
- [[dis-0-introduction]] — source.
