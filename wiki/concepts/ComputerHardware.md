---
title: "Computer Hardware"
type: concept
tags: [systems, hardware, architecture]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# Computer Hardware

The physical components of a [[ComputerSystem|computer system]]. Per [[dis-0-introduction]]'s opening definition, hardware **plus** an [[OperatingSystem|OS]] is what constitutes a computer system — hardware alone does not qualify.

## Core components named in [[DiveIntoSystems]]

- **[[CPU|Central Processing Unit (CPU)]]** — executes instructions; today essentially always [[MulticoreProcessor|multicore]].
- **[[RAM|Random-Access Memory (RAM)]]** — main working memory; volatile.
- **I/O ports** — interfaces to peripherals and the outside world.
- **Secondary storage** — non-volatile disk / SSD / Flash for persistent data.

## Integration trends

- **[[SystemOnAChip|System-on-a-chip (SoC)]]** — CPU + RAM (+ GPU, modem, etc.) on a single die; standard in smartphones and [[SingleBoardComputer|single-board computers]] like the [[RaspberryPi]].
- **Miniaturization** — desktops → laptops → SBCs → smartphones; the trajectory of the last two decades.
- **[[MulticoreProcessor|Multicore]]** — virtually every modern CPU exposes several cores, making [[ParallelComputing|parallel programming]] a baseline skill rather than a specialty.

## Connections

- [[ComputerSystem]] — hardware + OS.
- [[OperatingSystem]] — the software half.
- [[CPU]] / [[RAM]] / [[MulticoreProcessor]] / [[SystemOnAChip]] — components and integration patterns.
- [[MemoryHierarchy]] — the speed/cost stratification of memory components.
- [[SingleBoardComputer]] / [[RaspberryPi]] — compact-form-factor exemplars.
- [[dis-0-introduction]] — source.
