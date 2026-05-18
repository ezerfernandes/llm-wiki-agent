---
title: "RS (Reset-Set) Latch"
type: concept
tags: [circuit, storage, latch, sequential-logic, nand]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# RS (Reset-Set) Latch

The **RS latch** (also "SR latch") is the minimal 1-bit [[StorageCircuit|storage circuit]] in [[dis-5-4-3-storage-circuits|Ch 5.4.3]]'s build-up — the raw primitive on which the gated [[DLatch|D latch]] and ultimately the [[CpuRegister|CPU register]] are constructed.

## Construction

Two **cross-coupled [[NandGate|NAND]] gates** with a feedback loop:

- Two inputs: `S` (set) and `R` (reset).
- One output: `Q` (the stored bit). An inverted `Q̄` is also exposed.
- The `Q` output of the top NAND feeds back into the bottom NAND's input; the bottom NAND's output (`Q̄`) feeds into the top NAND's input. This **feedback loop** is what makes the circuit sequential — its current output participates in computing its next output.

## Operating modes

| `S` | `R` | Effect |
|----|----|------|
| 1 | 1 | **Hold** — latch maintains its current `Q` (the memory mode). |
| 1 | 0 | **Reset** — writes `Q = 0`. |
| 0 | 1 | **Set** — writes `Q = 1`. |
| 0 | 0 | **Forbidden** — both NANDs forced to `1`; behaviour is unstable / undefined. |

> "When S and R are both 1, the latch maintains its current value."
> — [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

The forbidden `S = R = 0` case is the chapter's motivation for the next layer up: the gated [[DLatch|D latch]] wraps the RS latch in a [[WriteEnable|WE]]-controlled front-end that makes the bad input combination **structurally unreachable**.

## Inputs are active-low

Because the cell is built from [[NandGate|NAND]] gates, both control inputs are **active-low**: drive `S` to `0` to *set*, drive `R` to `0` to *reset*. In the **hold** state both inputs sit at `1` — counterintuitive at first, but the natural consequence of the NAND-based construction.

## Connections

- [[StorageCircuit]] — Parent category.
- [[Latch]] — Generic term for level-sensitive 1-bit storage; RS is one variant.
- [[DLatch]] — The next layer up; wraps the RS latch with a [[WriteEnable|WE]]-gated front-end to eliminate the forbidden input case.
- [[NandGate]] — The single gate type the construction uses.
- [[CpuRegister]] — Indirectly built on top: register cells are D latches, and D latches are RS latches with control wrapping.
- [[Circuit]] — Sequential circuit (vs the combinational examples of [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] and [[dis-5-4-2-control-circuits|Ch 5.4.2]]).
- [[FlipFlop]] — Edge-triggered cousin (not built here).
- [[dis-5-4-3-storage-circuits]] — Source.

**Scope note**: Ch 5.4.3 builds the NAND-based RS latch. The dual NOR-based RS latch (with the opposite forbidden case `S = R = 1`) is not built but is mathematically equivalent.
