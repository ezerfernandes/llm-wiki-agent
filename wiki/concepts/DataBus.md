---
title: "Data Bus"
type: concept
tags: [computer-architecture, von-neumann, interconnect]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Data Bus

The **data bus** is one of the three classical [[Bus|system buses]] in the [[VonNeumannArchitecture|von Neumann architecture]] — it carries the **actual byte / word values** being read from or written to [[RAM|memory]] (or [[IODevice|I/O devices]]) ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]).

Width is typically the [[DataWord|word size]] of the architecture (or a multiple thereof) — a 32-bit CPU usually has a 32-bit data bus, though modern systems decouple internal word size from external memory-channel width.

## Connections

- [[Bus]] — parent umbrella.
- [[ControlBus]] / [[AddressBus]] — sibling buses.
- [[RAM]] — primary endpoint.
- [[CpuRegister]] — the [[CPU]]-side endpoint for most reads/writes.
- [[DataWord]] — the unit of transfer.
- [[VonNeumannArchitecture]] — the architecture that includes it.
- [[dis-5-2-von-neumann]] — source.
