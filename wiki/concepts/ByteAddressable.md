---
title: "Byte-Addressable Memory"
type: concept
tags: [computer-architecture, memory, von-neumann]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Byte-Addressable Memory

**Byte-addressable** memory is the convention where **each memory address corresponds to exactly one byte** — the *unit of addressing* equals the *unit of access granularity*. Per [[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]], modern systems are byte-addressable, which makes the address-bus-width ↔ addressable-RAM relationship one-to-one.

## Implication for the address bus

With byte addressing, a $N$-bit [[AddressBus|address bus]] supports $2^N$ distinct byte addresses:

- **32-bit** address bus → $2^{32}$ bytes = **4 GiB** maximum [[RAM|RAM]].
- **64-bit** address bus → $2^{64}$ bytes = 16 EiB (vastly beyond real DRAM scales; only 48–57 bits are physically wired on contemporary CPUs).

## Word-addressable alternative

The historical alternative is **word-addressable** memory (one address = one architectural word — e.g. 32 bits or 64 bits) — used on some early mainframes and DSPs. Byte-addressable won because **C** / **strings** / **byte-level I/O** all require per-byte addressing.

## Connections

- [[RAM]] — what byte addressing organizes.
- [[AddressBus]] — its width caps addressable bytes.
- [[VonNeumannArchitecture]] — the modern architecture's addressing convention.
- [[DataWord]] — the word abstraction layered on top of bytes.
- [[ByteOrder]] — how multi-byte words map onto byte addresses (endianness).
- [[dis-5-2-von-neumann]] — source.
