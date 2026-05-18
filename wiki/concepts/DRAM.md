---
title: "DRAM"
type: concept
tags: [memory, dram, ram, capacitor, refresh, main-memory]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# DRAM

**Dynamic Random-Access Memory** — main-memory technology in which each bit is stored as **charge on a tiny capacitor**, addressed by a single pass transistor (the canonical "1T1C" cell). DRAM is the **denser, cheaper, slower** sibling of [[SRAM]] in the [[MemoryHierarchy|memory hierarchy]] and is what populates the [[RAM|main-memory]] DIMMs of a typical computer.

## Introduced by [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

[[DiveIntoSystems|*Dive into Systems*]] Ch 5.4.3 names the SRAM/DRAM split as the technology choice underlying the [[MemoryHierarchy|memory hierarchy]]:

- [[SRAM]] — **circuit-based** (latches / flip-flops); fast; used for [[CpuRegister|CPU registers]] and on-chip cache. The [[Latch|latches]] Ch 5.4.3 builds are SRAM-style cells.
- **DRAM** — **capacitor-based**; slower; used for main [[RAM|memory]].

> "Dynamic RAM (DRAM) uses capacitors to store values and is slower but cheaper."
> — [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

## The "dynamic" word

A DRAM cell's capacitor **leaks charge** — a stored bit decays in milliseconds. DRAM controllers must therefore **refresh** every row periodically (typically every ~64 ms) by reading and rewriting it. This refresh overhead is the technology's headline downside; the upside is **6×–10× higher density** than SRAM because the cell is one transistor + one capacitor rather than the six-transistor cross-coupled-latch [[SRAM]] cell.

## Where DRAM sits

- **DRAM dies on DIMMs** = main memory; addressed by the [[CPU]] via the [[AddressBus|address bus]] and [[DataBus|data bus]] ([[dis-5-2-von-neumann|Ch 5.2]]).
- **SRAM caches** sit *between* the [[CpuRegister|register file]] and DRAM, hiding DRAM latency from the [[ArithmeticLogicUnit|ALU]].

## Connections

- [[StorageCircuit]] — Parent technology landscape: DRAM is one of the two memory-cell families.
- [[SRAM]] — Faster, lower-density sibling used for [[CpuRegister|registers]] and cache.
- [[RAM]] — Generic term; on a modern PC, "RAM" almost always means DRAM.
- [[MemoryHierarchy]] — DRAM occupies the main-memory tier.
- [[CPU]] / [[AddressBus]] / [[DataBus]] — How the CPU talks to DRAM.
- [[dis-5-4-3-storage-circuits]] — Source (introductory naming).

**Scope note**: Ch 5.4.3 introduces DRAM only by name; the 1T1C cell, refresh cycle, and DDR memory-controller protocol are not built. Stub can be expanded when a later source covers them.
