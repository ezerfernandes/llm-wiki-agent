---
title: "Bus (System Bus)"
type: concept
tags: [computer-architecture, von-neumann, interconnect]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Bus (System Bus)

A **bus** is — per [[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]] — a *"communication channel that transfers binary values between communication endpoints."* In the [[VonNeumannArchitecture|von Neumann architecture]], buses are the **wires that connect the five functional units** ([[ControlUnit|control unit]], [[ProcessingUnit|processing unit]], [[RAM|memory]], [[InputDevice|input]], [[OutputDevice|output]]) — the substrate over which instructions, addresses, data, and control signals flow.

## The three classical bus types

Ch 5.2 names three buses that together carry every CPU↔memory↔I/O transaction:

- **[[ControlBus|Control bus]]** — carries **command / control signals** (read vs write, interrupt acknowledge, bus grant, clock).
- **[[AddressBus|Address bus]]** — carries the **[[RAM|memory address]]** for the current read or write request. Its width caps addressable [[RAM|RAM]] (a 32-bit address bus → $2^{32}$ byte addresses → 4 GiB).
- **[[DataBus|Data bus]]** — carries the **actual byte / word values** being read or written.

## Why three buses

Splitting the bus by *what kind of binary value travels* lets all three move in parallel: the [[ControlUnit|control unit]] can drive a *"read this address"* command on the control + address buses **at the same time** the prior cycle's data is still flowing on the data bus, increasing pipeline throughput.

## Connections

- [[VonNeumannArchitecture]] — the architecture that organizes around three buses.
- [[ControlBus]] / [[AddressBus]] / [[DataBus]] — the three children.
- [[ControlUnit]] — the bus's primary commander.
- [[RAM]] — the bus's most-trafficked endpoint.
- [[CPU]] — the bus's other primary endpoint.
- [[FetchDecodeExecuteCycle]] — each phase corresponds to specific bus traffic.
- [[VonNeumannBottleneck|Von Neumann bottleneck]] — the throughput limit set by sharing one bus between instructions and data; cache hierarchies mitigate it.
- [[dis-5-2-von-neumann]] — source.
