---
title: "Flip-Flop"
type: concept
tags: [circuit, storage, flip-flop, sequential-logic, memory-cell]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# Flip-Flop

A **flip-flop** is a 1-bit [[StorageCircuit|storage circuit]]. In wider digital-design vocabulary the term denotes specifically an **edge-triggered** memory cell — one that samples its data input on a [[ClockSignal|clock]] edge and holds for the rest of the clock period — distinguishing it from a level-sensitive [[Latch|latch]] that is *transparent* while its control input is asserted.

## In [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

[[DiveIntoSystems|*Dive into Systems*]] Ch 5.4.3 **uses "flip-flop" informally as a synonym for the gated [[DLatch|D latch]]** — the chapter builds level-sensitive devices only and does not construct an edge-triggered master-slave flip-flop. The book's explicit gate-level builds are:

- **[[SRLatch|RS latch]]** — raw 1-bit cell from two cross-coupled [[NandGate|NAND]] gates.
- **[[DLatch|Gated D latch]]** — adds [[WriteEnable|WE]] control.

The clock-edge sampling, master-slave construction, and setup/hold timing that define a true edge-triggered flip-flop in digital-design textbooks are **deferred** in DIS — see later DIS chapters on processor build.

## Why edge-triggering matters (forward reference)

A transparent latch in a circuit driven by combinational logic risks **race-through**: while the control is high, changes at the input ripple through. Edge-triggered flip-flops sample only at the clock transition, giving each stage a full clock period to settle before its output is sampled — the discipline that makes synchronous pipelined CPUs feasible. DIS abstracts this away by using `WE` as a single binary control input.

## Connections

- [[StorageCircuit]] — Parent category.
- [[Latch]] — The level-sensitive cousin (DIS Ch 5.4.3 builds these explicitly).
- [[SRLatch]] / [[DLatch]] — DIS's two latch constructions; Ch 5.4.3 calls the D latch a "flip-flop" informally.
- [[ClockSignal]] — The edge a true flip-flop samples on; abstracted in Ch 5.4.3.
- [[WriteEnable]] — Ch 5.4.3's stand-in for clock-gated write control.
- [[CpuRegister]] — In real processors, registers are typically built from edge-triggered flip-flops, not transparent latches; DIS uses latches as a pedagogical simplification.
- [[Circuit]] — Sequential circuit.
- [[dis-5-4-3-storage-circuits]] — Source.

**Scope note**: This page documents the term as it surfaces in [[dis-5-4-3-storage-circuits|Ch 5.4.3]] (informal, used as a [[DLatch|D-latch]] synonym). A first-class edge-triggered-flip-flop page with master-slave construction can be promoted from this stub when a later source covers it.
