---
title: "Storage Circuit"
type: concept
tags: [circuit, storage, memory, sequential-logic, sram, dram, latch, register]
sources: [dis-5-4-3-storage-circuits, dis-5-4-circuits]
last_updated: 2026-05-17
---

# Storage Circuit

**Category-level page** for the **third** of the three [[Circuit|digital-circuit]] categories in [[dis-5-4-circuits|Ch 5.4]]'s partition — the sibling of [[ArithmeticLogicCircuit|arithmetic-and-logic circuits]] (which compute) and [[ControlCircuit|control circuits]] (which route). Storage circuits **remember**.

> "A storage circuit's value depends on its input values and also its currently stored value."
> — [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

The structural signature of a storage circuit is a **feedback loop** wiring an output back to an input. This is what makes the family **sequential** rather than combinational — outputs depend on history, not just the current input vector.

## The two-technology split

[[dis-5-4-3-storage-circuits|Ch 5.4.3]] introduces the [[MemoryHierarchy|memory-hierarchy]]-defining distinction:

- **[[SRAM|Static RAM (SRAM)]]** — **circuit-based** memory; faster, more expensive, lower density; used for [[CpuRegister|CPU registers]] and on-chip cache. The latches and registers built in this chapter are SRAM-style cells.
- **[[DRAM|Dynamic RAM (DRAM)]]** — **capacitor-based** memory; slower (charge leakage requires periodic refresh) but denser and cheaper; used for main [[RAM|memory]].

## Build-up ladder

Ch 5.4.3 builds storage circuits hierarchically, each layer adding a control discipline:

1. **[[SRLatch|RS (Reset-Set) latch]]** — minimal 1-bit cell. Two cross-coupled [[NandGate|NAND]] gates with feedback; inputs `S` / `R`, output `Q`. Holds value when `S = R = 1`. Forbidden input `S = R = 0`.
2. **[[DLatch|Gated D latch]]** — wraps an RS latch in a [[WriteEnable|WE]]-gated front-end taking a data input `D`. Structurally **prevents** the forbidden case and exposes a clean "store one bit on command" interface.
3. **[[CpuRegister|N-bit register]]** — 32 D latches sharing one `WE`; one [[DataWord|word]] of storage. The discipline matches [[Multiplexer|MUX]]'s two-way N-bit construction in [[dis-5-4-2-control-circuits|Ch 5.4.2]] — parallelize the 1-bit primitive across the word width.
4. **Register file / memory array** — collection of registers selected by address bits via a [[Decoder|decoder]] that drives the right register's `WE`. The chapter names this conceptually; full wiring is deferred to later chapters of [[DiveIntoSystems]].

## Connections

- [[Circuit]] — Parent umbrella. Storage circuits are the **sequential** third of the combinational/sequential partition.
- [[ArithmeticLogicCircuit]] / [[ControlCircuit]] — Sibling circuit categories. **Compute** / **route** / **remember**.
- [[SRLatch]] — The raw 1-bit cell.
- [[DLatch]] — The safe usable 1-bit cell.
- [[Latch]] / [[FlipFlop]] — General terms for 1-bit storage elements; the chapter introduces level-sensitive latches only.
- [[WriteEnable]] — The control input that turns a D latch into a writable register cell.
- [[CpuRegister]] / [[RegisterFile]] — The N-bit and N-register aggregations built on D latches.
- [[SRAM]] / [[DRAM]] — Technology split for the memory hierarchy.
- [[RAM]] / [[MemoryHierarchy]] — Where SRAM and DRAM cells sit physically.
- [[NandGate]] — The gate the chapter uses to build both [[SRLatch|RS]] and [[DLatch|D]] latches.
- [[dis-5-4-3-storage-circuits]] — Source.
- [[dis-5-4-circuits]] — Parent hub installing the three-category partition.
- [[dis-5-2-von-neumann]] — Names the [[CpuRegister|register file]] as part of the [[ProcessingUnit|processing unit]]; this chapter delivers its gate-level construction.

**Promoted from forward-reference to category page by [[dis-5-4-3-storage-circuits]] — closes the three-circuit-category partition Ch 5.4 opened.**
