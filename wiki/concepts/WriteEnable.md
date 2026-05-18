---
title: "Write Enable (WE)"
type: concept
tags: [circuit, storage, control-signal, write-enable, latch, register]
sources: [dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# Write Enable (WE)

**Write Enable (`WE`)** is the **single-bit control input** on a writable [[StorageCircuit|storage circuit]] cell that decides whether the cell should **update** from its data input or **hold** its current value.

## In [[dis-5-4-3-storage-circuits|Ch 5.4.3]]

The chapter introduces `WE` on the **gated [[DLatch|D latch]]**:

- **`WE = 0`** → the latch's internal `R` / `S` lines (driven from the [[NandGate|NAND]]-based front-end) are both forced to `1`, putting the underlying [[SRLatch|RS latch]] into **hold** mode. The cell ignores `D` and remembers whatever it stored last.
- **`WE = 1`** → the front-end drives internal `R` and `S` to opposite values determined by `D`, writing `D` into the cell.

The two-input-plus-control discipline is what makes the [[DLatch|D latch]] composable: the same `WE` wire can fan out to all `N` latches of an N-bit [[CpuRegister|register]] so that one control bit decides "load this register on this cycle, or hold it."

## Why `WE` rather than a clock

[[dis-5-4-3-storage-circuits|Ch 5.4.3]] uses `WE` as a **clock abstraction** — it stands in for the clock-gated control wire a real synchronous CPU would use. The chapter doesn't construct the explicit [[ClockSignal|clock]] / edge-triggering machinery; in production designs `WE` would typically be `(clock_edge AND register_write_command)`.

## At the next level up

- **[[CpuRegister|Register]]**: one `WE` wire shared by all N D-latches.
- **[[RegisterFile|Register file]]**: a [[Decoder|decoder]] on register-address bits gates the `WE` of exactly one register on any given write, leaving all other registers in hold mode.

## Connections

- [[StorageCircuit]] — Cell-level control input.
- [[DLatch]] — The chapter's headline cell exposing `WE`.
- [[SRLatch]] — The cell underneath; `WE = 0` forces it into hold mode.
- [[CpuRegister]] — N-bit aggregation: all N latches share one `WE`.
- [[RegisterFile]] — K-register array: address-decoded `WE` per register.
- [[Decoder]] — The control circuit that picks which register's `WE` to assert ([[dis-5-4-2-control-circuits|Ch 5.4.2]]).
- [[ClockSignal]] — `WE` is the abstracted stand-in for clock-gated write control.
- [[ControlBus]] — In [[VonNeumannArchitecture|von-Neumann]] systems, write-control signals like `WE` ride the [[ControlBus|control bus]] across the CPU.
- [[dis-5-4-3-storage-circuits]] — Source.
