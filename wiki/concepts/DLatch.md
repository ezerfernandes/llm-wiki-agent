---
title: "Gated D Latch"
type: concept
tags: [circuit, storage, latch, sequential-logic, write-enable, nand]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# Gated D Latch

The **gated D latch** is the **safe, usable 1-bit storage cell** in [[dis-5-4-3-storage-circuits|Ch 5.4.3]]'s build-up. It wraps an [[SRLatch|RS latch]] with control circuitry that exposes a clean "store a bit on command" interface and **structurally eliminates** the RS latch's forbidden input case.

## Construction

A gated D latch wraps an [[SRLatch|RS latch]] core in two additional [[NandGate|NAND]] gates forming a control front-end. Inputs to the cell:

- **`D`** — the **data** input: the bit you want to store.
- **`WE`** — **[[WriteEnable|Write Enable]]**: the control input deciding whether to update or hold.

Output: `Q` (the stored bit).

The front-end NAND gates compute the internal `R` / `S` signals fed to the underlying RS latch:

- One NAND combines `D` and `WE` → drives the internal `S` line.
- Another NAND combines `¬D` (or equivalently `D` through a NAND-based inverter) and `WE` → drives the internal `R` line.

## Operating modes

| `WE` | Effect |
|----|------|
| `0` | **Hold** — both internal `R` and `S` are forced to `1` (the [[SRLatch|RS latch]]'s hold state); the cell remembers its previous value regardless of `D`. |
| `1` | **Write** — internal `R` and `S` become complements of each other driven by `D`; the cell loads `D`'s value into `Q`. |

> "The gated D latch ... improves upon the RS latch by adding control circuitry that prevents simultaneous 0 inputs to both R and S."
> — [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

The construction makes the forbidden `R = S = 0` combination from the [[SRLatch|RS latch]] **unreachable from any combination of `D` and `WE`** — eliminating the bad case at the structural level.

## Why this is the building block

- **One bit in, one control wire, one bit out** — the right interface for higher composition.
- **Forbidden case eliminated by construction** — safe to drive from arbitrary upstream logic.
- **Composes trivially into [[CpuRegister|N-bit registers]]** — stack `N` D-latches with their `D` inputs receiving the `N` data bits and *one shared `WE` wire* driving every latch's write enable.

[[dis-5-4-3-storage-circuits|Ch 5.4.3]] uses "flip-flop" informally as a synonym for this cell — see [[FlipFlop]] for the level-sensitive-vs-edge-triggered distinction the chapter elides.

## Connections

- [[StorageCircuit]] — Parent category.
- [[Latch]] — Generic term; D latches are the level-sensitive variant with a clean control interface.
- [[SRLatch]] — The cell the D latch wraps; the D-latch front-end exists to forbid the RS latch's bad input case.
- [[WriteEnable]] — The control input; this page's headline contribution beyond the [[SRLatch|RS latch]].
- [[NandGate]] — The single gate type the full D-latch construction uses.
- [[CpuRegister]] — The N-bit aggregation: N D-latches sharing one `WE`.
- [[RegisterFile]] — The N-register array selecting which register's `WE` to assert via a [[Decoder|decoder]].
- [[FlipFlop]] — Edge-triggered cousin (informally called "flip-flop" in this chapter despite being level-sensitive).
- [[ClockSignal]] — In real designs `WE` is typically gated by a clock; Ch 5.4.3 abstracts this away.
- [[Circuit]] — Sequential circuit.
- [[dis-5-4-3-storage-circuits]] — Source.
