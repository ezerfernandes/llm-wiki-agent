---
title: "Dive into Systems — Ch 5.4.3 Storage Circuits"
type: source
tags: [dive-into-systems, textbook, computer-architecture, circuits, storage, memory, latch, flip-flop, register, sram, dram]
sources: [dis-5-4-3-storage-circuits]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/storagecircs.html
---

## Summary

**Storage circuits** are the third category in [[dis-5-4-circuits|Ch 5.4]]'s partition of processor circuitry (alongside [[ArithmeticLogicCircuit|arithmetic-and-logic]] and [[ControlCircuit|control]]). They are the gate-level substrate beneath [[CpuRegister|CPU registers]] and on-chip cache. The chapter draws the cardinal distinction between **[[SRAM|static RAM (SRAM)]]** — circuit-based, faster, used in registers / cache — and **[[DRAM|dynamic RAM (DRAM)]]** — capacitor-based, denser but requiring periodic refresh, used for main [[RAM|memory]]. The mechanism walk-through ladders up from the **[[SRLatch|RS latch]]** (raw 1-bit cell with feedback) → **[[DLatch|gated D latch]]** (adds [[WriteEnable|write-enable]] control) → **[[CpuRegister|32-bit register]]** (32 D-latches sharing a single WE wire).

## Key Claims

- **Storage circuits require feedback.** Unlike [[ArithmeticLogicCircuit|arithmetic-logic]] and [[ControlCircuit|control]] circuits whose outputs depend purely on current inputs, a storage circuit's output depends on its inputs **and** its currently stored value — implemented by a **feedback loop** wiring an output back to an input.
- **Two memory-cell technologies partition the [[MemoryHierarchy|memory hierarchy]].** [[SRAM]] is circuit-based — *"faster but more expensive"* — and is used for [[CpuRegister|registers]] and on-chip cache. [[DRAM]] stores bits as **capacitor charge** — denser and cheaper but **leaks** and therefore needs periodic refresh — and is used for main [[RAM|memory]].
- **The [[SRLatch|RS (reset-set) latch]] is the 1-bit primitive.** Built from two cross-coupled [[NandGate|NAND]] gates with feedback. Two inputs `S` (set) and `R` (reset) and one output `Q`. Invariants: both `S = R = 1` → latch holds its current value; pulse `R = 0` (with `S = 1`) writes a `0`; pulse `S = 0` (with `R = 1`) writes a `1`. The pathological case `S = R = 0` is forbidden and the next layer up exists precisely to forbid it.
- **The [[DLatch|gated D latch]] is the safe usable cell.** Wraps an [[SRLatch|RS latch]] in a control front-end (two extra [[NandGate|NAND]] gates) that takes a **data input** `D` and a **[[WriteEnable|Write Enable]]** `WE`. When `WE = 0`, the internal `R` and `S` lines are both forced to `1` → latch holds its value (storage). When `WE = 1`, the latch is driven from `D` → writes `D`'s value. The control front-end **structurally prevents** the forbidden `R = S = 0` case.
- **An N-bit [[CpuRegister|register]] = N parallel D-latches on a shared WE.** A 32-bit CPU register stacks 32 gated D-latches; each latch receives one of the 32 input bits, every latch shares the same `WE` wire, and the latch outputs jointly present the stored 32-bit word. Same composition discipline as [[Multiplexer|MUX]]'s two-way-N-bit form ([[dis-5-4-2-control-circuits|Ch 5.4.2]]) — single-bit primitive parallelized across the [[DataWord|data-word]] width.
- **Storage circuit ≠ memory cell ≠ register.** The chapter operationalizes a three-level hierarchy: **latch** (1-bit cell, the storage primitive) → **register** (N-bit word, an array of latches) → **register file / memory array** (collection of registers, mentioned but not built out at the gate level here).

## Key Quotes

> "A storage circuit's value depends on its input values and also its currently stored value."
> — Storage circuits depart from the combinational discipline of [[ArithmeticLogicCircuit|Ch 5.4.1]] and [[ControlCircuit|Ch 5.4.2]] circuits; the **feedback loop** is the structural signature.

> "Static RAM (SRAM) uses circuits to store values and is fast but expensive. Dynamic RAM (DRAM) uses capacitors to store values and is slower but cheaper."
> — The split that decides which physical technology sits where in the [[MemoryHierarchy|memory hierarchy]].

> "When S and R are both 1, the latch maintains its current value."
> — The RS latch's **hold state**, the invariant that makes the cell a memory.

> "The gated D latch ... improves upon the RS latch by adding control circuitry that prevents simultaneous 0 inputs to both R and S."
> — Why the [[DLatch|D latch]] supersedes the raw [[SRLatch|RS latch]] in practice — the WE-gated front-end eliminates the illegal-input case by construction.

## Connections

- [[DiveIntoSystems]] — Ch 5.4.3 *Storage Circuits*, the **closing subsection** of Ch 5.4. **Resolves** the [[StorageCircuit|storage]] forward-reference that the [[dis-5-4-circuits|Ch 5.4]] hub and [[ArithmeticLogicCircuit|Ch 5.4.1]] / [[ControlCircuit|Ch 5.4.2]] sibling pages have been pointing at.
- [[dis-5-4-circuits]] — Parent hub; the *storage* third of its three-category partition.
- [[dis-5-4-1-arithmetic-logic-circuits]] / [[dis-5-4-2-control-circuits]] — Sibling subsections. Where 5.4.1 computes and 5.4.2 routes, 5.4.3 **remembers**.
- [[dis-5-3-gates]] — Supplies the [[NandGate|NAND]] gate that is the elemental building block of both the [[SRLatch|RS latch]] and the [[DLatch|D latch]] in the chapter's construction.
- [[dis-5-2-von-neumann]] — Frames the [[CpuRegister|register file]] that this chapter now finally builds at the gate level: each [[CpuRegister|register]] holds one [[DataWord|word]]; here a word's worth of [[DLatch|D latches]] are wired to a common [[WriteEnable|WE]] line.
- [[Circuit]] — The umbrella; storage circuits are the sequential-logic third of its combinational/sequential partition.
- [[CpuRegister]] — Promoted by this chapter from "named place to put a word" to a **gate-level construction**: 32 [[DLatch|D-latches]] sharing one `WE`.
- [[StorageCircuit]] — Promoted from forward-reference stub to **category page** by this ingest.
- [[RAM]] / [[MemoryHierarchy]] — The SRAM/DRAM split sketched here is the entry point to the full memory-hierarchy treatment in later DIS chapters.

## Contradictions

None with the existing wiki. This ingest **resolves** the long-standing forward-reference to [[StorageCircuit]] (originating from the [[dis-5-4-circuits|Ch 5.4]] hub and reaffirmed by both [[dis-5-4-1-arithmetic-logic-circuits]] and [[dis-5-4-2-control-circuits]]). The SRAM/DRAM technology split is introduced here for the first time in the corpus and is consistent with the brief mentions of [[RAM|main memory]] in [[dis-5-2-von-neumann]].

## Scope Notes (what Ch 5.4.3 deliberately does **not** cover)

- **No edge-triggered flip-flop construction.** The chapter introduces level-sensitive latches only; a master-slave [[FlipFlop|D flip-flop]] is not built. The term "flip-flop" is used informally as a synonym for the gated D latch rather than as a distinct edge-triggered primitive.
- **No clock signal as a first-class wire.** [[ClockSignal|Clock]] timing is not introduced at the gate level in this chapter; `WE` is the abstracted write-control input. (The book's clock treatment lives later — see [[dis-5-5-procbuild]] when ingested.)
- **No register-file decoder wiring.** Multi-register selection (a [[Decoder]] on register-address bits driving the right register's `WE`) is mentioned conceptually as the "register file" but the wiring diagram is not produced.
- **No DRAM-cell construction.** SRAM/DRAM are named as a technology split; the DRAM 1T1C cell and refresh circuitry are not built.
- **No timing-hazard, metastability, or setup/hold treatment.** Latch dynamics are pitched at the functional-correctness level.
