---
title: "Multicore Processor"
type: concept
tags: [systems, hardware, parallelism, cpu]
sources: [dis-0-introduction]
last_updated: 2026-05-17
---

# Multicore Processor

A **multicore processor** is a [[CPU]] package containing two or more independent execution cores on a single die, capable of executing distinct instruction streams in parallel.

[[DiveIntoSystems]] Ch 0 names multicore as the default form of contemporary CPU silicon — from desktops and laptops down through [[SingleBoardComputer|single-board computers]] like the [[RaspberryPi]] and smartphone [[SystemOnAChip|SoCs]]. The pedagogical consequence: [[ParallelComputing|parallel programming]] is no longer a specialty, it is part of basic systems literacy.

## Why it matters for programmers

- A single thread on a single core leaves the rest of the machine idle. Code that wants to use the hardware must be **parallel-aware**.
- Multicore introduces shared-memory coordination problems (race conditions, synchronization, cache coherence) that single-core code did not have.
- Ch 0 frames the multicore reality as the *reason* the book devotes its later chapters to parallel programming on top of the [[OperatingSystem|OS]]'s threading abstractions.

## Connections

- [[CPU]] — the broader component.
- [[ParallelComputing]] — the programming paradigm multicore enables.
- [[ComputerHardware]] — multicore is the modern norm.
- [[SystemOnAChip]] — typical packaging in modern compact systems.
- [[dis-0-introduction]] — source.
