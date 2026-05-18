---
title: "Address Bus"
type: concept
tags: [computer-architecture, von-neumann, interconnect]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Address Bus

The **address bus** is one of the three classical [[Bus|system buses]] in the [[VonNeumannArchitecture|von Neumann architecture]] — it carries the **[[RAM|memory]] address** for the current read or write request between the [[CPU]] and [[RAM|memory]] / [[IODevice|I/O devices]] ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]).

## Width caps addressable memory

The address bus's bit width is the **architectural ceiling on addressable [[RAM|RAM]]**:

- A **32-bit** address bus → $2^{32}$ byte addresses → **4 GiB** max [[RAM|RAM]] (the historical 32-bit OS limit).
- A **64-bit** address bus → $2^{64}$ byte addresses → 16 EiB (effectively unlimited; modern CPUs implement only 48–57 of those bits).

Because modern systems are **[[ByteAddressable|byte-addressable]]** (one address = one byte), the address-bus width directly equals the addressable-byte exponent.

## Connections

- [[Bus]] — parent umbrella.
- [[ControlBus]] / [[DataBus]] — sibling buses.
- [[RAM]] — the bus's primary destination.
- [[ByteAddressable]] — the granularity convention that ties bus-width to addressable bytes.
- [[CPU]] — the bus's primary commander.
- [[VonNeumannArchitecture]] — the architecture that includes it.
- [[dis-5-2-von-neumann]] — source.
