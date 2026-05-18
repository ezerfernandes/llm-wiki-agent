---
title: "Register File"
type: concept
tags: [circuit, storage, register, register-file, sram, cpu, processing-unit]
sources: [dis-5-4-3-storage-circuits, dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Register File

A **register file** is the array of [[CpuRegister|CPU registers]] that lives inside the [[ProcessingUnit|processing unit]] — the small, fast on-chip [[StaticRAM|SRAM]] bank the [[ArithmeticLogicUnit|ALU]] reads operands from and writes results back to during the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]].

## Construction

[[dis-5-4-3-storage-circuits|Ch 5.4.3]] builds the register file in two layers:

1. **One register** — `N` [[DLatch|gated D latches]] sharing a single [[WriteEnable|`WE`]] wire. Each latch receives one bit of the [[DataWord|word]] on its `D` input; together they hold one N-bit word ([[DiveIntoSystems|DIS]] uses 32-bit registers as the canonical example).
2. **The register file** — `K` registers (typically `K = 16` or `K = 32` for general-purpose registers on a modern ISA) addressed by a register-index field that drives a [[Decoder|decoder]]. The decoder enables exactly one register's `WE` line on a write, and a [[Multiplexer|MUX]] selects which register's output to read.

The decoder + register-array + MUX construction is the **direct payoff** of the three Ch 5.4.2 control circuits ([[Decoder]], [[Multiplexer|MUX]], [[Demultiplexer|DMUX]]) applied to the storage primitive from Ch 5.4.3.

## What [[dis-5-4-3-storage-circuits|Ch 5.4.3]] explicitly builds vs defers

- **Built**: one 32-bit register as 32 D-latches on a shared `WE`.
- **Named only**: the multi-register file, including the address-decoder front-end and the read MUX. The chapter sketches the role conceptually but does not produce a full wiring diagram.

## Architectural context

Per [[dis-5-2-von-neumann|Ch 5.2]], the [[ProcessingUnit|processing unit]] = [[ArithmeticLogicUnit|ALU]] + register file. The register file:

- Holds the most-recently-used [[DataWord|words]] for the running program (operands, intermediate results).
- Is **the fastest storage layer** in the [[MemoryHierarchy|memory hierarchy]] — single-cycle access from the ALU.
- Is **architecturally visible** — the ISA names specific registers (e.g. `%rax`, `%rbx`, ... on x86-64; `x0` ... `x31` on RISC-V); the compiler / assembly programmer addresses them by name.
- Is **technologically SRAM** — circuit-based latches, not the capacitor-based [[DynamicRAM|DRAM]] cells of main [[RAM|memory]].

## Connections

- [[StorageCircuit]] — Parent category.
- [[CpuRegister]] — The N-bit cell; the register file is the K-register array.
- [[DLatch]] — The 1-bit primitive each register is made of.
- [[WriteEnable]] — The control wire per register; a [[Decoder|decoder]] picks which one to assert.
- [[Decoder]] — The address-decode front-end on the write side.
- [[Multiplexer]] — The read-side selector.
- [[Demultiplexer]] — Conceptually the inverse role on the write side (one data bus → fan out to selected register).
- [[ProcessingUnit]] — The CPU half that owns the register file ([[dis-5-2-von-neumann|Ch 5.2]]).
- [[ArithmeticLogicUnit]] — The consumer/producer of register-file values.
- [[FetchDecodeExecuteCycle]] — The cycle that reads and writes register-file entries on every instruction.
- [[SRAM]] / [[MemoryHierarchy]] — Technology / position in the hierarchy.
- [[DataWord]] — The unit each register stores.
- [[dis-5-4-3-storage-circuits]] — Source (gate-level build).
- [[dis-5-2-von-neumann]] — Architectural context.
