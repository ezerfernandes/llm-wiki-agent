---
title: "Clock Signal"
type: concept
tags: [circuit, clock, timing, sequential-logic, storage]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# Clock Signal

A **clock signal** is the periodic timing wire — a square wave alternating between `0` and `1` at a fixed frequency — that paces a synchronous digital circuit, scheduling when [[StorageCircuit|storage elements]] sample their inputs and update their outputs.

## In [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

The chapter **abstracts the clock away**. Storage cells expose a single binary [[WriteEnable|`WE`]] control input rather than a clock wire; updates happen *"while `WE = 1`"*, not *"on the rising edge of CLK"*. This pedagogical simplification:

- Keeps the gate-level diagrams focused on the data path.
- Sidesteps edge-triggering, master-slave [[FlipFlop|flip-flop]] construction, setup/hold timing, and metastability.
- Defers the explicit clock wire to later chapters of [[DiveIntoSystems]] (notably the processor-build chapter when ingested).

## What a clock would add in a real design

In an actual synchronous processor:

- The **clock distributes a common timing reference** across the whole chip — every register samples its input on the same clock edge, ensuring all stages settle in lockstep.
- A register's `WE` is typically derived as a logical AND of the clock and an upstream control signal — so the cell loads on a *clock-edge AND write-permission* condition, not on `WE` alone.
- The **clock period** must be at least the longest combinational propagation delay between two register stages (the *critical path*) — the inverse of clock frequency is the headline performance dial of a CPU.
- Edge-triggered [[FlipFlop|flip-flops]] (not just transparent [[Latch|latches]]) are typically used precisely so that each pipeline stage sees a clean snapshot per clock cycle.

## Connections

- [[StorageCircuit]] — Clock signals pace storage elements; the chapter that introduces them abstracts the clock to [[WriteEnable|WE]].
- [[WriteEnable]] — The chapter's stand-in for clock-gated write control.
- [[FlipFlop]] — Edge-triggered storage cells sample on a clock edge; not built explicitly in Ch 5.4.3.
- [[Latch]] — Level-sensitive storage cells (what Ch 5.4.3 builds); transparent while their control input is asserted.
- [[CpuRegister]] / [[RegisterFile]] — In real CPUs these are clocked storage elements; DIS Ch 5.4.3 omits the clock wire.
- [[CPU]] — Operates on a system clock; clock-frequency is the headline performance parameter (deferred in DIS Ch 5.4.3).
- [[ControlBus]] — In [[VonNeumannArchitecture|von-Neumann]] systems, the clock typically rides the [[ControlBus|control bus]] ([[dis-5-2-von-neumann|Ch 5.2]]).
- [[Circuit]] — Synchronous-circuit context.
- [[dis-5-4-3-storage-circuits]] — Source (introduces the topic implicitly by abstracting it).

**Scope note**: Ch 5.4.3 does not introduce the clock as a first-class wire; this page documents the concept as backdrop and acknowledges what the chapter elides. The page can be expanded in-place when a later DIS chapter (or another corpus source) covers clock distribution, edge-triggering, and timing budgets explicitly.
