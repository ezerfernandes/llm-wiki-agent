---
title: "System on a Chip (SoC)"
type: concept
tags: [systems, hardware, integration, soc]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# System on a Chip (SoC)

A **system on a chip (SoC)** is an integrated circuit that combines on a single die what used to occupy multiple physically separate chips on a motherboard — at minimum a [[CPU]] and [[RAM]], commonly also a GPU, network/modem, and various peripheral controllers.

[[DiveIntoSystems]] Ch 0 cites the SoC as the integration trend that enables modern smartphones and [[SingleBoardComputer|single-board computers]] like the [[RaspberryPi]] to function as full [[ComputerSystem|computer systems]] in a form factor smaller than a credit card.

## Why SoCs matter for the systems story

- They are the physical substrate of contemporary mobile and embedded-class general-purpose computing.
- They package the [[MemoryHierarchy|memory hierarchy]] very tightly — RAM on the same chip as the CPU changes latency/bandwidth tradeoffs.
- They are almost always [[MulticoreProcessor|multicore]].

## Connections

- [[ComputerHardware]] — SoCs are a hardware integration pattern.
- [[CPU]] / [[RAM]] / [[MulticoreProcessor]] — SoC ingredients.
- [[SingleBoardComputer]] / [[RaspberryPi]] — board-level form factors built around an SoC.
- [[ComputerSystem]] — what an SoC + OS adds up to.
- [[dis-0-introduction]] — source.
