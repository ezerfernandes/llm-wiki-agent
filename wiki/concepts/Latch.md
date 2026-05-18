---
title: "Latch"
type: concept
tags: [circuit, storage, latch, sequential-logic, memory-cell]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# Latch

A **latch** is a 1-bit [[StorageCircuit|storage circuit]] — a sequential-logic element with a feedback loop that **remembers** a single bit between updates. Latches are the foundational primitive from which [[CpuRegister|CPU registers]] and on-chip [[SRAM]] cells are built.

> "A storage circuit's value depends on its input values and also its currently stored value."
> — [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

A latch is **level-sensitive** — while its control input (write-enable / clock-high) is asserted, the latch is *transparent* and follows its data input; when deasserted, it **holds**. This contrasts with an edge-triggered [[FlipFlop|flip-flop]] (not built at the gate level in this chapter), which only samples on a clock edge.

## Variants in [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

- **[[SRLatch|RS (Reset-Set) latch]]** — the raw primitive. Two cross-coupled [[NandGate|NAND]] gates with inputs `S` / `R`, output `Q`. Hazard: the input combination `S = R = 0` is forbidden.
- **[[DLatch|Gated D latch]]** — the safe upgrade. Wraps an RS latch in a [[WriteEnable|WE]]-gated front-end taking a data input `D`. Structurally prevents the forbidden input case and provides a clean "write a bit on command" interface.

## "Latch" vs "flip-flop"

[[dis-5-4-3-storage-circuits|Ch 5.4.3]] uses **latch** and informal **flip-flop** roughly interchangeably and builds only level-sensitive devices. In wider digital-design vocabulary:

- **Latch** — level-sensitive (transparent while control asserted).
- **[[FlipFlop|Flip-flop]]** — edge-triggered (samples once per clock edge).

The book defers edge-triggered timing and explicit [[ClockSignal|clock]] wiring to later chapters; in Ch 5.4.3 the abstracted control is `WE` (write enable).

## Connections

- [[StorageCircuit]] — Parent category; latches are the 1-bit instance.
- [[SRLatch]] / [[DLatch]] — The two latch variants Ch 5.4.3 constructs.
- [[FlipFlop]] — Edge-triggered cousin; deferred at the gate level.
- [[WriteEnable]] — The control input on the gated [[DLatch|D latch]].
- [[ClockSignal]] — In real designs, `WE` is typically gated by a [[ClockSignal|clock]]; abstracted away in this chapter.
- [[CpuRegister]] — Built from N parallel D-latches sharing one `WE`.
- [[NandGate]] — The elemental gate Ch 5.4.3 uses to build both latches.
- [[SRAM]] — SRAM cells are essentially latches at scale.
- [[Circuit]] — Latches are sequential circuits (vs combinational).
- [[dis-5-4-3-storage-circuits]] — Source.
